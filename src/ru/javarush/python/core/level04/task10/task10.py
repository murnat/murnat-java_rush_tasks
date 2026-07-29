# Високосный год

# Напишите программу, которая запрашивает у пользователя год и проверяет, является ли он високосным.
# Используйте логические операторы для проверки условий високосного года.
# Високосный год делится на 4, но не делится на 100, за исключением годов, которые делятся на 400.

# request a year
year = int(input("Enter the year: "))
# check if the year is a leap
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# print the result
if is_leap:
    print('The year is leap')
else:
    print('The year is NOT leap')
