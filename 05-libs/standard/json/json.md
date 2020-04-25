La libreria json

Nos permite trabajar con ficheros en formato json

JSON (*JavaScript Object Notation*), es un formato de texto ligero para el
intercambio de datos. JSON es un __subconjunto__ de la notación literal de objetos
de JavaScript aunque hoy, debido a su amplia adopción como alternativa a XML, se
considera un formato de lenguaje independiente.

Es utilizado para proyectos de
lenguajes de programación diferentes como C, C++, Java, Javascript, Perl, Python
y muchos más. Estas propiedades hacen que JSON sea el lenguaje ideal para el
intercambio de datos.


 
Por lo tanto, JSON se puede considerar como un método simple de crear y
almacenar estructuras de datos y, gracias a su sintaxis, se utiliza en muchas
aplicaciones web. Una de sus principales virtudes es que, además de ser
relativamente eficiente, es
legible por un humano, con lo que actualemente es el formato usado por la
mayoría de las API.



Un ejemplo de datos con formato JSON es la siguiente:

{
    "username": "fmiller",
    "dob": "1988-02-26",
    "active": true}
}


El módulo utilizado para este propósito es el módulo json. Al ser parte de
la librera estándar, lo único que necesitas hacer para usar este módulo es importarlo:

import json

Usaremos esta librería para, o bien interpretar un texto y convertirlo en una
estructira de datos nativa de Python, o a la inversa, convertir en texto o
__serializar__ unos valores de python.


La funcion loads

Loads hace la primera de las operaciones. Le pasamos como argumento un texto
en formato json, y nos devuelve una estructura de datos con valores nativos
de Python.

import json
user_json = '''{"username": "fmiller", "dob": "1988-02-26", "active": true}'''
user = json.loads(user_json)
print(user)

La funcion dumps

La función `dumps` es la inversa de `loads`, acepta como parametro
una variable python (Incluyendo listas o diccionarios que contengan
otros valores), y devuelve una cadena de texto formateada en json.

Tenemos el siguiente diccionario en Python:

import json
pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
dictionaryToJson = json.dumps(pythonDictionary)
Si hacemos print dictionaryToJson, obtenemos los siguientes datos JSON:

{"age": 44, "isEmployed": true, "name": "Bob"}

Esta salida se considera la representación de los datos del objeto (diccionario). El método dumps() fue la clave para dicha operación.

Limitacines de json

Hay determinados tipos de valores que no se pueden representar en 
json. POr ejemplo, los datos de tipo fecha o timestamp no tienen una
representacion como tales en json. Un truco habitual es codificarlos
como string usando el formato ISO 8601.

En general, json puede trabajar con:

 - Valores booleanos
 - El objeto `None`
 - Números enteros o en coma flotante
 - Cadenas de caracgteres
 - Listas
 - Diccionarios

Cualquier otro tipo, incluyendo por supuesto nuestras clases, debera ser
adaptado a uno de estos tipos basicos para que se pueda convertir a json.

**Ejercicio**: Intentar serializar un objeto de tipo `datetime.datetime`.
Comprobar que da error. Intentar ahora con un objeto tipo `arrow.Arrow`.
Comprobar que tambien da error, pero asi podemos ver la utilida del
metodo `for_json`.

La libreria json nos permite ampliar los metodos `loads` y `dumps` para
que puedan interpretar determinados valores que no estan incluidos
en la especificacion de json pero que nosotros podemos  reconstruir o
serializar:



import json
import datetime

class SuperJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()[0:19]
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, arrow.Arrow):
            return obj.for_json()
        elif hasattr(obj, "to_dict"):
            return obj.to_dict()
        return super().default(obj)

def as_json(obj):
    return json.dumps(obj, cls=SuperJSONEncoder, indent=4)

Ejercicio: Supongamos que tenmos una clase para representar las
cartas de una baraja, como esta:

    class Card:

        SUITS = {
            'T': 'trébol',
            'D': 'diamantes',
            'C': 'corazones',
            'P': 'picas',
        }

        VALUES = {
            'A': 'as',
            '2': 'dos',
            '3': 'tres',
            '4': 'cuatro',
            '5': 'cinco',
            '6': 'seis',
            '7': 'siete',
            '8': 'ocho',
            '9': 'nueve',
            '10': 'diez',
            'J': 'jota',
            'Q': 'reina',
            'K': 'rey',
        }

        def __init__(self, code):
            self.suit = code[1]
            self.value = code[1:]

        def suit_name(self):
            return self.SUITS[self.suit]

        def value_name(self):
            returl self.VALUES[self.value]

        def __str__(self):
            return f"self.value_name()} de {self.suit_name()}"

Como podriamos guardar la informacion de una carta en JSON. Que es lo minima
informacion necesaria para poder almacenar y luego poder reconstruir 
una carta?

Nota: No hay realmente una forma "correcta" de resolver esto. Depende
mucho del contexto. Pero es interesante queplanteemos diferentes
formas de hacerlo.
