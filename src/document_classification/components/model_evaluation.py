from document_classification.entity import ModelEvaluationConfig
from document_classification.logging import logger
import pickle
import pandas as pd
from keras.utils import pad_sequences
import tensorflow as tf
import mlflow
from urllib.parse import urlparse
import mlflow.keras


class ModelEvaluation:

    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        self.loss = None
        self.accuracy = None
        self.model = None

    def get_model_evaluation(self):
        try:
            with open(self.config.tokenizer_path, 'rb') as handle:
                tokenizer = pickle.load(handle)
            df = pd.read_csv(self.config.data_path)
            X = df["Letters"]
            y = df["Target"]

            y_mapped = y.map({
                0: 0,
                2: 1,
                4: 2,
                6: 3,
                9: 4
            })
            X_sequences = tokenizer.texts_to_sequences(X)
            X_padded_sequences = pad_sequences(
                sequences=X_sequences, padding="post", maxlen=60)

            self.model = tf.keras.models.load_model(self.config.model_path)
            # Evaluate the restored model
            self.loss, self.accuracy = self.model.evaluate(
                X_padded_sequences, y_mapped, verbose=2)

            with open(self.config.metrics_file_name, "w") as f:
                f.write(f"Loss : {self.loss} and Accuracy : {self.accuracy}")

        except Exception as e:
            raise e

    def log_score_into_mlflow(self):
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {"loss": self.loss, "accuracy": self.accuracy}
            )

            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                logger.info("Model is being logged to MLFLOW")
                mlflow.keras.log_model(
                    self.model, "model", registered_model_name="LSTM")
            else:
                mlflow.keras.log_model(self.model, "model")
