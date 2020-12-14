import machine
import utime
from ultrasonic_sensor import UltrasonicSensor
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)


# estos son los pines expuestos en el conector grove (el beige al lado del USB) en la Atom Lite
grove_pin_principal = 32
grove_pin_secundario = 26

# Esto es una copia del codigo de Adruino que ofrece seeedstudio, traducido a micropython

# pinMode(_pin, OUTPUT);
# digitalWrite(_pin, LOW);
sensor_pin = machine.Pin(grove_pin_principal, mode=machine.Pin.OUT, value=0)
# delayMicroseconds(2);
utime.sleep_us(2)
# digitalWrite(_pin, HIGH);
sensor_pin.on()
# delayMicroseconds(5);
utime.sleep_us(5)
# digitalWrite(_pin, LOW);
sensor_pin.value(0)
# pinMode(_pin, INPUT);
sensor_pin = machine.Pin(grove_pin_principal, mode=machine.Pin.IN, pull=None) 
# long duration = pulseIn(_pin, HIGH);
duracion = machine.time_pulse_us(sensor_pin, 1, 1000000)  # pin, flanco, timeout
print(duracion)  # aqui nos devuelve la duracion del pulso que hay que traducir a distancia


# ahora lo encapsulamos todo en una clase y la utilizamos asi:

sensor_distancia = UltrasonicSensor(32)  # 32 es el GPIO del pin principal del puerto grove
while True:
    distancia = sensor_distancia.get_distancia()
    print(distancia)
    utime.sleep_ms(200)
