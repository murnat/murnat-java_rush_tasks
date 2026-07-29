# Неизвестность

# Напишите программу, которая запрашивает у пользователя два числа.
# Если пользователь не вводит значение (пустая строка), используйте значение по умолчанию None для этого числа.
# Вычислите и выведите сумму этих чисел.

# request numbers
num1 = input("Enter a number: ") or None
num2 = input("Enter another number: ") or None
# print results
if not num1 or not num2:
    print("Сумма чисел неизвестна")
else:
    print(f"Сумма чисел {int(num1)+int(num2)}")