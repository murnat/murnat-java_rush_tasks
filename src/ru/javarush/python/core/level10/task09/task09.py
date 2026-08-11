# Использование traceback
import traceback

# Напишите функцию divide_numbers, которая принимает два аргумента и делит первое число на второе.
# Если возникает исключение ZeroDivisionError, перехватите его и выведите стек-трейс, используя модуль traceback.

import traceback
import sys

def divide_numbers (a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f'Exception traceback: {traceback.format_exc()}')


divide_numbers(2,0)