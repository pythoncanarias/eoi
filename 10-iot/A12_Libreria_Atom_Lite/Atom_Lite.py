# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)

import neopixel
import machine
import time


class LedRGB:
    def __init__(self):
        self.np =neopixel.NeoPixel(machine.Pin(27), 1)
        self.temporizador = machine.Timer(-1)  # utilizamos un timer para programar el apagado cuando hacemos un parpadeo

    def encender(self):
        self.np[0] = (255, 255, 255)
        self.np.write()

    def apagar(self, *args):
        self.np[0] = (0, 0, 0)
        self.np.write()

    def parpadeo(self, duracion_ms):
        self.encender()
        self.temporizador.init(period=duracion_ms, mode=machine.Timer.ONE_SHOT, callback=self.apagar)
        # time.sleep_ms(duracion_ms)
        # self.apagar()

    def color(self, r, g, b):
        self.np[0] = (r, g, b)
        self.np.write()


class Boton:
    def __init__(self):
        self.flag = False
        self.boton = machine.Pin(39, machine.Pin.IN)
        self.boton.irq(self.cb, machine.Pin.IRQ_FALLING)

    def cb(self, inst):
        self.flag = True

    def get_pulsado(self):
        if not self.flag:
            return False
        self.flag = False
        return True
