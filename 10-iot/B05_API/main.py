from machine import Pin, reset
import utime
import urequests as requests
import ujson as json
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)
# la conexion a wifi la hacemos en boot.py

LATITUDE = "28.47"
LONGITUDE = "-16.25"

url = f"https://api.open-meteo.com/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=1"
r = requests.get(url)
if r.status_code != 200:
    print("algo salio mal")
else:

    # print(r.content)  # bytes
    # print(r.text)  # string
    # print(r.json())  # dict

        # Esto es opcional: guardamos la respuesta en un fichero para consultarlo offline
    # with open("datos_api.json", 'w') as f:
    #     f.write(datos)

    # Esto es opcional: si tenemos los datos en un fichero, lo podemos leer asi
    # with open("datos_api.json", 'r') as f:
    #     datos_dict = json.load(f)

    # ejemplo de respuesta en datos_api.json
    temp = r.json()['current_weather']['temperature']
    print(f"Temperatura {temp}ºC")
