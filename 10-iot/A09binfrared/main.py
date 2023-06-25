from machine import Pin
import utime
# Creado por Victor Suarez(suarez.garcia.victor@gmail.com) para curso EOI

pin = Pin(27,Pin.IN) #Inicializacion del pin

while True:
    utime.sleep_ms(100) # esperar 100 ms para recibir el dato
    if pin.value()==1:#si se recibe señal
        print("Señal recibida")
        utime.sleep_ms(1000) #esperar un segundo