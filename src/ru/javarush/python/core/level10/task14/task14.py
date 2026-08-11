# Иерархия пользовательских исключений

# Создайте базовый класс исключений ApplicationError и два подкласса NegativeValueError и ValueTooLargeError.
# Реализуйте функцию check_number, которая будет вызывать соответствующее исключение, если число отрицательное или слишком большое.
# Обработайте исключения в блоке try-except.

class ApplicationError(Exception):
    pass
class NegativeValueError(ApplicationError):
    pass
class ValueTooLargeError(ApplicationError):
    pass

def check_number(number):
    if number < 0:
        raise NegativeValueError(f'{number} is negative')
    elif number > 150:
        raise ValueTooLargeError(f'{number} is too large')

try:
    check_number(-2)
except NegativeValueError as e:
    print(f'Error occurred: {str(e)}')
except ValueTooLargeError as e:
    print(f'Error occurred: {str(e)}')
