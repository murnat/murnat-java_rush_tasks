# Автопарк.

# Напишите функцию check_subclass для проверки, является ли один класс подклассом другого.
# Используйте функцию issubclass() для выполнения проверки.
# Затем создайте классы Vehicle, Car, Bicycle, и проверьте, являются ли Car и Bicycle подклассами Vehicle.

def check_subclass(cls1, cls2):
    if (issubclass(cls1, cls2)):
        print(f'{cls1.__name__} is the subclass of {cls2.__name__}')
    else:
        print(f'{cls1.__name__} is not the subclass of {cls2.__name__}')

class Vehicle:
    pass

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass

check_subclass(Vehicle, Bicycle)
check_subclass(Car, Vehicle)
check_subclass(Bicycle, Vehicle)
check_subclass(Car, Bicycle)