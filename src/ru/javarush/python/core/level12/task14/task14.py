# Получение списка файлов и директорий
# Напишите программу, которая выводит содержимое текущей рабочей директории и
# для каждого файла или директории указывает, является ли это файлом или директорией.

import os

current_directory = os.getcwd()
print(f'Current directory is: {current_directory}')

content = os.scandir('.')
for entry in content:
    print(f'Entity name is: {entry.name}. Is directory: {entry.is_dir()}. Is file: {entry.is_file()}.')


