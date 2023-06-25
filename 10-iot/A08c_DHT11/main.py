from dht import DHT11
from machine import Pin
from utime import sleep_ms
# Creado por Victor Suarez(suarez.garcia.victor@gmail.com) para el curso de EOI

# Ejemplo de uso de DHT11
sensorDHT = DHT11(Pin(22,Pint.IN)) #Inicializacion del sensor recuerda cambiar por el GPIO usado

while True:
    sleep_ms(500)#esperamos 500ms
    sensorDHT.measure()# Realizamos la lectura
    temp = sensorDHT.temperature()# leemos la temperatura
    hum = sensorDHT.humidity() # leer la humedad
    print("T={:02d} ºC, {:02d} %".format(temp,hum)) # Mostrar mensaje
