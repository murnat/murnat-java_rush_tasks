# Длительность работы.

# Напишите программу, которая создает декоратор для измерения времени выполнения функции.
# Программа должна:
# Определить декоратор time_decorator, который измеряет и выводит время выполнения функции.
# Применить декоратор к функции compute_square(n), которая вычисляет квадрат числа и имитирует задержку с помощью time.sleep().
# Вызвать функцию compute_square(n).
import time
def time_decorator(func):
    def wrapper(n):
        start = time.time()
        func(n)
        end = time.time()
        print(f'Square computing took {end - start} seconds')
    return wrapper

@time_decorator
def compute_square(n):
    time.sleep(10)
    return n ** 2

compute_square(23)

