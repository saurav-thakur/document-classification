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
