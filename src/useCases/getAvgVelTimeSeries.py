from tkinter import filedialog, messagebox

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

from .datDataProcessing import DatDataProcessing


class GetAvgVelTimeSeries:
    def __init__(self):
        self.dat_data_processing = DatDataProcessing()

    def get_avg_vel_time_serie(self, coef_, intercept_):

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

            self.coef_ = coef_
            self.intercept_ = intercept_

            dataFrame["avg_vel_m_per_sec"] = dataFrame["velocityX_m_per_sec"].apply(
                lambda x: round(self.coef_ * x + self.intercept_, 3)
            )

            dataFrame["date"] = pd.to_datetime(dataFrame["date"])

            x = dataFrame["date"]
            y = dataFrame["avg_vel_m_per_sec"]

            y_min = y.min()
            y_mean = y.mean()
            y_max = y.max()

            plt.scatter(x, y, s=0.5)
            plt.axhline(0, color="gray", linestyle="dashed")

            plt.text(
                0.03,
                0.95,
                "Min: {:.2f} (m/s)\nMean: {:.2f} (m/s)\nMax: {:.2f} ( m/s)".format(
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
            plt.ylabel("Average Velocity (m/s)")
            plt.title("Time Series - Average Velocity (m/s)")
            plt.show()
        except:
            raise messagebox.showerror("Info", "Restart the aplication!")
