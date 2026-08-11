# Домашние животные.

# Напишите функцию check_type для проверки, является ли переданный объект экземпляром класса Animal или его подклассов.
# Используйте функцию isinstance() для выполнения проверки.
# Затем создайте классы Animal, Dog, Cat и проверьте несколько объектов.
def check_type(a):
    return isinstance(a, Animal)

class Animal:
    def __init__(self, type):
        self.type = type


class Dog(Animal):
    def __init__(self, type, name):
        super().__init__(type)
        self.name = name

class Cat(Animal):
    def __init__(self, type, name):
        super().__init__(type)
        self.name = name

dog = Dog('dog','Iris')
cat = Cat('cat','Kitsun')
cat2 = Cat('cat','Shvaya')

animals = [dog, cat, cat2]

for animal in animals:
    if check_type(animal):
        print(f'{animal.name} is an animal')
    else:
        print(f'{animal.name} is not an animal')

