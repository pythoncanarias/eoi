#!/usr/bin/env python3

"""Servidor UDP de ejemplo
"""

import socket
import logging

FORMAT = '%(asctime)-15s %(name)s %(levelname)-8s %(message)s'

logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger('UDPSRV')

PORT = 20022

BUFFER_SIZE = 1024

IS_WORKING = True

server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', PORT))  # Bind to address and ip
logger.info("UDP server up and listening on port %s", PORT)

while(IS_WORKING):
    message, client_address = server_socket.recvfrom(BUFFER_SIZE)
    message = message.decode('utf-8')
    logging.info("Client %r send message %r", client_address, message)
    response = message.upper()
    server_socket.sendto(response.encode('utf-8'), client_address)
