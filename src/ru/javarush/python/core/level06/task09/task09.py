# Котовасия

# Напиши программу, которая хранит множество из 5 самых популярных имен котов.
# Пользователь должен пытаться угадать их. Когда он угадывает имя кота, оно удаляется из множества.
# Цель игры - угадать всех котов за как можно меньшее число попыток.

cat_set = {'Bzun', 'Kitsun', 'Shvaya', 'Mayka', 'Rusya'}
count = 0
while cat_set:
    temp_element = input('Guess a cat name: ')
    cat_set.discard(temp_element)
    count += 1
print(f'All names are guessed. Attempts: {count}.')