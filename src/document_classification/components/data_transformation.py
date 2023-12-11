from document_classification.logging import logger
from document_classification.entity import DataTransformationConfig
from document_classification.utils.common import read_yaml, create_directories

import numpy as np
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras import Sequential
from keras.layers import Dense, SimpleRNN, Flatten, Embedding, LSTM
from sklearn.model_selection import train_test_split
import pickle
import os


class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config

    def transform_data(self):

        try:

            df = pd.read_csv(self.config.ingested_train_csv_file_path)
            tokenizer = Tokenizer()
            tokenizer.fit_on_texts(df["Letters"])

            # Save the tokenizer as a pickle file in the specified directory
            tokenizer_file_path = os.path.join(
                self.config.root_dir, 'tokenizer.pickle')
            # saving
            with open(tokenizer_file_path, 'wb') as handle:
                pickle.dump(tokenizer, handle,
                            protocol=pickle.HIGHEST_PROTOCOL)

        except Exception as e:
            raise e
