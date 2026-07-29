# Сумма кортежей
#from ru.javarush.python.core.level05.task20.task20 import my_tuple

# Напишите программу, которая создает кортеж, содержащий несколько вложенных кортежей из целых чисел.
# Программа должна использовать цикл for для вычисления суммы всех элементов во вложенных кортежах и вывести результат.

my_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
total = 0
for tuple1 in my_tuple:
    for item in tuple1:
        total += item

print(total)