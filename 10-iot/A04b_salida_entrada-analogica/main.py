import machine
import utime
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)
# Ampliado por Victor Suarez (suarez.garcia.victor@gmail.com) para curso de Python EOI (eoi.es)

# Para ESP32 usar los GPIO disponibles
# Para ATomLite usar GPIO33
# Para Raspberry Pi usar GPIO28 por ejemplo
led = machine.Pin(12, machine.Pin.OUT)
led_pwm = machine.PWM(led, freq=1000)
# led_pwm.freq(1000)  # la frecuencia se puede cambiar en cualquier momento, aunque solemos dejarla fija (cambiamos el duty)
led_pwm.duty(511)  # La resolucion del PWM del ESP32 es de 10 bits, lo que significa que va desde 0 (0%) hasta 1023 (100%)
utime.sleep_ms(1000)
adc = machine.ADC(machine.Pin(13))
adc.atten(machine.ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
# ver https://docs.micropython.org/en/latest/esp32/quickref.html?highlight=timer#adc-analog-to-digital-conversion

def remapear(x, in_min, in_max, out_min, out_max):
    # esto es la implementacion de la funcion "map" de arduino
    # https://www.arduino.cc/reference/en/language/functions/math/map/
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


while True:
    valor = adc.read()
    # NOTA: el conversor ADC del ESP32 es de 12bits, lo que significa que devolvera un numero entre 0 y 4095
    salida = remapear(valor, 0, 4095, 0, 511) # Se remapea para que tenga los valores debido al DAC que tiene 8 bits
    led_pwm.duty(int(salida)) # se manda la salida ya remapeada
    
    utime.sleep_ms(100)
