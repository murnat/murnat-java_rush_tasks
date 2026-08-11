# Базовые классы.

# Создайте два базовых класса Base1 и Base2, каждый из которых имеет метод describe().
# Создайте производный класс Combined, который наследует от обоих базовых классов.
# Реализуйте метод describe() в каждом базовом классе. Вызовите метод describe() у объекта класса Combined.

class Base1:
    def describe(self):
        print(f'Method of Base1')

class Base2:
    def describe(self):
        print(f'Method of Base2')

class Combined (Base1, Base2):
    pass

combined = Combined()
combined.describe()