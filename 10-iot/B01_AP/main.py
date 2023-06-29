from machine import Pin
import network
import usocket as socket
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)


def web_page(estado_led_str):
    html = """<html><head> <title>Ejemplo 1</title> <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:;base64,iVBORw0KGgo="><style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #4286f4;}</style></head><body> <h1>CONTROL DE LED</h1> 
    <p>Estado LED: <strong>""" + estado_led_str + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
    <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
    return html

print("iniciando modo Access Point...")
#Modo AP descomentar y comentar modo STA
#red = network.WLAN(network.AP_IF)  # modo AP, por defecto te crea una red MicroPython-xxxxx password micropythoN
#Modo STA
red=network.WLAN(network.STA_IF)
red.active(True)  # por algun motivo hay que activar la red antes de cambiar la configuracion ?!?
#Desconectar en Modo AP
#red.config(essid="MicroP", password="12345678")  # si el password es corto da error

print(red.ifconfig())  # ('192.168.4.1', '255.255.255.0', '192.168.4.1', '192.168.1.1')

# creamos y configuramos el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # address family (ip4), socket type (TCP)
s.bind(('0.0.0.0', 80))  # tupla ip puerto, dejar ip vacia para localhost
s.listen(5)  # empieza a escuchar, argumento maximo numero de conexiones en cola (maximo 5)
# si el puerto se quedo abierto, lanza excepcion OSError: [Errno 98] EADDRINUSE
# s.settimeout(5)  # se puede especificar un timeout (opcional)

led = Pin(2, Pin.OUT)
led.value(1)  # inicialmente apagado

while True:
    print("esperando conexion...")
    conn, addr = s.accept()  # esta llamada bloquea hasta que haya alguna conexion entrante
    # si se especificó timeout, lanza excepcion OSError: [Errno 110] ETIMEDOUT
    print("Conexion desde {}".format(str(addr))
    request = conn.recv(1024)  # bytes maximos que se pueden recibir de cada vez
    request_str = request.decode()  # la peticion viene en bytes, lo pasamos a ascii
    print(request_str)
    if request_str.find('/?led=on') is 4:  # si miramos el request, la direccion empieza en la posicion 4
        print('LED ON')
        led.value(0)  # recordamos logica negativa -> el 0 enciende el led
    elif request_str.find('/?led=off') is 4:
        print('LED OFF')
        led.value(1)
    led_state = "OFF" if led.value() else "ON"
    contenido_respuesta = web_page(led_state)
    conn.send('HTTP/1.1 200 OK\n')  # cabecera
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(contenido_respuesta)
    conn.close()
