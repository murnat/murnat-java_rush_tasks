# Замыкание.

# Напишите программу, которая создает функцию фильтра с использованием замыканий.
# Программа должна:
# Определить внешнюю функцию make_filter(threshold), которая создает и возвращает внутреннюю функцию filter_func(value).
# Внутренняя функция filter_func(value) должна возвращать True, если value больше threshold.
# Создать несколько функций фильтров с различными пороговыми значениями и
# использовать их для фильтрации списка данных, выводя результат на экран.

def make_filter(threshold):
    def filter_func(value):
        return value > threshold
    return filter_func

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

filter_above_2 = make_filter(2)
filter_above_5 = make_filter(5)
filter_above_10 = make_filter(10)
filtered1 = list(filter(filter_above_2,my_list))
print('List filtered above 2 is',filtered1)
filtered2 = list(filter(filter_above_5,my_list))
print('List filtered above 5 is',filtered2)
filtered3 = list(filter(filter_above_10,my_list))
print('List filtered above 10 is',filtered3)

