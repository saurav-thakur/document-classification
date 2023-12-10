from document_classification.config.configuration import ConfigurationManager
from document_classification.components.data_ingestion import DataIngestion
from document_classification.logging import logger


class DataIngestionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.collect_clean_split_and_save_data(
                train_data_name="train.csv", test_data_name="test.csv")

        except Exception as e:
            raise e
