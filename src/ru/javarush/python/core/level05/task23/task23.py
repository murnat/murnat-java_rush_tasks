# Обратный кортеж

# Напишите программу, которая создает кортеж из произвольного количества элементов, запрашиваемых у пользователя.
# Затем программа должна вывести кортеж в обратном порядке с использованием среза.

my_tuple = tuple(input("Enter a tuple elements split by spaces: ").split())
reversed_tuple = my_tuple[::-1]
print(reversed_tuple)