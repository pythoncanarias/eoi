---
title: Antipatrones
---
## Antipatrones

### Usar el \* al importar

Esta forma de importación trae al espacio de nombres en curso todos
aquellos contenidos dentro del módulo (o paquete) que estén listados
dentro de la variable `__all__` del módulo. Si esa variable no está
definida, se importan todos los atributos cuyo nombre no empiece por el
carácter subrayado `_`.

Esta forma de importación está pensada como un atajo cómodo para las
sesiones intereactivas: no debería usarse dentro de un programa.

Mi recomendación es importar siempre módulos, no clases ni funciones ni
otros nombres. Seguir esta regla asegura la claridad y la precisioon, y
evita trampas sutiles que se pueden provocar cuando se importan
"cosas desde un módulo". Por ejemplo, a veces se puede ver código que
hace:

    from datetime import datetime

Esto es confuso para otros programadores, que quizá esperan que
`datetime` sea un módulo, no una clase. En esta caso, además, al
sobreescribir el nombre del módulo, ya no podemos acceder a este.

### Usar el operador `is` en vez de `==`

Encuentre el problema en el siguiente código:

    status = get_status_function()
    if status is not 'ok':
        logging.error('Algo horrible ha pasado')

A veces se usa este patrón por imitación de usar `is` para comparar si
un valor es `None`. En el caso de `None`, y en algunos otros casos
particulares, si es correcto hacerlo así. Pero, en general, para
comparar números, cadenas de texto, etc. siempre hay que utilizar el
operador `==` (o `!=`) en vez de `is` (o `not is`).

Esto es porque el operador `is` compara las **identidades** de los
valores, no los valores en si.

Para ver la diferencia, se puede ajecutar el siguiente código:

    a = 'etc'
    b = 'etc'
    print(a is b, a == b)

Asi que todo parece correcto, pero ejecutemos ahora:

    a = 'etc'
    b = ''.join('e', 't', 'c')
    print(a is b, a == b)

Lo que ha pasado es que hemos usado el operador `is` de forma
incorrecta. Se usa `is` para comparar las **identidades** de los
objetos, mientras que se usa `==` para comprobar la **igualdad** de los
objetos. Como en este caso estamos interesados en que ambas cadenas sean
iguales (es decir, que contengan los mismos caracteres), el uso de `is`
es inadecuado, hay que usar `==`.

La razón por la que el primer ejemplo parece funcionar bien, es por una
funcionalidad de Python: se
[internalizan](https://en.wikipedia.org/wiki/String_interning) la
mayoría de las cadenas de texto. Segun wikipedia:


> Interned strings speed up string comparisons, which are
 sometimes a performance bottleneck in applications (such as compilers and
 dynamic programming language runtimes) that rely heavily on hash tables with
 string keys. Without interning, checking that two different strings are equal
 involves examining every character of both strings. This is slow for several
 reasons: it is inherently O(n) in the length of the strings; it typically
 requires reads from several regions of memory, which take time; and the reads
 fills up the processor cache, meaning there is less cache available for other
 needs. With interned strings, a simple object identity test suffices after the
 original intern operation; this is typically implemented as a pointer equality
 test, normally just a single machine instruction with no memory reference at
 all.

Por tanto, cuando se tienen dos cadenas de texto literales (Textos
incluidos dentro del código, es decir, entre comillas) que tienen **el
mismo valor**, el interprete de forma automática internaliza (a veces)
el valor, de forma que las dos variables apuntan a la misma posición de
memoria. El problema es que esta operación no se realiza siempre, y la
casuistica que decide si se hace o no es demasiado complicada como para
confiar en ella (además, depende de la implementación).

Así que si ejecutamos:

    a = 'etc'
    b = 'etc'
    print(id(a), id(b), id(a) == id(b))

Vemos que `a` y `b` están realmente apuntando a la misma posición de memoria.
En este caso, como tienen la misma identidad, el operador `is` funciona como
esperamos. Pero si la cadena de texto se obtiene por otro medio (como en el
segundo ejemplo), aunque ambas cadenas contengan exactamente lo mismo, no
funciona, porque son **iguales**, pero no son **la misma**.

Para resumir, `a is b` es equivalente a `id(a) == id(b)`.

En el caso de comparar con `None`, si es seguro usar `is`, porque todas
las instancias de `None` son en realidad la misma (véase el [patrón
Singleton](01-singleton.md)).

Como curiosidad, se usa una técnica similar con los números enteros
(Véase esta entrada en la documentación oficial:
[PyLong\_FromLong](https://docs.python.org/3.8/c-api/long.html?highlight=integers%20between#c.PyLong_FromLong)).
Todos los valores entre `-5` y `256` están ya generados y almacenados,
por lo que cualquier asignación en este rango va a provocar que se usa
la misma posición en memoria. Pero si salimos del rango, valores iguales
se almacenarán en distintas posiciones de memoria y de nuevo fallaría el
uso de `is`:

    a = 256
    b = 256
    a is b  # returns True

pero:

    a = 1725
    b = 1725
    a is b  # returns False
