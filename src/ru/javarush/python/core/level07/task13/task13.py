# Обход словаря.

# Напишите программу, которая создает словарь с информацией о человеке (например, имя, возраст, адрес, и контактная информация).
# Программа должна:
# Перебрать все элементы словаря, включая вложенные словари, с использованием циклов.
# Реализовать функцию для обхода всех уровней вложенности и вывода ключей и значений.

address = {
    "street": "56,Sich",
    "zip": "11803"
}

details = {
    "age": 45,
    "city": "Kyiv",
    "address": address
}

person = {
    "name": "Lia",
    "details": details,
    "gender": "female"
}

def print_person(d, indent=0):
    for key, value in d.items():
        print("  " * indent + str(key) + ": ", end="")
        if isinstance(value, dict):
            print()
            print_person(value, indent + 1)
        else:
            print(value)

print_person(person)