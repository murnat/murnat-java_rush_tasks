# Проверка на пустоту.

# Напишите программу, которая создает несколько словарей с различным количеством элементов.
# Программа должна:
# Вывести количество элементов в каждом словаре.
# Проверить, пустой ли каждый словарь, и вывести соответствующее сообщение.
# Для проверки пустоты словаря нужно создать функцию check_empty

dict1 = {}
dict2 = {"name":"John","surname":"Snow","age":25}
dict3 = dict(pet = "dog",name = "Iris",age = 7,color = "red and white")
print(f'The length of the first dict is {len(dict1)}')
print(f'The length of the second dict is {len(dict2)}')
print(f'The length of the third dict is {len(dict3)}')

def check_empty(dict_to_check, dict_name):
    if dict_to_check == {}:
       print(f'{dict_name} is empty')
    else:
        print(f'{dict_name} is not empty')

check_empty(dict1,"Dictionary 1")
check_empty(dict2,"Dictionary 2")
check_empty(dict3,"Dictionary 3")