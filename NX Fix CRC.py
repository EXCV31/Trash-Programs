from tkinter import filedialog
from tkinter import Tk
import os
import pyautogui, sys
import time

root = Tk()
root.withdraw()
directory = filedialog.askdirectory()

for allx in os.listdir(directory):
    print("1")
    time.sleep(1)
    os.startfile(directory + "\\" + allx)
    print("2")
    time.sleep(2)
    pyautogui.moveTo(63, 33)  # save button in nx editor
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1340,9 )  # close button in nx editor
    pyautogui.click()

root.destroy()

