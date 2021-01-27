from tkinter import filedialog
from tkinter import Tk
import os
import shutil
import logging
import logging.config

root = Tk()
root.withdraw()
print("Wybierz folder z programami do przerobienia.\n")
print("Upewnij się że w folderze nie znajdują się inne pliki niż .nxf !\n\n")
directory = filedialog.askdirectory()
from pathlib import Path
logger = logging.getLogger('my_application')

desktop_path = os.path.join(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\'))
try:
    os.makedirs(desktop_path + "\\Obrobione programy\\", exist_ok=True)
    for allx in os.listdir(directory):
        with open(directory + "\\" + allx, 'r') as file:  # without encoding='utf-8'
            filedata = file.read()
        filedata = filedata.replace('$KD2', '$PS6')
        name = Path(allx).stem
        os.remove(directory + "\\" + allx)
        with open(name+".nxf", 'w') as file:
            file.write(filedata)
        shutil.move(name + ".nxf", desktop_path + "Obrobione programy\\")
        print("Przerobiono: " + allx)
except Exception as e:
    print("Wystąpił błąd podczas przerabiania pliku " + allx + ":\n")
    print(e)
    input("\nNaciśnij dowolny klawisz i enter aby zamknąć program...")
    sys.exit()
    


root.destroy()
input("Przerobiono wszystkie programy. Naciśnij dowolny klawisz i enter aby zamknąć program...")
