# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)

import utime
import esp32
from machine import Pin


class NP:
    def __init__(self):
        self.rmt = esp32.RMT(0, pin=Pin(27), clock_div=8)  # RMT(channel=0, pin=18, source_freq=80000000, clock_div=8)
        # resolcion 100ns una unidad 100ns

    @staticmethod
    def _sacar_secuencia(valor):
        uno = [7, 6]
        cero = [4, 8]
        mascara = 0b10000000
        valor_sec = []
        for i in range(8):
            r = valor & mascara
            if r == 0:
                valor_sec += cero
            else:
                valor_sec += uno
            mascara = mascara >> 1
        # print(valor_sec)
        return valor_sec
    
    def color(self, red, green, blue):
        pulsos = tuple(self._sacar_secuencia(green) + self._sacar_secuencia(red) + self._sacar_secuencia(blue))
        self.rmt.write_pulses(pulsos, start=1) 
        utime.sleep_us(50)
        self.rmt.write_pulses(pulsos, start=1)


neopixel = NP()
neopixel.color(128, 194, 21)
