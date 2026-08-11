# Итератор для коллекции

# Напишите класс CollectionIterator, который будет итерироваться по произвольной коллекции (список, строка и т.д.).
# Реализуйте методы __iter__ и __next__.

class CollectionIterator:
    def __init__(self, collection):
        self.iterator = iter(collection)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)