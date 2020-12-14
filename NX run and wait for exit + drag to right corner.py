from tkinter import filedialog
from tkinter import Tk
import os
import subprocess
import ctypes
import pyautogui
import time

root = Tk()
root.withdraw()
directory = filedialog.askdirectory()
number_of_files = len(os.listdir(directory))
counter = 0
for allx in os.listdir(directory):
    process = subprocess.Popen(["C:\\Program Files (x86)\\Dynalab\\NX\\NXEditor.exe", directory + "/" + allx])
    time.sleep(1.5)
    pyautogui.moveTo(360, 20)  # point to program x y - for drag purposes
    time.sleep(0.2)
    pyautogui.mouseDown()
    pyautogui.moveTo(1366, 360)  # drag to right pane
    pyautogui.mouseUp()
    time.sleep(0.2)
    pyautogui.moveTo(950, 40)  # drag to combobox
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(0.2)
    pyautogui.moveTo(920, 100) # click workflow in combobox
    time.sleep(0.2)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    process.wait()
    counter +=1
    print(f"Ukończono", counter, "z", number_of_files, "programów. Zostało", number_of_files-counter)

ctypes.windll.user32.MessageBoxW (0, 'Ukończono wszystkie programy', "Ok", 0x10)

root.destroy()
