import machine
import utime
import math

#Creado por Victor Suarez(suarez.garcia.victor@gmail.com) para curso de Python de EOI.

#Inicializacion de los Pines
led = machine.Pin(2, machine.Pin.OUT)
led_pwm = machine.PWM(led, freq=1000)
# led_pwm.freq(1000)  # la frecuencia se puede cambiar en cualquier momento, aunque solemos dejarla fija (cambiamos el duty)
led_pwm.duty(511)  # La resolucion del PWM del ESP32 es de 10 bits, lo que significa que va desde 0 (0%) hasta 1023 (100%)
utime.sleep_ms(1000)

def remapear(x, in_min, in_max, out_min, out_max):
    # esto es la implementacion de la funcion "map" de arduino
    # https://www.arduino.cc/reference/en/language/functions/math/map/
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


# Para ESP32 usar los GPIO disponibles
# Para ATomLite usar GPIO33
# Para Raspberry Pi usar GPIO28 por ejemplo
adc = machine.ADC(machine.Pin(28))
adc.atten(machine.ADC.ATTN_11DB) #Atenuacion

while True:
    valor = adc.read()
    # NOTA: el conversor ADC del ESP32 es de 12bits, lo que significa que devolvera un numero entre 0 y 4095
    voltaje = remapear(valor, 0, 4095, 0, 3.6) #Remapeo del valor
    led_pwm.duty(voltaje)# escritura PWM
    utime.sleep_ms(100) #Esperar 100ms
