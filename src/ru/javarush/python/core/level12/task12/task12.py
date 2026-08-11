# Проверка существования файла

# Напишите программу, которая проверяет, существует ли файл example.txt, и если существует, удаляет его.

import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print('File removed')
else :
    print('File does not exist')