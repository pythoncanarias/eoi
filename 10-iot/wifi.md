# Conexión a la red

Uno de los principales atractivos del uso de estos microcontroladores es que tienen conectividad usando Wifi.

Tanto ESP32, Raspberry Pi pico (solo version W) como Atom Lite, permite utilizar conexión inalámbrica con conexión Wifi.

Veamos un ejemplo para conectar a una WIfi:

```python
red = network.WLAN(network.STA_IF)
red.active(True)
red.connect(ssid, password)#SSId y password a utilizar
while not red.isconnected():  # Espera hasta que este conectado
    utime.sleep(0.1)
print("conectado!")
print(red.ifconfig())
```

En este ejemplo deberiáis de poder ver la configuración de red del dispositivo Wifi.

## Ejemplos con conexión

Hasta ahora, hemos estado trabajando de forma offline y con un solo fichero. Ahora, verás que hay ficheros llamados _boot.py_ que contendrán la configuración y conexión Wifi. En microPython, el fichero boot.py se ejecuta siempre al inicio.

Veamos el ejemplo de Boot.py:

```python
from machine import Pin
import utime
import network
from credenciales import ssid, password

# Configurar hardware
led = Pin(2, Pin.OUT)#Pin Placa
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
```

Como puedes ver, se requiere un fichero llamado _credentials.py_; este fichero contiene el SSID y el password de nuestra wifi.

Ejemplo:

```python
ssid = "El_nombre_de_mi_wifi"
password = "la_contraseña_de_mi_wifi"
```

A partir de ahora, muchos de nuestros ejemplos utilizarán esta configuración.
