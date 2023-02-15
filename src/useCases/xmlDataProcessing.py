import os
import xml.etree.ElementTree as et
from datetime import datetime as dt
from tkinter import filedialog, messagebox

import numpy as np
import pandas as pd


class XmlDataProcessing:
    def __init__(self):
        self.input_format = "%m/%d/%Y %H:%M:%S"
        self.output_format = "%Y-%m-%d %H:%M:%S"
        self.mean_area_list = []
        self.meanQoverA_list = []
        self.start_date_time_list = []
        self.end_date_time_list = []
        self.mean_area_dict = {}
        self.meanOvearA_dict = {}
        self.start_date_time_dict = {}
        self.end_date_time_dict = {}
        self.xml_document_directory = None
        self.filtered_mean_area_list = None
        self.filtered_meanQoverA_list = None
        self.flow_rate_list = None
        self.average_velocity_list = None

    def ask_open_xml_file_directory(self):
        messagebox.showinfo(
            "INFO", "Select the folder containing the .xml extension files!"
        )
        self.xml_document_directory = filedialog.askdirectory()

    def set_mean_area_values(self):

        file_path_list = []
        files_list = os.listdir(self.xml_document_directory)

        # popula o dicionario com listas vazias
        for i in range(len(files_list)):
            self.mean_area_dict["list_{}".format(i)] = []

        # popula a lista com os caminhos
        for file in files_list:
            file_path = os.path.join(self.xml_document_directory, file)
            file_path_list.append(file_path)

        for i, file_path in enumerate(file_path_list):
            key = "list_{}".format(i)
            document = et.parse(file_path)
            for other in document.iterfind(".//Other"):
                self.mean_area_dict[key].append(other.findtext("MeanArea"))

        for key in self.mean_area_dict:
            self.mean_area_dict[key] = [
                item for item in self.mean_area_dict[key] if item is not None
            ]

        for key, value in self.mean_area_dict.items():
            self.mean_area_list.extend(value)
            self.mean_area_list = [float(i) for i in self.mean_area_list]

        # print(f"MEAN_AREA_DICT {self.mean_area_dict}")
        print(f"MEAN_AREA_LIST {self.mean_area_list}")
        # return self.mean_area_list

    def set_meanQoverA_values(self):
        file_path_list = []
        files_list = os.listdir(self.xml_document_directory)

        # popula o dicionario com listas vazias
        for i in range(len(files_list)):
            self.meanOvearA_dict["list_{}".format(i)] = []

        # popula lista com os caminhos
        for file in files_list:
            file_path = os.path.join(self.xml_document_directory, file)
            file_path_list.append(file_path)

        for i, file_path in enumerate(file_path_list):
            key = "list_{}".format(i)
            document = et.parse(file_path)
            for other in document.iterfind(".//Other"):
                self.meanOvearA_dict[key].append(other.findtext("MeanQoverA"))

        for key in self.meanOvearA_dict:
            self.meanOvearA_dict[key] = [
                item for item in self.meanOvearA_dict[key] if item is not None
            ]

        for key, value in self.meanOvearA_dict.items():
            self.meanQoverA_list.extend(value)
            self.meanQoverA_list = [float(i) for i in self.meanQoverA_list]

        print(f"MEAN_OVER_A_LIST {self.meanQoverA_list}")
        # return self.meanQoverA_list

    def set_start_date_time_values(self):

        file_path_list = []
        files_list = os.listdir(self.xml_document_directory)

        # popula o dicionario com listas vazias
        for i in range(len(files_list)):
            self.start_date_time_dict["list_{}".format(i)] = []

        # popula a lista com os caminhos
        for file in files_list:
            file_path = os.path.join(self.xml_document_directory, file)
            file_path_list.append(file_path)

        for i, file_path in enumerate(file_path_list):
            key = "list_{}".format(i)
            document = et.parse(file_path)
            for transect in document.iterfind("Transect"):
                self.start_date_time_dict[key].append(
                    transect.findtext("StartDateTime")
                )

        for key, value in self.start_date_time_dict.items():
            for i, date_string in enumerate(value):
                date = dt.strptime(date_string, self.input_format)
                converted_date_string = date.strftime(self.output_format)
                value[i] = converted_date_string

        for key, value in self.start_date_time_dict.items():
            date_time_objects = [
                dt.strptime(date_time, "%Y-%m-%d %H:%M:%S") for date_time in value
            ]
            timestamps = [date_time.timestamp() for date_time in date_time_objects]
            avarage_time = sum(timestamps) / len(timestamps)
            avarage_time = dt.fromtimestamp(avarage_time)
            self.start_date_time_dict[key] = [
                avarage_time.strftime("%Y-%m-%d %H:%M:%S")
            ]

        for key, value in self.start_date_time_dict.items():
            self.start_date_time_list.extend(value)

        print(f"START_DATE_TIME_LIST {self.start_date_time_list}")
        # return self.start_date_time_list

    def set_end_date_time_values(self):

        file_path_list = []
        files_list = os.listdir(self.xml_document_directory)

        # popula o dicionario com listas vazias
        for i in range(len(files_list)):
            self.end_date_time_dict["list_{}".format(i)] = []

        # popula a lista com os caminhos
        for file in files_list:
            file_path = os.path.join(self.xml_document_directory, file)
            file_path_list.append(file_path)

        for i, file_path in enumerate(file_path_list):
            key = "list_{}".format(i)
            document = et.parse(file_path)
            for transect in document.iterfind("Transect"):
                self.end_date_time_dict[key].append(transect.findtext("EndDateTime"))

        for key, value in self.end_date_time_dict.items():
            for i, date_string in enumerate(value):
                date = dt.strptime(date_string, self.input_format)
                converted_date_string = date.strftime(self.output_format)
                value[i] = converted_date_string

        for key, value in self.end_date_time_dict.items():
            date_time_objects = [
                dt.strptime(date_time, "%Y-%m-%d %H:%M:%S") for date_time in value
            ]
            timestamps = [date_time.timestamp() for date_time in date_time_objects]
            avarage_time = sum(timestamps) / len(timestamps)
            avarage_time = dt.fromtimestamp(avarage_time)
            self.end_date_time_dict[key] = [avarage_time.strftime("%Y-%m-%d %H:%M:%S")]

        for key, value in self.end_date_time_dict.items():
            self.end_date_time_list.extend(value)

        print(f"END_DATE_TIME_LIST {self.end_date_time_list}")
        # return self.end_date_time_list

    def set_flow_rate_values(self):

        mean_area_array = np.array(self.mean_area_list)
        meanOverA_array = np.array(self.meanQoverA_list)
        flow_rate_array = mean_area_array * meanOverA_array
        flow_rate_array = np.round(flow_rate_array, decimals=3)
        self.flow_rate_list = flow_rate_array.tolist()

    def set_average_velocity_values(self):

        mean_area_array = np.array(self.mean_area_list)
        flow_rate_array = np.array(self.flow_rate_list)
        average_velocity_array = flow_rate_array / mean_area_array
        average_velocity_array = np.round(average_velocity_array, decimals=3)
        self.average_velocity_list = average_velocity_array.tolist()

    def get_dataFrame(self):

        xml_dataFrame = pd.DataFrame(
            {
                "start_datetime": self.start_date_time_list,
                "end_datetime": self.end_date_time_list,
                "area_sq_m": self.mean_area_list,
                "discharge_m3_per_sec": self.flow_rate_list,
                "avg_vel_m_per_s": self.average_velocity_list,
            }
        )
        xml_dataFrame["start_datetime"] = pd.to_datetime(
            xml_dataFrame["start_datetime"]
        )
        xml_dataFrame["end_datetime"] = pd.to_datetime(xml_dataFrame["end_datetime"])

        print(f"ESTE É O DATAFRAME xml_datafram \n {xml_dataFrame}")
        return xml_dataFrame
