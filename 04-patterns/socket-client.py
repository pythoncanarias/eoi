#!/usr/bin/env python
# coding: utf-8

import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8401))
response = client.recv(1024).decode('utf-8')
print(f"Received: {response}".format(client.recv(1024)))
client.close()