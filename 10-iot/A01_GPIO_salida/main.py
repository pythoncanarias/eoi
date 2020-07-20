import machine
import utime
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)


# inicializamos el pin 2 (donde esta conectado el led azul de la placa) configurandolo como salida (OUT)
led = machine.Pin(2, machine.Pin.OUT)

while True:  # bucle infinito
    # NOTA tal y como esta conectado el led en la placa, 0v hace que se encienda y 3,3v hace que se apague
    led.off()  # pone la salida correspondiente a 0v
    # led.value(0)  # hace lo mismo que la linea anterior
    print("X LED encendido")
    utime.sleep(1)  # hace una pausa de x segundos
    led.on()  # pone la salida correspondiente a 3,3v
    # led.value(1)  # hace lo mismo que la linea anterior
    print("- LED apagado")
    utime.sleep_ms(1000)  # como alternativa se puede definir las pausas en milisegundos
