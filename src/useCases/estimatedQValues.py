import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class EstimatedQValues:
    def get_estimated_q_values(self, file_path, avg_velocity, mean_area):
        file_path = r"{}".format(file_path)
        if file_path[-4:] == ".csv":
            xlsx_dataFrame = pd.read_csv(file_path)
        else:
            xlsx_dataFrame = pd.read_excel(file_path)

        # configura dados vazõ observada
        q_m3_per_sec = np.array(xlsx_dataFrame.discharge_m3_per_sec)

        print(f"Mean area {mean_area}")
        print(f"Avg_veloc {avg_velocity}")

        estimated_q_values = mean_area * avg_velocity

        print(f"Vazão observada {q_m3_per_sec}")
        print(f"Vazão estimada {estimated_q_values}")

        mean_q_m3_per_sec = np.mean(q_m3_per_sec)
        numerator = np.sum((q_m3_per_sec - estimated_q_values) ** 2)
        denominator = np.sum((q_m3_per_sec - mean_q_m3_per_sec) ** 2)
        cns = 1 - (numerator / denominator)
        print(cns)

        # plotar grafico
        plt.scatter(q_m3_per_sec, estimated_q_values)
        # plt.scatter(q_m3_per_sec, q_m3_per_sec, color="r")
        plt.plot(q_m3_per_sec, q_m3_per_sec, color="red")

        plt.annotate(
            "Discharge (m³/s) Observed - Estimated",
            xy=(q_m3_per_sec.min(), estimated_q_values.min()),
            xytext=(q_m3_per_sec.min(), estimated_q_values.max()),
        )

        # adiciona legendas
        plt.xlabel("Observed Values - Discharge (m³/s)")
        plt.ylabel("Estimated Values - Discharge (m³/s)")

        plt.title(f"NSE = {cns:.4f}")
        plt.show()
