# День рождения.

# Напишите программу, которая запрашивает у пользователя дату его рождения (год, месяц и день),
# а затем выводит количество дней, прошедших с этой даты до сегодняшнего дня.
# Программа должна:
# Запросить у пользователя год, месяц и день его рождения.
# Создать объект даты рождения с помощью класса datetime.date.
# Получить текущую дату с помощью метода today().
# Вычислить разницу между текущей датой и датой рождения.
# Вывести количество дней, прошедших с даты рождения.

import datetime

day = (int(input('Provide day of birth: ')))
month = (int(input('Provide month of birth: ')))
year = (int(input('Provide year of birth: ')))
birthday = datetime.date(year, month, day)
current_date = datetime.date.today()

difference = current_date - birthday
print(difference.days)