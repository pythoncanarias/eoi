from machine import Pin, reset, unique_id, Timer
import utime
from umqtt.simple import MQTTClient
from ubinascii import hexlify
import ujson as json


class Mimqtt:
    def __init__(self, registro_recibido_callback):
        self.registro_recibido_callback = registro_recibido_callback
        # El nombre con el que nos registremos en el broker tiene que ser unico
        # para eso podemos utilizar unique_id que nos devuelve la mac de nuestro dispositivo
        id_cliente = hexlify(unique_id())
        mqtt_server = "broker.hivemq.com"  # broker publico con el que podemos hacer pruebas
        # tiene un cliente web en http://www.hivemq.com/demos/websocket-client/
        self.client = MQTTClient(id_cliente, mqtt_server)  # si no decimos nada usa el puerto por defecto 1883
        self.client.set_callback(self.mqtt_callback)  # cuando entren mensajes por los topics a los que estamos suscritos, dispara el callback
        self.client.connect()
        self.client.subscribe(b'curso_eoi')  # nos suscribimos a los topics que nos interese
        # programamos un timer para que compruebe mensajes periodicamente, y cuando lleguen salte mqtt_callback
        self.timer = Timer(-1)
        self.timer.init(period=50, mode=Timer.PERIODIC, callback=lambda x: self.client.check_msg())

    def enviar(self, nombre, tiempo):
        topic = b'curso_eoi'
        datos = {
            "nombre": nombre,
            "tiempo": tiempo
        }
        datos_serializados = json.dumps(datos)
        self.client.publish(topic, datos_serializados)

    def mqtt_callback(self, topic, msg):
        #print("me llego por '{}' esto: {}".format(topic, msg))
        try:
            datos = json.loads(msg.decode())
            nombre = datos['nombre']
            tiempo = int(datos['tiempo'])  # nos aseguramos que sea un entero
        except:  # si algo de lo anterior falta o falla, salta esta excepcion
            print("MQTT mensaje invalido")
            print(msg)
            return
        # una vez comprobado que este bien, el resto lo hacemos en la clase Juego
        self.registro_recibido_callback(nombre, tiempo)  

    def disconnect(self):
        self.timer.deinit()
        self.client.disconnect()
