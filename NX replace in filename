from tkinter import filedialog
from tkinter import Tk
import os
root = Tk()
root.withdraw()
directory = filedialog.askdirectory()
for allx in os.listdir(directory):
    file_name = str.split(allx, "-") # replace "-" with "separator"
    print(file_name)
    try:
        os.rename(directory + "/" + allx, directory + "/" + file_name[0].replace("F" or "FS", "") + file_name[1] + "_" +
                file_name[2]  +"_CAR_MT.nxf")
    except IndexError:
        pass
    except FileExistsError:
        pass
