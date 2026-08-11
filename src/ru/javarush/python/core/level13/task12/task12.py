# Использование прокси-сервера с модулем http.client

# Напишите программу, которая отправляет GET-запрос через прокси-сервер с использованием библиотеки http.client.

import http.client

url = 'httpbin.org'
path = '/ip'
proxy_host = '113.160.132.26'
proxy_port = 8080

try:

    conn = http.client.HTTPConnection(proxy_host, proxy_port)
    conn.set_tunnel(url)
    conn.request('GET', path, headers={'Host': url})

    response = conn.getresponse()
    print(response.read().decode('utf-8'))
    print(response.status, response.reason)

except http.client.HTTPException as e:
    print(e)

except Exception as e:
    print(e)

finally:
    conn.close()
