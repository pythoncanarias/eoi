# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)
# Parte de micrpython (ESP32)

import socket

UDP_PORT = 7000  # puerto por el que escucharemos

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # address family (ip4), socket type (UDP)
sock.bind( ("0.0.0.0", UDP_PORT) )  # escuchamos por el puerto

while True:
    print("Escuchando por puerto {}...".format(UDP_PORT))
    data, addr = sock.recvfrom(256)
    print("Recibido mensaje de {} por el puerto {}:".format(addr[0], addr[1]))
    print(data.decode())  # llega en bytes, lo pasamos a string
    respuesta = "pong"
    print("Enviando respuesta: {}".format(respuesta))
    sock.sendto(respuesta, addr)
sock.close()
