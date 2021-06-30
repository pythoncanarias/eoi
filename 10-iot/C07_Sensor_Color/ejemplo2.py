import tcs34725
import machine
import utime
import neopixel


# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)

i2c=machine.I2C(1, sda=machine.Pin(26), scl=machine.Pin(32), freq=400000 )  # instanciamos y configuramos bus I2C en los pines sda y scl

color_sensor = tcs34725.TCS34725(i2c)
color_sensor.gain(16)
color_sensor.integration_cycles(tcs34725.INTEG_CYCLES_42)
color_sensor.active(True)
utime.sleep_ms(100)

# Usa este codigo para ver los valorese del sensor y calibar el umbral
# while True:
#     temperature, lux = color_sensor.read_temperature_and_lux()
#     print("temperature {}\tlux {}".format(temperature, lux))
#     utime.sleep_ms(100)

THRESHOLD = const(100)  # umbral por debajo del cual se considera que detecta objeto
contador = 0

lux = THRESHOLD+1
print("Detectando objetos...")
while True:
    # Esperamos que un objeto tape el sensor
    while lux > THRESHOLD:
        utime.sleep_ms(100)
        temperature, lux = color_sensor.read_temperature_and_lux()
    print("Sensor tapado ({:.0f}<{})...".format(lux, THRESHOLD), end='')
    contador += 1
    while lux < THRESHOLD:
        utime.sleep_ms(100)
        temperature, lux = color_sensor.read_temperature_and_lux()
    print("liberado ({:.0f}>{}) Total objetos detectados: {}".format(lux, THRESHOLD, contador))
