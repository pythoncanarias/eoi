from machine import Pin
import utime
import network
import usocket as socket
from errno import ETIMEDOUT
from credenciales import ssid, password


# Constantes
UDP_PORT = 5005

# Configurar hardware
led = Pin(2, Pin.OUT)
boton = Pin(0, Pin.IN)

# Conectando a la wifi
led.value(0)  # led inicialmente encendido para indicar que nos estamos intentando conectar a la wifi
print("\nConectado a {} ...".format(ssid), end='')
red = network.WLAN(network.STA_IF)
red.active(True)
# red.scan()  # Escanea y te muestra redes disponibles
red.connect(ssid, password)
while not red.isconnected():  # Espera hasta que este conectado
    utime.sleep(0.1)
print("conectado!")
print(red.ifconfig())  # ver la ip que se nos ha asignado por DHCP
led.value(1)  # apagamos led para indicar que ya estamos conectados

# Funciones adicionales
def parpadeo_breve():
    """ un breve parpadeo del led para indicar que se envio un paquete """
    led.value(0)
    utime.sleep_ms(100)
    led.value(1)

# En este ejemplo no nos "enlazamos" en ningun puerto
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # address family (ip4), socket type (UDP)
# sock.bind(('0.0.0.0', UDP_PORT))  # tupla ip puerto
# si el puerto se quedo abierto, lanza excepcion OSError: [Errno 98] EADDRINUSE

while True:
    mensaje = "hay alguien ahi?"
    print("enviando: " + mensaje)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # address family (ip4), socket type (UDP)
    # sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)    
    sock.sendto(mensaje, ("192.168.1.255", UDP_PORT))  # Si el ultimo valor de la ip es 255 lo mandamos como broadcast
    sock.settimeout(5)  # tiempo en segundos que espera por la respuesta, luega salta excepcion ETIMEDOUT
    try:
        data, origen = sock.recvfrom(256)   # tamaño maximo de paquete en bytes que podemos recibir
        # print(data, origen)
        print("Recibido: '{}' de {}".format(data.decode(), origen[0]))
    except OSError:  #ETIMEDOUT
        print("parece que no hay nadie :(")
    sock.close()
    parpadeo_breve()
    utime.sleep(1)
