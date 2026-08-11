# Использование пакета requests.

# Используйте пакет requests для выполнения GET-запроса к API.
# Выполните следующие шаги:
# Установите пакет requests с помощью pip.
# Используйте пакет requests для выполнения GET-запроса к API, например, к https://jsonplaceholder.typicode.com.
# Выведите на экран результат запроса.

import subprocess
subprocess.run(['pip', 'install', 'requests'])

import requests

get_response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print(get_response.json())
