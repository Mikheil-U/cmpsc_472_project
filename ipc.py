import socket
import multiprocessing


# Function to send data over a socket
def send_data():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen(1)
    print("Server: Waiting for a connection...")
    conn, addr = server_socket.accept()
    print(f"Server: Connected by {addr}")
    data = "Hello from the server"
    conn.send(data.encode())
    conn.close()
    server_socket.close()


# Function to receive data over a socket
def receive_data():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))
    received_data = client_socket.recv(1024)
    print(f"Client received: {received_data.decode()}")
    client_socket.close()


def ipc_run():
    server_process = multiprocessing.Process(target=send_data)
    client_process = multiprocessing.Process(target=receive_data)

    server_process.start()
    client_process.start()

    server_process.join()
    client_process.join()


