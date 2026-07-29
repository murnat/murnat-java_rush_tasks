# Лес

# Напишите программу, которая создает список из названий деревьев, затем с использованием цикла и функции enumerate() выводит каждый элемент списка и его индекс.

trees = ['pine','oak','maple','hornbeam','birch','linden']
for index, element in enumerate(trees):
    print(index, element)