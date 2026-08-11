# Создание сокет-сервера

# Напишите программу, которая создает сокет-сервер, принимает входящие соединения от клиентов и отвечает им "Hello, client!".

import socket

# Создание сокета
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
# Связывание сокета с адресом и портом
    server_socket.bind(('localhost', 12345))
# Прослушивание входящих соединений
    server_socket.listen(5)
    print("Server waits for the connection...")

    while True:
        try:
        # Принятие нового соединения
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")

        # Получение данных от клиента
            data = client_socket.recv(1024)
            print(f"Received: {data.decode('utf-8')}")

        # Отправка данных клиенту
            client_socket.sendall(b'Hello, client!')
            client_socket.close()

        except socket.error as e:
            print(e)

        except Exception as e:
            print(e)

