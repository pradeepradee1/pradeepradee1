from django.db import models
from django.utils import timezone
# Create your models here.

class TransposeAudit(models.Model):
    ProcessId = models.CharField(max_length=150)
    RunningAccountTranscationFile = models.CharField(max_length=250)
    JLAccountTranscationFile = models.CharField(max_length=150)
    RunningAccountTranscationColumns = models.CharField(max_length=150)
    JLAccountTranscationColumns = models.CharField(max_length=150)
    OtherAcccountMonths = models.CharField(max_length=150)
    JLAccountMonths = models.CharField(max_length=150)
    ResetIndex = models.CharField(max_length=150)
    Iteration = models.CharField(max_length=150)
    Iteration1 = models.CharField(max_length=150)
    Template = models.CharField(max_length=150)
    JLTableName = models.CharField(max_length=150)
    OtherAccountTableName = models.CharField(max_length=150)
    MappingTable = models.CharField(max_length=150)
    MonthTable = models.CharField(max_length=150)
    OutputFile = models.CharField(max_length=150)
    Product = models.CharField(max_length=150)
    CallbackURL = models.CharField(max_length=150)
    Status = models.CharField(max_length=150)
    TransposeStatus = models.CharField(max_length=150)
    ErrorMessage = models.TextField(blank=True, null=True)


class TransposeMPAudit(models.Model):
    ProcessId = models.CharField(max_length=150)
    InputFile = models.CharField(max_length=250)
    OutputFile = models.CharField(max_length=150)
    OutputDirectory = models.CharField(max_length=150)
    InputUniqueValuesColumns = models.CharField(max_length=1000)
    InputTransposeValues = models.CharField(max_length=1000)
    InputTransposeColumns = models.CharField(max_length=1000)
    LabelEncodingColumns = models.CharField(max_length=1000)
    LabelEncodingColumnsFillValue = models.CharField(max_length=1000)
    OutputTransposeIndex = models.CharField(max_length=1000)
    OutputTransposeColumn = models.CharField(max_length=1000)
    OutputTransposeValues = models.CharField(max_length=1000)
    ModuleName = models.CharField(max_length=150)
    Template = models.CharField(max_length=150)
    Product = models.CharField(max_length=150)
    CallbackURL = models.CharField(max_length=150)
    Status = models.CharField(max_length=150)
    TransposeStatus = models.CharField(max_length=150)
    ErrorMessage = models.TextField(blank=True, null=True)



class SamplingAudit(models.Model):
    ProcessId = models.CharField(max_length=150)
    InputFile = models.CharField(max_length=250)
    OutputDirectory = models.CharField(max_length=150)
    OutputFeatureNames = models.CharField(max_length=1000)
    OutputType = models.CharField(max_length=1000)
    SamplingType = models.CharField(max_length=1000)
    ModuleName = models.CharField(max_length=1000)
    ModuleEnable = models.CharField(max_length=1000)
    Template = models.CharField(max_length=1000)
    Product = models.CharField(max_length=1000)
    CallbackURL = models.CharField(max_length=150)
    Status = models.CharField(max_length=150)
    SamplingStatus = models.CharField(max_length=150)
    ErrorMessage = models.TextField(blank=True, null=True)


class CleanserAudit(models.Model):
    ProcessId = models.CharField(max_length=150)
    ModelType = models.CharField(max_length=150)
    InputFile = models.CharField(max_length=150)
    OutputFile = models.CharField(max_length=150)
    ModelFile = models.CharField(max_length=150)
    TemplateName = models.CharField(max_length=150)
    ProductName = models.CharField(max_length=150)
    AlgorithmName = models.CharField(max_length=150)
    CleansingDFTableName = models.CharField(max_length=150)
    CleansingFeaturesList = models.CharField(max_length=150)
    ColumnNameForFeaturesList = models.CharField(max_length=150)
    Strategy = models.CharField(max_length=150)
    LowerRange = models.CharField(max_length=150)
    UpperRange = models.CharField(max_length=150)
    HeapMemorySize = models.CharField(max_length=150)
    StackMemorySize = models.CharField(max_length=150)
    Status = models.CharField(max_length=150)
    CleansingStatus = models.CharField(max_length=150)
    CallbackURL = models.CharField(max_length=150)
    CallbackStatus = models.CharField(max_length=150)
    ErrorMessage = models.TextField(blank=True, null=True)
    UpdatedDate = models.DateTimeField(default=timezone.now)


class CleanserMPAudit(models.Model):
    ProcessId = models.CharField(max_length=150)
    ModelType = models.CharField(max_length=150)
    File1 = models.CharField(max_length=150)
    File2 = models.CharField(max_length=150)
    OutputFile = models.CharField(max_length=150)
    ModelFile = models.CharField(max_length=150)
    TemplateName = models.CharField(max_length=150)
    AlgorithmName = models.CharField(max_length=150)
    LowerRangePercentage = models.CharField(max_length=150)
    UpperRangePercentage = models.CharField(max_length=150)
    Strategy = models.CharField(max_length=150)
    DateFeatures = models.CharField(max_length=150)
    OutputFeaturesList = models.CharField(max_length=500)
    DropedFeatures = models.CharField(max_length=2000)
    Status = models.CharField(max_length=150)
    CleansingStatus = models.CharField(max_length=150)
    CallbackURL = models.CharField(max_length=150)
    CallbackStatus = models.CharField(max_length=150)
    ErrorMessage = models.TextField(blank=True, null=True)
    UpdatedDate = models.DateTimeField(default=timezone.now)

class OutlierAudit(models.Model):
    ProcessId = models.CharField(max_length=150)
    InputFile = models.CharField(max_length=150)
    OutputFile = models.CharField(max_length=150)
    ProductName = models.CharField(max_length=150)
    TableName = models.CharField(max_length=150)
    AlgorithmName = models.CharField(max_length=150)
    AlgorithmType = models.CharField(max_length=150)
    TemplateName = models.CharField(max_length=150)
    OutliersColumns = models.CharField(max_length=150)
    OutliersType = models.CharField(max_length=150)
    OutliersOptions = models.CharField(max_length=150)
    Q1 = models.CharField(max_length=150)
    Q2 = models.CharField(max_length=150)
    HeapMemorySize = models.CharField(max_length=150)
    StackMemorySize = models.CharField(max_length=150)
    Status = models.CharField(max_length=150)
    OutlierStatus = models.CharField(max_length=150)
    CallbackURL = models.CharField(max_length=150)
    CallbackStatus = models.CharField(max_length=150)
    ErrorMessage = models.TextField(blank=True, null=True)
    UpdatedDate = models.DateTimeField(default=timezone.now)

class EncoderAudit(models.Model):
    process_id = models.CharField(max_length=150)
    input_file = models.CharField(max_length=150)
    output_file = models.CharField(max_length=150)
    input_cols = models.TextField(blank=True, null=False)
    output_cols = models.TextField(blank=True, null=False)
    algorithm_name = models.CharField(max_length=150)
    template_name = models.CharField(max_length=150)
    product_name = models.CharField(max_length=150)
    label_col = models.CharField(max_length=150)
    table_name = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    encoding_status = models.CharField(max_length=150)
    callback_url = models.CharField(max_length=150)
    callback_status = models.CharField(max_length=150)
    file_size = models.CharField(max_length=150)
    checksum = models.CharField(max_length=150)
    error_message = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(default=timezone.now)

class EncoderMPAudit(models.Model):
    ProcessId = models.CharField(max_length=150)
    ModelType = models.CharField(max_length=150)
    File1 = models.CharField(max_length=150)
    File2 = models.CharField(max_length=150)
    OutputFile = models.CharField(max_length=150)
    ModelFile = models.CharField(max_length=150)
    TemplateName = models.CharField(max_length=150)
    AlgorithmName = models.CharField(max_length=150)
    Handle_Unknown = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    encoding_status = models.CharField(max_length=150)
    callback_url = models.CharField(max_length=150)
    callback_status = models.CharField(max_length=150)
    error_message = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(default=timezone.now)


class FeatureselecionAudit(models.Model):
    process_id = models.CharField(max_length=150)
    input_file = models.CharField(max_length=150)
    output_file = models.CharField(max_length=150)
    feature_seletion_type = models.CharField(max_length=150)
    feature_selection_list = models.CharField(max_length=150)
    label_col = models.CharField(max_length=150)
    input_cols = models.TextField(blank=True, null=False)
    output_cols = models.TextField(blank=True, null=False)
    algorithm_name = models.CharField(max_length=150)
    template_name = models.CharField(max_length=150)
    product_name = models.CharField(max_length=150)
    table_name = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    feature_status = models.CharField(max_length=150)
    callback_url = models.CharField(max_length=150)
    callback_status = models.CharField(max_length=150)
    file_size = models.CharField(max_length=150)
    checksum = models.CharField(max_length=150)
    error_message = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(default=timezone.now)


class ScalarAudit(models.Model):
    process_id = models.CharField(max_length=150)
    input_file = models.CharField(max_length=150)
    output_file = models.CharField(max_length=150)
    feature_seletion_type = models.CharField(max_length=150)
    feature_selection_list = models.CharField(max_length=150)
    label_col = models.CharField(max_length=150)
    input_cols = models.TextField(blank=True, null=False)
    output_cols = models.TextField(blank=True, null=False)
    algorithm_name = models.CharField(max_length=150)
    template_name = models.CharField(max_length=150)
    product_name = models.CharField(max_length=150)
    table_name = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    scalar_status = models.CharField(max_length=150)
    callback_url = models.CharField(max_length=150)
    callback_status = models.CharField(max_length=150)
    file_size = models.CharField(max_length=150)
    checksum = models.CharField(max_length=150)
    error_message = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(default=timezone.now)


class ScalerMPAudit(models.Model):
    ProcessId = models.CharField(max_length=150)
    ModelType = models.CharField(max_length=150)
    File1 = models.CharField(max_length=150)
    File2 = models.CharField(max_length=150)
    OutputFile = models.CharField(max_length=150)
    ModelFile = models.CharField(max_length=150)
    TemplateName = models.CharField(max_length=150)
    AlgorithmName = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    scalar_status = models.CharField(max_length=150)
    callback_url = models.CharField(max_length=150)
    callback_status = models.CharField(max_length=150)
    error_message = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(default=timezone.now)

class TrainAudit(models.Model):
    process_id = models.CharField(max_length=150)
    input_file = models.CharField(max_length=150)
    train_file = models.CharField(max_length=150)
    output_file = models.CharField(max_length=150)
    test_file = models.CharField(max_length=150)
    encoding_path = models.CharField(max_length=150)
    feature_selection_path = models.CharField(max_length=150)
    scalar_path = models.CharField(max_length=150)
    model_path = models.CharField(max_length=150)
    feature_seletion_type = models.CharField(max_length=150)
    feature_selection_list = models.CharField(max_length=150)
    input_cols = models.TextField(blank=True, null=False)
    output_cols = models.TextField(blank=True, null=False)
    algorithm_name = models.CharField(max_length=150)
    algorithm_type = models.CharField(max_length=150)
    template_name = models.CharField(max_length=150)
    product_name = models.CharField(max_length=150)
    train_table_name = models.CharField(max_length=150)
    max_depth = models.IntegerField()
    max_bins = models.IntegerField()
    num_trees = models.IntegerField()
    label_col = models.CharField(max_length=150)
    feature_col = models.CharField(max_length=150)
    metrics_name = models.CharField(max_length=150)
    prediction_score = models.CharField(max_length=150)
    test_table_name = models.CharField(max_length=150)
    handleinvalid = models.CharField(max_length=150)
    HeapMemorySize = models.CharField(max_length=150)
    StackMemorySize = models.CharField(max_length=150)    
    status = models.CharField(max_length=150)
    train_status = models.CharField(max_length=150)
    callback_url = models.CharField(max_length=150)
    callback_status = models.CharField(max_length=150)
    train_file_size = models.CharField(max_length=150)
    test_file_size = models.CharField(max_length=150)
    train_checksum = models.CharField(max_length=150)
    test_checksum = models.CharField(max_length=150)
    error_message = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(default=timezone.now)


class TrainMPAudit(models.Model):
    ProcessId = models.CharField(max_length=150)
    ModelType = models.CharField(max_length=150)
    File1 = models.CharField(max_length=150)
    File2 = models.CharField(max_length=150)
    OutputFile = models.CharField(max_length=150)
    ModelFile = models.CharField(max_length=150)
    TemplateName = models.CharField(max_length=150)
    AlgorithmName = models.CharField(max_length=150)
    AlgorithmType = models.CharField(max_length=150)
    TestSize = models.CharField(max_length=150)
    RandomStatePattern = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    train_status = models.CharField(max_length=150)
    callback_url = models.CharField(max_length=150)
    callback_status = models.CharField(max_length=150)
    error_message = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(default=timezone.now)

class TestAudit(models.Model):
    process_id = models.CharField(max_length=150)
    input_file = models.CharField(max_length=150)
    output_file = models.CharField(max_length=150)
    model_path = models.CharField(max_length=150)
    encoding_path = models.CharField(max_length=150)
    scalar_path = models.CharField(max_length=150)
    feature_seletion_type = models.CharField(max_length=150)
    feature_selection_list = models.CharField(max_length=150)
    algorithm_name = models.CharField(max_length=150)
    algorithm_type = models.CharField(max_length=150)
    template_name = models.CharField(max_length=150)
    product_name = models.CharField(max_length=150)
    label_col = models.CharField(max_length=150)
    metrics_name = models.CharField(max_length=150)
    prediction_score = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    test_status = models.CharField(max_length=150)
    callback_url = models.CharField(max_length=150)
    callback_status = models.CharField(max_length=150)
    error_message = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(default=timezone.now)
    handleinvalid = models.CharField(max_length=150)

class TestMPAudit(models.Model):
    ProcessId = models.CharField(max_length=150)
    ModelType = models.CharField(max_length=150)
    TestingFile = models.CharField(max_length=150)
    ActualFile = models.CharField(max_length=150)
    OutputFile = models.CharField(max_length=150)
    ModelFile = models.CharField(max_length=150)
    TemplateName = models.CharField(max_length=150)
    AlgorithmName = models.CharField(max_length=150)
    AlgorithmType = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    test_status = models.CharField(max_length=150)
    callback_url = models.CharField(max_length=150)
    callback_status = models.CharField(max_length=150)
    error_message = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(default=timezone.now)

class EvaluationAudit(models.Model):
    process_id = models.CharField(max_length=150)
    input_file = models.CharField(max_length=150)
    Imputer_path = models.CharField(max_length=150)
    encoding_path = models.CharField(max_length=150)
    feature_selection_path = models.CharField(max_length=150)
    scalar_path = models.CharField(max_length=150)
    model_path = models.CharField(max_length=150)
    output_file = models.CharField(max_length=150)
    Cleansing_Features_list = models.CharField(max_length=150)
    algorithm_name = models.CharField(max_length=150)
    algorithm_type = models.CharField(max_length=150)
    template_name = models.CharField(max_length=150)
    label_col = models.CharField(max_length=150)
    output_features = models.CharField(max_length=150)
    prediction_score = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    evaluation_status = models.CharField(max_length=150)
    callback_url = models.CharField(max_length=150)
    callback_status = models.CharField(max_length=150)
    output_file_size = models.CharField(max_length=150)
    output_file_checksum = models.CharField(max_length=150)
    error_message = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(default=timezone.now)
    table_name = models.CharField(max_length=150)
    product_name = models.CharField(max_length=150)
    customer_case = models.CharField(max_length=150)
    Customer_id = models.CharField(max_length=150)
    purpose = models.CharField(max_length=150)




class EvaluationMPAudit(models.Model):
    ProcessId = models.CharField(max_length=150)
    ModelType = models.CharField(max_length=150)
    InputFile = models.CharField(max_length=150)
    CategoricalImputerFile = models.CharField(max_length=150)
    ContinousImputerFile = models.CharField(max_length=150)
    EncodingFile = models.CharField(max_length=150)
    ScalingFile = models.CharField(max_length=150)
    ModelFile = models.CharField(max_length=150)
    OutputFile = models.CharField(max_length=150)
    DropedFeatures = models.CharField(max_length=150)
    CustomerIdFeatures = models.CharField(max_length=150)
    TemplateName = models.CharField(max_length=150)
    AlgorithmName = models.CharField(max_length=150)
    AlgorithmType = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    evaluation_status = models.CharField(max_length=150)
    callback_url = models.CharField(max_length=150)
    callback_status = models.CharField(max_length=150)
    error_message = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(default=timezone.now)