import socket

HOST = '127.0.0.1'  # Адреса сервера
PORT = 65432        # Порт, що використовується сервером

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))  # З'єднуємося із сервером
    while True:
        message = input("Enter message to send to server (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode('utf-8'))  # Надсилаємо дані
        data = client_socket.recv(1024)  # Отримуємо відповідь
        print(f"Received from server: {data.decode('utf-8')}")




