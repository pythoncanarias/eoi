from machine import Pin, reset, unique_id
import utime
from umqtt.simple import MQTTClient
from ubinascii import hexlify
import ujson as json


class Mimqtt:
    def __init__(self):
        # El nombre con el que nos registremos en el broker tiene que ser unico
        # para eso podemos utilizar unique_id que nos devuelve la mac de nuestro dispositivo
        id_cliente = hexlify(unique_id())
        mqtt_server = "broker.hivemq.com"  # broker publico con el que podemos hacer pruebas
        # tiene un cliente web en http://www.hivemq.com/demos/websocket-client/
        self.client = MQTTClient(id_cliente, mqtt_server)  # si no decimos nada usa el puerto por defecto 1883
        self.client.set_callback(self.mqtt_callback)  # cuando entren mensajes por los topics a los que estamos suscritos, dispara el callback
        self.client.connect()
        # self.client.subscribe(b'luz_salon_775')  # nos suscribimos a los topics que nos interese

    def enviar(self, nombre, tiempo):
        topic = b'curso_eoi'
        datos = {
            "nombre": nombre,
            "tiempo": tiempo
        }
        datos_serializados = json.dumps(datos)
        self.client.publish(topic, datos_serializados)

    def mqtt_callback(self, topic, msg):
        print("me llego por '{}' esto: {}".format(topic, msg))
