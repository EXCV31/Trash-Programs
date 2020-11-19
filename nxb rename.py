from tkinter import filedialog
from tkinter import Tk
import os
import shutil

root = Tk()
root.withdraw()
images_dir = filedialog.askdirectory()


for file in os.listdir(images_dir):
    file_path = os.path.join(images_dir, file)
    name_without_extension = os.path.splitext(file)[0]
    shutil.copy(file_path, os.path.join(images_dir, name_without_extension + ".nxb"))

root.destroy()
