from document_classification.constants import *
from document_classification.utils.common import read_yaml, create_directories
from document_classification.entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig
import os


class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 ):

        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            local_data_file=config.local_data_file,
            cleaned_dataset=config.cleaned_dataset,
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            required_files_list=config.required_files_list,
            required_files_path=config.required_files_path,
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            ingested_train_csv_file_path=config.ingested_train_csv_file_path,
        )

        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            tokenizer_path=config.tokenizer_path,
            save_model_path=config.save_model_path,
            BATCH_SIZE=self.params.BATCH_SIZE,
            EPOCHS=self.params.EPOCHS,
            CLASSES=self.params.CLASSES,

        )

        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path=config.model_path,
            tokenizer_path=config.tokenizer_path,
            metrics_file_name=config.metrics_file_name,
            all_params=self.params,
            # set environment variable before using this else this will return None.
            mlflow_uri=os.getenv("MLFLOW_TRACKING_URI")



        )

        return model_evaluation_config
