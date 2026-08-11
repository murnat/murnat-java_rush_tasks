# Использование оператора with для работы с файлами
from os import write

# Напишите программу, которая открывает файл example.txt в режиме добавления, записывает в него строку "Новая линия.".
# Нужно корректно обрабатывать исключение FileNotFoundError, закрывая файл в любом случае.
# Нужно использовать оператор with для автоматического закрытия файла.
try:
    with open('example.txt','a') as file:
        file.write('Новая линия.\n')
except FileNotFoundError:
    print('File not found')

