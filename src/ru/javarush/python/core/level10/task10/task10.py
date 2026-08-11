# Анализ стек-трейс

# Напишите функцию complex_operation, которая вызывает несколько вложенных функций и может вызвать исключение.
# Если возникает исключение, перехватите его и извлеките "сырые" сведения о
# трассировке стека с использованием traceback.extract_tb().
# Выведите информацию о каждом фрейме стека (файл, строка, имя функции, текст строки).

import traceback
import sys

def a():
    return 1/0

def b():
    a()

def c():
    b()

def complex_operation():
    try:
        c()
    except ZeroDivisionError as e:
        tb = sys.exc_info()[2]
        extracted_tb = traceback.extract_tb(tb)
        print(e)
        for frame in extracted_tb:
            print(frame)
            print(f"File: {frame.filename}")
            print(f"Line: {frame.lineno}")
            print(f"Function: {frame.name}")
            print(f"Text: {frame.line}")
            print("-" * 40)

complex_operation()

