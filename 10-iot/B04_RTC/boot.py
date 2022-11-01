# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
# import uos
# uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()


from machine import Pin
import utime
import network
from credenciales import ssid, password


# Configurar hardware
led = Pin(2, Pin.OUT)
# boton = Pin(0, Pin.IN)

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
