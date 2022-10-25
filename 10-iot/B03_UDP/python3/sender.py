# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)
# Parte de pyton3

import socket

UDP_PORT = 7000  # puerto al que enviaremos los mensajes
# cambiar la ip por la del destino, o por 255 para broadcast
IP_DESTINO = "192.168.1.181"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mensaje_a_enviar = "ping"
print("enviando: {}".format(mensaje_a_enviar))
sock.sendto(mensaje_a_enviar.encode(), (IP_DESTINO, UDP_PORT))  # mensaje en bytes
sock.settimeout(5)  # tiempo maximo que esperamos por la respuesta
print("esperando respuesta...")
try:
    data, addr = sock.recvfrom(256)  # payload maximo en bytes
except OSError:
    print("no ha llegado nada")
else:
    print("Ha llegado el siguiente mensaje de {} por puerto {}:".format(addr[0], addr[1]))
    print(data.decode())  # el mensaje llega en bytes, lo pasamos a string
finally:
    sock.close()
