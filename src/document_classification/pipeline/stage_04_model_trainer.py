from document_classification.config.configuration import ConfigurationManager
from document_classification.components.model_trainer import ModelTrainer
from document_classification.logging import logger


class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(
                config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e
