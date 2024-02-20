import socket

def server_program():
    #get host name 
    host = socket.gethostname() #the host name
    port = 3024 #the port where the process will run

    server_socket_practise = socket.socket()
    server_socket_practise.bind(('',port))


    print("Connections is on: " + str(port) + " " + str(host))
    server_socket_practise.listen(4) #this is to declare how many clients a server can listen too at a time
    conn, address = server_socket_practise.accept()

    print("Connection from: " + str(address))

    while True:
        data = conn.recv(10240).decode()
        if not data:
            break
        print("from connected user: " + str(data) )
        data = input(' -> ')
        conn.send(data.encode())

    conn.close()

if __name__ == '__main__':
    server_program()
    