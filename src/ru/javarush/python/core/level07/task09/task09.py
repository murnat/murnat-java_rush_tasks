# Студент - это звучит гордо.

# Напишите программу, которая создает словарь с информацией о студенте (name и age).
# Программа должна:
# Добавить новый элемент "university" в словарь.
# Добавить элемент "city" только в том случае, если его еще нет в словаре.
# Добавить несколько новых элементов с использованием метода update().
# Вывести обновленный словарь после каждого добавления.

student = {
    "name":"John Snow",
    "age":25
}

student["university"] = "Harvard University"
print(student)

if "city" not in student.keys():
    student["city"] = "New York"
print(student)

updates = {
    "average mark":81,
    "has another diploma":True
}
student.update(updates)
print(student)



