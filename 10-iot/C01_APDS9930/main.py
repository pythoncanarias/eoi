from machine import Pin, I2C
import utime
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)


i2c=I2C(sda=Pin(4), scl=Pin(5))  # instanciamos y configuramos bus I2C en los pines sda y scl
dispositivos_conectado = i2c.scan()  # manda mensajes por el bus i2c a todas las direcciones para ver que dispositivos contestan
# devuelve un listado de dispositivos conectados
print(dispositivos_conectado)  # NOTA las direcciones las muestra en decimal, normalmente usaremos hexadecimal para trabajar con el i2c

from apds9930 import APDS9930
sensor = APDS9930(i2c)  # creamos una instancia del sensor y le pasamos el manejador del i2c
# el manejador del i2c lo creamos aqui porque si tenemos varios sensores en el bus, le pasamos el mismo manejador a todos

sensor.activar_proximidad()  # este metodo modifica un registro interno del APDS9930 para activar el sensor de proximidad

print("Acerca la mano al sensor para activarlo")
while True:
    proximidad = sensor.get_proximidad()
    if proximidad is not 0:
        print("Activado! lectura {}".format(proximidad))
        utime.sleep_ms(100)  # para que no sature la consola con prints
