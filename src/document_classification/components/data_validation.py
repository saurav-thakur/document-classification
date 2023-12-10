from document_classification.logging import logger
import os
from document_classification.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exists(self) -> bool:
        try:
            validation_status = None
            all_files = os.listdir(self.config.required_files_path)

            for file in all_files:
                if file not in self.config.required_files_list:
                    validation_status = False
                    with open(self.config.status_file, "w") as f:
                        f.write(f"Validation Status : {validation_status}")

                else:
                    validation_status = True
                    with open(self.config.status_file, "w") as f:
                        f.write(f"Validation Status : {validation_status}")

            return validation_status

        except Exception as e:
            raise e
