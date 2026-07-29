# Добавление элемента

# Напишите программу, которая создает кортеж из 5 элементов, запрашиваемых у пользователя.
# Затем программа должна запросить у пользователя новый элемент и добавить его в конец кортежа, создавая новый кортеж.
# Программа должна вывести обновленный кортеж.

my_tuple = tuple([input('Enter a tuple element: ') for _ in range(5)])
my_list = list(my_tuple)
my_list.append(input('Provide one nore element: '))
my_tuple = tuple(my_list)
print(my_tuple)
