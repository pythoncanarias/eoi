from machine import Pin
import network
from juego import Juego
from credenciales import ssid, password
import utime


def conectar_wifi():
    led = Pin(2, Pin.OUT)
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


conectar_wifi()
juego = Juego("Dani")
juego.start()
