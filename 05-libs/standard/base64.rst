El módulo base64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El proposito de este módulo es proporcionar un sistema que permita codificar
y decodificar información binaria usando solo caracteres ASCII imprimibles. De
esta forma se pueden trasmitir contenidos binarios a traves de sistemas que
solo permitan codificar como texto, como sistemas de correo electronico, ser
parte de los contenidos de una URL. dentro de una peticion POST en la web,
e incluso imprimiendolos en papel.

Se incluyen diversos sistemas, todos ellos definidos en el `RFC 3549`_, conocidos
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

  Por ultimo, el tercer parametro, ``validate``, por defecto puesto a
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



.. _RFC 3594: https://tools.ietf.org/html/rfc3548.html

.. _protocolo Buffer: https://docs.python.org/3/c-api/buffer.html




base64.b64decode(s, altchars=None, validate=False)

    Decode the Base64 encoded bytes-like object or ASCII string s and return the decoded bytes.

    Optional altchars must be a bytes-like object or ASCII string of at least length 2 (additional characters are ignored) which specifies the alternative alphabet used instead of the + and / characters.

    A binascii.Error exception is raised if s is incorrectly padded.

    If validate is False (the default), characters that are neither in the normal base-64 alphabet nor the alternative alphabet are discarded prior to the padding check. If validate is True, these non-alphabet characters in the input result in a binascii.Error.

base64.standard_b64encode(s)

    Encode bytes-like object s using the standard Base64 alphabet and return the encoded bytes.

base64.standard_b64decode(s)

    Decode bytes-like object or ASCII string s using the standard Base64 alphabet and return the decoded bytes.

base64.urlsafe_b64encode(s)

    Encode bytes-like object s using the URL- and filesystem-safe alphabet, which substitutes - instead of + and _ instead of / in the standard Base64 alphabet, and return the encoded bytes. The result can still contain =.

base64.urlsafe_b64decode(s)

    Decode bytes-like object or ASCII string s using the URL- and filesystem-safe alphabet, which substitutes - instead of + and _ instead of / in the standard Base64 alphabet, and return the decoded bytes.

base64.b32encode(s)

    Encode the bytes-like object s using Base32 and return the encoded bytes.

base64.b32decode(s, casefold=False, map01=None)

    Decode the Base32 encoded bytes-like object or ASCII string s and return the decoded bytes.

    Optional casefold is a flag specifying whether a lowercase alphabet is acceptable as input. For security purposes, the default is False.

    RFC 3548 allows for optional mapping of the digit 0 (zero) to the letter O (oh), and for optional mapping of the digit 1 (one) to either the letter I (eye) or letter L (el). The optional argument map01 when not None, specifies which letter the digit 1 should be mapped to (when map01 is not None, the digit 0 is always mapped to the letter O). For security purposes the default is None, so that 0 and 1 are not allowed in the input.

    A binascii.Error is raised if s is incorrectly padded or if there are non-alphabet characters present in the input.

base64.b16encode(s)

    Encode the bytes-like object s using Base16 and return the encoded bytes.

base64.b16decode(s, casefold=False)

    Decode the Base16 encoded bytes-like object or ASCII string s and return the decoded bytes.

    Optional casefold is a flag specifying whether a lowercase alphabet is acceptable as input. For security purposes, the default is False.

    A binascii.Error is raised if s is incorrectly padded or if there are non-alphabet characters present in the input.

base64.a85encode(b, *, foldspaces=False, wrapcol=0, pad=False, adobe=False)

    Encode the bytes-like object b using Ascii85 and return the encoded bytes.

    foldspaces is an optional flag that uses the special short sequence ‘y’ instead of 4 consecutive spaces (ASCII 0x20) as supported by ‘btoa’. This feature is not supported by the “standard” Ascii85 encoding.

    wrapcol controls whether the output should have newline (b'\n') characters added to it. If this is non-zero, each output line will be at most this many characters long.

    pad controls whether the input is padded to a multiple of 4 before encoding. Note that the btoa implementation always pads.

    adobe controls whether the encoded byte sequence is framed with <~ and ~>, which is used by the Adobe implementation.

    New in version 3.4.

base64.a85decode(b, *, foldspaces=False, adobe=False, ignorechars=b' \t\n\r\v')

    Decode the Ascii85 encoded bytes-like object or ASCII string b and return the decoded bytes.

    foldspaces is a flag that specifies whether the ‘y’ short sequence should be accepted as shorthand for 4 consecutive spaces (ASCII 0x20). This feature is not supported by the “standard” Ascii85 encoding.

    adobe controls whether the input sequence is in Adobe Ascii85 format (i.e. is framed with <~ and ~>).

    ignorechars should be a bytes-like object or ASCII string containing characters to ignore from the input. This should only contain whitespace characters, and by default contains all whitespace characters in ASCII.

    New in version 3.4.

base64.b85encode(b, pad=False)

    Encode the bytes-like object b using base85 (as used in e.g. git-style binary diffs) and return the encoded bytes.

    If pad is true, the input is padded with b'\0' so its length is a multiple of 4 bytes before encoding.

    New in version 3.4.

base64.b85decode(b)

    Decode the base85-encoded bytes-like object or ASCII string b and return the decoded bytes. Padding is implicitly removed, if necessary.

    New in version 3.4.

The legacy interface:

base64.decode(input, output)

    Decode the contents of the binary input file and write the resulting binary data to the output file. input and output must be file objects. input will be read until input.readline() returns an empty bytes object.

base64.decodebytes(s)

    Decode the bytes-like object s, which must contain one or more lines of base64 encoded data, and return the decoded bytes.

    New in version 3.1.

base64.decodestring(s)

    Deprecated alias of decodebytes().

    Deprecated since version 3.1.

base64.encode(input, output)

    Encode the contents of the binary input file and write the resulting base64 encoded data to the output file. input and output must be file objects. input will be read until input.read() returns an empty bytes object. encode() inserts a newline character (b'\n') after every 76 bytes of the output, as well as ensuring that the output always ends with a newline, as per RFC 2045 (MIME).

base64.encodebytes(s)

    Encode the bytes-like object s, which can contain arbitrary binary data, and return bytes containing the base64-encoded data, with newlines (b'\n') inserted after every 76 bytes of output, and ensuring that there is a trailing newline, as per RFC 2045 (MIME).

    New in version 3.1.

base64.encodestring(s)

    Deprecated alias of encodebytes().

    Deprecated since version 3.1.

An example usage of the module:
