import socket

def client_program():
    host = socket.gethostname()
    port =3024

    client_socket = socket.socket()
    client_socket.connect((host, port))

    print("Connections is on: " + str(port) + " " + str(host))
    message = input(" -> ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(10240).decode()

        print('Received from server: ' + data)

        message = input(" -> ")  # again take input

    client_socket.close()


if __name__ == '__main__':
    client_program()
