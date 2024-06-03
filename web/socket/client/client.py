import socket


def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    client_socket.sendall(b'Hello from client')

    data = client_socket.recv(1024)
    print(f"Received data from server: {data.decode()}")

    client_socket.close()


if __name__ == "__main__":
    tcp_client()
