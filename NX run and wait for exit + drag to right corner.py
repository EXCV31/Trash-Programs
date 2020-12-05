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

for allx in os.listdir(directory):
    process = subprocess.Popen(["C:\\Program Files (x86)\\Dynalab\\NX\\NXEditor.exe", directory + "/" + allx])
    time.sleep(1.5)
    pyautogui.moveTo(963, 260)
    time.sleep(0.2)
    pyautogui.mouseDown()
    pyautogui.moveTo(1366, 360)
    pyautogui.mouseUp()
    process.wait()

ctypes.windll.user32.MessageBoxW (0, 'OK', "Jest super", 0x10)

root.destroy()
