from machine import Pin
import utime
import urandom
from mimqtt import Mimqtt


class Juego:
    def __init__(self, nombre):
        self.nombre = nombre
        self.led = Pin(2, Pin.OUT)
        self.led.value(1)  # empiezo con el led apagado
        self.boton = Pin(0, Pin.IN)
        self.mimqtt = Mimqtt()

    def start(self):
        print()
        while True:
            print("Pulsa el boton cuando se encienda el led")
            self.encender_led_aleatorio()
            tiempo_inicio = utime.ticks_ms()  # guardamos tiempo nada mas encender led
            self.apagar_led_boton()
            tiempo_fin = utime.ticks_ms()  # guardamos tiempo justo al presionar el boton
            tiempo_total = utime.ticks_diff(tiempo_fin, tiempo_inicio) #tiempo reaccion fin-inicio
            print("has apagado el led en {}ms".format(tiempo_total))
            self.mimqtt.enviar(self.nombre, tiempo_total)

    def encender_led_aleatorio(self):
        tiempo_random = urandom.getrandbits(12)  # valor entre 0 y 4095
        tiempo_random += 3000  # valor entre 3000 y 7095
        utime.sleep_ms(tiempo_random)
        self.led.value(0) # enciendo led

    def apagar_led_boton(self):
        while self.boton.value() == 1:  #espero que se pulse el boton 
            utime.sleep_ms(1)
        self.led.value(1)  # apago led
