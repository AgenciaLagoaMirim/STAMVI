import tkinter as tk
from tkinter import messagebox, ttk

import pandas as pd

from src.useCases import (
    EstimatedQValues,
    ExportData,
    FileDialog,
    GetTimeSeries,
    LeastSquareHeightArea,
    LeastVelXAvgVel,
)

APP_HEIGHT = 600
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
        self.get_time_series = GetTimeSeries()

        # Frame da TreeViewWidget
        self.trv_frame = tk.LabelFrame(self.root, text="Final DataFrame Display")
        self.trv_frame.place(height=300, width=800)

        # Frame Data Processing

        self.data_processing_frame = tk.LabelFrame(
            self.root,
            text="Load Data/Export Processed Data:",
        )
        self.data_processing_frame.place(height=70, width=262, rely=0.53, relx=0.01)

        # Label
        self.label_file = ttk.Label(self.data_processing_frame, text="No file Selected")
        self.label_file.place(rely=0, relx=0.01)

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
        self.btn_export_csv_data.place(relx=0.35, rely=0.35)

        self.btn_load_excel_data = ttk.Button(
            self.data_processing_frame,
            padding=2,
            text="load file",
            command=lambda: [self.file_path.set_file_path(), load_excel_data(self)],
        )
        self.btn_load_excel_data.place(relx=0.681, rely=0.35)

        # Frame Open File Dialog

        self.file_dialog_frame = tk.LabelFrame(self.root, text="Execute Models:")
        self.file_dialog_frame.place(height=60, width=262, rely=0.67, relx=0.01)

        # Botões Least Squares

        self.btn_least_square_mean_area_height = ttk.Button(
            self.file_dialog_frame,
            padding=2,
            text="Mean Area",
            command=lambda: [
                self.least_square_height_area.plot_least_squares(
                    self.file_path.file_path
                ),
                load_height_area_label(self),
            ],
        )
        self.btn_least_square_mean_area_height.place(relx=0.01, rely=0.2)

        self.btn_least_square_velx_avgVel = ttk.Button(
            self.file_dialog_frame,
            padding=2,
            text="Avg. velocity",
            command=lambda: [
                self.least_square_velx_avgVel.plot_least_squares(
                    self.file_path.file_path
                ),
                load_velocityx_avg_vel_label(self),
            ],
        )
        self.btn_least_square_velx_avgVel.place(relx=0.35, rely=0.2)

        self.btn_estimated_q_values = ttk.Button(
            self.file_dialog_frame,
            padding=2,
            text="CNS",
            command=lambda: [
                self.estimated_q_values.get_estimated_q_values(
                    self.file_path.file_path,
                    self.least_square_velx_avgVel.avg_vel_predict,
                    self.least_square_height_area.area_predict,
                )
            ],
        )
        self.btn_estimated_q_values.place(relx=0.681, rely=0.2)

        # Frame Valores estimados

        self.estimated_values_frame = tk.LabelFrame(self.root, text="Get Time Series:")
        self.estimated_values_frame.place(height=60, width=262, rely=0.80, relx=0.01)

        # Botões Least Squares

        self.btn_avg_vel_time_series = ttk.Button(
            self.estimated_values_frame,
            padding=2,
            text="Avg velocity",
            command=lambda: [
                self.get_time_series.get_avg_vel_time_serie(
                    self.least_square_velx_avgVel.coef_,
                    self.least_square_velx_avgVel.intercept_,
                )
            ],
        )
        self.btn_avg_vel_time_series.place(relx=0.01, rely=0.2)

        self.btn_least_square_velx_avgVel = ttk.Button(
            self.estimated_values_frame,
            padding=2,
            text="Height",
            command=lambda: [
                self.least_square_velx_avgVel.plot_least_squares(
                    self.file_path.file_path
                ),
            ],
        )
        self.btn_least_square_velx_avgVel.place(relx=0.35, rely=0.2)

        self.btn_estimated_q_values = ttk.Button(
            self.estimated_values_frame,
            padding=2,
            text="Q values",
            command=lambda: [
                self.estimated_q_values.get_estimated_q_values(
                    self.file_path.file_path,
                    self.least_square_velx_avgVel.avg_vel_predict,
                    self.least_square_height_area.area_predict,
                )
            ],
        )
        self.btn_estimated_q_values.place(relx=0.681, rely=0.2)

        # Frame para os parametros

        # Height-Area
        self.height_area_param_values_frame = tk.LabelFrame(
            self.root, text="Height - Area Equation:"
        )
        self.height_area_param_values_frame.place(
            height=70, width=460, relx=0.4, rely=0.53
        )

        # VelocityX - Average Velocity
        self.velocityx_avg_velocity_param_values_frame = tk.LabelFrame(
            self.root, text="Velocity X - Average Velocity Equation:"
        )
        self.velocityx_avg_velocity_param_values_frame.place(
            height=70, width=460, relx=0.4, rely=0.67
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
            yscrollcommand=self.trv_scroll_y.set, xscrollcommand=self.trv_scroll_x.set
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
                self.data_processing_frame, text=f"{self.file_name}"
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

        def load_height_area_label(self):
            self.height_area_label_equation = tk.Label(
                self.height_area_param_values_frame,
                text=f"Area(m²) = {self.least_square_height_area.coef_}height(m) + {self.least_square_height_area.intercept_}  R² = {self.least_square_height_area.score}",
            )
            self.height_area_label_equation.place(relx=0.2, rely=0.3)

        def load_velocityx_avg_vel_label(self):
            self.velx_avg_vel_label_equation = tk.Label(
                self.velocityx_avg_velocity_param_values_frame,
                text=f"Average Velocity(m/s) = {self.least_square_velx_avgVel.coef_}velocityX(m/s) + {self.least_square_velx_avgVel.intercept_}  R² = {self.least_square_velx_avgVel.score}",
            )
            self.velx_avg_vel_label_equation.place(relx=0.10, rely=0.3)

        self.root.mainloop()


if __name__ == "__main__":
    app = MainApp()
