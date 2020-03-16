Antipatrones
----------------------------

Usar el * al importaar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It import (into the current namespace) whatever names the module (or package) lists in its __all__ attribute -- missing such an attribute, all names that don't start with _.

It's mostly intended as a handy shortcut for use only in interactive interpreter sessions: as other answers suggest, don't use it in a program.

My recommendation, per Google's Python style guide, is to only ever import modules, not classes or functions (or other names) from within modules. Strictly following this makes for clarity and precision, and avoids subtle traps that may come when you import "stuff from within a module".

Importing a package (or anything from inside it) intrinsically loads and executes the package's __init__.py -- that file defines the body of the package. However, it does not bind the name __init__ in your current namespace (so in this sense it doesn't import that name).

Usar el operador ``is`` en vez de ``==``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Encuentre el problema en el siguiente codigo::

    status = get_status_function()
    if status is not 'ok':
        logging.error('Algo horrible ha pasado')

A veces se usa este patrón por imitación de usar ``is`` para comparar si un valor es ``None``. En el
caso de ``None``, y en algunos otros casos particulares, si es correcto hacerlo así. Pero, en general,
para comparar números, cadenas de texto, etc... siempre hay que utilizar el operador ``==`` (o ``!=``)
en vez de ``is`` (o ``not is``).

Esto es porque el operador ``is`` compara las **identidades** de los valores, no los valores en si.

Para ver la diferencia, se puede ajecutar el siguiente código::

    a = 'etc'
    b = 'etc'
    print(a is b, a == b)

Asi que todo parece correcto, pero ejecutemos ahora::

    a = 'etc'
    b = ''.join('e', 't', 'c')
    print(a is b, a == b)

Lo que ha pasado es que hemos usado el operador ``is`` de forma incorrecta. Se usa ``is`` para comparar
las **identidades** de los objetos, mientras que se usa ``==`` para comprobar la **igualdad** de los
objetos. Como en este caso estamos interesados en que ambas cadenas sean iguales (es decir, que
contengan los mismos caracteres), el uso de ``is`` es inadecuado, hay que usar ``==``.

La razón por la que el primer ejemplo parece funcionar bien, es por una funcionalidad de Python: se
internalizan_ la mayoría de las cadenas de
texto. Segun wikipedia:

.. pull-quote::  Interned strings speed up string comparisons, which are sometimes a performance bottleneck in
    applications (such as compilers and dynamic programming language runtimes) that rely heavily on
    hash tables with string keys. Without interning, checking that two different strings are equal
    involves examining every character of both strings. This is slow for several reasons: it is
    inherently O(n) in the length of the strings; it typically requires reads from several regions of
    memory, which take time; and the reads fills up the processor cache, meaning there is less cache
    available for other needs. With interned strings, a simple object identity test suffices after the
    original intern operation; this is typically implemented as a pointer equality test, normally just
    a single machine instruction with no memory reference at all.

Por tanto, cuando se tienen dos cadenas de texto literales (Textos incluidos dentro del código, es
decir, entre comillas) que tienen **el mismo valor**, el interprete de forma automática internaliza
(a veces) el valor, de forma que las dos variables apuntan a la misma posición de memoria. El
problema es que esta operación no se realiza siempre, y la casuistica que decide si se hace o no es
demasiado complicada como para confiar en ella (además, es dependiente de la implementación).

Así que si ejecutamos::

    a = 'etc'
    b = 'etc'
    print(id(a), id(b), id(a) == id(b))

Vemos que ``a`` y ``b`` están realmente apuntando a la misma posición de memoria. Asi que en este caso,
como tienen la misma identidad, el operador ``is`` funciona como esperamos.  Pero si la cadena
de texto se obtiene por otro medio (como en el segundo ejemplo), aunque ambas cadenas
contengan exactamente lo mismo, no funciona, porque son **iguales**, pero no son **la misma**.

Para resumir, ``a is b`` es equivalente a ``id(a) == id(b)``.

En el caso de comparar con ``None``, si es seguro usar ``is``, porque todas las instancias de ``None`` son
en realidad la misma (véase el patrón Singleton)

Como curiosidad, se usa una técnica similar con los números enteros (Véase esta
entrada en la documentación oficial: PyLong_FromLong_). Todos los valores entre
``-5`` y ``256`` están ya generados y almacenados, por lo que cualquier
asignación en este rango va a provocar que se usa la misma posición en memoria.
Pero si salimos del rango, valores iguales se almacenarán en distintas
posiciones de memoria y de nuevo fallaría el uso de ``is``::

    a = 256
    b = 256
    a is b  # returns True

pero::

    a = 1725
    b = 1725
    a is b  # returns False

.. _internalizan: https://en.wikipedia.org/wiki/String_interning
.. _PyLong_FromLong: https://docs.python.org/3.8/c-api/long.html?highlight=integers%20between#c.PyLong_FromLong
