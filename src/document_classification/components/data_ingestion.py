import os
import numpy as np
import pandas as pd
from document_classification.logging import logger
from document_classification.utils.common import get_file_size, create_directories
from document_classification.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # the function to collect the data
    def data_collection(self) -> pd.DataFrame:
        data = []
        labels = []

        classes = []

        for i in os.listdir(self.config.local_data_file):
            classes.append(i)

        splitted_path = os.path.split(self.config.local_data_file)[0]

        # iterating through each class
        for each_class in classes:
            file_dir = f"{splitted_path}/ocr/{each_class}"

            for i in os.listdir(file_dir):
                with open(os.path.join(file_dir, i), 'r', encoding="utf-8") as f:

                    # removing the unwanted spaces from left and right
                    lines = [line.strip()
                             for line in f.readlines() if line.strip()]

                    concatenated_lines = ' '.join(lines)
                    data.append(concatenated_lines)
                    labels.append(each_class)
            print(f"{each_class} label is done!!")
        logger.info(f"Data collection is done")

        df = pd.DataFrame({"Letters": data, "Target": labels})

        # shuffling the data
        df = df.sample(frac=1).reset_index(drop=True)

        # replacing empty string with nan
        df["Letters"] = df["Letters"].replace({"": np.nan})

        null_in_letters = df.isnull().sum()["Letters"]
        null_in_target = df.isnull().sum()["Target"]

        logger.info(f"Letters consists of {null_in_letters} null values.")
        logger.info(f"Target consists of {null_in_target} null values.")

        # dropping nan values
        df.dropna(inplace=True, axis=0)

        logger.info(
            f"NaN values has been dropped and clean dataset is returned.")

        return df

    def collect_clean_and_save_data(self, dataset_name):
        file_saving_dir = self.config.cleaned_dataset
        dataset_directory = self.config.local_data_file

        create_directories([file_saving_dir])

        logger.info("Preprocessing Dataset")
        preprocessed_dataframe = self.data_collection()

        logger.info(
            f"Dataset Preprocessed and now saving to {file_saving_dir} as {dataset_name}")
        preprocessed_dataframe.to_csv(
            f"{file_saving_dir}/{dataset_name}", index=False)
