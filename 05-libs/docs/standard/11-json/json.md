---
title: json - Trabajar con el formato json
---
## Introducción a `json`

Python incopora en la librería estándar una libreria para trabajar con el
formato **JSON**. JSON es un formato de texto que nos permite guardar de forma
estructurada nuestros datos.

Ventajas de JSON frente a CSV:

- Formato estándar

- Tipos de datos y estructuras de datos

- No solo tablas

JSON es utilizado por casi todos los servicios web para el envío y
recepción de datos.

A partir de la versión 2.6 Python incorpora en su librería estándar el
módulo `json`, con una API similar a la de `pickl`e, para codificar y
decodificar información en el formato JSON. «Codificar» y «decodificar»
deben ser entendidos como convertir de un objeto Python a JSON y
viceversa.

El formato JSON es bastante similar a la sintaxis de Python, pero
contiene únicamente dos tipos de estructuras: diccionarios y listas.
Diccionario es lo que en Python conocemos como tal, un conjunto de pares
con una clave y un valor. Y una lista no es más que un conjunto ordenado
de objetos, que en Python podria ser o bien una lista, un array o
incluso en conjunto.

### La función `dumps`

La función `dumps` acepta casi cualquier valor o estructura de datos en
Python, y nos devuelve una cadena de texto en JSON equivalente. Al ser
una cadena de texto, podemos guardarla en un fichero, en una base de
datos, mandarla por correo, crear un codigo QR a partir de ella,
imprimirla en papel y enviarla por correo postal, etc.

Podemos codificar en json casi cualquier tipo de valor, veamos algunas
pruebas:

```python
import json

assert json.dumps(1) == '1'
assert json.dumps('hola') == '"hola"'
assert json.dumps("hola") == '"hola"'
assert json.dumps(None) == 'null'
assert json.dumps(True) == 'true'
assert json.dumps(False) == 'false'
assert json.dumps(3.1416) == '3.1416'
assert json.dumps(['a', 'b', 'c']) == '["a", "b", "c"]'
assert json.dumps(['texto', 23, False]))
assert json.dumps(('a', 'b', 'c')))
assert json.dumps({
    'uno': 1,
    'dos': 2,
    'alpha': 'texto',
    })
```

Si bien los resultados son similares, vemos que hay diferencias. Por ejemplo,
el `None` de Python se representa como `null`. En Python podemos usar comillas
simples o doples, pero JSON requiere comillas dobles. Los valores booleanos
Python `True` y `False` son `true` y `false`.

Algunos tipos de datos, y especialmente las clases, no pueden representarse en
json:

```python
import datetime
import json

json.dumps(date.date.today())
```

Como vemos, llamar a `json.dumps` con un objeto que no puede ser
representado como JSON elevará una excepción del tipo `TypeError`.

En resumen, estos son los tipos de datos y estructuras que podemos
codificar sin mayor problema en JSON:

- Diccionarios (dict)

- Listas y tuplas (list, tuple)

- Cadenas (str en Python 3, unicode en Python 2)

- Números (int, float)

- True, False, y None

**Pregunta**: ¿Cómo podemos guardar entonces una fecha, por ejemplo, en
JSON?

### La funcion `loads`

La función `loads` es la inversa de `dumps`: le pasamos una cadena de
texto en formato JSON y nos devuelve un valor Python perfectamente
válido (Siempre y cuando la cadena JSON no sea correcta).

```python
import json

data = json.loads('[null, true, false, "Hola, mundo!"]')

assert data[0] is None
assert data[1] is True
assert data[2] is False
assert data[3] == "Hola, mundo!"
assert len(data) == 4
```

### Codificar y decodificar archivos

Además, el módulo `json` provee las funciones `dump` y `load`,
similares a `dumps` y `loads` pero que operan con archivos. Por ejemplo,
podemos almacenar una lista de Python en un archivo con el formato JSON
usando el siguiente código:

```python
data = [True, False, None, 'Hola, mundo!']
with open("data.json", "w") as f:
    json.dump(data, f)
```

De forma análoga recuperamos el objeto
leyendo desde el fichero vía `load()`:

```python
with open("data.json") as f:
    data = json.load(f)
```

De hecho las funciones no se limitan únicamente a archivos del disco, sino que
aceptan cualquier objeto que soporte los métodos `write()` o `read()`:

```python
from io import StringIO
stream = StringIO()
data = [True, False, None, 'Hola, mundo!']
json.dump(data, stream)
print(stream.getvalue())
```

### Otras opciones

Para mostrar una estructura de JSON en formato agradable y legible podemos usar
el parámetro `indent`, que indica la cantidad de espacios que deben emplearse
como indentación.

```python
import json

data = [True, False, {"lang": "python", "version": 3.9}]
print(json.dumps(data, indent=2))
```

Produce:

```javascript
[
  true,
  false,
  {
    "lang": "python",
    "version": 3.9
  }
]
```

Podemos usar el parámetro `separators`,
que por defecto equivale a `(", ", ": ")`, para definir los separadores
entre las parejas clave/valor de un diccionario o los 
elementos de una lista. Esto se puede usar, por ejemplo, para hacer la
representación ligeramente más compacta:

```python
import json

data = [True, False, {"lang": "python", "version": 3.9}]
json.dumps(data, separators=(",", ":"))
```

Produce:

```json
[true,false,{"lang":"python","version":3.9}]
```

Otro parámetro opcional que puede resultar útil es `sort_keys`, que por defecto
está definido como `False`. Poniéndolo a `True` obtenemos los resultados de los
diccionarios ordenados por los valores de las claves:

```python
import json

json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
```

Produce:

```json
{"a": 0, "b": 0, "c": 0}
```

Documentación oficial de `json`: <https://docs.python.org/es/3/library/json.html>
