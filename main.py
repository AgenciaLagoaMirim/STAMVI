import tkinter as tk
from tkinter import ttk

from src.useCases import (
    DatDataProcessing,
    ExportData,
    LeastSquareHeightArea,
    XmlDataProcessing,
)


APP_HEIGHT = 550
APP_WIDTH = 650


class MainApp:
    def __init__(self):

        # configuração janela principal
        self.root = tk.Tk()
        self.root.geometry(f"{APP_HEIGHT}x{APP_WIDTH}")
        self.root.resizable(0, 0)
        # use cases
        self.xml_data_processing = XmlDataProcessing()
        self.dat_data_processing = DatDataProcessing()
        self.export_data = ExportData()
        self.least_square_height_area = LeastSquareHeightArea()

        # Frame da TreeViewWidget
        self.trv_frame = tk.LabelFrame(self.root, text="Final DataFrame")
        self.trv_frame.place(height=225, width=650)

        # Frame Open File Dialog
        self.file_dialog_frame = tk.LabelFrame(self.root, text="Files Dialog")
        self.file_dialog_frame.place(height=100, width=400, rely=0.65, relx=0)

        # Frame Botões

        self.btn = ttk.Button(
            self.file_dialog_frame,
            padding=2,
            text="Botao",
            command=self.least_square_height_area.plot_least_squares(),
        )

        # TreeViewWidget
        self.tree_view = ttk.Treeview(self.trv_frame)
        self.tree_view.place(relheight=1, relwidth=1)

        self.trv_scroll_y = ttk.Scrollbar(
            self.trv_frame, orient="vertical", command=self.tree_view.yview
        )
        self.trv_scroll_x = ttk.Scrollbar(
            self.trv_frame, orient="horizontal", command=self.tree_view.xview
        )

        self.tree_view.configure(
            xscrollcommand=self.trv_scroll_y.set, yscrollcommand=self.trv_scroll_x.set
        )
        self.trv_scroll_x.pack(side="bottom", fill="x")
        self.trv_scroll_y.pack(side="right", fill="y")

        self.root.mainloop()


if __name__ == "__main__":
    app = MainApp()
