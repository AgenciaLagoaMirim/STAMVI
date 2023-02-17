from tkinter import filedialog, messagebox

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

from .datDataProcessing import DatDataProcessing


class GetHeightTimeSeries:
    def __init__(self):
        self.dat_data_processing = DatDataProcessing()

    def get_height_time_serie(self):
        try:
            self.dat_data_processing.ask_open_dat_file_directory()
            dataFrame = self.dat_data_processing.get_dat_dataFrames()
            dataFrame = dataFrame.rename(
                columns={
                    "Date": "date",
                    "VelocityX": "velocityX_m_per_sec",
                    "Pressure": "stage_m",
                }
            )

            dataFrame["date"] = pd.to_datetime(dataFrame["date"])

            x = dataFrame["date"]
            y = dataFrame["stage_m"]

            y_min = y.min()
            y_mean = y.mean()
            y_max = y.max()

            plt.scatter(x, y, s=0.5)
            plt.axhline(0, color="gray", linestyle="dashed")

            plt.text(
                0.03,
                0.95,
                "Min: {:.2f} (m)\nMean: {:.2f} (m)\nMax: {:.2f} (m)".format(
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
            plt.ylabel("Stage (m)")
            plt.title("Time Series - Stage (m)")
            plt.show()
        except:
            raise messagebox.showerror("Info", "Restart the aplication!")
