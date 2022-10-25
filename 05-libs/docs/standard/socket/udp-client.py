#!/usr/bin/env python3

import socket
import sys

HOST = 'localhost'
PORT = 20022
BUFF_SIZE = 1024

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

message = " ".join(sys.argv[1:]) or "ping"
client_socket.sendto(message.encode('utf-8'), (HOST, PORT))
response, server_address = client_socket.recvfrom(BUFF_SIZE)
response = response.decode('utf-8')
print(f"Repuesta del servidor: {response}")
