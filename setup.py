import sys

from cx_Freeze import Executable, setup

# Read dependencies from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

build_exe_options = {
    "zip_include_packages": ["numpy", "pandas", "matplotlib", "scikit-learn"],
    "include_files": ["requirements.txt"],
}

# Path to your main.py file.
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("main.py", base=base)]

setup(
    name="NomeDoSeuProjeto",
    version="0.1",
    description="Descrição do seu projeto",
    options={"build_exe": build_exe_options},
    executables=executables,
    install_requires=requirements,
)

# python setup.py build_exe
