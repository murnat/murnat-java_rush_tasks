# Создаем объекты.

# Создайте класс Car с атрибутами make, model и year.
# Добавьте метод display_info(), который выводит информацию о машине.
# Затем создайте объект этого класса и вызовите метод display_info().

class Car:
    make = "Renault"
    model = "Megane"
    year= 2013
    def display_info(self):
        print(f'Car is made by {self.make}, the model is {self.model} and the year is {self.year}')

new_car = Car()
new_car.display_info()