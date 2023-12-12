from document_classification.config.configuration import ConfigurationManager
from document_classification.components.model_evaluation import ModelEvaluation
from document_classification.logging import logger


class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(
                config=model_evaluation_config)
            model_evaluation.get_model_evaluation()
            model_evaluation.log_score_into_mlflow()
        except Exception as e:
            raise e
