import socket


def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)

    print("TCP Server listening on port 12345...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        data = client_socket.recv(1024)
        print(f"Received data: {data.decode()}")

        client_socket.sendall(b'Hello from server')
        client_socket.close()


if __name__ == "__main__":
    tcp_server()
