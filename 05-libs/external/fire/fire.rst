``fire``: Interfaz de línea de comandos
=======================================

La librería **fire_** nos permite generar automáticamente una interfaz de línea
de comando a partir de cualquier objeto python. Alguna de sus caracterísitcas
máß notables son:

- Es muy sencilla de usar

- Incluye herramientas para desarrollo y depuración

- Convierte codigo preexistente en un cliente de línea de comando

- Facilita pasar cóodigo de Bash a Python

Instalación
-----------

Podemos instalar la librería con Pip::

    pip install fire


Ejemplo de uso.
---------------

Para usar fire solo necesitamos instanciar un objeto de la clase ``Fire``.
Le podemos pasar como parámetro cualquier objeto
de Python, como por ejemplo una función, pero si no le pasamos nada intentará
convertir en una opción cualquier *callable* definido en el programa:

Veamoslo con un ejemplo, para convertir este código::

    def hola(name="Mundo"):
        return "Hola %s!" % name

en un CLI, solo hay que hacer estos cambios:

.. literalinclude:: hola.py
   :language: Python
   :emphasize-lines: 1,6,7
   :lines: 3-

Ahora, **desde la línea de comandos**, podemos ejecutar::

   python hola.py
   python hola.py hola
   python hola.py hola Sam

Si incluimos un *docstring* en la función, también se usará en la ayuda:

.. literalinclude:: hola-docs.py
   :language: Python
   :lines: 3-

Realmente es impresionante lo sencillo que es comparado con ``argparse``.

**Ejercicio**: Modificar hola.py e incluir alguna otra función. Comprobar
que fire la ha convertido en una opcion más accesible desde la línea de
comando con ``python hola --help``. Por ejemplo una función ``add``
como esta::

    def add(a, b):
        return a + b


Exponer múltiples comandos
--------------------------

Un problema con llamar a ``Fire`` sin parámetros es que este convertirá cualquier
objeto *callable* que encuentre en una opción, pero esto es algo que
normalmente no queremos. En general preferiríamos definir exclusivamente
algunos puntos de entrada. 

Esto se puede lograr de varias formas. Vamos a ver en detalle
cada una de ellas, desde la más sencilla (exporta todo) a las más
elaboradas.

Primera opción: exportar todo
-----------------------------

La forma más simple de exponer múltiples comandos es, como ya hemos visto,
definir múltiples funciones y luego instanciar ``Fire`` sin ningún parámetro,

.. literalinclude:: 02-simple-calc.py
   :language: Python
   :lines: 3-

Observa que ``Fire`` ha interpretado correctamente los valores 10 y 20 como
números y no como cadenas de textos. Explicaremos porque pasa esto más
adelante.

Segunda opción: usar un diccionario
-----------------------------------

Podemos seleccionar las funciones que queremos exponer a la línea de
comando, instanciando de la clase ``Fire`` pasando como parámetro un
diccionario con las funciones deseadas.

.. literalinclude:: 03-simple-calc.py
   :language: Python


Tercera opción: Usar una clase
------------------------------

La clase ``Fire`` también puede ser instanciada con un objeto o una clase.
En ambos casos, todos los métodos definidos en la clase serán accesibles
desde la línea de comandos.

.. literalinclude:: 04-simple-calc.py
   :language: Python

En general es preferible pasar como parámetro a la clase Fire otra
clase, en vez de un objeto, porque esto nos permite usar argumentos de
la línea de comandos para el constructor de la clase.

**Ejercicio**: Hacer un pequeño programa para imprimir una tabla de
multiplicación. El programa debe aceptar un argumento que seria el numero de la
tabla que queremos imprimir (hicimos un programa similar cuando vimos la
libreria ``argparse``).

Acceder a propiedades
---------------------

Hasta ahora solo hemos accedido a funciones pero también podemos acceder
a las propiedades de las clases.

En el siguiente ejemplo veremos un pequeño programa con el que podemos
mostrar información de aeropuertos internacionales usando el código del
aeropuerto (La información fue obtenida de https://github.com/trendct-data/airports.py).

.. literalinclude: find-airport.py
   :language: Python
    

Encadenando llamadas de funciones
---------------------------------

Podemos encadenar llamadas de una forma sencilla, todo lo que tenemos
que hacer es escribir una clase cuyo métodos siempre devuelvan ``self``,
como en el siguiente ejemplo:

.. literalinclude:: canvas.py
   :language: python
   :lines: 3-

**Ejercicio**: Probar desde la shell::

    python canvas.py move 3 3 on move 3 6 on move 6 3 on move 6 6 on move 7 4 on move 7 5 on

Salidas personalizada
~~~~~~~~~~~~~~~~~~~~~

En el ejemplo anterior hemos pintado en pantalla el resultado de nuestra
órdenes encadenadas con el formato que definimos en el método
``__str__``.

Si se define un método ``__str__`` propios serán este método el que se
usará para mostrar como salida. Si no se define, se usará la pantalla de
ayuda.

Llamando a funciones y métodos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los argumentos para los constructores siempre deben pasarse por nombre y
usar la sintaxis ``--name=value``.

Los argumentos para otros métodos o funciones se pueden pasar por
posición o por nombre.

Una cosa muy útil es que los guiones (``-``) y los subrayados (``_``)
son intercambiables tanto en los nombres de las funciones como en los
argumentos de la línea de comandos. De igual manera el signo de ``=``
entre el nombre de la opción y el valor es opcional.

Interpretación de los argumentos.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los tipos de los argumentos vienen determinados por su valor y no por la
signatura de la funcion o método que se vaya a usar. Se puede pasar
como argumento desde la línea de comandos cualquier valor literal que
Python puede interpretar: números, cadenas de textos, tuplas, listas y
diccionarios ( dependiendo de la versión de Python que estes usando
también conjuntos).

También puedes usar colecciones anidadas siempre y cuando estas solo
contengan literales.

A modo de demostración, el siguiente programa nos dice de qué tipo
Python es el argumento que le pasamos.

.. literalinclude:: arguments.py
   :language: Python
   
Que podemos usar de la siguiente manera::

    $ python arguments.py 23
    int
    $ python arguments.py hola
    str
    $ python arguments.py 3.4
    float
    $ python arguments.py {"uno":1}
    dict

Nota para usuarios de Bash. Ten cuidado con las comillas. Si queremos pasar la
cadena de textos ``"10"`` en vez del número entero ``10`` necesitamos escapar
las comillas dos veces porque Bash hara su propia interpretación de la cadena
con lo cual elimina las comillas exteriores.

Las expresiones ``True`` y ``False`` se interpretan como valores booleanos.
Otra forma de pasar valores booleanos a nuestro programa sería usar la sintaxis
de doble guión en la forma ``--name`` para ajustar el valor a ``True`` y
``--noname`` para ajustar el valor a ``False``.

Como con ``argparse``, un *flag* que siempre puedes usar es ``--help``, para
mostrar explicaciones y formas de usos. ``Fire`` incorpora tus *docstrings*
dentro de la ayuda que él genera automáticamente.

Fire tiene varias opciones interesantes más, especialmente de agrupación de
comandos. El CLI de git funciona asi, usando subcomandos dentro de git. consúltalas en la página
web https://github.com/google/python-fire si estás interesado.

.. _fire: https://github.com/google/python-fire

Otras librerías similares o relacionadas
----------------------------------------

- [Typer](https://github.com/tiangolo/typer): Typer es una librería
  para aplicaciones CLI basada en el sistema de
  anotaciones incorporado en Python 3.6
  
- [Rich](https://github.com/willmcgugan/rich) Rich es un
  paquete de Python para proporcionar texto enriquecido
  y formato en la terminal. Rich también puede
  representar tablas, barras de progreso, markdown, código
  fuente resaltado por sintaxis, trazas y más.


- cement - CLI Application Framework for Python.

- click - A package for creating beautiful command line interfaces in a composable way.

- cliff - A framework for creating command-line programs with multi-level commands.

- docopt - Pythonic command line arguments parser.

- python-prompt-toolkit - A library for building powerful interactive command lines.


- alive-progress - A new kind of Progress Bar, with real-time throughput, eta and very cool animations.

- asciimatics - A package to create full-screen text UIs (from interactive forms to ASCII animations).

- bashplotlib - Making basic plots in the terminal.
colorama - Cross-platform colored terminal text.

- [tqdm](https://github.com/tqdm/tqdm) - Fast, extensible progress bar for loops and CLI. Derives from the Arabic word taqaddum (تقدّم) which can mean "progress," and is an abbreviation for "I love you so much" in Spanish (te quiero demasiado).. Instantly make your loops show a smart progress meter - just wrap any iterable with tqdm(iterable), and you're done! 