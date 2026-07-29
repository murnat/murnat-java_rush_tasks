# Максималист

# Напишите функцию find_max(a, b), которая принимает два числа в качестве аргументов и возвращает большее из них.
# Если числа равны, функция должна вернуть любое из них.
# Затем напишите программу, которая запрашивает у пользователя два числа, вызывает эту функцию и выводит результат.
# function finding bigger number
def find_max(a,b):
    if a >= b:
        return a
    else:
        return b
# request numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
# print result
print(find_max(num1,num2))