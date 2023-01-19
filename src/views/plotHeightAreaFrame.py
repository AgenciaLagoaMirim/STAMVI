import tkinter as tk

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class PlotHeightAreaFrame:
    def __init__(self, parent):

        # frame de contenção
        self.plot_frame = tk.LabelFrame(
            parent,
            text="Plot Relation Height (m) - Mean Area(m²) ",
            border=1.5,
            relief="solid",
        )
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.plot_frame.place(relx=0.005, rely=0, relheight=0.5, relwidth=0.33)
