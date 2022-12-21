from machine import Pin
from utime import sleep_ms
import urequests as requests
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)
# la conexion a wifi la hacemos en boot.py

boton = Pin(39, Pin.IN)
url = "https://animechan.vercel.app/api/random"

# Ejemplo de la respuesta de esta API
"""{
    "anime": "Re:Zero kara Hajimeru Isekai Seikatsu",
    "character": "Crusch Karsten",
    "quote":"Stand up! lift your faces! Take up your weapons! Look at that boy. He's so weak and fragile a breath could blow him away and he's unarmed! He is a powerless boy, whose defeat I have seen with my own eyes! He's weaker than anyone else here! Yet he's shouting louder than anyone that we can still do this so how can we sit down, with downcast gaze? If our 
weakest man has not given up how is kneeling in defeat acceptable for us? Did you come this far to wallow in shame?"
}"""

def get_frase():
    r = requests.get(url)
    if r.status_code != 200:
        print("algo salio mal.")
        return("")
    # print(r.content)  # bytes
    # print(r.text)  # string
    # print(r.json())  # dict
    rdict = r.json()
    return rdict['quote'] + f"\nde \'{rdict['character']}\' en \'{rdict['anime']}\'"


print("Pulsa el boton")
while True:
    sleep_ms(200)
    if boton.value():    
        continue
    print("Descargando frase...")
    print(get_frase())
