# Номер кортежа

# Напишите программу, которая создает кортеж из 5 элементов, запрашиваемых у пользователя.
# Затем программа должна запросить у пользователя индекс элемента и вывести значение элемента по этому индексу.
# Если индекс выходит за пределы кортежа, программа должна вывести соответствующее сообщение.

my_tuple = (tuple(input('Enter a tuple with 5 elements split by coma: ').split(',')))
while len(my_tuple) < 5 or len(my_tuple) > 5:
    my_tuple = tuple(input("Invalid tuple length. Please enter a tuple with 5 elements split by comma: ").split(','))

while True:
    ind = int(input("Enter index between 0 and 4: "))
    if ind in range(len(my_tuple)):
        break
    else:
        print("Invalid index")
        continue

print(my_tuple[ind])

