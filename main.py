import tkinter as tk
from tkinter import messagebox, ttk

import pandas as pd

from src.useCases import (
    DatDataProcessing,
    EstimatedQValues,
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

        self.export_data = ExportData()
        self.least_square_height_area = LeastSquareHeightArea()
        self.least_square_velx_avgVel = LeastVelXAvgVel()
        self.estimated_q_values = EstimatedQValues()

        # Frame da TreeViewWidget
        self.trv_frame = tk.LabelFrame(self.root, text="Final DataFrame")
        self.trv_frame.place(height=250, width=800)

        # Frame Data Processing

        self.data_processing_frame = tk.LabelFrame(
            self.root,
            text="Export Processed Data:",
        )
        self.data_processing_frame.place(height=70, width=200, rely=0.53, relx=0.01)

        # Data Processing Button

        self.btn_export_excel_data = ttk.Button(
            self.data_processing_frame,
            padding=2,
            text="as .xlsx",
            command=lambda: [
                self.export_data.setup_final_dataFrame(),
                self.export_data.export_xlsx(),
            ],
        )
        self.btn_export_excel_data.place(relx=0.01, rely=0.35)

        self.btn_export_csv_data = ttk.Button(
            self.data_processing_frame,
            padding=2,
            text="as .csv",
            command=lambda: [
                self.export_data.setup_final_dataFrame(),
                self.export_data.export_csv(),
            ],
        )
        self.btn_export_csv_data.place(relx=0.58, rely=0.35)

        # Frame Open File Dialog

        self.file_dialog_frame = tk.LabelFrame(self.root, text="Files Dialog")
        self.file_dialog_frame.place(height=70, width=550, rely=0.53, relx=0.3)

        # Label
        self.label_file = ttk.Label(self.file_dialog_frame, text="No file Selected")
        self.label_file.place(rely=0, relx=0.01)

        # Frame Botões

        self.btn_load_excel_data = ttk.Button(
            self.file_dialog_frame,
            padding=2,
            text="load file",
            command=lambda: [self.file_path.set_file_path(), load_excel_data(self)],
        )
        self.btn_load_excel_data.place(relx=0.01, rely=0.39)

        self.btn_least_square_mean_area_height = ttk.Button(
            self.file_dialog_frame,
            padding=2,
            text="Mean Area",
            command=lambda: [
                self.least_square_height_area.plot_least_squares(
                    self.file_path.file_path
                ),
            ],
        )
        self.btn_least_square_mean_area_height.place(relx=0.2, rely=0.39)

        self.btn_least_square_velx_avgVel = ttk.Button(
            self.file_dialog_frame,
            padding=2,
            text="Average velocity",
            command=lambda: [
                self.least_square_velx_avgVel.plot_least_squares(
                    self.file_path.file_path
                ),
            ],
        )
        self.btn_least_square_velx_avgVel.place(relx=0.39, rely=0.39)

        self.btn_estimated_q_values = ttk.Button(
            self.file_dialog_frame,
            padding=2,
            text="Q Values",
            command=lambda: [
                self.estimated_q_values.get_estimated_q_values(
                    self.file_path.file_path,
                    self.least_square_velx_avgVel.avg_vel_predict,
                    self.least_square_height_area.area_predict,
                )
            ],
        )
        self.btn_estimated_q_values.place(relx=0.62, rely=0.39)

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

            self.label_file = ttk.Label(
                self.file_dialog_frame, text=f"{self.file_name}"
            )
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

            self.loaded_dataFrame_rows = self.loaded_dataFrame.to_numpy().tolist()
            for row in self.loaded_dataFrame_rows:
                self.tree_view.insert("", "end", values=row)

        def clear_data(self):
            self.tree_view.delete(*self.tree_view.get_children())

        self.root.mainloop()


if __name__ == "__main__":
    app = MainApp()
