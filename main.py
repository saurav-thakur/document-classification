from document_classification.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from document_classification.pipeline.stage_02_data_validation import DataValidationPipeline
from document_classification.logging import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(
        f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(
        f">>>>>> {STAGE_NAME} Completed <<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e
