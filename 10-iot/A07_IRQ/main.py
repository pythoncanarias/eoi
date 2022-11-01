from machine import Pin
import utime
import micropython
micropython.alloc_emergency_exception_buf(100)
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)


FILTRO_RUIDO = 100  # milisegundos que tiene que estar el boton presionado para considerarse pulsación válida


class Boton:
    def __init__(self, pin_n):
        self.pin_n = pin_n
        self.pulsado = False
        self.boton = Pin(self.pin_n, Pin.IN)
        self.boton.irq(self.cb_pulsado, Pin.IRQ_FALLING)
        self.tiempo_inicio = 0
        self.tiempo_fin = 0

    def get_pulsado(self):
        if not self.pulsado:
            return False
        self.pulsado = False  # reiniciamos estado
        self.boton.irq(self.cb_pulsado, Pin.IRQ_FALLING)  # rehabilitamos interrupciones
        return True

    def cb_pulsado(self, inst):
        # esto es una interrupcion, no hacer operaciones "caras" como trabajar con float, listas, prints, etc
        micropython.schedule(self.post_cb_pulsado, 0) # creamos una tarea para que se ejecute cuanto antes, pero sin la prioridad de una interrupcion

    def post_cb_pulsado(self, inst):
        # aqui no hay peligro de hacer operaciones que lleven mas tiempo
        self.tiempo_inicio = utime.ticks_ms()
        self.boton.irq(self.cb_liberado, Pin.IRQ_RISING)

    def cb_liberado(self, inst):
        # esto es una interrupcion, no hacer operaciones "caras" como trabajar con float, listas, prints, etc
        micropython.schedule(self.post_cb_liberado, 0) # creamos una tarea para que se ejecute cuanto antes, pero sin la prioridad de una interrupcion

    def post_cb_liberado(self, inst):
        # aqui no hay peligro de hacer operaciones que lleven mas tiempo
        self.tiempo_fin = utime.ticks_ms()
        # comprobar que el boton se mantuvo presionado durante un tiempo (de lo contrario lo consideramos ruido)
        duracion = utime.ticks_diff(self.tiempo_fin, self.tiempo_inicio)
        print("\nDEBUG pulso de {}ms".format(duracion))
        if duracion < FILTRO_RUIDO:
            self.boton.irq(self.cb_pulsado, Pin.IRQ_FALLING)  # cambiamos la interrupcion para detectar siguiente pulso
        else:  # pulsacion valida
            self.pulsado = True
            self.boton = Pin(self.pin_n, Pin.IN)  # esto deshabilita la interrupcion, hasta que alguien lea el estado

        
boton_placa = Boton(0)
led = Pin(2, Pin.OUT)
led.value(1)  # inicialmente apagado

while True:
    if boton_placa.get_pulsado():
        print("\nse ha pulsado el boton")
        led.value(not led.value())  # alterna estado (toggle)
    print(".", end='')
    utime.sleep_ms(100) 
