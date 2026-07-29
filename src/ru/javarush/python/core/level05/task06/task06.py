# Поиск строки

# Напишите программу, которая создает список из 10 элементов.
# Программа просит пользователя ввести строку, а потом проверяет - есть она в списке или нет.

my_list = ["bird", "car", "mouse", "cat", "food", "toy", "arm", "tiger", "dog", "lion"]
element = input("Provide a string: ")
if element in my_list:
    print("Element found")
else:
    print("Element not found")
