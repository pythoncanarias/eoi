#!/usr/bin/env python
# coding: utf-8

import socket

def respond(client, addr):
    response = input("Enter a value: ")
    message = f"Hello {addr} this is your response: {response}"
    client.send(message.encode('utf8'))
    client.close()
    return response == 'exit'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8401))
server.listen(1)
try:
    while True:
        client, addr = server.accept()
        must_exit = respond(client, addr)
        if must_exit:
            break
finally:
    server.close()