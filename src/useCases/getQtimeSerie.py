from tkinter import filedialog, messagebox

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

from .datDataProcessing import DatDataProcessing


class GetQTimeSeries:
    def __init__(self):
        self.dat_data_processing = DatDataProcessing()

    def get_estimated_q_time_serie(
        self, area_coef_, area_intercept_, avg_coef_, avg_intercept_
    ):
        try:
            self.dat_data_processing.ask_open_dat_file_directory()
            dataFrame = self.dat_data_processing.get_dat_dataFrames()
            dataFrame = dataFrame.rename(
                columns={
                    "Date": "date",
                    "VelocityX": "velocityX_m_per_s",
                    "Pressure": "stage_m",
                }
            )
            print(f"PRINT{dataFrame}")
            self.avg_coef_ = avg_coef_
            self.avg_intercept_ = avg_intercept_

            self.area_coef_ = area_coef_
            self.area_intercept_ = area_intercept_

            dataFrame["avg_vel_m_per_s"] = dataFrame["velocityX_m_per_s"].apply(
                lambda x: self.avg_coef_ * x + self.avg_intercept_
            )

            dataFrame["area_sq_m"] = dataFrame["stage_m"].apply(
                lambda y: self.area_coef_ * y + self.area_intercept_
            )

            dataFrame["discharge_m3_per_sec"] = (
                dataFrame["area_sq_m"] * dataFrame["avg_vel_m_per_s"]
            )
            dataFrame["date"] = pd.to_datetime(dataFrame["date"])

            ask_ok_cancel = messagebox.askokcancel("Save as xlsx", "Save as xlsx?")

            if ask_ok_cancel:
                file_path = filedialog.asksaveasfilename(defaultextension=".xlsx")
                if file_path:
                    dataFrame.to_excel(file_path, index=False)

            x = dataFrame["date"]
            y = dataFrame["discharge_m3_per_sec"]

            y_min = y.min()
            y_mean = y.mean()
            y_max = y.max()

            plt.scatter(x, y, s=0.5)
            plt.axhline(0, color="gray", linestyle="dashed")

            plt.text(
                0.03,
                0.95,
                "Min: {:.2f} (m³/s)\nMean: {:.2f} (m³/s)\nMax: {:.2f} (m³/s)".format(
                    y_min, y_mean, y_max
                ),
                fontsize=8.5,
                transform=plt.gcf().transFigure,
                verticalalignment="top",
                bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5),
            )

            plt.xticks(rotation=90, ha="center", fontsize=7)
            plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=50))
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %d %Y"))

            plt.xlabel("Date")
            plt.ylabel("Discharge (m³/s)")
            plt.title("Time Series - Discharge (m³/s)")
            plt.show()
        except:
            raise messagebox.showerror("Info", "Restart the aplication!")
