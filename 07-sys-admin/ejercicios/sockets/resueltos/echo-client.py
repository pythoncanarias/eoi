import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        string = input('> ')
        s.sendall(string.encode('utf-8'))
        data = s.recv(1024)
        if data == b'exit':
            break

print('Received', repr(data))
