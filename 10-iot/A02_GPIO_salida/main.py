import machine
import utime


led = machine.Pin(2, machine.Pin.OUT)
# inicializamos otro pin, esta vez el 0 que es donde esta conectado el boton, y en modo entrada (IN)
boton = machine.Pin(0, machine.Pin.IN)

while True:  # bucle infinito
    # NOTA tal y como esta conectado el boton, pondra la linea a 0v si se pulsa y 3,3v si se libera
    estado_boton = boton.value()  # devuelve 0 si esta a 0v, o 1 si esta a 3,3v
    led.value(estado_boton)  # hacemos que el led se encienda o apague funcion del estado del boton
    # recordamos nuevamente que por la conexion del boton a la placa, trabajamos con logica negativa (al reves de lo "logico")
    if estado_boton:
        print("- boton liberado")
    else:
        print("X boton pulsado")
    utime.sleep_ms(100)  # hacemos una pausa para poder ver los prints
