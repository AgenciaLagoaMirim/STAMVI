import tkinter as tk
from tkinter import filedialog, ttk

import matplotlib.backends.backend_tkagg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

from src.useCases import DatDataProcessing, ExportData, XmlDataProcessing

APP_WIDTH = 1292
APP_HEIGHT = 380


class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.state("zoomed")

        self.container_frame = tk.Frame(self.root)
        self.container_frame.place(relx=0, rely=0, relheight=1, relwidth=0.998)

        # use cases
        self.xml_data_processing = XmlDataProcessing()
        self.dat_data_processing = DatDataProcessing()
        self.export_data = ExportData()

        # LabelFrames
        self.plot_frame_vel_avgVel = tk.LabelFrame(
            self.root,
            text="Plot Relation Velocity X (m/s) - Average Velocity(m/s) ",
            border=1.5,
            relief="solid",
        )
        self.plot_frame_vel_avgVel.place(
            relx=0.53, rely=0, relheight=0.6, relwidth=0.45
        )

        self.plot_frame_height_area = tk.LabelFrame(
            self.root,
            text="Plot Relation Height (m) - Mean Area(m²) ",
            border=1.5,
            relief="solid",
        )
        self.plot_frame_height_area.place(
            relx=0.005, rely=0, relheight=0.6, relwidth=0.45
        )

        self.btn = ttk.Button(
            self.container_frame,
            padding=2,
            text="Botao",
            command=self.plot_least_square_height_area(),
        )

        self.root.mainloop()

    def plot_least_square_height_area(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", ".xlsx")])
        xlsx_dataFrame = pd.read_excel(file_path)

        height_list = np.array(xlsx_dataFrame.height_m)
        height_mtx = height_list.reshape(-1, 1)

        area_list = np.array(xlsx_dataFrame.mean_area_sqm)
        # area_mtx = area_list.reshape(-1, 1)
        # treina o modelo
        linear_model = LinearRegression()
        linear_model.fit(height_mtx, area_list)
        # obtem previsões
        area_predict = linear_model.predict(height_mtx)

        # plota os dados e a linha de regressão
        plt.scatter(height_list, area_list)
        plt.plot(height_list, area_predict, color="red")

        # adiciona a equação da linha de regressão
        plt.annotate(
            f"mean_area(m²) = {linear_model.coef_[0]:.2f}height(m) + {linear_model.intercept_:.2f}",
            xy=(height_list.min(), area_predict.min()),
            xytext=(height_list.min(), area_predict.max()),
            # arrowprops=dict(arrowstyle="->", color="red"),
        )

        # adiciona as legandas
        plt.xlabel("Height(m)")
        plt.ylabel("Mean Area (m²)")

        # adiciona o valor de R²
        plt.title(f"R² = {linear_model.score(height_mtx, area_list):.4f}")

        # exibe o grafico

        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(
            plt.gcf(), master=self.plot_frame_height_area
        )
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


if __name__ == "__main__":
    app = MainApp()
