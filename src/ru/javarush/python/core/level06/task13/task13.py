# Объединение и пересечение

# Напишите программу, которая создает два множества из элементов, запрашиваемых у пользователя.
# Программа должна объединить эти множества с использованием метода union() и найти их пересечение с использованием метода intersection().
# Программа должна вывести оба результата

set_1 = {int(input('Provide any integer for the first set: ')) for _ in range(5)}
set_2 = {int(input('Provide any integer for the second set: ')) for _ in range(5)}

united_set = set_1.union(set_2)
print(f'Union of two sets is {united_set}')

sets_intersection = set_1.intersection(set_2)
print(f'Intersection of two sets is {sets_intersection}')