# Детектив

# Напиши функцию set_detector, которая проходится по списку(кортежу) своих аргументов и определяет - есть среди них множество или нет.
# Вызови функцию set_detector с разными вариантами параметров (с множеством и без).

def set_detector(*args):
    my_tuple = tuple(args)
    for element in my_tuple:
        if type(element) is set:
            return True
    return False

print(set_detector(1, 2, 3, 4, {1,2,3,4,5}))
print(set_detector(1, 2, 3, 4))