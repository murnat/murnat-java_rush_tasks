# Выполнение POST-запроса с использованием http.client

# Напишите программу, которая выполняет POST-запрос на сервер с передачей данных и выводит ответ.
# Программа должна обрабатывать возможные ошибки.

import http.client
import json

try:
    connect = http.client.HTTPSConnection("jsonplaceholder.typicode.com")

    payload = json.dumps({
        "title": "foo",
        "body": "bar",
        "userId": 1
    })

    headers = {
        'Content-Type': 'application/json'
    }

    connect.request("POST", "/posts", body=payload, headers=headers)

    response = connect.getresponse()
    print(response.status, response.reason)

    data = response.read().decode('utf-8')
    print(f'Response data: {data}')

except http.client.HTTPException as e:
    print(f'HTTP error: {e}')
except Exception as e:
    print(f'Some other error: {e}')
finally:
    connect.close()