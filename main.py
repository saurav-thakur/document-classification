from document_classification.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from document_classification.pipeline.stage_02_data_validation import DataValidationPipeline
from document_classification.pipeline.stage_03_data_transformation import DataTransformationPipeline
from document_classification.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from document_classification.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
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


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(
        f">>>>>> {STAGE_NAME} Completed <<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(
        f">>>>>> {STAGE_NAME} Completed <<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(
        f">>>>>> {STAGE_NAME} Completed <<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e
