from hcsr04 import HCSR04 #importar la libreria; el fichero hcsr04.py debe estar en la misma carpeta
import utime
# Creado por Victor Suarez (suarez.garcia.victor@gmail.com) para el curso EOI


hcsr04sensor = HCSR04(22,26)# Inicializamos el sensor recuerda cambiar los pines.

while True:
    distance_mm = hcsr04sensor.distance_mm() #Distancia en mm.
    utime.sleep_ms(500) # esperar
    print("{} mm".format(distance_mm)) # Mostrar distancia