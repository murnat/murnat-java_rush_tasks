# Нечетный

# Напишите программу, которая выводит числа от 1 до 100, пропуская четные числа.
# Используйте цикл while и оператор continue для пропуска четных чисел.

count = 0

while count < 100:
# increase the counter
    count += 1
# skip the loop for even numbers
    if count % 2 == 0:
        continue
# print uneven numbers
    else:
        print(count)

