from tkinter import filedialog


class FileDialog:
    def __init__(self):
        self.file_path = None
        self.loaded_dataFrame = None

    def set_file_path(self):
        self.file_path = filedialog.askopenfilename(
            initialdir="/", title="Select a file", filetypes=[("Excel Files", ".xlsx")]
        )
