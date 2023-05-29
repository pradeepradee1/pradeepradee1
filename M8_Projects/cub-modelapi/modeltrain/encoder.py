from os import execv
from modeltrain.train import train
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import OneHotEncoder, VectorAssembler
from pyspark.ml import Pipeline
from rest_framework import status
from modeltrain.models import EncoderAudit,EncoderMPAudit
from modeltrain.utils import create_table,df_tosql,get_checksum,get_file_size
import pandas as pd

from pathlib import Path
from sklearn.preprocessing import OneHotEncoder
import pickle
import logging
from modeltrain.Reduce_Memory import Reduce_Memory_Usage

logger = logging.getLogger(__name__)

def encoder(request):
    
    response = request
    
    try:        
        input_file = request.get('input_file')
        output_file = request.get('output_file')
        label_col = request.get('label_col')
        process_id = request.get('process_id')
        product_name = request.get('product_name')
        template_name = request.get('template_name')

        input_file=input_file.replace("template_name",str(template_name))
        input_file=input_file.replace("process_id",str(process_id))
        input_file=input_file.replace("product_name",str(product_name))

        output_file=output_file.replace("template_name",str(template_name))
        output_file=output_file.replace("process_id",str(process_id))
        output_file=output_file.replace("product_name",str(product_name))

        # Output_file_Directory
        if "/" in output_file:
            Path(output_file).mkdir(parents=True, exist_ok=True)
        elif "\\" in output_file:
            Path(output_file).mkdir(parents=True, exist_ok=True)
        # input_file=input_file+"/outliers.csv"
        output_file=output_file+"/encoding.csv"

        #module process
        spark = SparkSession.builder.getOrCreate()
        df = spark.read.csv(input_file,inferSchema =True,header=True)
        print(len(df.columns))
        
        CONT_COLS_NAMES=[]
        STRING_COLS_NAMES=[]
        for i in df.dtypes:
            if label_col not in i:
                if i[1] == "string":
                    STRING_COLS_NAMES.append(i[0])
                else:
                    CONT_COLS_NAMES.append(i[0])
        
        si = []
        ohe = []
        out_cols = []
        for i in STRING_COLS_NAMES:
            stage = StringIndexer(inputCol= i, outputCol= "".join([i,"_index"]))
            si.append(stage)
            ohe.append(stage.getOutputCol())
            out_cols.append("".join([i,"_encoded"]))
        
        in_out_cols = [*out_cols,*CONT_COLS_NAMES]
        oheout = OneHotEncoder(inputCols=ohe, outputCols= out_cols)
        vecass = VectorAssembler(inputCols=in_out_cols, outputCol='features')
        regression_pipeline = Pipeline(stages=[*si,oheout,vecass])
        ppmodel = regression_pipeline.fit(df)
        data = ppmodel.transform(df)
        print(data.select('features').show(1))

        #WritingCSV
        data1=data.toPandas()
        data1.to_csv(output_file,index=False)
        df1 = pd.read_csv(output_file)
        # create_table(table_name,df1)
        # df_tosql(table_name,df1)
        file_size = get_file_size(output_file)
        checksum = get_checksum(output_file)
        response['status'] = status.HTTP_200_OK
        response['encoding_status'] = ['Encoding Completed']
        response['file_size'] = file_size
        response['checksum'] = checksum
        response['error_message'] = ''
        
    except Exception as e:
        response['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
        response['encoding_status'] = 'Failed'
        response['file_size'] = ''
        response['checksum'] = ''
        response['error_message'] = [str(e), 'Error occured while encoding. Please check the debug logs']

    finally:
        audit = EncoderAudit(**response)
        audit.save()        
    
    return response




def Encoding_MP(request):
    response = request
    try:
        logger.info("Encoding Module Started Successfuly MP")
        ProcessId = request.get('ProcessId')
        ModelType = request.get('ModelType')
        File1 = request.get('File1')
        File2 = request.get('File2')
        OutputFile = request.get('OutputFile')
        ModelFile = request.get('ModelFile')
        TemplateName = request.get('TemplateName')
        AlgorithmName = request.get('AlgorithmName')
        Handle_Unknown = request.get('Handle_Unknown')
        logger.info("Request Got It Successfully For Encoding Module")

        # Output_file_Directory
        logger.info("Output Directory Process")
        if "/" in OutputFile:
            OutputFile = "/".join((OutputFile,ProcessId,TemplateName,AlgorithmName,"Encoding"))
            ModelFile = "/".join((ModelFile,ProcessId,TemplateName,AlgorithmName,"EncodingModel"))
            Path(OutputFile).mkdir(parents=True, exist_ok=True)

        elif "\\"  in OutputFile:
            OutputFile = "\\".join((OutputFile,ProcessId,TemplateName,AlgorithmName,"Encoding"))
            ModelFile = "\\".join((ModelFile,ProcessId,TemplateName,AlgorithmName,"EncodingModel"))
            Path(OutputFile).mkdir(parents=True, exist_ok=True)
        logger.info("Output Directory Process Completed")
        
        # Module process
        logger.info("Encoding Module Process")
        logger.info("Reading The Input Files")
        InputDataFrame = pd.read_csv(File1)
        Rows_Count,Columns_Count=InputDataFrame.shape
        logger.info("InputDataFrame Rows {} And Columns {}".format(Rows_Count,Columns_Count))
        logger.info("Calling The Reduce Memory Function")
        InputDataFrame=Reduce_Memory_Usage(InputDataFrame)

        logger.info("Reading The Output Files")
        OutputDataFrame = pd.read_csv(File2)
        Rows_Count,Columns_Count=OutputDataFrame.shape
        logger.info("OutputDataFrame Rows {} And Columns {}".format(Rows_Count,Columns_Count))
        logger.info("Calling The Reduce Memory Function")
        OutputDataFrame=Reduce_Memory_Usage(OutputDataFrame)      
        
        logger.info("Spliting The Categorical And Continous")
        CategoricalDataFrame=InputDataFrame.select_dtypes(include=['object','category'])
        Rows_Count,Columns_Count=CategoricalDataFrame.shape
        logger.info("CategoricalDataFrame Rows {} And Columns {}".format(Rows_Count,Columns_Count))

        ContinousDataFrame=InputDataFrame.select_dtypes(exclude=['object','category'])
        Rows_Count,Columns_Count=ContinousDataFrame.shape
        logger.info("ContinousDataFrame Rows {} And Columns {}".format(Rows_Count,Columns_Count))
        
        logger.info("Encoding Process")
        encoder = OneHotEncoder(sparse = False , handle_unknown = Handle_Unknown)
        encoder.fit(CategoricalDataFrame)
        CategoricalEncodedDataFrame=pd.DataFrame(encoder.transform(CategoricalDataFrame))
        # CategoricalEncodedDataFrame.columns=encoder.get_feature_names_out()
        Rows_Count,Columns_Count=CategoricalEncodedDataFrame.shape
        logger.info("CategoricalEncodedDataFrame Rows {} And Columns {}".format(Rows_Count,Columns_Count))
        logger.info("Encoding Process Completed")
        
        logger.info("Saving The Encoding Process")
        with open(OutputFile+"/"+'ENCODING.pkl','wb') as f:
            pickle.dump(encoder,f)
        logger.info("Saving The CategoricalDataFrame Model Completed")

        logger.info("Merging The ContinousDataFrame And CategoricalDataFrame Process")
        InputDataFrame = pd.concat([ContinousDataFrame,CategoricalEncodedDataFrame],axis=1)
        logger.info("Merging The ContinousDataFrame And CategoricalDataFrame Completed")
        Rows_Count,Columns_Count=InputDataFrame.shape
        logger.info("InputDataFrame Rows {} And Columns {}".format(Rows_Count,Columns_Count))     
        
        logger.info("Exporting The Input And Output DataFrame")
        InputDataFrame.to_csv(OutputFile+"/"+"Input.csv",index=False)
        OutputDataFrame.to_csv(OutputFile+"/"+"Output.csv",index=False)
        
        response['status'] = status.HTTP_200_OK
        response['encoding_status'] = ['Encoding Completed']
        response['error_message'] = ''
        
    except Exception as e:
        response['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
        response['encoding_status'] = 'Failed'
        response['error_message'] = [str(e), 'Error occured while encoding. Please check the debug logs']

    finally:
        audit = EncoderMPAudit(**response)
        audit.save()        
    
    return response