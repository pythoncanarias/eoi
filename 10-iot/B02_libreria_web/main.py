from machine import Pin
import network
import utime
from credenciales import ssid, password
from corneto import Corneto

# estas credenciales tienen que estar en un fichero credenciales.py
#ssid = "mi_wifi"
#password = "gsdfsdfgds"

# Configurar hardware
led = Pin(2, Pin.OUT)

# Conexion wifi
led.value(0)  # encendemos el led para indicar el tiempo que tarda en conectarse
print("\nConectandose a wifi...", end='')
red = network.WLAN(network.STA_IF)
red.active(True)
red.connect(ssid, password)
while not red.isconnected():  # Espera hasta que este conectado
    utime.sleep(0.1)
print("conectado!")
print(red.ifconfig())
led.value(1) # apagamos el led mara indicar que ya estamos conectados

web = Corneto()

def home(x):
    contexto = {
        "tiempo": str(utime.ticks_ms() // 1000),
    }
    return("index.html", contexto)

def led_encender(x):
    led.value(0)
    contexto = {}
    return("luz.html", contexto)

def led_apagar(x):
    led.value(1)
    contexto = {}
    return("luz.html", contexto)


web.add_view("/", home)
web.add_view("/encender", led_encender)
web.add_view("/apagar", led_apagar)

web.run_server()
