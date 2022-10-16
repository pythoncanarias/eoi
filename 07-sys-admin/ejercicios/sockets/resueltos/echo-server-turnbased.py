import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected from', addr)
        while True:
            print('client says: ', end='', flush=True)
            data = conn.recv(1024)
            if not data or data == b'exit':
                break
            print(data.decode('utf-8'))
            data = input('> ')
            conn.sendall(data.encode('utf-8'))
