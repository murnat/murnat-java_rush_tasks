# Создание простого итератора


# Напишите класс SimpleIterator, который будет итерироваться по последовательности чисел от start до end.
# Реализуйте методы __iter__ и __next__.

class SimpleIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current


