# Запись бинарных данных

# Напишите программу, которая читает изображение input_image.jpg и записывает его в другой файл output_image.jpg.

with open('input_image.jpg','rb') as file:
    image = file.read()
with open('output_image.jpg','wb') as file:
    file.write(image)