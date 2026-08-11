# Копирование файла

# Напишите программу, которая копирует файл source.txt в файл destination.txt

import shutil

with open('source.txt', 'r') as file:
    content = file.read()

with open('destination.txt', 'w') as file:
    file.write(content)