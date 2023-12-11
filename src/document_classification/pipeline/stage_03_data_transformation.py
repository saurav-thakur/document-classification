from document_classification.config.configuration import ConfigurationManager
from document_classification.components.data_transformation import DataTransformation
from document_classification.logging import logger


class DataTransformationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(
                config=data_transformation_config)
            data_transformation.transform_data()
        except Exception as e:
            raise e
