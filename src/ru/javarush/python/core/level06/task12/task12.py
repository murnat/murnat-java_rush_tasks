# Замена

# Напишите программу, которая создает множество, содержащее названия нескольких фруктов.
# Программа должна вывести фрукты на экран.
# Затем программа должна запросить у пользователя индекс (с учетом порядка вывода на экран) и новое название фрукта для замены.
# Затем найти фрукт по индексу, заменить его новым названием и вывести обновленное множество.

fruit_set = {'apple', 'banana', 'orange', 'pear', 'peach'}
print(fruit_set)
ind_to_replace = int(input('Provide an index of the fruit to replace (starting from 0): '))
new_fruit = input('Provide a new fruit: ')

for index,element in enumerate(fruit_set):
    if index == ind_to_replace:
        fruit_set.remove(element)
        fruit_set.add(new_fruit)

print(fruit_set)
