hashlib - hashes y códigos de verificación e integridad
=======================================================

El módulo ``hashlib`` define una interfaz común a una serie de
algoritmos conocidos como *funciones de hash criptográficos* o
*funciones resumen*: SHA1, SHA224, SHA256,  SHA384 y SHA512, así como
el algoritmo MD5 de RSA (Definido como estándar en el RFC 1321).

Su uso en muy sencillo: Por ejemplo, usamos ``md5()`` para crear un
objeto. A partir de ahi, podemos ir actualizando los datos sobre los
que se tienen que hacer el *hash* con sucesivas llamadas a su método
``update()``. Hacer una serie de llamadas sucesivas con partes del
texto es equivalente a hacer un solo ``update()`` con todo el texto
concatenado en un único valor; en otras palabras::

    m.update(a); m.update(b)

es equivalente a::

    m.update(a+b)

Durante cualquier momento del proceso se puede pedir el código de
*hash*. Por ejemplo, para obtener el *hash* criptográfico de la frase
"Su teoría es descabellada, pero no lo suficente para ser correcta.",
podemos hacer::

.. include:: partial_hash.py
   :start: 4

El código obtenido depende de los datos suministrados, de forma que cualquier
alteración, por mínima que sea, en el texto original, provocará una alteración
enorme en el código de salida. Por ejemplo, veamos como cambia el resultado
simplemente cambiando una coma de lugar ::

    >>> from hashlib import md5
    >>> print(md5('Perdón imposible, ejecutar prisionero').hexdigest())
    eafd88022b53be13af86520a6a221024
    >>> print(md5('Perdón, imposible ejecutar prisionero').hexdigest())
    2b4360dbca5fd7b7b5df3fc4af7bab24
