# Бесконечность не предел.

# Напишите программу, которая принимает произвольное количество чисел и выводит их сумму.
# Программа должна:
# Определить функцию sum_numbers(*args), которая принимает произвольное количество чисел.
# Вычислить сумму всех переданных чисел.
# Вывести результат.

def sum_numbers(*args):
    sum_numb = 0
    for x in args:
        sum_numb += x
    return sum_numb

my_list = [int(x) for x in input('Provide any amount of numbers separated by coma: ').strip(',').split(',')]

print(f'Sum of all numbers is {sum_numbers(*my_list)}')