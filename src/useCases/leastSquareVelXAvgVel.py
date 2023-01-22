import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


class LeastVelXAvgVel:
    def plot_least_squares(self, file_path):
        xlsx_dataFrame = pd.read_excel(file_path)

        velocityX_list = np.array(xlsx_dataFrame.velocityX_mps)
        velocityX_mtx = velocityX_list.reshape(-1, 1)

        avg_vel_list = np.array(xlsx_dataFrame.avg_vel_mps)
        # treina o modelo
        linear_model_velx_avgVel = LinearRegression()
        linear_model_velx_avgVel.fit(velocityX_mtx, avg_vel_list)
        # obtem previsões
        avg_vel_predict = linear_model_velx_avgVel.predict(velocityX_mtx)

        # plota os dados e a linha de regressão
        plt.scatter(velocityX_list, avg_vel_list)
        plt.plot(velocityX_list, avg_vel_predict, color="red")

        # adiciona a equação da linha de regressão
        plt.annotate(
            f"Average Velocity(m/s) = {linear_model_velx_avgVel.coef_[0]:.2f}Velocity X(m/s) + {linear_model_velx_avgVel.intercept_:.2f}",
            xy=(velocityX_list.min(), avg_vel_predict.min()),
            xytext=(velocityX_list.min(), avg_vel_predict.max()),
        )

        # adiciona as legandas
        plt.xlabel("Velocity X (m/s)")
        plt.ylabel("Average Velocity (m/s)")

        # adiciona o valor de R²
        plt.title(f"R² = {linear_model_velx_avgVel.score(velocityX_mtx, avg_vel_list):.4f}")

        plt.show()
