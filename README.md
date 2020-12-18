# Trash-Programs

[EN] Programs written to be used only once and to be deleted. Without any code refactoring etc.

[PL] Programy napisane aby użyć ich tylko raz i je skasować. Żadnej refaktoryzacji itp.


## NX extractor.py

[EN] Program for finding specific values in .nxf files and put lines with this values in output.txt

[PL] Program służący do wyszukiwania konkretnych wartości w plikach .nxf oraz umieszczaniu całych linii z tymi konkretnymi wartościami w pliku output.txt


## get_data_from_file

[EN] Program which scan hard-coded directory for files and prints name, absolute path, modification date and size rounded to two decimal places. Program was used only for small files <50kB so prints only size in kilobytes. Used for generate SQL table with this data.

[PL] Program służący do sprawdzania zakodowanego na stałe folderu w poszukiwaniu plików, a następnie wyrzuca na konsole nazwy, ścieżkę, datę modyfikacji oraz rozmiar zaogrąglony do dwóch miejsc po przecinku - używany był tylko dla małych plików <50kB temu też wyrzuca rozmiar w kilobajtach. Użyty został do wygenerowania tabeli SQL z tymi danymi.


## NX change extension.py

[EN] Change file extension from .jpg to .nxb while keeping the original file.

[PL] Zmiana rozszerzenia pliku z .jpg na .nxb wraz z zachowaniem oryginalnego pliku.


## NX find and replace in nxf.py 

[EN] Simply find and replace specific value in each file from user choosen folder

[PL] Znajduje i zamienia konkretne wartości w każdym pliku z folderu wybranego przez użytkownika


## NX CRC fix.py - Useful if changes were made outside of NX Editor

[EN] Fixes "Error 705 - Checksum failed." on Dynalab NX Testers. Opens user choosen folder, opens each program by os.startfile (NX Editor must be choose as default program), click save and close - works on 1920x1080 display resolution - if you want to work on other resolutions you must replace X and Y coordinates for "save" button and "X" button (right upper corner). 

[PL] Naprawia błąd 705 na centralkach Dynalab NX. Program otwiera pliki nxf w folderze wybranym przez użytkownika poprzez os.startfile (NX Editor musi być wybrany jako domyślny program), klika "zapisz" oraz zamyka program. Działa na rozdzielczości 1920x1080, jeżeli chciałbyś żeby pracował na innej rozdzielczości trzeba podmienić koordynaty X oraz Y dla przycisku "zapisz' oraz "x" - tego w prawym górnym rogu.


## NX add to filename.py

[EN] In choosen by user folder program adds to each file specific characters. To get program working you need only change "_MCH_MT" in code.

[PL] W wybranym przez użytkownika folderze dodaje do każdego jednego pliku konkretne znaki. Do działania trzeba podmienić "_MCH_MT".


## NX run and wait for exit.py

[EN] In the folder selected by the user, it runs the files one after the other with the program whose path is saved in "full_path_to_program" and waits for closing.

[PL] W wybranym przez użytkownika folderze uruchamia pliki po sobie za pomocą programu do którego ścieżka jest zapisana w "full_path_to_program" i czeka na zamknięcie.


## NX run and wait for exit + drag to right corner.py

[EN] In the folder selected by the user, it runs the files one after the other with the program whose path is saved in "full_path_to_program" and waits for closing. Additionally, it drags the enabled file to the right edge of the screen.

[PL] W wybranym przez użytkownika folderze uruchamia pliki po sobie za pomocą programu do którego ścieżka jest zapisana w "full_path_to_program" i czeka na zamknięcie. Dodatkowo przeciąga włączony plik do prawej krawędzi ekranu.


## NX replace in filename.py

[PL] Podmienia w nazwie pliku konkretne wartości używając separatora. Działał na plikach z nazwami typu 12-12345-1234-123.ext
