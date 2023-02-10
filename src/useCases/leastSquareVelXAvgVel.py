import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


class LeastVelXAvgVel:
    def __init__(self):
        self.avg_vel_predict = None
        self.coef_ = None
        self.intercept_ = None
        self.score = None

    def plot_least_squares(self, file_path):
        file_path = r"{}".format(file_path)
        if file_path[-4:] == ".csv":
            xlsx_dataFrame = pd.read_csv(file_path)
        else:
            xlsx_dataFrame = pd.read_excel(file_path)

        velocityX_list = np.array(xlsx_dataFrame.velocityX_m_per_s)
        velocityX_mtx = velocityX_list.reshape(-1, 1)

        avg_vel_list = np.array(xlsx_dataFrame.avg_vel_m_per_s)
        self.avg_vel_mtx = avg_vel_list.reshape(-1, 1)
        # treina o modelo
        linear_model_velx_avgVel = LinearRegression()
        linear_model_velx_avgVel.fit(velocityX_mtx, avg_vel_list)
        # obtem previsões
        avg_vel_predict = linear_model_velx_avgVel.predict(velocityX_mtx)
        self.avg_vel_predict = np.around(avg_vel_predict, 2)

        # plota os dados e a linha de regressão
        plt.scatter(velocityX_list, avg_vel_list)
        plt.plot(velocityX_list, avg_vel_predict, color="red")

        # adiciona as legandas
        plt.xlabel("Velocity X (m/s)")
        plt.ylabel("Average Velocity (m/s)")

        # adiciona o valor de R²
        plt.title(
            f"Average Velocity(m/s) = {linear_model_velx_avgVel.coef_[0]:.3f}Velocity X(m/s) + {linear_model_velx_avgVel.intercept_:.3f}\n R² = {linear_model_velx_avgVel.score(velocityX_mtx, avg_vel_list):.3f}"
        )

        self.coef_ = round(linear_model_velx_avgVel.coef_[0], 3)
        self.intercept_ = round(linear_model_velx_avgVel.intercept_, 3)
        self.score = round(
            linear_model_velx_avgVel.score(velocityX_mtx, avg_vel_list), 4
        )

        plt.show()

    def get_predict_avg_vel_values(self):
        predict_avg_vel_values = self.linear_model_velx_avgVel(self.velocityX_list)
        return predict_avg_vel_values
