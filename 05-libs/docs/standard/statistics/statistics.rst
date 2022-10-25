La librería statistics
----------------------

La librería **statistics** incluye algunas funciones matemáticas para realizar
cálculos estadísticos.

Alcance y limitaciones
~~~~~~~~~~~~~~~~~~~~~~

Esta librería está muy lejos de la potencia de otras librerías de terceros
como numPy, sciPy y otros, pero tiene la ventaja de venir incorporada
en lo librería estandar (desde Python 3.4), y tiene funcionalidad suficiente
para realizar varias gráficas y cálculos relativamente complejos.

Estas funciones trabajan con números enteros, en coma flotante (*float*),
decimales (``Decimal``) y fraciones (``Fraction``). Pero es muy
recomendable trabajar con listas y otras colecciones que los datos
sean homogeneos. Por ejemplo, una lista de enteros solo deberia tener 
enteros.

Funciones de medias y medidas similares
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La función mean
^^^^^^^^^^^^^^^

La funcion **mean** calcula la media aritmética de un conjunto de datos
(Una poblacion o una muestra, en terminis estadisticsos)

Ejercicio: Calcular la media aritmética de $23, 76, 99 y 12$.

La función geometric_mean
^^^^^^^^^^^^^^^^^^^^^^^^^

la función **geometric_mean()** es equivalente a la anterior, pero calcula
media geométrica. La media geométrica de $n$ numeros es la raíz n-ésima del
producto de todos los números. Se usa por ejemplo para promediar intereses
compuestos.
	
Por ejemplo, la media geométrica de 2 y 18 es:

.. math::

    {\displaystyle {\sqrt[{2}]{2\cdot 18}}={\sqrt[{2}]{36}}=6}

Otro ejemplo, la media geométrica de 1, 3 y 9 sería:

.. math::

    {\displaystyle {\sqrt[{3}]{1\cdot 3\cdot 9}}={\sqrt[{3}]{27}}=3}

La función median
^^^^^^^^^^^^^^^^^

La función **median()** calcula la mediana de una serie de valores, es
decir, el valor que está en la posición central en un conjunto de datos
ordenados. Si el número de datos es impar, la posicion central es unica y el
valor que esté ahí es la mediada, pero si son pares, el valor de la mediana es
la media de los dos valores que estan a la mitad.

Por ejemplo, la serie [3, 6, 9, 12, 24], como tiene 5 elementos, impar, la
posicion de la mediana es 3 y para este caso la mediana vale 9.

Pero si el número de elementos es par, como en [3, 6, 9, 12], no hay una
posición central única; podría ser tanto la segunda como la tercera
posición. Así que lo que se hace es tomar la media de los valores en
esas posiciones, 3 y 6, dando un valor para la mediana de 4.5.

La función mode
^^^^^^^^^^^^^^^

La función **mode()** nos da la moda, esto es, el valor o valores
que más se repite dentro de la serie.

Por ejemplo, para los valores [1, 2, 4, 4, 4, 4, 7, 39142], la moda es 4.

Esta función es la única dentro de esta librería que acepta valores discretos,
además de números. Por ejemplo::

    print(mode(["red", "blue", "blue", "red", "green", "red", "red"]))
    'red'


Ejercicio: Dado el siguiente texto:

    - Haga el favor de poner atención en la primera cláusula porque es muy
      importante. Dice que… la parte contratante de la primera parte será
      considerada como la parte contratante de la primera parte. ¿Qué tal, está
      muy bien, eh?

    - No, eso no está bien. Quisiera volver a oírlo.

    - Dice que… la parte contratante de la primera parte será considerada como
      la parte contratante de la primera parte.

    - Esta vez creo que suena mejor.

    - Si quiere se lo leo otra vez.

    - Tan solo la primera parte.

    - ¿Sobre la parte contratante de la primera parte?

    - No, solo la parte de la parte contratante de la primera parte.

    - Oiga, ¿por qué hemos de pelearnos por una tontería como ésta? La
      cortamos.

    - Sí, es demasiado largo. ¿Qué es lo que nos queda ahora?

    - Dice ahora… la parte contratante de la segunda parte será considerada
      como la parte contratante de la segunda parte.

    - Eso si que no me gusta nada. Nunca segundas partes fueron buenas.
      Escuche: ¿por qué no hacemos que la primera parte de la segunda parte
      contratante sea la segunda parte de la primera parte? 

1) Usa ``statistics.mean`` para encontrar la media de la longitud de las palabras

2) Usa ``statistics.mode`` para encontrar la palabra más repetida

Podemos ayudarnos de esta función, a la que le pasamos un texto y nos devuelve
en una lista todas las palabras que contiene, manteniendo el orden pero
eliminando símbolos como ``-``, ``?``, ``!`` entre otros, y a la vez elimina palabras que
son demasiado comunes como ``y`` o ``la``::

    def text_to_words(text):
        exclude_words = ['', 'el', 'la', 'los', 'las', 'y', 'o']
        pat_seps = re.compile("[\-\s!?¿+\.,;:]+")
        words = (w.strip().lower() for w in pat_seps.split(text))
        return [for w in words if w not in exclude_words]


La función multimode
^^^^^^^^^^^^^^^^^^^^

La función **multimode(data)** es como la anterior, pero devuelve varios
valores si hay varias modas. La función ``mode`` siempre devuelve un único
valor (Si hay varias modas, devuelve la primera que encuentra).  Por ejemplo::

    import statistics

    sample = 'aabbbbccddddeeffffgg'
    assert statistics.multimode(sample) == ['b', 'd', 'f']
    assert statistics.mode(sample) == 'b'



las funciones stdev y variance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: desviación estándar
.. index:: varianza


La función **stdev(data, xbar=None)** devuelve la desviación estándar (esto es,
la raiz cuadrada de la varianza). Tambien podemos calcular directamente la
varianza con la funcion **variance(data, xbar=None)**.

Las dos funciones usan los mismo parámetros, y ambas se usan para medir la
variabilidad, es decir, cuan dispersos o agrupados están los datos. Valores
altos indican datos muy dispersos, mientras que valores pequeños indican datos
muy agrupados. Un valor de cero significaría que no hay dispersión en absoluto
y, por tanto, que todos los valores son iguales.


La función harmonic_mean
^^^^^^^^^^^^^^^^^^^^^^^^

Por último, la funcion **harmonic_mean(data)** devuelve la media
armónica. Esta es muy útil en conjuntos de números que se definen
en relación con alguna unidad, por ejemplo la velocidad 
(distancia por unidad de tiempo):

.. math::

    {\displaystyle {\bar {x}}=n\cdot \left(\sum _{i=1}^{n}{\frac {1}{x_{i}}}\right)^{-1}}

La media armónica es la inversa de la media aritmética, aplicado a los inversos
de los valores. Es decir, que donde la media divide, ahora multiplicamos, pero
la suma no se hace con los valores, sino con los inversos de los valores.

Por ejemplo, la media armónica de los números 34, 27, 45, 55, 22 y 34 es:


.. math::

    {\displaystyle {\frac {6}{{\frac {1}{34}}+{\frac {1}{27}}+{\frac {1}{45}}+{\frac {1}{55}}+{\frac {1}{22}}+{\frac {1}{34}}}}\approx 33,018}

Nota: Si alguno de los valores es cero, la media armónica se considera 0.

Para que sirve la media armónica? para aquellos valores que sean proporciones
o ratios, por ejemplo las velocidades.

Pregunta: Supongamos un coche que circula 10 kilometros a 40 km/h, luego otros 10 km a
60 km/h. Calcular su velocidad media::

    import statistics

    assert statistics.harmonic_mean([40, 60]) == 48.0

Pregunta: Supongamos un inversor que ha invertido la misma cantidad en tres
compañias, que le proporcionan un ratio de ganancias (Precio/Beneficio) 
de 2.5, 3 y 10. Calcular  el ratio de ganancias de toda la cartera::

    import statistics

    assert statistics.harmonic_mean([2.5, 3, 10]) == 3.6

Miniproyecto: Calcular el tamaño medio de todos los archivos que hay en un 
una carpeta determinada. Usa el esqueleto que vimos en la librería **os**
para recorrer un arbol de directorios con la funcion `walk`.

Bonus: Informa tambien de los valores máximo, mínimo y desviación estándar
de la media.
