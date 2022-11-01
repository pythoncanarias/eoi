import neopixel
import machine
import time


# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)

class LedRGB:
    def __init__(self):
        self.np =neopixel.NeoPixel(machine.Pin(27), 1)
        self.temporizador = machine.Timer(-1)

    def encender(self):
        self.np[0] = (255, 255, 255)
        self.np.write()

    def apagar(self, *args):
        self.np[0] = (0, 0, 0)
        self.np.write()

    def flash(self):
        self.encender()
        self.temporizador.init(period=500, mode=machine.Timer.ONE_SHOT, callback=self.apagar)
        # time.sleep_ms(500)
        # self.apagar()

class Boton:
    def __init__(self, pinNumero):
        self.flag = False
        self.boton = machine.Pin(pinNumero, machine.Pin.IN)
        self.boton.irq(self.cb, machine.Pin.IRQ_FALLING)

    def cb(self, inst):
        self.flag = True

    def get_pulsado(self):
        if not self.flag:
            return False
        self.flag = False
        return True
