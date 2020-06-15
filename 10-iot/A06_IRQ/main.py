from machine import Pin
import utime


class Boton:
    def __init__(self, pin):
        self.pulsado = False
        self.boton = Pin(0, Pin.IN)
        self.boton.irq(self.cb, Pin.IRQ_FALLING)

    def get_pulsado(self):
        if not self.pulsado:
            return False
        self.pulsado = False
        return True

    def cb(self, inst):
        # esto es una interrupcion, no hacer operaciones "caras" como trabajar con float, listas, prints, etc
        self.pulsado = True

boton_placa = Boton(0)

while True:
    if boton_placa.get_pulsado():
        print("\nse ha pulsado el boton")
    print(".", end='')
    utime.sleep_ms(100) 
