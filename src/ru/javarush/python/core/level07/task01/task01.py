# Словарь.

# Напишите программу, которая создает словарь с информацией о человеке (например, имя, возраст и город) тремя различными способами:
# Использование фигурных скобок {}.
# Использование функции dict() с последовательностью пар ключ-значение.
# Использование функции dict() с именованными аргументами.
# Программа должна вывести все три словаря.

person1 = {"Name":"John","Surname":"Snow","Birth year":930}
person2 = dict([("Name","Cercey"),("Surname","Lannister"),("Birth year",920)])
person3 = dict(Name = "Tyrion",Surname = "Lannister",Birth_year = 910)

print(person1)
print(person2)
print(person3)