import os
root = "C:\\Users\\xxx\\Desktop\\ProgramyNxf\\"
for root, _, files in os.walk("C:\\Users\\xxx\\Desktop\\ProgramyNxf\\"):
    for file in files:
        file_x = os.path.join(root, file)

        with open(file_x, encoding='utf-8') as search:
            out = open("output.txt", "a")
            out.write("\n")
            out.close
            for line in search:
                line = line.rstrip()
                if 'oper="0" var="$TC7" expr=' in line:
                    print(file)
                    out = open("output.txt", "a")
                    out.write( file + " Ilosc "+ line + "\n")
                if '<PartVar name="$IF9" val="WT:' in line:
                    print(file)
                    out.write( file +" " + " Waga" + line +'\n')
                    out.close()
