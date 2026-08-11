# Извлечение информации из исключения

# Напишите функцию read_integer, которая принимает строку и пытается преобразовать её в целое число.
# Если возникает ValueError, обработайте исключение и выведите аргументы ошибки и тип ошибки.
# Дополнительно, сохраните исключение в переменной и выведите её за пределами блока except.

def read_integer(a : str):
    error = None
    try:
        return int(a)
    except ValueError as e:
        error = e
        print(f'Error type: {type(e)}, error arguments: {e.args}')
    print(f'Outside Try {error}')

read_integer('jhjh')