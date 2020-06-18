from machine import Pin, reset
import utime
import urequests as requests
import ujson as json


# la conexion a wifi la hacemos en boot.py

codigo_cuidad = "773692"  # Codigo con el que metaweather identifica a Santa Cruz
url = "https://www.metaweather.com/api/location/{}/".format(codigo_cuidad)
r = requests.get(url)
if r.status_code is not 200:
    print("Error al acceder a metawether. Codigo de estado {} Contenido:".format(r.status_code))
    print(r.content)
    utime.sleep(10)
    reset()
# Si llega hasta aqui es por que status code que respondió la API es 200 (OK)
datos = r.content.decode()  # content es un array de bytes, lo pasamos a cadena de texto normal
# print(resultado)
# datos en este punto es un string que contiene la respuesta de la api en formato json
datos_dict = json.loads(datos)  # lo desserializamos convirtiendolo en un Diccionario

# Esto es opcional: guardamos la respuesta en un fichero para consultarlo offline
with open("datos_api.json", 'w') as f:
    f.write(datos)

# Esto es opcional: si tenemos los datos en un fichero, lo podemos leer asi
with open("datos_api.json", 'r') as f:
    datos_dict = json.load(f)

# miramos como es esa estructura de datos en un navegador o abriendo datos_api.json
# para saber como llegar a la informacion que buscamos
temperatura_manana = datos_dict["consolidated_weather"][1]['the_temp']
humedad_manana = datos_dict["consolidated_weather"][1]['humidity']
print("La previsión para mañana es: ", end='')
print("Temperatura {}ºC Humedad {}%".format(temperatura, humedad))
