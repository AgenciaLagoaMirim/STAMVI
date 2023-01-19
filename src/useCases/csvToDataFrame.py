from tkinter import filedialog

import pandas as pd


class CsvToDataFrame:
    def __init__(self):
        self.data_frame = None
        self.file_path = None

    def setup_dataframe(self, filepath):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")]
        )
        print(self.file_path)
        self.data_frame = pd.read_csv(self.file_path)
        return self.data_frame
