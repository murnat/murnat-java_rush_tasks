# Обработка ошибок запросов с модулем requests

# Напишите программу, которая отправляет GET-запрос на сервер и обрабатывает возможные ошибки, используя исключения.

import requests

try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f'HTTP Error occurred: {e}')
except requests.exceptions.RequestException as e:
    print(f'Other error occurred: {e}')
else:
    print('Success')