from datetime import datetime

import pandas as pd


class PersistenceExcel:
    """
    This class provides functionality to save job details to an Excel file.

    Attributes:
        WRITER_ENGINE (str): The engine used for writing Excel files (default is 'xlsxwriter').
        WRITER_INDEX (bool): Whether to include the DataFrame index in the Excel file (default is False).

    Dependencies:
        - Requires the 'pandas' library for working with DataFrames.
        - The 'datetime' module is used to append the current date and time to the file name.
    """

    WRITER_ENGINE = 'xlsxwriter'
    WRITER_INDEX = False

    @staticmethod
    def save(job_list, file_name):
        """
        Saves a list of job details to an Excel file.

        Parameters:
            job_list (list): List of job details in dictionary format.
            file_name (str): The base name for the Excel file (without extension).

        Returns:
            None

        Note:
            - The current date and time are appended to the file name to ensure uniqueness.
            - The Excel file is saved in the 'output' directory with a '.xlsx' extension.
        """

        # Convert JSON to DataFrame
        df = pd.json_normalize(job_list)

        # Append the current date and time to the file name
        current_datetime = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        file_name = file_name + '_' + current_datetime

        # Save DataFrame to Excel
        writer = pd.ExcelWriter(f'output/{file_name}.xlsx', engine=PersistenceExcel.WRITER_ENGINE)
        df.to_excel(writer, index=PersistenceExcel.WRITER_INDEX)
        writer.save()
