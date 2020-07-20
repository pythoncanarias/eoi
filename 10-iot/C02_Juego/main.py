from machine import Pin, I2C
import network
from juego import Juego
from credenciales import ssid, password
import utime
import uos
from apds9930 import APDS9930
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)


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


i2c=I2C(sda=Pin(4), scl=Pin(5))  # instanciamos y configuramos bus I2C en los pines sda y scl
try:
    sensor = APDS9930(i2c)  # creamos una instancia del sensor y le pasamos el manejador del i2c
    sensor.activar_proximidad()  # este metodo modifica un registro interno del APDS9930 para activar el sensor de proximidad
except Exception as e:
    print("No se ha podido iniciar el sensor APDS9930. El juego funcionará con el boton. Error:")
    print(e)
    sensor = None

conectar_wifi()
juego = Juego("Dani")  # instanciamos el juego pasandole el nombre del jugador
juego.usar_sensor(sensor)  # si comentamos esta linea funcionaria con el boton de la placa
try:
    juego.comenzar()  #  bucle infinito
except Exception as e:
    print(e)
    juego.finalizar()

# uos.remove("juegodb")  # con esta linea podemos eliminar la base de datos para empezar de cero
