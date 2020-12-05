from tkinter import filedialog
from tkinter import Tk
import os

root = Tk()
root.withdraw()
directory = filedialog.askdirectory()
from pathlib import Path


for allx in os.listdir(directory):
    print(allx)
    with open(directory + "\\" + allx, 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('Ecn', 'ECN')
    name = Path(allx).stem
    os.remove(directory + "\\" + allx)
    with open(name+".nxf", 'w') as file:
        file.write(filedata)

root.destroy()

