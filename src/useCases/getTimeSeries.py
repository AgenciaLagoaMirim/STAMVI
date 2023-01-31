import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

from .datDataProcessing import DatDataProcessing


class GetTimeSeries:
    def __init__(self):
        self.dat_data_processing = DatDataProcessing()

    def get_avg_vel_time_serie(self, coef_, intercept_):

        self.dat_data_processing.ask_open_dat_file_directory()
        dataFrame = self.dat_data_processing.get_dat_dataFrames()
        dataFrame = dataFrame.rename(
            columns={
                "Date": "date",
                "VelocityX": "velocityX_mps",
                "Pressure": "height_m",
            }
        )
        print(f"PRINT{dataFrame}")
        self.coef_ = coef_
        self.intercept_ = intercept_

        print(f" COEFICIENTE {self.coef_}")
        print(f" INTERCEPT {self.intercept_}")

        dataFrame["avg_vel_mps"] = dataFrame["velocityX_mps"].apply(
            lambda x: self.coef_ * x + self.intercept_
        )

        print(dataFrame)
        dataFrame["date"] = pd.to_datetime(dataFrame["date"])

        x = dataFrame["date"]
        y = dataFrame["avg_vel_mps"]

        y_min = y.min()
        y_mean = y.mean()
        y_max = y.max()

        plt.scatter(x, y, s=0.5)
        plt.axhline(0, color="gray", linestyle="dashed")

        plt.text(
            0.03,
            0.95,
            "Min: {:.2f}(m/s)\nMean: {:.2f}(m/s)\nMax: {:.2f}(m/s)".format(
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
