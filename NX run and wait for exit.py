from tkinter import filedialog
from tkinter import Tk
import os
import subprocess

root = Tk()
root.withdraw()
directory = filedialog.askdirectory()

for allx in os.listdir(directory):
    subprocess.call(["full_path_to_program", directory + "/" + allx])


root.destroy()
