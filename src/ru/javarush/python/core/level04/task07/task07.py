# Круглый математик

# Напишите программу, которая запрашивает у пользователя вещественное число и округляет его вниз (с использованием math.floor()),
# вверх (с использованием math.ceil()) и до ближайшего целого числа (с использованием round()).
# Выведите результаты всех трех округлений.

import math
# request a float number
number = float(input("Enter a float number: "))
# round it up, down and to the closes int
rnd_down = math.floor(number)
rnd_up = math.ceil(number)
rnd = round(number)
# print the result
print(f'The rounded down number is {rnd_down} \nThe rounded up number is {rnd_up} \nThe rounded to closest integer number is {rnd}')