from machine import reset
from utime import sleep
import urequests as requests
import ujson as json
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)


# la conexion a wifi la hacemos en boot.py

# Ejemplo de la respuesta de esta API
"""{
    "_id": "5a6ce86f2af929789500e847",
    "en": "I have no special talent. I am only passionately curious.",
    "author": "Albert Einstein",
    "id": "5a6ce86f2af929789500e847"
}"""

def get_frase():
    url = "https://programming-quotes-api.herokuapp.com/quotes/random"
    r = requests.get(url)
    if r.status_code is not 200:
        print("Error al acceder a la API. Codigo de estado {} Contenido:".format(r.status_code))
        print(r.content)
        sleep(10)
        reset()
    datos = r.content.decode()
    # print(datos)
    datos_dic = json.loads(datos)
    frase = datos_dic["en"]
    autor = datos_dic["author"]
    return "'{}' de {}".format(frase, autor)


while True:
    print(get_frase())
    sleep(15)
