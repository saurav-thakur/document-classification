from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    local_data_file: Path
    cleaned_dataset: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str
    required_files_list: list
    required_files_path: Path


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    ingested_train_csv_file_path: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    tokenizer_path: Path
    save_model_path: Path
    BATCH_SIZE: int
    EPOCHS: int
    CLASSES: int


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metrics_file_name: Path
    mlflow_uri: str
    all_params: dict
