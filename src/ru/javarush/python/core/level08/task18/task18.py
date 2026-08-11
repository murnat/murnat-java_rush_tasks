# Timezone.

# Напишите программу, которая конвертирует текущее время из часового пояса UTC в заданный пользователем часовой пояс.
# Программа должна:
# Получить текущее время в часовом поясе UTC.
# Запросить у пользователя смещение в часах относительно UTC.
# Создать объект часового пояса с заданным смещением.
# Конвертировать текущее время в заданный часовой пояс.
# Вывести текущее время в UTC и в заданном часовом поясе.

import datetime

current_time_utc = datetime.datetime.now(datetime.timezone.utc)
delta = int(input("Enter time difference in hours: "))
new_timezone = datetime.timezone(datetime.timedelta(hours=delta))
new_time = current_time_utc.astimezone(new_timezone).time()
print(f'UTC time is {current_time_utc.strftime("%H:%M")}. Time in the new timezone is {new_time.strftime("%H:%M")}')