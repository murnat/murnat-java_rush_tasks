# Защищайтесь.

# Создайте класс Car, который будет иметь публичный атрибут brand и защищенный атрибут _model.
# Добавьте методы для получения и установки значения защищенного атрибута _model.
# Создайте объект класса Car, установите значения атрибутов и выведите их на экран.

class Car:
    def __init__(self, brand):
        self.brand = brand
        self._model = None

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model


new_car =  Car('Renault')
new_car.set_model('Megane')
print(f'The new car brand is {new_car.brand} and the model is {new_car.get_model()}')


