# Ты ему слово, он тебе ссылку

# Напишите программу, которая создает два списка, присваивает один из них другой переменной и проверяет, указывают ли обе переменные на один и тот же объект.
# Используйте оператор is для проверки ссылок.

# create two lists
list1 = [1,2,3]
list2 = list1
if list1 is list2:
    print(f"Lists are pointing the same object")
else:
    print(f"Lists are not pointing the same object")
