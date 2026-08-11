# Переупаковка исключения

# Напишите функцию validate_input, которая принимает строку и проверяет,
# что она не пустая и что ее длина не превышает 10 символов.
# Если строка пустая, запустите ValueError с сообщением "Input cannot be empty".
# Если строка слишком длинная, запустите ValueError с сообщением "Input is too long".
# Затем перехватите это исключение и переупакуйте его в пользовательское исключение InputValidationError, сохранив исходное исключение как причину.

class InputValidationError(Exception):
    pass

def validate_input(a : str):
    try:
        if a == "":
            raise ValueError('Input cannot be empty')
        elif len(a) > 10:
            raise ValueError('Input is too long')
    except ValueError as e:
        raise InputValidationError(str(e)) from e

# Пример использования:
try:
    validate_input("fnlsdnldn.,mnb")
except InputValidationError as e:
    print(f"Caught custom exception: {e}")
    print(f"Original exception: {e.__cause__}")




