# Выполнение GET-запроса с использованием http.client

# Напишите программу, которая выполняет GET-запрос на сервер, читает и выводит ответ.
# Программа должна обрабатывать возможные ошибки.

import http.client

try:
    connect = http.client.HTTPSConnection("www.google.com")
    connect.request("GET", "/")

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


