import tkinter as tk
from tkinter import ttk

from src.useCases import DatDataProcessing, ExportData, XmlDataProcessing
from src.views import PlotAvgVelVelxFrame, PlotHeightAreaFrame

APP_WIDTH = 1292
APP_HEIGHT = 380


class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.state("zoomed")

        self.container_frame = tk.Frame(self.root)
        self.container_frame.place(relx=0, rely=0, relheight=1, relwidth=0.998)

        self.xml_data_processing = XmlDataProcessing()
        self.dat_data_processing = DatDataProcessing()
        self.export_data = ExportData()

        self.plot_height_ara_frame = PlotHeightAreaFrame(self.root)
        self.plot_avgVel_velx_frame = PlotAvgVelVelxFrame(self.root)
        self.btn = ttk.Button(
            self.container_frame,
            padding=2,
            text="Botao",
            command=self.export_data.setup_final_dataFrame(),
        )
        self.btn = ttk.Button(
            self.container_frame,
            padding=2,
            text="Botao",
            command=self.export_data.export_csv(),
        )

        self.root.mainloop()


if __name__ == "__main__":
    app = MainApp()
