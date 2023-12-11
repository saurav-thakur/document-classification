from document_classification.entity import ModelEvaluationConfig
from document_classification.logging import logger
import pickle
import pandas as pd
from keras.utils import pad_sequences
import tensorflow as tf


class ModelEvaluation:

    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

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
                sequences=X_sequences, padding="post", maxlen=100)

            model = tf.keras.models.load_model(self.config.model_path)
            # Evaluate the restored model
            loss, acc = model.evaluate(X_padded_sequences, y_mapped, verbose=2)

            with open(self.config.metrics_file_name, "w") as f:
                f.write(f"Loss : {loss} and Accuracy : {acc}")

        except Exception as e:
            raise e
