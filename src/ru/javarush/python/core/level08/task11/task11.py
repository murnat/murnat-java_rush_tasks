# Множество декораторов.

# Напишите программу, которая использует несколько декораторов для одной функции.
# Программа должна:
# Определить два декоратора decorator1 и decorator2, которые логируют свои вызовы.
# Применить оба декоратора к функции say_hello.
# Вызвать функцию say_hello.

def decorator1(func):
    def wrapper(name):
        print('Decorator 1 start')
        func(name)
        print('Decorator 1 end')
    return wrapper
def decorator2(func):
    def wrapper(name):
        print('Decorator 2 start')
        func(name)
        print('Decorator 2 end')
    return wrapper

@decorator1
@decorator2
def say_hello(name):
    print(f'Hello {name}!')

say_hello('John')
