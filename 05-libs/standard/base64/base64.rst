El módulo base64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El proposito de este módulo es proporcionar un sistema que permita codificar
y decodificar información binaria usando solo caracteres ASCII imprimibles. De
esta forma se pueden trasmitir contenidos binarios a traves de sistemas que
solo permitan codificar como texto, como sistemas de correo electronico, ser
parte de los contenidos de una URL. dentro de una peticion POST en la web,
e incluso imprimiendolos en papel.

Se incluyen diversos sistemas, todos ellos definidos en el `RFC 3548`_, conocidos
como **Base16**, **Base32** y **Base64** (Este último es de largo el más
utilizado por ser el más eficiente). También se implementan en esta librería
los estándares de facto **Ascii85** y **Base85**. más raramente usados.


Codificar/Decodificar en base64
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En base64 se usan un subconjunto de ASCII de 65 caracteres, todos ellos
imprimibles. Para la codificación en si se usan 64 de los caracteres, mientras
que el caracter extra, ``=``, se usa para un proposito especial que veremos más
adelante.

Hay dos interfaces disponibles. La interfaz moderna permito codificar variables
que ya estan en formato de bytes. Esto es:

- Objetos de tipo ``byte``
- Objetos de tipo ``bytearray``
- Objetos de tipo ``array.array``
- Objetos de tipo ``memoryview``
- Cualquier objeto que soporte el `protocolo Buffer` y que pueda exportar un 
  buffer de bytes tipo ``C``.

a cadenas imprimibles ASCII. La interfaz antigua solo permitia codificar
ficheros y solo soportaba el protocolo Base64. En esta introducción solo
usaremos la interfaz moderna.


.. index:: b64encode (base64)

Las dos funciones más importantes de este módulo son **b64encode** y
**b64decode**. Veámoslas con un poco más de detalle:

- ``b64encode(s, altchars=None)``: Esta función nos permite codificar en base 64 cualquier
  contenido binario que le pasemos como primer argumento. Devuelve una
  cadena de *bytes* ASCII, imprimible.

  Acepta un parámetro opcional que nos permite alterar parte de la tabla de
  codificacion, de forma que no se usen ni el caracter ``+`` ni el caracter
  ``/`` en la salida (en vez de eso, se usan ``-`` y ``_``). La razón de este
  cambio es poder incluir cadenas codificadas dentro de una URL, donde tanto el
  caracter ``+`` como el ``/`` tienen un significado propio, o evitar
  conflictos con el sistema de ficheros, donde ``/`` también tiene un
  significado propio. Esta codificación (Que, técnicamante no es base64 *puro*)
  se denomina Codificacion Base64 usando alfabeto seguro para URL y sistemas de
  ficheros (*Base 64 Encoding with URL and Filename Safe Alphabet*)


Ejercicio: Codificar la cadena de bytes `Hola, mundo!` usando base64

.. index:: b64decode (base64)

- ``b64decode(s, altchars=None, validate=False)``: Esta función es la inversa
  de la anterior, es decir, acepta una cadena de bytes codificadad en base64
  y nos devuelte el objeto binario inicial. El segundo parámetro es identico
  al de b64encode, permite usar la codificacion alternativa para URLs y 
  sistemas de ficheros.

  Si la codificacion tuviera el error de no estar bien alineada
  (explicaremos esto más adelante) la función elevaría la exceptción
  ``binascii.Error``. 

  Por ultimo, el tercer parámetro, ``validate``, por defecto puesto a
  ``False``, comprueba si los caracteres usados corresponden con la tabla
  de valores permitidos por base64. Copn el valor ``False`` asignado por
  defecto, cualquera de esos valores es simplemente descartado. Sin embargo, si
  se establece a ``True``, la aparicion de cualquier caracter no permitido
  daría lugar a una excepción ``binascii.Error``.


Ejercicio: Decodificar, usando el protocolo base64 puro, el siguiente texto::

    aHR0cHM6Ly90b29scy5pZXRmLm9yZy9odG1sL3JmYzM1NDguaHRtbA==

Notas: Obsérvese que al hablar de codificar o decodificar podría
interpretarse que estamos ante algún tipo de sistema de cifrado, pero
**no** es este el caso. Cualquier contenido codificado en Base64 o cualquiera de
los otros algoritmos implementados en este módulo no necesita ninguna clave
para obtener los contenidos originales. En suma, es solo otra forma de
codificar una información, y en modo alguno una forma de cifrarla o
encriptarla. Todo contenido codificado en base64 (o sus primos) es, a todos los
efectos, pública.


Otras funciones útiles en este múdulo son las siguientes:


- ``standard_b64encode(s)``

    [TODO]

- ``base64.standard_b64decode(s)``

    [TODO]

- ``base64.urlsafe_b64encode(s)``

    [TODO]

- ``base64.urlsafe_b64decode(s)``

    [TODO]

[TODO explicar alineamiento]

[TODO explicar code32 y code16]

[TODO Ejercicio molon]


.. _RFC 3548: https://tools.ietf.org/html/rfc3548.html

.. _protocolo Buffer: https://docs.python.org/3/c-api/buffer.html
