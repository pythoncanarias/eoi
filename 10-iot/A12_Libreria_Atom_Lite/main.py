# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)
from Atom_Lite import LedRGB, Boton
import utime
from random import randrange

# demostracion del uso de la libreria. Cuando se pulsa el boton, el led cambia a un color aleatorio

boton = Boton()
led = LedRGB()
while True:  # bucle infinito
    if boton.get_pulsado():
        r = randrange(0,255)
        g = randrange(0,255)
        b = randrange(0,255)
        led.color(r, g, b)
    utime.sleep_ms(50)
