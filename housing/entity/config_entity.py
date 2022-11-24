from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig",["dataset_download_url","tgz_download_url","raw_data_url","ingested_train_dir","ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig",["schema_file_path"])

DataTransforamtionConfig = namedtuple("DataTransforamtionConfig",["add_bedroom_per_room","transformed_train_dir","transformed_test_dir","preprocessed_object_file_path"])

ModelTrainerConfig = namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig",["export_dir_path"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",["artifact_dir"])