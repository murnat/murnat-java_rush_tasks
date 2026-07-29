# Декоратор.

# Напишите программу, которая создает простой декоратор для логирования вызовов функции.
# Программа должна:
# Определить декоратор log_decorator, который выводит сообщение перед и после вызова функции.
# Применить декоратор к функции greet(), которая выводит приветственное сообщение.
# Вызвать функцию greet().

def log_decorator(func):
    def inner(*args,**kwargs):
        print('Before function call')
        func(*args,**kwargs)
        print('After function call')
    return inner

@log_decorator
def greet():
    print('Hello')

greet()