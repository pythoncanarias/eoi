import tcs34725
import machine
import utime
import neopixel

# Usando el sensor de color TCS34725, leemos los valores RGB y los sacamos por el neopixel
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)

np = neopixel.NeoPixel(machine.Pin(27), 1)  # La placa Atom Lite tiene un neopixel en el GPIO 27
i2c=machine.I2C(1, sda=machine.Pin(26), scl=machine.Pin(32), freq=400000 )  # instanciamos y configuramos bus I2C en los pines sda y scl

dispositivos_conectado = i2c.scan()  # manda mensajes por el bus i2c a todas las direcciones para ver que dispositivos contestan
print(dispositivos_conectado)  # NOTA las direcciones las muestra en decimal, normalmente usaremos hexadecimal para trabajar con el i2c

color_sensor = tcs34725.TCS34725(i2c)
color_sensor.gain(16)
color_sensor.integration_cycles(tcs34725.INTEG_CYCLES_42)
color_sensor.active(True)
utime.sleep_ms(100)
while True:
    rgb = color_sensor.read_rgb()
    print(rgb)
    np[0] = rgb  # cambiamos los colores del neopixel segun lo que lea el sensor
    np.write()
    utime.sleep_ms(500)
