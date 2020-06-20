from machine import Pin
import utime
import urandom
from mimqtt import Mimqtt
from basedatos import Basedatos


class Juego:
    TIEMPO_LIMITE = 3000  # milisegundos antes de que salte el timeout
    def __init__(self, nombre):
        self.nombre = nombre
        self.led = Pin(2, Pin.OUT)
        self.led.value(1)  # empiezo con el led apagado
        self.boton = Pin(0, Pin.IN)
        self.mimqtt = Mimqtt(self.registro_recibido)  # le pasamos un callback para que nos avise 
        self.sensor = None
        self.basedatos = Basedatos()
        self.mostrar_mejores_puntuaciones() # al iniciar mostramos las mejores puntuacinoes guardadas (Si hay)

    def usar_sensor(self, sensor):
        """ Si le pasamos la instancia de un sensor APDS9930, lo utilizamos en vez del boton """
        self.sensor = sensor

    def comenzar(self):
        """ Bucle infinito que hace toda la logica de esperar, led on, esperar por boton, led off, medir tiempo """
        print()
        while True:
            print("Pulsa el boton cuando se encienda el led")
            self.esperar_tiempo_random()
            if self.check_pulsado():  # comprueba si esta pulsado antes de que se encienda el led
                print("No valido. Has pulsado antes de que se encendiera el led. ",end='')
                continue
            self.led.value(0) # enciendemos led
            tiempo_inicio = utime.ticks_ms()  # guardamos tiempo nada mas encender led
            valido = self.esperar_pulsacion()  # espera por boton o sensor, y devuelve si fue valido o timeout
            self.led.value(1)  # apagamos led
            if not valido:
                print("Has tardado demasiado. Intentalo otra vez. ", end='')
                continue
            tiempo_fin = utime.ticks_ms()  # guardamos tiempo justo al presionar el boton
            tiempo_total = utime.ticks_diff(tiempo_fin, tiempo_inicio)  # tiempo reaccion fin-inicio
            print("has apagado el led en {}ms".format(tiempo_total))
            self.mimqtt.enviar(self.nombre, tiempo_total)
            utime.sleep_ms(100)

    def check_pulsado(self):
        """ Comprueba si el dispositivo de entrada (boton o sensor) esta pulsado/activado """
        if self.sensor is None:
            return self.check_boton()  # si sensor es None comprobamos boton de la placa
        else:
            return self.check_sensor()  # sino comprobamos sensor

    def esperar_pulsacion(self):
        """ Espera que el dispositivo de entrada (boton o sensor) se active, o salte el timeout """
        tiempo_inicio = utime.ticks_ms()
        while not self.check_pulsado():  # bucle mientra no se pulse el boton o sensor
            utime.sleep_ms(1)
            if utime.ticks_diff(utime.ticks_ms(), tiempo_inicio) > Juego.TIEMPO_LIMITE:
                return False  # con False indicamos que salto el timeout
        return True  # con True indicamos que fue una pulsacion valida

    def check_sensor(self):
        """ Devuelve True si el sensor de proximidad esta activado """
        return self.sensor.get_proximidad() > 0  # si nos devuelve un valor mayor que cero es que esta activado
        # y evalua como True, por lo que devuelve True. Si es cero evalua y devuelve False

    def check_boton(self):
        """ Devuelve True si el boton de la placa esta presionado """
        return self.boton.value() == 0  # el boton funciona con logica negativa, es igual a cero cuando se pulsa

    def registro_recibido(self, nombre, tiempo):
        """ callback que salta desde mimqtt, cuando hay un nuevo registro valido """
        print("registro de '{}' tiempo {}ms".format(nombre, tiempo))
        # se lo pasamos a nuestra base de datos para que lo guarde si procede (nuevo o record)
        self.basedatos.nuevo_registro(nombre, tiempo)

    def mostrar_mejores_puntuaciones(self):
        """ Muestra por consola las 3 mejores puntuaciones guardadas en la base de datos """
        mejores_puntuaciones = self.basedatos.get_mejores_puntuaciones()
        if not mejores_puntuaciones:  # si es una lista vacia no hacemos nada
            return
        print("\nMejores puntuaciones historicas\n===============================")
        posiciones = ("Primero", "Segundo", "Tercero")
        for indice, tupla_nombre_tiempo in enumerate(mejores_puntuaciones):  # es una lista de maximo 3 tuplas con (nombre, tiempo)
            print("{} - {} con {}ms".format(posiciones[indice], tupla_nombre_tiempo[0].decode(), int(tupla_nombre_tiempo[1])))

    def finalizar(self):
        """ Detiene todo lo que esta en marcha """
        self.mimqtt.disconnect() # cancela timer de comprobar mensajes y desconecta cliente
        self.basedatos.close()  # cierra todo lo relaccionado con la db

    @staticmethod
    def esperar_tiempo_random():
        tiempo_random = urandom.getrandbits(12)  # valor de 12 bits -> entre 0 y 4095
        utime.sleep_ms(tiempo_random + 3000)  # valor entre 3000 y 7095
