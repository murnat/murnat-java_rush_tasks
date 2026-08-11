# Обработка исключений.

# Напишите функцию safe_division, которая принимает два числа и выполняет их деление.
# Обработайте исключения, которые могут возникнуть при делении на ноль
# и при передаче некорректных значений (например, строки вместо чисел).
# Функция должна возвращать сообщение об ошибке или результат деления.

def safe_division(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        return f'Division by zero'
    except TypeError:
        return f'Wong type of variable(s)'
    else:
        return result

print(safe_division(1,0))
print(safe_division(2,int))
print(safe_division(1,2))


