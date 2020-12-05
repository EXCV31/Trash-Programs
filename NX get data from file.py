import os
import time
from datetime import datetime

path = "C:\\Users\\xxx\\Desktop\\Programy NxView\\"
for a,b,tuple_of_files in os.walk(path):
    for file in tuple_of_files:
        print(file)
        full_path = os.path.abspath(path+file)
        print(full_path)
        c_time = os.path.getmtime(full_path)
        local_time = datetime.fromtimestamp(c_time).strftime('%d-%m-%Y %H:%M')
        print(local_time)
        print(str(round(os.path.getsize(full_path)/1024,2))+"kB")
        print("\n")
