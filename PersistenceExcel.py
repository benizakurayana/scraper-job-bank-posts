from datetime import datetime

import pandas as pd


class PersistenceExcel:
    WRITER_ENGINE = 'xlsxwriter'
    WRITER_INDEX = False

    @staticmethod
    def save(job_list, file_name):
        # Convert JSON to DataFrame
        df = pd.json_normalize(job_list)

        # Append the current date and time to the file name
        current_datetime = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        file_name = file_name + '_' + current_datetime

        # Save DataFrame to Excel
        writer = pd.ExcelWriter(f'output/{file_name}.xlsx', engine=PersistenceExcel.WRITER_ENGINE)
        df.to_excel(writer, index=PersistenceExcel.WRITER_INDEX)
        writer.save()
