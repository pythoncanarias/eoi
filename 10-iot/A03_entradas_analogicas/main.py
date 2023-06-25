import machine
import utime
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)
# Ampliado por Victor Suarez (suarez.garcia.victor@gmail.com) para curso de Python EOI (eoi.es)

# Para ESP32 usar los GPIO disponibles
# Para ATomLite usar GPIO33
# Para Raspberry Pi usar GPIO28 por ejemplo
adc = machine.ADC(machine.Pin(28))
adc.atten(machine.ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
# ver https://docs.micropython.org/en/latest/esp32/quickref.html?highlight=timer#adc-analog-to-digital-conversion

def remapear(x, in_min, in_max, out_min, out_max):
    # esto es la implementacion de la funcion "map" de arduino
    # https://www.arduino.cc/reference/en/language/functions/math/map/
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


while True:
    valor = adc.read()
    # NOTA: el conversor ADC del ESP32 es de 12bits, lo que significa que devolvera un numero entre 0 y 4095
    voltaje = remapear(valor, 0, 4095, 0, 3.6)
    porcentaje = int(remapear(valor, 0, 4095, 0, 100))
    print("Valor: {}\tvoltaje: {:.2f}v\tporcentaje: {}%".format(valor, voltaje, porcentaje))
    utime.sleep_ms(100)
