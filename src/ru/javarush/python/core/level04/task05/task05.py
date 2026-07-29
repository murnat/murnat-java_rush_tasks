# Математика 8 класса

# Напишите программу, которая запрашивает у пользователя число и использует библиотеку math для вычисления и вывода квадратного корня и факториала этого числа.

import math
num = int(input("Provide a number: "))
num_sqrt = math.sqrt(num)
num_factorial = math.factorial(num)
print(f"The square root of {num} is {num_sqrt:.2f} the factorial is {num_factorial}")