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
            data_ingestion.collect_clean_and_save_data(
                dataset_name="text_dataset.csv")

        except Exception as e:
            raise e
