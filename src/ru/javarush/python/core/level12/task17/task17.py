# Сериализация списка в файл

# Напишите программу, которая сериализует список в файл с использованием модуля pickle,
# а затем десериализует этот список из файла.

import pickle

# Пример списка для сериализации
data = [1, 2, 3, 'a', 'b', 'c']


with open("list.pkl", "wb") as file:
    pickle.dump(data, file)

with open("list.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)