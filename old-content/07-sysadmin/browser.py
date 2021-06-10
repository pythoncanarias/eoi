#!/usr/bin/env python3

import socket
import sys

PORT = 80

def get(site):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((site, PORT))
        request = f'GET / HTTP/1.1\r\nHost: {site}\r\n\r\n'
        s.send(bytes(request, 'ascii'))
        data = s.recv(4096)
        return data.decode('ascii').split('\r\n\r\n')[1]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Uso: {sys.argv[0]} example.com')
    else:
        print(get(sys.argv[1]))
