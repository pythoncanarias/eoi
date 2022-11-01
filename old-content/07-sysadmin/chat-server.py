#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f'Conexión desde {addr}')
    while True:
        data = conn.recv(1024)
        if data == b'':
            break
        print(f'Cliente envió: "{data.decode("utf-8")}"')
        entradausuario = input('> ')
        if entradausuario == 'toledo':
            break
        entradausuario = bytes(entradausuario, 'utf-8')
        conn.send(entradausuario)
