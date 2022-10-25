import machine
import utime
import math
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)


led = machine.Pin(2, machine.Pin.OUT)
led_pwm = machine.PWM(led, freq=1000)
# led_pwm.freq(1000)  # la frecuencia se puede cambiar en cualquier momento, aunque solemos dejarla fija (cambiamos el duty)
led_pwm.duty(511)  # La resolucion del PWM del ESP32 es de 10 bits, lo que significa que va desde 0 (0%) hasta 1023 (100%)
utime.sleep_ms(1000)

while True:
    print("aumentando")
    for i in range(1023):
        led_pwm.duty(i)
        utime.sleep_ms(2)
    print("disminuyendo")        
    for i in range(1024,0,-1):
        led_pwm.duty(i)
        utime.sleep_ms(2)        

    # Como alternativa podemos pasarle funciones sinusoidales, comparar el resultado
    # for i in range(20):
    #     sin_duty = int(math.sin(i / 10 * math.pi) * 512 + 511)
    #     # sin_duty = int(math.sin(i / 10 * math.pi) * 1023)
    #     led_pwm.duty(sin_duty)
    #     utime.sleep_ms(50)
