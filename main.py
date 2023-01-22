import tkinter as tk
from tkinter import messagebox, ttk

import pandas as pd

from src.useCases import (
    DatDataProcessing,
    ExportData,
    FileDialog,
    LeastSquareHeightArea,
    LeastVelXAvgVel,
    XmlDataProcessing,
)

APP_HEIGHT = 500
APP_WIDTH = 800


class MainApp:
    def __init__(self):
        self.file_path = FileDialog()

        # configuração janela principal
        self.root = tk.Tk()
        self.root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.root.resizable(0, 0)
        # use cases
        self.xml_data_processing = XmlDataProcessing()
        self.dat_data_processing = DatDataProcessing()
        self.export_data = ExportData()
        self.least_square_height_area = LeastSquareHeightArea()
        self.least_square_velx_avgVel = LeastVelXAvgVel()

        # Frame da TreeViewWidget
        self.trv_frame = tk.LabelFrame(self.root, text="Final DataFrame")
        self.trv_frame.place(height=250, width=800)

        # Frame Open File Dialog
        self.file_dialog_frame = tk.LabelFrame(self.root, text="Files Dialog")
        self.file_dialog_frame.place(height=100, width=800, rely=0.65, relx=0)

        self.label_frame = ttk.Label(self.file_dialog_frame, text="No file Selected")

        # Label
        self.label_file = ttk.Label(self.file_dialog_frame, text="No file Selected")
        self.label_file.place(rely=0, relx=0)

        # Frame Botões

        self.btn1 = ttk.Button(
            self.file_dialog_frame,
            padding=2,
            text="Botao1",
            command=lambda: [self.file_path.set_file_path(), load_excel_data(self)],
        )
        self.btn1.pack()

        self.btn2 = ttk.Button(
            self.file_dialog_frame,
            padding=2,
            text="Botao2",
            command=lambda: [
                self.least_square_height_area.plot_least_squares(
                    self.file_path.file_path
                ),
            ],
        )
        self.btn2.pack()

        self.btn3 = ttk.Button(
            self.file_dialog_frame,
            padding=2,
            text="Botao3",
            command=lambda: [
                self.least_square_velx_avgVel.plot_least_squares(
                    self.file_path.file_path
                ),
            ],
        )
        self.btn3.pack()

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

        def load_excel_data(self):
            try:
                self.file_name = r"{}".format(self.file_path.file_path)
                if self.file_name[-4:] == ".csv":
                    self.loaded_dataFrame = pd.read_csv(self.file_name)
                else:
                    self.loaded_dataFrame = pd.read_excel(self.file_name)

            except ValueError:
                messagebox.showerror("Attention!", "Invalid file extension")

            except FileNotFoundError:
                messagebox.showerror("Attention", f"No such file as {self.file_path}")

            self.label_file = ttk.Label(self.file_dialog_frame, text=f"{self.file_name}")
            self.label_file.place(rely=0, relx=0)
            clear_data(self)
            self.tree_view["column"] = list(self.loaded_dataFrame)
            self.tree_view["show"] = "headings"
            for column in self.tree_view["columns"]:
                self.tree_view.column(
                    column,
                    anchor="center",
                    stretch=tk.NO,
                    minwidth=0,
                )
                self.tree_view.heading(column, text=column)
                # self.tree_view.columnconfigure(column, weight=1)

            self.loaded_dataFrame_rows = self.loaded_dataFrame.to_numpy().tolist()
            for row in self.loaded_dataFrame_rows:
                self.tree_view.insert("", "end", values=row)

        def clear_data(self):
            self.tree_view.delete(*self.tree_view.get_children())

        self.root.mainloop()


if __name__ == "__main__":
    app = MainApp()
