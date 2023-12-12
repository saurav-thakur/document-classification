from document_classification.logging import logger
import pickle
import numpy as np
import pandas as pd
from keras.utils import pad_sequences
import tensorflow as tf
from document_classification.config.configuration import ConfigurationManager


class PredictionPipeline:
    def __init__(self):
        configuration_manager = ConfigurationManager()
        self.config = configuration_manager.get_model_evaluation_config()

    def predict(self, text):
        try:
            text = [text]
            text = np.array(text)

            logger.info("Loading Tokenizer and model")
            with open(self.config.tokenizer_path, 'rb') as handle:
                tokenizer = pickle.load(handle)
            model = tf.keras.models.load_model(self.config.model_path)

            logger.info("Model and Tokenizer loaded sucessfully.")
            logger.info("Performing Data Transformation")
            text_sequences = tokenizer.texts_to_sequences(text)
            text_padded_sequences = pad_sequences(
                sequences=text_sequences, padding="post", maxlen=60)

            logger.info("Data Transformation Completed.")

            logger.info("Predicting the document type")
            prediction_probabilites = model.predict(text_padded_sequences)
            final_prediction = np.argmax(prediction_probabilites, axis=1)
            print(prediction_probabilites, "-------------------")

            print(f"FINAL PREDICTION OF DOCUMENT TYPE IS : {final_prediction}")

            map_final_prediciton = {
                0: 0,
                1: 2,
                2: 4,
                3: 6,
                4: 9
            }

            print("THIS IS FINAL ANS",
                  map_final_prediciton[final_prediction[0]])

            return map_final_prediciton[final_prediction[0]]

        except Exception as e:
            raise e
