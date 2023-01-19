from tkinter import filedialog

import pandas as pd


class XlsxToDataFrame:
    def __init__(self):
        self.data_frame = None
        self.file_path = None

    def setup_dataframe(self, filepath):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("XLSX Files", "*.xlsx")]
        )
        print(self.file_path)
        self.data_frame = pd.read_excel(self.file_path)
        return self.data_frame
