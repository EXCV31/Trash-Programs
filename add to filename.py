from tkinter import filedialog
from tkinter import Tk
import os
root = Tk()
root.withdraw()
directory = filedialog.askdirectory()

for allx in os.listdir(directory):
    name_list = os.path.splitext(allx)
    os.rename(directory + "/" + allx, directory + "/" + name_list[0] + "_MCH_MT" + name_list[1])

root.destroy()
