import numpy as np
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras import Sequential
from keras.layers import Dense, SimpleRNN, Flatten, Embedding, LSTM
from sklearn.model_selection import train_test_split
import pickle
import os

from document_classification.config.configuration import ModelTrainerConfig


class ModelTrainer:

    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):

        try:
            with open(self.config.tokenizer_path, 'rb') as handle:
                tokenizer = pickle.load(handle)

            df = pd.read_csv(self.config.train_data_path)
            X = df["Letters"]
            y = df["Target"]

            y_mapped = y.map({
                0: 0,
                2: 1,
                4: 2,
                6: 3,
                9: 4
            })

            X_train, X_test, y_train, y_test = train_test_split(
                X, y_mapped, test_size=0.2, random_state=42)
            X_train_sequences = tokenizer.texts_to_sequences(X_train)
            X_test_sequences = tokenizer.texts_to_sequences(X_test)

            X_train_padded_sequences = pad_sequences(
                sequences=X_train_sequences, padding="post", maxlen=60)
            X_test_padded_sequences = pad_sequences(
                sequences=X_test_sequences, padding="post", maxlen=60)

            vocab_size = len(tokenizer.word_index) + 1
            model = Sequential()
            model.add(Embedding(input_dim=vocab_size,
                      output_dim=50, input_length=60))
            model.add(LSTM(units=50, return_sequences=True))
            model.add(LSTM(units=50))
            model.add(Dense(units=self.config.CLASSES, activation='softmax'))

            model.compile(loss='sparse_categorical_crossentropy',
                          optimizer='adam', metrics=['accuracy'])
            model.fit(X_train_padded_sequences, y_train, epochs=self.config.EPOCHS, batch_size=self.config.BATCH_SIZE,
                      validation_data=(X_test_padded_sequences, y_test))

            # Save the entire model as a `.keras` zip archive.
            model.save(self.config.save_model_path)

        except Exception as e:
            raise e
