from machine import Pin
import utime
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)


# VARIABLES GLOBALES
boton_pulsado = False
contador = 0

def boton_callback(inst):
    # esto es una interrupcion, no hacer operaciones "caras" como trabajar con float, listas, prints, etc
    global boton_pulsado, contador
    boton_pulsado = True
    contador += 1

boton = Pin(0, Pin.IN)
boton.irq(boton_callback, Pin.IRQ_FALLING)

while True:
    if boton_pulsado:
        print("\nse ha pulsado el boton {} veces".format(contador))
        boton_pulsado = False  # reiniciar el estado
    print(".", end='')
    utime.sleep_ms(100) 
