# Сравнивать очень просто

# Напишите программу, которая запрашивает у пользователя два вещественных числа и сравнивает их с использованием допустимой погрешности epsilon.
# Выведите результат сравнения на экран.

import math
# request a float number
number1 = float(input("Enter the first float number: "))
number2 = float(input("Enter the second float number: "))

# set epsilon
epsilon = 1e-9
# compare numbers and print results
if abs(number1 - number2) < epsilon:
    print('The two numbers are equal')
else:
    print('The two numbers are not equal')

