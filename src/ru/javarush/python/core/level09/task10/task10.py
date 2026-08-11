# Рычащие.

# Создайте базовый класс Animal с методом speak, который возвращает строку "Ррррр!".
# Затем создайте дочерний класс Dog, который будет наследовать от Animal и переопределять метод speak,
# добавляя к поведению родительского класса собственное поведение с использованием метода super().

class Animal:
    def speak(self):
        return f'Ррррр!'

class Dog(Animal):
    def speak(self):
        parent_speech = super().speak()
        return f'{parent_speech} Гав!'

dog = Dog()
print(dog.speak())