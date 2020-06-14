import machine
import utime


adc = machine.ADC(0)

def remapear(x,in_min, in_max, out_min, out_max):
    # esto es la implementacion de la funcion "map" de arduino
    # https://www.arduino.cc/reference/en/language/functions/math/map/
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


while True:
    valor = adc.read()
    # NOTA: el conversor ADC del ESP es de 10bits, lo que significa que devolvera un numero entre 0 y 1023 (0v - 3,3v)
    # convertimos ese valor en voltaje
    voltaje = remapear(valor, 0, 1023, 0, 3.3)
    print("Valor: {}\tvoltaje: {:.3f}v".format(valor, voltaje))
    utime.sleep_ms(100)
