# В глубинах самых глубин.

# Напишите программу, которая создает словарь с информацией о человеке (name, age, address (city, street, house), contact_info(email, phone)).
# Программа должна:
# Изменить значения верхнего уровня, вложенного словаря и более глубокого уровня вложенности.
# Добавить новый элемент во вложенный словарь.
# Удалить элемент из вложенного словаря и верхнего уровня.

address = {
    "street": "Sich",
    "house": 56,
    "zip": "11803"
}

contact_info = {
    "email":"test@test.com",
    "phone":"123-456-7890"
}

person = {
    "name": "Lia",
    "age":45,
    "address": address,
    "contact_info": contact_info
}

person["name"] = "LiaM"
person["address"]["zip"] = 30811
person["contact_info"]["WatsApp"] = "@liam"
del person["name"]
del person["address"]["street"]

