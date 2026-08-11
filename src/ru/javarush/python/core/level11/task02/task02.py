# Динамический импорт модуля

# Напишите программу, которая запрашивает у пользователя название модуля для импорта
# и имя функции для вызова из этого модуля.
# Программа должна динамически импортировать модуль и вызвать указанную функцию с любым аргументом.
# Для получения дочернего элемента у модуля используйте функцию getattr

module_name = input('Provide a module name: ')
module = __import__(module_name)
func_name = input('Provide a function name: ')
function = getattr(module, func_name)
function(None)
