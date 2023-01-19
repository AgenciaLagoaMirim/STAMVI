import os
from tkinter import filedialog, messagebox

import pandas as pd

DBA_TO_MCA_CONVERSION_CONSTANT = 1.092
CENTIMETER_TO_METER = 0.01


class DatDataProcessing:
    def __init__(self):
        self.dataFrame_dict = {}
        self.dat_dataframe = None
        self.dat_document_directory = None

    def ask_open_dat_file_directory(self):
        messagebox.showinfo(
            "INFO", "Select the folder containing the .dat extension files!"
        )
        self.dat_document_directory = filedialog.askdirectory()

    def get_dat_dataFrames(self):
        file_path_list = []
        files_list = os.listdir(self.dat_document_directory)

        # popula o dicionario com listas vazias
        for i in range(len(files_list)):
            self.dataFrame_dict["list_{}".format(i)] = []

        # popula a lista com os caminhos
        for file in files_list:
            file_path = os.path.join(self.dat_document_directory, file)
            file_path_list.append(file_path)

        for i, file_path in enumerate(file_path_list):
            key = "list_{}".format(i)
            document = pd.read_csv(file_path, sep="\s+")
            dat_dataFrame = document.loc[
                :,
                [
                    "Year",
                    "Month",
                    "Day",
                    "Hour",
                    "Minute",
                    "Second",
                    "VelocityX",
                    "Pressure",
                ],
            ]
            dat_dataFrame["Date"] = pd.to_datetime(
                dat_dataFrame.loc[:, "Year":"Second"]
            )
            self.dataFrame_dict[key].append(dat_dataFrame)
        new_dict = {}
        for key, value in self.dataFrame_dict.items():
            new_key = key.replace("list", "dict")
            new_dict[new_key] = value[0]

        self.dataFrame_dict = new_dict
        result_dict = {"concatenated_dict": pd.concat(self.dataFrame_dict.values())}
        self.dataFrame_dict = result_dict

        print(
            f"ESTE É O DATAFRAME dat_dataframe \n {self.dataFrame_dict['concatenated_dict']}"
        )
        self.dat_dataframe = self.dataFrame_dict["concatenated_dict"]
        self.dat_dataframe = self.dat_dataframe.drop(
            columns=[
                "Year",
                "Month",
                "Day",
                "Hour",
                "Minute",
                "Second",
            ]
        )
        self.dat_dataframe = self.dat_dataframe.reindex(
            columns=[
                "Date",
                "VelocityX",
                "Pressure",
            ]
        )
        self.dat_dataframe["Pressure"] = (
            self.dat_dataframe["Pressure"] * DBA_TO_MCA_CONVERSION_CONSTANT
        )
        self.dat_dataframe["Pressure"] = (
            self.dat_dataframe["Pressure"].round(3)
        )
        self.dat_dataframe["VelocityX"] = (
            self.dat_dataframe["VelocityX"] * CENTIMETER_TO_METER
        )
        self.dat_dataframe["VelocityX"] = (
            self.dat_dataframe["VelocityX"].round(3)
        )

        return self.dat_dataframe
