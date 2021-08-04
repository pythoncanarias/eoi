# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)
# Esta pensado para seleccionar partes del codigo y lanzarlas con la opcion Pymakr -> run current selecction



# Salida digital
# Osciloscopio 400us Y -T - 2v DC x1
from machine import Pin
import utime
pin = Pin(33, Pin.OUT)
# Trigger Sweep Auto
pin.value(0)
pin.value(1)
# Trigger Sweep Single
while True:
    pin.value(1)
    utime.sleep_us(100)
    pin.value(0)
    utime.sleep_us(300)

# PWM
# Osciloscopio 400us Y -T - 2v DC x1
from machine import Pin, PWM
pin_pwm = PWM(Pin(33, Pin.OUT), freq=1000)
pin_pwm.duty(1023)  # 100%
pin_pwm.duty(511)  # 50%
pin_pwm.duty(768)  # 75%
pin_pwm.duty(255)  # 25%


# RMT pulsos microsegundos
# Osciloscopio 10us Y -T - 2v DC x1
from machine import Pin
import esp32
np_rmt = esp32.RMT(0, pin=Pin(33), clock_div=8)  # RMT(channel=0, pin=x, source_freq=80000000, clock_div=8)
# La resolucion del canal es 100ns (1/(source_freq/clock_div)).
np_rmt.write_pulses((7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6), start=1)
np_rmt.write_pulses((7, 18, 7, 18, 7, 18, 7, 18, 7, 18, 7, 18, 7, 18, 7, 18), start=1)



# UltrasonicSensor
# Osciloscopio 400us Y -T - 2v DC x1 (para ver pulso inicial) pasar a 10 ms para ver respuesta
from ultrasonic_sensor import UltrasonicSensor
sensor_distancia = UltrasonicSensor(32)
sensor_distancia.get_distancia()
