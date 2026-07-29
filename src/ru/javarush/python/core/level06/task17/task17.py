# Поиск подстроки.

# Напишите программу, которая принимает строку и подстроку от пользователя.
# Программа должна проверить, входит ли подстрока в строку с использованием оператора in,
# найти первое вхождение подстроки с использованием метода find() и
# подсчитать количество вхождений подстроки с использованием метода count().
# Программа должна вывести все результаты.

strng = input('Provide a string: ')
substrng = input ('Provide a substring: ')
print(f'The substring is a part of the string: {substrng in strng}')
print(f'Index of the first substring entry is {strng.find(substrng)}')
print(f'Amount of substring entries is: {strng.count(substrng)}')
