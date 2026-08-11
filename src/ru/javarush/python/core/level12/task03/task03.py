# Чтение всего файла

# Напишите программу, которая читает и выводит на экран содержимое файла example.txt полностью.

file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()