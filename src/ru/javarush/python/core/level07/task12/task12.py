# Словарь из списка кортежей.

# Напишите программу, которая создает список кортежей с информацией о сотрудниках (например, имя и должность).
# Программа должна:
# Использовать dictionary comprehension для создания словаря из списка кортежей.
# Вывести созданный словарь.

employees = [("Igor Kotchetkov","Lead dev"),("Serhiy Riznyk","Senior dev"),("Lia Mur","Lead QA")]

employee_dict = {key:value for key,value in employees}
print(employee_dict)
