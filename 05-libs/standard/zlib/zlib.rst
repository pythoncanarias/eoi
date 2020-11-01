La librería zlib
----------------

Aunque la capadidad de almacenamiento en los ordenadores sigue
incrementándose, también lo hace la cantidad de detos que queremos
almacenar. Para solucionar esto se inventaron hace tiempo varios
**algoritmos de compresión**, que nos permiten almacenar la misma
cantidad de información en menos espacio, teniendo que usar, eso si,un
poco más de tiempo para acceder o modificar la informacion.

En python, Los módulos ``zlib`` y ``gzip`` nos permiten acceder a estos
dos algoritmos de compresión clásicos, mientras que el modulo ``bzip2``
usa un formato y algoritmo algo mås reciente.

Siempre trabajamos con un flujo de *bytes*, es decir, que podemos
comprimir información en cualquier formato que nos interese, porque los
algoritmos no se preocupan por el formato, solo “ven” secuencias de
bytes.

Los tres módulos incluyen también funciones para trabajar, de forma
transpareente, con ficheros comprimidos.

Ademas de las funciones de compresión, habitualmente se usa también el
concepto de **archivado**, esto es, incluir varios archivos dentro de
otro, normalmente para copias de seguridad o trasmision.

Estos dos conceptos, compresión y archivado no son lo mismo.

-  puedes tener un fichero comprimido, sin archivado (es decir, que solo
   esta comprimido un unico fichero)

-  O se puede tener un archivador sin usar compresión.

-  Pero normalmente estas dos funcionalidades suelen ir juntas.

Nota: En la librería estándar hay módulos para trabajar con otros
formatos de compresión/archivado, como ``tarfile`` para trabajar con
ficheros *.tar*, usados frecuentemente en sistemas tipo Unix, o
``zipfile`` para manipular archivos *.zip*, un formato muy popular en
los entornos Windows desde los tiempos del MS/DOS (Ambos sistemas pueden
encontrarse ya en cualquier entorno, no obstante). En este curso no
veremos estos módulos, pero es importante que sepan que están ahí, en
caso de que los necesiten.

Como siempre, para poder usarlo tenemos que importarlo:

.. code:: ipython3

    import zlib

Podemos comprimir y descomprimir directamente contenidos en memoria. En
el caso de ``zlib``, usamos los métodos **``compress``** y
**``decompress``**. Vamos a verlo ejecutando el siguiente ejemplo.

.. code:: ipython3

    import zlib
    
    message = """
    Hola, me llamo Íñigo Montoya. Tu mataste a mi padre. Preparate a morir
    """.encode("utf-8")
    print(f"El mensaje original ocupa {len(message)} bytes")
    compressed = zlib.compress(message)
    print(f"El mensaje comprimido ocupa {len(compressed)} bytes")


.. parsed-literal::

    El mensaje original ocupa 74 bytes
    El mensaje comprimido ocupa 78 bytes


Ejercicio: ¿Notan algo raro en el ejemplo anterior?

.. figure:: ../img/emosido.jpg
   :alt: El mensaje comprimido ocupa más que el mensaje sin descomprimir

   El mensaje comprimido ocupa más que el mensaje sin descomprimir

Efectivamente ¡El mensaje comprimido ocupa más que el mensaje sin
descomprimir! Justo lo contrario de lo que deberia pasar! Esto es por
varias razones:

-  Los algoritmos de compresión trabajan mejor cuanto mas repeticiones
   de símbolos haya (trabajan reduciendo la redundancia)

-  Cuanto más contenido, mejor compresión (Más probabilidad de encontrar
   redundacia)

Vamos a ver que tal funciona con una supuesta secuencia de genes (Solo
cuatro símbolos, ``G``, ``A``, ``T`` y ``C``):

.. code:: ipython3

    import zlib
    
    message = b"GGAAATGGTAGGGCTAGATGCCCCTTAGCTCATGCGCTGCGCTCATCAAACCTAGGTTATTAGCACTAACAT"
    
    print(f"El mensaje original ocupa {len(message)} bytes")
    compressed = zlib.compress(message)
    print(f"El mensaje comprimido ocupa {len(compressed)} bytes")


.. parsed-literal::

    El mensaje original ocupa 72 bytes
    El mensaje comprimido ocupa 49 bytes


Ejercicio: Descomprimir un mensaje
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hemos recibido el siguiente mensaje, comprimido con ``zlib``:

.. code:: ipython3

    message = b'x\x9c\xf3\xc9WH\xce\xcf+NM/\xcd,.IU\x04\x00,\xcc\x05\xa6'

Usa la función ``decompress`` del modulo ``zlib``.

.. code:: ipython3

    import zlib
    
    message = b'x\x9c\xf3\xc9WH\xce\xcf+NM/\xcd,.IU\x04\x00,\xcc\x05\xa6'
    print(zlib.decompress(message))
    



.. parsed-literal::

    b'Lo conseguiste!'


Compresion/Decompresión incremental
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El problema de comprimir en memoria es que nos limita, porque
necesitamos mantener a la vez los datos comprimidos y sin descomprimir.

Para solucionar esto tenemos las clases ``Compress`` y ``Decompress``
(Que obtentmeos con las llamdas a ``compressobj`` y ``decompressobj``)
que nos permiten trabajar con los datos de forma incremental y con datos
demasiadograndes para caber en memoria. Podemos objener un objeto de la
clase ``Compress`` llamando a la función ``compressobj``.

Este ejemplo lee el contenido de un archivo de texto en pequeños trozos
(de 64 bytes como máximo) y se los pasa al compresor. Como el algoritmo
depende de cálculos realizados en bloques de tamaño fijo, puede que el
compresor no esté listo para devolver la secuencia de salida comprimida,
en ese caso devuelve una cadena vacia (de ahí el ``if`` después de la
llamada a ``compress``)

Cuando ya se han enviado todos los datos, se llama al método ``flush``
para forzar al compresor a terminar con el ultimo bloque y deveolver el
resto de los datos comprimidos.

.. code:: ipython3

    !ls -lah ../lorem.txt



.. parsed-literal::

    -rw-rw-r-- 1 jileon jileon 56K Apr 12  2020 ../lorem.txt


.. code:: ipython3

    import zlib
    
    compressor = zlib.compressobj(wbits=9)
    
    original_size = 0
    compressed_size = 0
    buffer = bytearray()
    filename = "../lorem.txt"
    print(f"Comprimiento fichero {filename}", end=": ")
    with open(filename, 'r') as input:
        while True:
            block = input.read(2048).encode('utf-8')
            if not block:
                break
            original_size += len(block)
            compressed = compressor.compress(block)
            if compressed:
                compressed_size += len(compressed)
                buffer += compressed
                print("█", end="")
            else:
                print("░", end='')
        remaining = compressor.flush()
        compressed_size += len(remaining)
        buffer += remaining
    print("[OK]")
    
    p = round(compressed_size * 100.0 / original_size,2)
    print(f"Fichero {filename} comprimido con tasa de compresion {p:.02f}")
    print("[Tam. original:", original_size)
    print("Tam. comprimido:", compressed_size)


.. parsed-literal::

    Comprimiento fichero ../lorem.txt: █░░░░░░░░░░░█░░░░░░░░░░░█░░[OK]
    Fichero ../lorem.txt comprimido con tasa de compresion 52.55
    [Tam. original: 57060
    Tam. comprimido: 29987


Ejercicio 2: Descomprimir de memoria

El contenido del fichero “lorem.txt” está ahora en memoria, si se ha
ejecutado la calda anterior, en la variable ``buffer``. descomprime el
contenido y muestra las primeras 3 líneas de texto. Puedes usar
``decompress``.

Recuerda que después de descomprimirlo siguen siendo *bytes*, asi que
hay que decodificarlos para obtener texto. Se codifico originalmente con
``utf-8``, asi que hay que usar el mismo esquema para decodificar.

.. code:: ipython3

    import zlib
    
    text = zlib.decompress(buffer).decode('utf-8')
    
    for i, line in enumerate(text.split("\n\n")):
        print(f"linea {i}: \"{line}\"")
        if i == 2: 
            break


.. parsed-literal::

    linea 0: "1. Una reunión muy esperada"
    linea 1: "Cuando el señor Bilbo Bolsón de Bolsón Cerrado anunció que muy pronto celebraría su cumpleaños centésimo decimoprimero con una fiesta de especial magnificencia, hubo muchos comentarios y excitación en Hobbiton. Bilbo era muy rico y muy peculiar y había sido el asombro de la Comarca durante sesenta años, desde su memorable desaparición e inesperado regreso. Las riquezas que había traído de aquellos viajes se habían convertido en leyenda local y era creencia común, contra todo lo que pudieran decir los viejos, que en la colina de Bolsón Cerrado había muchos túneles atiborrados de tesoros. Como si esto no fuera suficiente para darle fama, el prolongado vigor del señor Bolsón era la maravilla de la Comarca. El tiempo pasaba, pero parecía afectarlo muy poco. A los noventa años tenía el mismo aspecto que a los cincuenta. A los noventa y nueve comenzaron a considerarlo «bien conservado», pero «sin cambios» hubiese estado más cerca de la verdad. Había muchos que movían la cabeza pensando que eran demasiadas cosas buenas; parecía injusto que alguien tuviese (en apariencia) una juventud eterna y a la vez (se suponía) bienes inagotables."
    linea 2: "—Tendrá que pagar —decían—. ¡No es natural, y traerá problemas!"


Checksums
~~~~~~~~~

Además de las funciones de compresión y descompresión, se incluyen en
``zlib`` dos funciones para calcular *checksums* de los datos,
``adler32`` y ``crc32``. Ambas funciones estan pensadas para ser usadas
unicamente para propositos de verificacion de datos, ya que no se
consideran seguras desde el punto de vista criptográfico.

.. code:: ipython3

    zlib.crc32(buffer), zlib.adler32(buffer)




.. parsed-literal::

    (3465102946, 136868278)



.. code:: ipython3

    zlib.crc32(buffer)




.. parsed-literal::

    3465102946



.. code:: ipython3

    zlib.crc32(buffer + b"A")




.. parsed-literal::

    1890260921



.. code:: ipython3

    
    buffer2 = buffer + b'a'
    len(buffer), len(buffer2)




.. parsed-literal::

    (29987, 29988)



.. code:: ipython3

    zlib.crc32(buffer2), zlib.crc32(buffer)




.. parsed-literal::

    (1271215985, 3465102946)


