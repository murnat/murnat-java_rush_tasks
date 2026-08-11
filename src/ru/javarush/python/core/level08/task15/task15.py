# Работа с директориями.

# Напишите программу, которая создает директорию, переходит в нее, создает файл внутри этой директории,
# записывает в файл текст, а затем читает и выводит его содержимое.
# Программа должна:
# Создать директорию test_directory.
# Перейти в директорию test_directory.
# Создать файл test_file.txt и записать в него строку "Hello, World!".
# Прочитать содержимое файла test_file.txt и вывести его на экран.
# Удалить файл и директорию.
import os

# make new directory
if 'test_directory' not in os.listdir('.'):
    os.mkdir('test_directory')

# change current directory
os.chdir('test_directory')

# make file and write to it
with open('test_file.txt', 'w') as f:
    f.write('Hello, World!')

# read file and print content
with open('test_file.txt', 'r') as f:
    print(f.read())

# remove file
os.remove('test_file.txt')

# change directory
os.chdir('..')

# remove dir
os.rmdir('test_directory')



