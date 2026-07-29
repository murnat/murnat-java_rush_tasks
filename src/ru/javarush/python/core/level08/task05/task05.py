# Генератор.

# Напишите программу, которая создает функцию-генератор счетчика с использованием замыканий.
# Программа должна:
# Определить внешнюю функцию make_counter(), которая создает и возвращает внутреннюю функцию counter().
# Внутренняя функция counter() должна увеличивать значение счетчика и возвращать его.
# Создать несколько независимых счетчиков и вызвать их несколько раз, выводя результат на экран.

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter1 = make_counter()
print('Counter 1 is',counter1())
print('Counter 1 is',counter1())
counter2 = make_counter()
print('Counter 2 is',counter2())
print('Counter 2 is',counter2())
print('Counter 2 is',counter2())
counter3 = make_counter()
print('Counter 3 is',counter3())
print('Counter 3 is',counter3())
print('Counter 3 is',counter3())
print('Counter 3 is',counter3())






