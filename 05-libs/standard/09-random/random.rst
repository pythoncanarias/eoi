``random``: Generación de números pseudo-aleatorios
===================================================

Este módulo implementa generadores de números pseudo-aleatorios
para distintas distribucines. Para enteros, podemos hacer
una selección uniforme dentro de un rango; para secuencias, una
selección uniforme de un elemento. Podemos reordenar al azar
-barajar- una secuencia y obtener una muestra al azar.
También podemos trabajar con distribucions uniformes, normales
(Gauss), logaritmica normal, exponencial negativa, y distribuciones
gamma y beta.

La función ``random``
---------------------

La función ``random.random()`` devuelve un número al azar en coma flotante cuyo
valor puede ser mayor o igual que 0 y estríctamente menor que 1, es decir, el
valor 1.0 esta excluido. En otras palabras, genera un número al azar en el
intervalo semiabierto [0.0, 1.0).

Casi todas las funciones dependen de esta función básica ``random()``.

La función ``seed``
-------------------

La función ``random.seed([x])`` inicializa el generador de números con un
determinado valor.  Si se omite, se usa un valor obtenido a partir de la fecha
y hora actual. Esto nos permite obtener o bien valores menos deterministas (Es
decir, algo mas al azar) al estar influidos por la fecha y hora actual, o
valores deterministas, esto es, si inicializamos con ``seed`` a un valor
especifico, las siguientes llamadas a cualquiera de las funciones nos devuelven
las mismas secuencias 

En otras palabras, si inicializo, usando ``seed`` con un valor determinado, digamos
173, las siguientes llamadas a ``random``, por ejemplo, devolveran los mismos valores.

Si ejecutamos el siguiente código::

    import random
    random.seed(173)
    for _ in range(3):
        print(random.random())
    random.seed(173)
    for _ in range(3):
        print(random.random())

Veremos que la salida del programa anterior debería dar un resultado similar al siguiente.
Observa que los valores se repiten a partir del cuarto, porque volvemos a fijar
el valor de semilla o *seed*::

    0.8041030466905951
    0.44217778729817014
    0.02432865274376439
    0.8041030466905951
    0.44217778729817014
    0.02432865274376439

Puede ser un poco difícil ver la utilidad o necesidad de esto. Después de todo,
si queremos valores aleatorios, queremos qe los valores sean lo más diferentes
posibles, ¿no? Pero a veces, especialmente en simulaciones, queremos crear un
entorno más o menos al azar, pero **reproducible**, porque queremos probar
distintos parámetros del modelo, por ejemplo. En estos casos queremos que el
entorno producido sea el mismo en las dos simulaciomes, para que el único
cambio en los dos escenarios sean en los parámetros del modelo, no en los datos
de entrada.

La función ``randint``
----------------------

La función ``random.randint(a, b)`` genera un entero :math:`n` al azar tal que
:math:`a <= n <= b`.


La función ``randrange``
------------------------

La función ``random.randrange(a, b)`` es similar a ``randint``, pero los
parámetros son similares a los de la función ``range`` y, en general, a la
forma en que se definen los rangos en Python, en los que el último valor no
está incluido. En otras palabras, genera un entero :math:`n` al azar tal
que :math:`a <= n < b`.


La función ``choice``
---------------------

La función ``random.choice(seq)`` devuelve un elemento al azar de los
perteneciente a la secuencia ``seq`` Si ``seq`` está vacio, eleva una excepción
``IndexError``.

.. note:: **Ejercicio** Simulación de cartas

Supongamos la siguiente clase, que proporciona un modelo de una carta de la
baraja francesa:

.. literalinclude:: cards.py
   :language: Python
   :lines: 4-

Con esa clase, podemos crear un objeto de tipo naipe o ``Card``. El siguiente
ejemplo crea una variable para representar el as de picas::

    from cards import Card
    as_picas = Card(Card.SPADES, 1)
    print(as_picas)

que produciría la siguiente salida::

    As de Picas

Con el siguiente codigo creamos toda la baraja::

    from cards import Card

    baraja = []
    for palo in [Card.CLUB, Card.DIAMONDS, Card.SPADES, Card.HEARTS]:
        for valor in range(1, 14):
            baraja.append(Card(palo, valor))
    assert len(baraja) == 52

El siguiente programa crea una baraja francesa completa, y deberia mostrar una carta
elegida al azar, pero esta incompleto. Arreglalo para que funcione:

.. literalinclude:: ejercicio_01.py
   :language: python
   :lines: 4-

La función ``shuffle``
----------------------

La función ``random.shuffle(x[, random])`` baraja la secuencia (internamente,
es decir, no genera una nueva secuencia). El argumento opcional ``random`` es
una función sin argumentos que devuelve un número en coma flotante en el
intervalo [0.0, 1.0); por defecto es la función ``random()``.

.. note:: **Ejercicio**: Escribe un programa que reparta cinco cartas al azar, simulando
   la entrega de una mano a un jugador. Puedes usar como esqueleto el código siguiente:

.. literalinclude:: ejercicio_02.py
   :language: Python
   :lines: 4-

La función ``gauss``
--------------------

La función ``random.gauss(mu, sigma)`` devuelve un valor que sigue la
distribución normal o de Gauss. Los parámetros pasados son ``mu``, la media, y
``sigma`` que es la desviación estandar.

.. note:: **Ejercicio**: Una fabrica de tornillos produce los tornillos de 10 milimetros de diámetro con un error que presenta una desviación estándar de 0.0245. Escribir un programa que produzca una simulación de 10 tornilos producidos por esa fábrica:

.. literalinclude:: tornillos.py
   :language: Python
   :lines: 4-
