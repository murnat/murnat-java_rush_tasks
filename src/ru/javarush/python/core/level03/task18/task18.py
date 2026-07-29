# Считаем деньги

# Напишите программу, которая запрашивает у пользователя числа и суммирует их, пока пользователь не введет отрицательное число.
# Используйте цикл while и оператор break для завершения ввода при отрицательном числе.

total_sum = 0
while True:
    # request a number
    number = int(input("Enter a positive number:"))
    # add number to the total_sum if number is positive
    if number >= 0:
        total_sum += number
    # stop loop if number is negative
    else:
        break
# print the result
print(total_sum)
