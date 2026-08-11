# Полиморфизм.

# Создайте базовый класс Shape с методом perimeter, который будет возвращать периметр фигуры.
# Затем создайте дочерние классы Triangle и Rectangle, которые будут переопределять метод perimeter для расчета периметра своих фигур.
# Используйте полиморфизм, чтобы создать список фигур и вычислить их периметры.

class Shape:
    def perimeter(self):
        raise NotImplementedError("Subclasses should implement this method!")

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b)*2

shapes = [Triangle(3, 4, 5), Rectangle(4, 6), Triangle(5, 12, 13)]
perimeters = [shape.perimeter() for shape in shapes]

for perimeter in perimeters:
    print(perimeter)
