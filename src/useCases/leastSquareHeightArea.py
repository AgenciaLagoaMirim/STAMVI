import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


class LeastSquareHeightArea:
    def __init__(self):
        self.area_predict = None

    def plot_least_squares(self, file_path):
        file_path = r"{}".format(file_path)
        if file_path[-4:] == ".csv":
            xlsx_dataFrame = pd.read_csv(file_path)
        else:
            xlsx_dataFrame = pd.read_excel(file_path)

        height_list = np.array(xlsx_dataFrame.height_m)
        height_mtx = height_list.reshape(-1, 1)

        area_list = np.array(xlsx_dataFrame.mean_area_sqm)
        self.mean_area_mtx = area_list.reshape(-1, 1)
        # treina o modelo
        linear_model_height_mean_area = LinearRegression()

        linear_model_height_mean_area.fit(height_mtx, area_list)
        # obtem previsões
        area_predict = linear_model_height_mean_area.predict(height_mtx)
        self.area_predict = np.around(area_predict, 2)

        # plota os dados e a linha de regressão
        plt.scatter(height_list, area_list)
        plt.plot(height_list, area_predict, color="red")

        # adiciona as legandas
        plt.xlabel("Height(m)")
        plt.ylabel("Mean Area (m²)")

        # adiciona o valor de R²
        plt.title(
            f" mean_area(m²) = {linear_model_height_mean_area.coef_[0]:.2f}height(m) + {linear_model_height_mean_area.intercept_:.2f} \n R² = {linear_model_height_mean_area.score(height_mtx, area_list):.4f}"
        )

        plt.show()
