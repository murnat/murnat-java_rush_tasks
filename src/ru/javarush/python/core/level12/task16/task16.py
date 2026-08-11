# Сериализация с помощью yaml

# Напишите программу, которая сериализует и десериализует объект Python с использованием модуля yaml.
# Объектом для сериализации будет словарь, содержащий информацию о фильме: название, режиссёр и год выпуска.

import yaml

# Пример словаря с информацией о фильме
film_info = {
    'title': 'Inception',
    'director': 'Christopher Nolan',
    'year': 2010
}

film_str = yaml.dump(film_info)
print(film_str)

film_loaded = yaml.load(film_str, Loader=yaml.FullLoader)
print(film_loaded)

