# Случайный середнячок

# Напишите программу, которая генерирует 10 случайных чисел в диапазоне от 1 до 100, используя библиотеку random.
# Затем подсчитайте их среднее значение и выведите его на экран.

import random
# create list wth 10 random numbers
rand_nums = [random.randint(1, 100) for _ in range(10)]
# calculate average for all numbers in list
total = sum(rand_nums) / len(rand_nums)
# print result
print(total)
