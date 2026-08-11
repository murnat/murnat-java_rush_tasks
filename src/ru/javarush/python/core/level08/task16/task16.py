# Платформа.

# Напишите программу, которая получает и выводит информацию о текущей операционной системе
# и платформе с помощью библиотеки platform. Программа должна:
# Получить и вывести имя операционной системы.
# Получить и вывести имя компьютера в сети (hostname).
# Получить и вывести версию операционной системы.
# Получить и вывести архитектуру процессора.
# Получить и вывести версию Python.

import platform

os_name = platform.system()
print("Operating System:", os_name)

host_name = platform.node()
print("Hostname:", host_name)

os_version = platform.version()
print("OS Version:", os_version)

processor_architecture = platform.processor()
print("Processor Architecture:", processor_architecture)

python_version = platform.python_version()
print("Python Version:", python_version)