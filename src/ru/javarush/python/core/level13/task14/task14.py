# Создание сокет-клиента

# Напишите программу, которая создает сокет-клиента, подключается к сокет-серверу, отправляет ему сообщение и получает ответ.

import socket

server_host = 'localhost'
server_port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_host, server_port))
    print(f'Connected to server: {server_host}:{server_port}')
    client_socket.sendall(b'Hello, server!')
    received_data = client_socket.recv(1024).decode('utf-8')
    print(f'Received data: {received_data}')

except socket.error as e:
    print(f'Socket error: {e}')

finally:
    client_socket.close()
    print('Connection closed')

