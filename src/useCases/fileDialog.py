from tkinter import filedialog, messagebox


class FileDialog:
    def __init__(self):
        self.file_path = None
        self.loaded_dataFrame = None

    def set_file_path(self):
        file_path = filedialog.askopenfilename(
            initialdir="/",
            title="Select a .xlsx or a .csv file",
            filetypes=[("ALL Files", "*.*")],
        )
        if file_path.endswith(".xlsx") or file_path.endswith(".csv"):
            self.file_path = file_path
        else:
            messagebox.showerror(
                "Invalid file type", "Please select a .xlsx or csv file!"
            )
