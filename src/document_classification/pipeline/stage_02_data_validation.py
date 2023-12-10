from document_classification.config.configuration import ConfigurationManager
from document_classification.components.data_validation import DataValidation
from document_classification.logging import logger


class DataValidationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_files_exists()

        except Exception as e:
            raise e
