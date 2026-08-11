# Использование прокси-сервера с модулем requests

# Напишите программу, которая отправляет GET-запрос через прокси-сервер с использованием библиотеки requests.

import requests

url = 'http://httpbin.org/ip'

proxies = {'http': '178.212.144.7:80', 'https': '113.160.132.26:8080'}

try:
    response = requests.get(url, proxies=proxies)
    print(response.status_code)
    print(response.reason)
    print(response.text)
except requests.exceptions.ProxyError as err:
    print(err)
except requests.exceptions.RequestException as err:
    print(err)
except Exception as err:
    print(err)
