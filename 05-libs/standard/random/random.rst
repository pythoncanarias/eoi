La librería random
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Este módulo implementa generadores de números pseudo-aleatorios
para distintas distribucines. Para enteros, podemos hacer
una selección uniforme dentro de un rango; para secuencias, una
selección uniforme de un elemento. Podemos reordenar al azar
-barajar- una secuencia y obtener una muestra al azar.
También podemos trabajar con distribucions uniformes, normales
(Gauss), logaritmica normal, exponencial negativa, y distribuciones
gamma y beta.

Casi todas las funciones dependen de la función básica ``random()``, que
genera un numero al azar en el intervalo semiabierto [0.0, 1.0).

    ``random.seed([x])``

        Inicializa el generador de números con un determinado valor.
        Si se omite, se usa un valor obtenido a partir de la fecha y
        hora actual

    ``random.random()``

        Devuelve un número al azar en coma flotante en el intervalo
        [0.0, 1.0).

    ``random.randint(a, b)``

        Genera un entero N al azar tal que a <= N <= b.


    ``random.choice(seq)``

        Devuelve un elemento al azar de los perteneciente a la secuencia
        ``seq`` Si ``seq`` está vacio, eleva una excepción ``IndexError``.

    ``random.shuffle(x[, random])``

        Baraja la secuencia (internamente, es decir, no genera una
        nueva secuencia). El argumento opcional ``random`` es una
        función sin argumentos que devuelve un número en coma flotante
        en el intervalo [0.0, 1.0); por defecto es la función
        ``random()``.


    ``random.gauss(mu, sigma)``

        Distribución normal o de Gauss. ``mu`` es la media, ``sigma``
        es la desviación estandar.
