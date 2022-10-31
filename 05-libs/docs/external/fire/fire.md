---
title: fire - Interfaz de línea de comandos
---

## Introducción a `fire`

La librería [**fire**](https://github.com/google/python-fire) nos permite
generar automáticamente una interfaz de línea de comando a partir de cualquier
objeto Python. Alguna de sus características más notables son:

- Es muy sencilla de usar

- Incluye herramientas para desarrollo y depuración

- Convierte código preexistente en un cliente de línea de comando

- Facilita pasar código de *Bash* a Python

## Instalación de fire

Podemos instalar la librería con `pip`:

    pip install fire


## Ejemplo de uso de fire

Para usar esta librería solo necesitamos instanciar un objeto de la clase
`Fire`.  Le podemos pasar como parámetro cualquier objeto de Python, como por
ejemplo una función, pero si no le pasamos nada intentará convertir en una
opción cualquier _callable_ definido en el programa:

Por ejemplo, para convertir este código:

```python
def hola(name="Mundo"):
    return "Hola %s!" % name
```

En un [CLI](https://es.wikipedia.org/wiki/Interfaz_de_l%C3%ADnea_de_comandos),
solo hay que hacer estos cambios:

```python
--8<--
./docs/external/fire/hola.py
--8<--
```

Ahora, **desde la línea de comandos**, podemos ejecutar:

```shell
python hola.py
python hola.py hola
python hola.py hola Sam
```

Si incluimos un *docstring* en la función, también se usará en la ayuda:

```python
--8<--
./docs/external/fire/hola-docs.py
--8<--
```

Es realmente impresionante lo sencillo que es de usar comparado con `argparse`.

**Ejercicio**: Modificar `hola.py` e incluir alguna otra función.
Comprobar que `fire` la ha convertido en una opción más accesible desde la
línea de comando con `python hola --help`. Por ejemplo una función `add`
como esta:

```python
def add(a, b):
    return a + b
```

## Exponer múltiples comandos

Un problema con llamar a `Fire` sin parámetros es que este convertirá cualquier
objeto *callable* que encuentre en una opción, pero esto es algo que
normalmente no queremos. En general preferiríamos definir exclusivamente
algunos puntos de entrada.

Esto se puede lograr de varias formas. Vamos a ver en detalle cada una de
ellas, desde la más sencilla (exporta todo) a las más elaboradas.

### Primera opción: exportar todo

La forma más simple de exponer múltiples comandos es, como ya hemos
visto, definir múltiples funciones y luego instanciar `Fire` sin ningún
parámetro,

```python
--8<--
./docs/external/fire/02-simple-calc.py
--8<--
```

Observa que `Fire` ha interpretado correctamente los valores $10$ y $20$
como números y no como cadenas de textos. Explicaremos porqué pasa esto
más adelante.

### Segunda opción: usar un diccionario

Podemos seleccionar las funciones que queremos exponer a la línea de comando,
instanciando de la clase `Fire` pasando como parámetro un diccionario con las
funciones deseadas.

```python
--8<--
./docs/external/fire/03-simple-calc.py
--8<--
```

#### Tercera opción: Usar una clase

La clase `Fire` también puede ser instanciada con un objeto o una clase.  En
ambos casos, todos los métodos definidos en la clase serán accesibles desde la
línea de comandos.

```python
--8<--
./docs/external/fire/04-simple-calc.py
--8<--
```

En general es preferible pasar como parámetro a la clase `Fire` otra clase, en
vez de un objeto, porque esto nos permite usar argumentos de la línea de
comandos para el constructor de la clase.

**Ejercicio**: Hacer un pequeño programa para imprimir una tabla de
multiplicación. El programa debe aceptar un argumento que seria el
número de la tabla que queremos imprimir (hicimos un programa similar
cuando vimos la librería `argparse`).

## Acceder a propiedades

Hasta ahora solo hemos accedido a funciones pero también podemos acceder a las
propiedades de las clases.

En el siguiente ejemplo veremos un pequeño programa con el que podemos
mostrar información de aeropuertos internacionales usando el código del
aeropuerto (La información fue obtenida de <https://github.com/trendct-data/airports.py>).

```python
--8<--
./docs/external/fire/find-airport.py
--8<--
```

Podemos usar este programa pasándole el código internacional del aeropuerto, y
en ese caso nos devolverá un mensaje con la información completa, que incluye
el nombre, la latitud y la longitud:

```shell
python ./find-airport.py --code=LAX
LAX  "Los Angeles International Airport" (-118.4079971, 33.94250107)
```

pero también podemos pedir cualquiera de los atributos que defina la instancia
dela clase:

```shell
$ python ./find-airport.py --code=LAX nombre
"Los Angeles International Airport"

$ python ./find-airport.py --code=LAX latitud
-118.4079971

$ python ./find-airport.py --code=LAX longitud
33.94250107

$ python ./find-airport.py --code=LAX coords
[-118.4079971, 33.94250107]
```

## Encadenando llamadas de funciones

Podemos encadenar llamadas de una forma sencilla, todo lo que tenemos
que hacer es escribir una clase cuyo métodos siempre devuelvan `self`,
como en el siguiente ejemplo:

```python
--8<--
./docs/external/fire/canvas.py
--8<--
```

**Ejercicio**: Probar desde la shell:

```shell
python canvas.py move 3 3 on move 3 6 on move 6 3 on move 6 6 on move 7 4 on move 7 5 on
```

## Salidas personalizada

En el ejemplo anterior hemos pintado en pantalla el resultado de nuestra
órdenes encadenadas con el formato que definimos en el método `__str__`.

Si se define un método `__str__` propios serán este método el que se
usará para mostrar como salida. Si no se define, se usará la pantalla de
ayuda.

## Llamando a funciones y métodos

Los argumentos para los constructores siempre deben pasarse por nombre y
usar la sintaxis `--name=value`.

Los argumentos para otros métodos o funciones se pueden pasar por
posición o por nombre.

Una cosa muy útil es que los guiones (`-`) y los subrayados (`_`) son
intercambiables tanto en los nombres de las funciones como en los
argumentos de la línea de comandos. De igual manera el signo de `=`
entre el nombre de la opción y el valor es opcional.

## Interpretación de los argumentos.

Los tipos de los argumentos vienen determinados por su valor y no por la
signatura de la función o método que se vaya a usar. Se puede pasar como
argumento desde la línea de comandos cualquier valor literal que Python
puede interpretar: números, cadenas de textos, tuplas, listas y
diccionarios (Dependiendo de la versión de Python que estés usando,
también conjuntos).

También puedes usar colecciones anidadas siempre y cuando estas solo
contengan literales.

A modo de demostración, el siguiente programa nos dice de qué tipo
Python es el argumento que le pasamos.

```python
--8<--
./docs/external/fire/arguments.py
--8<--
```

Que podemos usar de la siguiente manera:

```shell
$ python arguments.py 23
int
$ python arguments.py hola
str
$ python arguments.py 3.4
float
$ python arguments.py {"uno":1}
dict
```

Nota para usuarios de *Bash*. Ten cuidado con las comillas. Si queremos
pasar la cadena de textos `"10"` en vez del número entero `10`
necesitamos escapar las comillas dos veces porque *Bash* hace su propia
interpretación de la cadena con lo cual elimina las comillas exteriores.

Las expresiones `True` y `False` se interpretan como valores booleanos.
Otra forma de pasar valores booleanos a nuestro programa sería usar la
sintaxis de doble guión en la forma `--name` para ajustar el valor a
`True` y `--noname` para ajustar el valor a `False`.

Como con `argparse`, un *flag* que siempre puedes usar es `--help`, para
mostrar explicaciones y formas de usos. `Fire` incorpora tus
*docstrings* dentro de la ayuda que él genera automáticamente.

La clase `Fire` tiene varias opciones interesantes más, especialmente de agrupación
de comandos. El CLI de *git* funciona así, usando sub-ordenes dentro de
git.


## Otras librerías similares o relacionadas

- [`Typer`](https://github.com/tiangolo/typer) es una librería para
  aplicaciones CLI basada en el sistema de anotaciones incorporado en Python
  3.6

- [`Rich`](https://github.com/willmcgugan/rich) es un paquete de Python para
  proporcionar texto enriquecido y formato en la terminal. Rich también puede
  representar tablas, barras de progreso, markdown, código fuente resaltado por
  sintaxis, trazas y más.

- [`docopt`](https://pypi.org/project/alive-progress/) también está orientado a
  facilitar el procesado de las opciones de línea de comando, pero toma una
  aproximación muy interesante: Se escribe en texto plano la documentación que
  deseamos para las opciones (con ciertas restricciones) y `docopt` genera
  automáticamente un parser para esas opciones.

- [`cement`](https://builtoncement.com/) es un *framework* orientado a la
  creación de aplicaciones CLI en Python.

- [`click`](https://click.palletsprojects.com/en/8.0.x/) es un paquete para la
  creación de interfaces de línea de comandos en forma de elementos que podemos
  combinar a nuestro gusto.

- [`cliff`](https://docs.openstack.org/cliff/latest/) es otro framework para la
  cración de aplicaciones CLI, especialmente para la creación de multiples
  niveles de comandos.

- [`python-prompt-toolkit`](https://python-prompt-toolkit.readthedocs.io/en/master/)
  es una librería para construir aplicaciones de línea de comandos poderosas e
  interactivas. Puede servir como reemplazo de la función [readline de
  GNU](http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html) y también de
  reemplazo en aplicaciones de pantalla completa.

- [`alive-progress`](https://pypi.org/project/alive-progress/) una bara de
  progreso con animaciones, tiempo estimado y algunas características más muy
  interesantes.

- [`Asciimatics`](https://github.com/peterbrittain/asciimatics) permite crear
  aplicaciones a pantalla completa en modo texto, incluyendo animaciones o
  formularios, en varias plataformas.

- [`Colorama`](https://github.com/tartley/colorama) permite usar colores en la
  terminal, sobre varias plataformas.

- [`tqdm`](https://github.com/tqdm/tqdm) es un añadido que nos permite
  incluir una barra de progreso en nuestros programas de línea de comandos.
  Su nombre deriva de la palabra árabe *taqaddum (تقدّم)* que
  significa «progreso», y tabmién es la abreviación de la frase en Español "Te
  Quiero Demasiado". 
