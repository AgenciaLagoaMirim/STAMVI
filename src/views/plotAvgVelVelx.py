import tkinter as tk
from tkinter import ttk


class PlotAvgVelVelxFrame:
    def __init__(self, parent):

        # frame de contenção
        self.plot_frame = tk.LabelFrame(
            parent,
            text="Plot Relation Velocity X (m/s) - Average Velocity(m/s) ",
            border=1.5,
            relief="solid"
        )
        self.plot_frame.place(relx=0.34, rely=0, relheight=0.5, relwidth=0.33)
