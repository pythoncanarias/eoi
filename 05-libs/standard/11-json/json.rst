``json``: Trabajar con el formato json
======================================

Python incopora en la librería estándar una libreria para
trabajar con el formato :term:JSON. JSON es un formato de texto
que nos permite guardar de forma estructurada nuestros datos.

ventajas sobre CSV

- formato estandar
- tipos de datos y estructuras de datos
- no solo tablas

JSON  es utilizado por casi todos los servicios web para el envío y recepción de datos.

A partir de la versión 2.6 Python incorpora en su librería estándar el módulo json, con una API similar a la de pickle, para codificar y decodificar información en el formato JSON. «Codificar» y «decodificar» deben ser entendidos como convertir de un objeto Python a JSON y viceversa.
 
El formato JSON es bastante similar a la sintaxis de Python, pero contiene únicamente dos tipos de estructuras: diccionarios y listas. Diccionario es lo que en Python conocemos como tal, un conjunto de pares con una clave y un valor. Y una lista no es más que un conjunto ordenado de objetos, que en Python podria ser o bien una lista, un array o incluso en conjunto.

La función ``dumps``
--------------------

La función ``dumps`` acepta casi cualquier valor o estructura de datos en
Python, y nos devuelve una cadena de texto en JSON equivalente. Al ser una
cadena de texto, podemos guardarla en un fichero, en una base de datos,
mandarla por correo, crear un codigo QR a partir de ella, imprimirla en papel
y enviarla por correo postal, etc.

Podemos codificar en json casi cualquier tipo de valor, veamos algunas
pruebas::

    import json

    print(json.dumps(1))
    print(json.dumps('hola'))
    print(json.dumps("hola"))
    print(json.dumps(None))
    print(json.dumps(True))
    print(json.dumps(False))
    print(json.dumps(3.1416))
    print(json.dumps(['a', 'b', 'c']))
    print(json.dumps(['texto', 23, False]))
    print(json.dumps(('a', 'b', 'c')))
    print(json.dumps({
        'uno': 1,
        'dos': 2,
        'alpha': 'texto',
        })


Si bien los resultados son similares, vemos que hay diferencias. Por ejemplo, el ``None`` de Python se representa como ``null``. En Python podemos usar comillas simples o doples, pero json requiere comillas dobles. Los valores booleanos Python ``True`` y ``False`` son ``true`` y ``false``.

Algunos tipos de datos, y especialmente las clases, no pueden representarse en
json::

    import datetime
    import json

    json.dumps(date.date.today())

Como vemos, llamar a ``json.dumps`` con un objeto que no puede ser representado como JSON
elevará una excepción del tipo TypeError.

En resumen, estos son los tipos de datos y estructuras que podemos
codificar sin mayor problema en JSON:

- Diccionarios (dict)
- Listas y tuplas (list, tuple)
- Cadenas (str en Python 3, unicode en Python 2)
- Números (int, float)
- True, False, y None

**Pregunta**: ¿Cómo podemos guardar entonces una fecha, por ejemplo, en JSON?

La funcion ``loads``
--------------------

La funci'on ``loads`` es la inversa de ``dumps``: le psasmos una cadena de
texto en formato JSON y nos devuelve un valor Python perfectamente válido (A no
ser que la cadena JSON no sea correcta).

    import json

    data = json.loads('[null, true, false, "Hola, mundo!"]')
>>> data
[None, True, False, 'Hola, mundo!']
>>> data[1]
True
>>> data[3]
'Hola, mundo!'
Otros ejemplos:

>>> d = json.loads('{"url": "recursospython.com", "sitio": "Recursos Python"}')
>>> d["url"]
'recursospython.com'
>>> d["sitio"]
'Recursos Python'
Codificar y decodificar en archivos
Además, el módulo json provee las funciones dump y load, similares a dumps y loads pero que operan con archivos. Por ejemplo, podemos almacenar una lista de Python en un archivo con el formato JSON:

data = [True, False, None, 'Hola, mundo!']
with open("data.json", "w") as f:
   json.dump(data, f)
De forma análoga recuperamos el objeto leyendo el fichero vía load().

with open("data.json") as f:
    data = json.load(f)
# Imprime [True, False, None, 'Hola, mundo!'].
print(data)
De hecho las funciones no se limitan únicamente a archivos del disco, sino que aceptan cualquier objeto que soporte los métodos write() o read().

from io import StringIO
stream = StringIO()
data = [True, False, None, 'Hola, mundo!']
json.dump(data, stream)
print(stream.getvalue())
Otras opciones
Para mostrar una estructura de JSON en formato agradable y legible podemos usar el parámetro indent, que indica la cantidad de espacios que deben emplearse como «indentación».

>>> data = [True, False, {"site": "Recursos Python"}]
>>> print(json.dumps(data, indent=4))
[
    true,
    false,
    {
        "site": "Recursos Python"
    }
]
Por otro lado, en algunos casos se quiere comprimir lo más posible el resultado. Para esto podemos usar el parámetro separators, que por defecto equivale a (", ", ": "), para remover los espacios entre claves, valores y elementos de la lista.

>>> json.dumps(data, separators=(",", ":"))
'[true,false,{"site":"Recursos Python"}]'
Por último, especificando el parámetro sort_keys, que por defecto es False, logramos ordenar por claves la estructura que resulta de la codificación.

>>> json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
'{"a": 0, "b": 0, "c": 0}'
¡No olvides chequear la documentación de json para el resto de las opciones!
