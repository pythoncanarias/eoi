#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        entradausuario = input('> ')
        if entradausuario == 'toledo':
            break
        entradausuario = bytes(entradausuario, 'utf-8')
        s.send(entradausuario)
        data = s.recv(1024)
        if data == b'':
            break
        print(f'Servidor envió: "{data.decode("utf-8")}"')

