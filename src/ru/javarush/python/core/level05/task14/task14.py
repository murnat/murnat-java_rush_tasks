# Фильтрация

# Напишите программу, которая создает список из 20 случайных чисел в диапазоне от 1 до 100 с использованием List Comprehension.
# Затем с использованием List Comprehension создает новый список, содержащий только четные числа из исходного списка.
# Программа должна вывести оба списка.
import random
my_list = [random.randint(1,100) for x in range(1,21)]
list_even = [x for x in my_list if x % 2 == 0]
print(*my_list, sep=', ')
print(*list_even, sep=', ')
