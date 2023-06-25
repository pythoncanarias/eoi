from machine import Pin, reset, unique_id
import utime
from umqtt.simple import MQTTClient
from ubinascii import hexlify
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)
# Modificado por Victor Suarez (suarez.garcia.victor@gmail.com) para curso de Python de EOI

# la conexion a wifi la hacemos en boot.py
# los pines (led y boton) los configuramos en boot.py

# CONSTANTES
TIEMPO_ENTRE_ENVIOS = 5000 # ms

def mqtt_callback(topic, msg):
    """ Cuando hacemos check_msg() y hay mensajes en los topics a los que estamos suscritos
    entra aqui """ 
    msg = msg.decode()  # son array de bytes, lo pasamos a string
    topic = topic.decode()
    if topic == "luz_salon_775":
        # por este topic controlo el LED y segun el mensaje lo enciendo o apago
        if msg.strip().lower() == "on" or msg.strip() == "1" or msg.strip().lower() == "true":
            led.value(0)
            print("encendiendo luz")
        elif msg.strip().lower() == "off" or msg.strip() == "0" or msg.strip().lower() == "false":
            led.value(1)
            print("apagando luz")
    print("me llego por '{}' esto: {}".format(topic, msg))


# El nombre con el que nos registremos en el broker tiene que ser unico
# para eso podemos utilizar unique_id que nos devuelve la mac de nuestro dispositivo
id_cliente = hexlify(unique_id())

mqtt_server = "broker.hivemq.com"  # broker publico con el que podemos hacer pruebas
# tiene un cliente web en http://www.hivemq.com/demos/websocket-client/
client = MQTTClient(id_cliente, mqtt_server)  # si no decimos nada usa el puerto por defecto 1883
client.set_callback(mqtt_callback)  # cuando entren mensajes por los topics a los que estamos suscritos, dispara el callback
client.connect()
client.subscribe(b'luz_salon_775')  # nos suscribimos a los topics que nos interese
client.subscribe(b'planta_baja/temperatura')  # notese que ponemos la b delante porque la libreria lo espera en formato byte array

proximo_envio = utime.ticks_ms() + TIEMPO_ENTRE_ENVIOS  # utilizamos este sistema para enviar mensajes cada 5 segundos

while True:
    client.check_msg()  # comprueba mensajes, llamar frecuentemente pero no de continuo que nos da error
    # client.wait_msg()  # lo mismo que la linea anterior pero bloquea    
    if utime.ticks_ms() > proximo_envio:  # periodicamente manda mensajes, pero sin bloquear
        mensaje = "hola mundo, soy Dani"
        client.publish(b'clase_eoi', mensaje)
        print(mensaje)
        proximo_envio = utime.ticks_ms() + TIEMPO_ENTRE_ENVIOS
    utime.sleep_ms(100)
