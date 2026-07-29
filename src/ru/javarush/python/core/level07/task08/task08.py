# Лига Плюща

# Напишите программу, которая создает словарь с информацией о студенте (имя, возраст, университет).
# Программа должна:
# Проверить наличие значения "MIT" с использованием метода values().
# Проверить наличие значения "Harvard" с использованием функции set().
# Проверить наличие значения 22 с использованием генератора.

student = {
    "name":"John Snow",
    "age":25,
    "university":"Harvard"
}

if "MIT" in student.values():
    print("MIT is in values")
else:
    print("MIT is not in values")

value_set = set(student.values())
if "Harvard" in value_set:
    print("Harvard is in values")
else:
    print("Harvard is not in values")

value_to_find = 22

if any(value == value_to_find for value in student.values()):
    print(f"{value_to_find} is in values")
else:
    print(f"{value_to_find} is not in values")