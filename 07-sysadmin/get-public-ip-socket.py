import socket

with socket.socket() as s:
    s.connect(('ifconfig.io', 80))
    s.sendall(b'GET / HTTP/1.1\r\nHost: ifconfig.io\r\nUser-Agent: curl\r\n\r\n')
    data = s.recv(1024)
    data_str = data.decode('ascii')
    ip = data_str = data_str.split('\r\n\r\n')[1].rstrip()
    print(ip)
