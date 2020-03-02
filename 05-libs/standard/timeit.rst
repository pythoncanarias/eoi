El módulo ``timeit``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: timeit

El módulo ``timeit`` permite obtener una medida fiable de los los tiempos de ejecución
de un fragmento de código Python.

En el siguiente cófigo mostramos dos formas diferentes de intercambiar
los valores de dos variables, la primera con una variable auxiliar
y la segunda usando el mecanismo de empaquetado/desempaquetado de tuplas::

    >>> # Usando una variable auxiliar
    >>> a = 7; b = 12
    >>> temp = a; a = b; b = temp
    >>>
    >>> # Usando tuplas
    >>> a = 7; b = 12
    >>> a, b = b, a

Pero ¿cuál será más rápida? Usando el módulo ``timeit`` podemos
salir de dudas::

    >>> from timeit import Timer
    >>> Timer('t=a; a=b; b=t', 'a=7; b=12').timeit()
    0.032704691999995816
    >>> Timer('a,b = b,a', 'a=7; b=12').timeit()
    0.02891511800000046

El intercambio por medio de tuplas es más rápido.

El módulo ``timeit`` usa funciones específicas del sistema operativo para medir estos tiempos, para
intentar conseguir la máxima precisión posible. Por la misma razón, ejecuta el código muchas veces
para reducir al mínimo el desvío o error causado por el inicio y finalización de la prueba.

.. index:: Timer

El módulo solo define una clase, ``Timer``. El constructor de la clase espera como primer
parámetro o bien un *callable* (Una función, por ejemplo) que se pueda invocar sin ningún parámetro,
o una o más líneas de código para ser medidas. Como segundo parámetro, opcional, una o varias líneas
de inicialización o *setup*, normalmente usadas para inicializar valores. Una vez creado un objeto
de la clase `Timer`, podemos medir su tiempo de ejecución medio usando el método `timeit`, al cual
le podemos pasar como parámetro opcional el número de bucles o iteraciones que queremos repetir para
prevenir errores esstadísticosi (Aunque generalmente es buena idea dejarle esa desición al propio
módulo).

..aside:: Uso de ``timeit`` como un *one-liner*.

En el siguiente ejemplo
usamos ``timeit`` desde la línea de comandos para comprobar si el método ``join`` de las
cadenas de texto es más rápido cuando se le pasa una lista de enteros que previamente
hemos de transformar a *strings* usando 1) una expresion generadora, 2) una *list comprehension*
o 3) usando map::

    .. highlight:: shell
    $ python -m timeit '"-".join(str(n) for n in range(100))'
    10000 loops, best of 5: 22.5 usec per loop
    $ python -m timeit '"-".join([str(n) for n in range(100)])'
    10000 loops, best of 5: 20.8 usec per loop
    $ python -m timeit '"-".join(map(str, range(100)))'
    20000 loops, best of 5: 16.3 usec per loop

Los resultados varian para listas de diferentes tamaños::

    .. highlight:: shell
    $ python -m timeit '"-".join(str(n) for n in range(1000))'
    1000 loops, best of 5: 225 usec per loop
    $ python -m timeit '"-".join([str(n) for n in range(1000)])'
    1000 loops, best of 5: 210 usec per loop
    $ python -m timeit '"-".join(map(str, range(1000)))'
    2000 loops, best of 5: 169 usec per loop

``timeit`` es lo suficientemente listo como para ajustar el número de veces
que ejecuta el código al tiempo que tarda en ejecutarse una sola vez. En estas segundas pruebas,
como la lista de numeros es 10 veces más grande, en vez de ejecutar 10.000 iteraciones solo
ejecute 1.000.

