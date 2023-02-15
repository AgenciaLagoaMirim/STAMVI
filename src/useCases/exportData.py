from tkinter import filedialog, messagebox

import pandas as pd

from .datDataProcessing import DatDataProcessing
from .xmlDataProcessing import XmlDataProcessing


class ExportData:
    def __init__(self):
        self.xml_data_processing = XmlDataProcessing()
        self.dat_data_processing = DatDataProcessing()
        self.final_data_dataFrame = None

    def setup_final_dataFrame(self):

        self.xml_data_processing.ask_open_xml_file_directory()
        self.dat_data_processing.ask_open_dat_file_directory()
        # configuração dos dados
        self.xml_data_processing.set_start_date_time_values()
        self.xml_data_processing.set_end_date_time_values()
        self.xml_data_processing.set_mean_area_values()
        self.xml_data_processing.set_meanQoverA_values()
        self.xml_data_processing.set_flow_rate_values()
        self.xml_data_processing.set_average_velocity_values()

        xml_dataFrame = self.xml_data_processing.get_dataFrame()
        dat_dataFrame = self.dat_data_processing.get_dat_dataFrames()

        start_date_time = pd.to_datetime(xml_dataFrame["start_datetime"])
        end_date_time = pd.to_datetime(xml_dataFrame["end_datetime"])

        filtered_df = pd.DataFrame()

        for start, end in zip(start_date_time, end_date_time):
            df = dat_dataFrame[
                (dat_dataFrame["Date"] >= start) & (dat_dataFrame["Date"] <= end)
            ]
            filtered_df = pd.concat([filtered_df, df])

        filtered_date = filtered_df["Date"].to_list()
        date_list = pd.to_datetime(filtered_date)

        # realiza a busca inversa

        filtered_xml_dataFrame = xml_dataFrame[
            xml_dataFrame.apply(
                lambda x: any(
                    x["start_datetime"] <= d <= x["end_datetime"] for d in date_list
                ),
                axis=1,
            )
        ]

        filtered_df["index"] = range(1, len(filtered_df) + 1)
        filtered_xml_dataFrame["index"] = range(1, len(filtered_xml_dataFrame) + 1)

        print(filtered_df)
        print(filtered_xml_dataFrame)

        final_dataFrame = filtered_df.merge(
            filtered_xml_dataFrame, left_on="index", right_on="index"
        )

        print(final_dataFrame)

        final_dataFrame = final_dataFrame.rename(
            columns={
                "Date": "date",
                "VelocityX": "velocityX_m_per_s",
                "Pressure": "stage_m",
            }
        )

        final_dataFrame = final_dataFrame.reindex(
            columns=[
                "index",
                "start_datetime",
                "end_datetime",
                "date",
                "velocityX_m_per_s",
                "stage_m",
                "area_sq_m",
                "discharge_m3_per_sec",
                "avg_vel_m_per_s",
            ]
        )

        print(final_dataFrame)
        self.final_data_dataFrame = final_dataFrame
        # return final_dataFrame

    def export_xlsx(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xslx", filetypes=[("XLSX files", "*.xlsx")]
        )
        self.final_data_dataFrame.to_excel(file_path, index=False)
        messagebox.showinfo("INFO", f"File exported at {file_path}")

    def export_csv(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv", filetypes=[("CSV files", "*.csv")]
        )
        self.final_data_dataFrame.to_csv(file_path, index=False)
        messagebox.showinfo("INFO", f"File exported at {file_path}")
