import machine
import utime


# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)
# Basado en el codigo de seedstudio
# https://github.com/Seeed-Studio/Seeed_Arduino_UltrasonicRanger/blob/master/Ultrasonic.cpp


class UltrasonicSensor:
    def __init__(self, gpio_number):
        self._sensor_pin = machine.Pin(gpio_number, mode=machine.Pin.IN, pull=None)

    def get_duracion(self):
        '''Devuelve la duracion en microsegundos (us)'''
        # ponemos el pin como salida y damos un pulso para activar el emisor
        self._sensor_pin.init(mode=machine.Pin.OUT)
        self._sensor_pin.off()
        utime.sleep_us(2)
        self._sensor_pin.on()
        utime.sleep_us(5)
        self._sensor_pin.off()
        # cambiamos el pin a entrada y medimos cuanto tarda en recibir el eco
        self._sensor_pin.init(mode=machine.Pin.IN, pull=None) 
        duracion = machine.time_pulse_us(self._sensor_pin, 1, 1000000)  # pin, flanco, timeout
        return duracion

    def get_distancia(self):
        '''Devuelve la distancia en milimetros'''
        return int(self.get_duracion() * (10/2) / 29)
