# Режимы доступа

# Напишите программу, которая создает или открывает файл example.txt в режиме записи и
# записывает в него строку "Hello, World!".
# Затем откройте файл в режиме добавления и добавьте строку "Appended text.".

file = open('example.txt', 'w')
file.write('Hello, World!')
file = open('example.txt', 'a')
file.write('\nAppended text.')
file.close()

