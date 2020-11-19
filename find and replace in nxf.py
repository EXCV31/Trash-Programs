from tkinter import filedialog
from tkinter import Tk
import os

root = Tk()
root.withdraw()
images_dir = filedialog.askdirectory()
from pathlib import Path


for allx in os.listdir(images_dir):
    print(allx)
    with open(images_dir + "\\" + allx, 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('Ecn', 'ECN')
    name = Path(allx).stem
    os.remove(images_dir + "\\" + allx)
    with open(name+".nxf", 'w') as file:
        file.write(filedata)

root.destroy()

