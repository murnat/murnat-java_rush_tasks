# Преобразование данных.

# Напишите функцию convert_and_sum, которая принимает два аргумента в виде строк,
# преобразует их в целые числа и возвращает их сумму.
# Обработайте исключения, которые могут возникнуть при преобразовании строк в числа
# (например, если переданы некорректные значения).

def convert_and_sum(a:str,b:str):
    try:
        first_arg = int(a)
        second_arg = int(b)
    except ValueError:
        return f'Incorrect value'
    else:
        return first_arg + second_arg

print(convert_and_sum('1','2'))
print(convert_and_sum('1','int'))
print(convert_and_sum('1','0.111'))

