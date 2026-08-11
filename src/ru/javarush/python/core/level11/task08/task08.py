# Использование пакета cowsay

# Установите пакет cowsay и используйте его для отображения сообщения.
# Выполните следующие шаги:
# Установите пакет cowsay с помощью pip.
# Используйте пакет cowsay для отображения сообщения "Нужно было учить Python...".
# Удалите пакет cowsay с помощью pip.


# Установка пакета cowsay
import subprocess
subprocess.run(['pip', 'install', 'cowsay'])
import cowsay

# Использование пакета cowsay для отображения сообщения
cowsay.cow("Нужно было учить Python...")

# Удаление пакета cowsay
subprocess.run(['pip', 'uninstall', 'cowsay', '-y'])