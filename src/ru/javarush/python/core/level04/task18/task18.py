# Нашли кота

# Напишите функцию create_cat_profile(name, age, breed="Неизвестно"), которая принимает имя, возраст и необязательный параметр "порода" (по умолчанию "Неизвестно").
# Функция должна выводить профиль кота в формате "Имя: [name], Возраст: [age], Порода: [breed]".
# Затем напишите программу, которая вызывает эту функцию с различными параметрами.

def create_cat_profile(name, age, breed="Неизвестно"):
    print(f"Имя: {name}, Возраст: {age}, Порода: {breed}")

create_cat_profile("Kitsun",11,"Brit")
create_cat_profile("Shvaya",3,"calico")
create_cat_profile("Bzun",19)