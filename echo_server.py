import socket

HOST = '127.0.0.1'  # Локальний хост
PORT = 65432        # Порт для прослуховування

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server started at {HOST}:{PORT}")
    
    while True:
        conn, addr = server_socket.accept()  # Приймаємо з'єднання
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)  # Отримуємо дані
                if not data:
                    break
                print(f"Received: {data.decode('utf-8')}")
                conn.sendall(data)  # Надсилаємо ті ж дані назад



