# Удаление элемента

# Напишите программу, которая создает список из 5 элементов, запрашивает у пользователя индекс элемента для удаления
# и удаляет элемент по этому индексу с использованием метода pop().
# Программа должна вывести обновленный список и удаленный элемент.
# Если индекс не существует, программа должна вывести сообщение об этом.

my_list = ["bird", "car", "mouse", "cat", "food"]
ind = int(input("Please provide index of element to delete: "))
if ind < 0 or ind > len(my_list)-1:
    print("Please provide a valid index")
else:
    print(my_list.pop(ind))
    print(*my_list, sep=", ")