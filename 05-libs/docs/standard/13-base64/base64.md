---
title: El módulo base64
---

### Objetivo de la librería

El propósito de este módulo es proporcionar un sistema que permita codificar y
decodificar información binaria usando **solo carácteres ASCII imprimibles**.

De esta forma se pueden trasmitir contenidos binarios a través de sistemas que
solo permitan texto, como sistemas de correo electrónico, ser parte de los
contenidos de una _URL_ dentro de una petición POST en la web, e incluso impresos
en papel.

Se incluyen diversos sistemas, todos ellos definidos en el 
[RFC 3548](https://tools.ietf.org/html/rfc3548.html), conocidos como **Base16**,
**Base32** y **Base64** (Este último es de largo el más utilizado por ser el
más eficiente).

También se implementan en esta librería los estándares de facto **Ascii85** y
**Base85**, más raramente usados.

### Codificar/Decodificar en base64

En `base64` se usan un subconjunto de ASCII de 65 carácteres, todos ellos
imprimibles. Para la codificación se usan 64 de los carácteres,
mientras que el carácter extra, `=`, se usa para un propósito especial
que veremos más adelante.

Tabla de codificación para `base64`:

|     | $+0$  | $+8$  | $+16$ | $+24$ | $+32$ | $+40$ | $+48$ | $+56$ | 
|-----|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| $0$ | A     | I     | Q     | Y     | g     | o     | w     | 4     |
| $1$ | B     | J     | R     | Z     | h     | p     | x     | 5     |
| $2$ | C     | K     | S     | a     | i     | q     | y     | 6     |
| $3$ | D     | L     | T     | b     | j     | r     | z     | 7     |
| $4$ | E     | M     | U     | c     | k     | s     | 0     | 8     |
| $5$ | F     | N     | V     | d     | l     | t     | 1     | 9     |
| $6$ | G     | O     | W     | e     | m     | u     | 2     | +     |
| $7$ | H     | P     | X     | f     | n     | v     | 3     | /     |

Cada uno de estos 64 símbolos nos permite ahora representar 6 bits ($2^6 = 64$ ). En este esquema `A`
vale `0` y `p`, `41`.

**Pregunta**: ¿Cuánto vale en este esquema la __zeta minúscula__? ¿Y la __U mayúscula__?

Si usamos dos símbolos, tenemos 12 bits ($2^{6+6} = 2^{12} = 4096)$. Al
añadir un tercer símbolo, tenemos 16 bits. Un cuarto símbolo nos pone en 24 bits. Y 24 bits son 
exactamente 3 bytes.

Para codificar en base 64, podemos usar 4 carácteres de nuestros alfabeto para representar 3 bytes.

Veamos un ejemplo, supongamos que desea codificar tres bytes, `42`, `231` y `92`. Si
pasamos estos valores a binario:

| Decimal |    | Binario    |
|---------|:--:|------------|
| `42`    | ≋  | `00101010` | 
| `231`   | ≋  | `11100111` |
| `92`    | ≋  | `01011100` |

concatenamos los tres secuencias de bits nos da:
    
> `001010101110011101011100`

Estos 24 bits pueden ser agrupados ahora en grupos de 6 bits

> `001010` | `101110` | `011101` | `011100`

Cada uno de estos grupos de 6 bits puede ser codificado ahora con un
símbolo de nuestro vocabulario:
    
- `001010` ≋ `10` ≋ `K`
- `101110` ≋ `46` ≋ `u`
- `011101` ≋ `29` ≋ `d`
- `011100` ≋ `28` ≋ `c`

Así que la representación `base64` de los bytes `42`, `231` y `92` sería **`Kudc`**.

**Ejercicio**: Calcular la "sobrecarga" que pagamos por tener nuestro contenido binario en
forma imprimible.

- Pista: Cada 3 bytes de información necesitan 4 símbolos, que al final van a
  necesitar un byte cada uno.

- Pista: Por tanto si 3 bytes se codifican con 4 bytes, entonces 100 bytes se
  codifican con $100 \cdot 4 / 3 = 133.33\overline{3}...$. La sobrecarga sera,
  por tanto de ...

**Solución**: La sobrecarga será aproximadamente de un 33.33%. Es decir, que si
un fichero binario ocupa **8 Mbytes**, el fichero en `base64` ocupará unos **10.6
Mbytes**.

¿Qué pasa si el número de bytes a codificar no es un múltiplo exacto
de tres?

Para eso se añaden bits a cero hasta llegar al siguiente múltiplo de 3, y luego
se usa el carácter especial `=`, (que al principio comentamos que tenía un
significado especial) al final de la cadena como "relleno".

De esa forma siempre se tienen grupos de 4 carácteres, que decodifican a 3
bytes, y usando el número de carácteres `=` al final se puede descartar los
bytes de relleno. Siempre serán uno o dos bytes los que se van a descartar.
¿Por qué?

### Funciones de `base64`

Hay dos interfaces disponibles. La interfaz moderna permite codificar
variables que ya están en formato de bytes. Esto es:

- Objetos de tipo `byte`

- Objetos de tipo `bytearray`

- Objetos de tipo `array.array`

- Objetos de tipo `memoryview`

- Cualquier objeto que soporte el [protocolo Buffer]{.title-ref} y que
  pueda exportar un _buffer_ de bytes tipo `C`.

La interfaz antigua solo permitía codificar ficheros y solo soportaba el
protocolo `Base64`. En esta introducción solo veremos la interfaz moderna.

Las dos funciones más importantes de este módulo son **`b64encode`** y
**`b64decode`**. Vamos a verlas con un poco más de detalle:

### base64.b64encode

__`b64encode(s, altchars=None)`__: Esta función nos permite codificar en base
64 cualquier contenido binario que le pasemos como primer argumento. Devuelve
una cadena de *bytes* ASCII, imprimible.

Acepta un parámetro opcional que nos permite alterar parte de la tabla de
codificación, de forma que no se usen ni el carácter `+` ni el carácter `/` en
la salida (en vez de eso, se usan `-` y `_`).

La razón de este cambio es poder incluir cadenas codificadas dentro de una
_URL_, donde tanto el carácter `+` como el `/` tienen un significado propio,
o evitar conflictos con el sistema de ficheros, donde `/` también tiene un
significado propio.

Esta codificación (Que técnicamente no es `base64` *puro*) se denomina Codificación
Base64 usando alfabeto seguro para URL y sistemas de ficheros (*Base
64 Encoding with URL and Filename Safe Alphabet*)

**Ejercicio**: Usando `base64.b64.encode`, codificar la cadena de bytes `"Hola, mundo!"`.

```python
import base64

texto = b"Hola, mundo!"
print(base64.b64encode(texto))
```

### base64.b64decode

__`b64decode(s, altchars=None, validate=False)`__: Esta función es la inversa
de la anterior, es decir, acepta una cadena de bytes codificada en `base64` y
nos devuelve el objeto binario inicial.

El segundo parámetro es idéntico al de `b64encode`, permite usar la
codificación alternativa para _URLs_ y sistemas de ficheros.

Si la codificación tuviera el error de no estar bien alineada (es decir, que la
longitud del texto no sea múltiplo de 4, como explicamos antes) la función
eleva la excepción `binascii.Error`.

Por ultimo, el tercer parámetro, `validate`, por defecto puesto a `False`,
comprueba si los caracteres usados corresponden con la tabla de valores
permitidos por `base64`. Con el valor `False` asignado por defecto, cualquiera de
esos valores es simplemente descartado. Sin embargo, si se establece a `True`,
la aparición de cualquier carácter no permitido daría lugar a una excepción
`binascii.Error`.

**Ejercicio**: Usar `b64decode` para comprobar el ejemplo de codificación.

Al principio vimos un ejemplo donde codificamos los bytes `42`, `231` y `92`
para obtener la secuencia `Kudc`. Usa la función `b64decode` para comprobar que
nuestro cálculos eran correctos.

```python
import base64

for b in base64.b64decode(b'Kudc'):
    print(b)
```

**Ejercicio**: Decodificar, usando el protocolo `base64` puro, el siguiente
texto:

```
QklFTiBIRUNITywgTUFRVUlOQSE=
```

Solución:

```python
import base64
print(base64.b64decode(b"QklFTiBIRUNITywgTUFRVUlOQSE="))
```

```
b'BIEN HECHO, MAQUINA!'
```

!!! warning
    Obsérvese que al hablar de codificar o decodificar podría interpretarse que
    estamos ante algún tipo de sistema de cifrado, pero este **no es el caso**.

    Cualquier contenido codificado con `base64` o cualquiera de los otros
    algoritmos implementados en este módulo no necesita ninguna clave para
    obtener los contenidos originales.

    En suma, es solo otra forma de codificar una información, y **de ningUna
    manera una forma de cifrarla o encriptarla**. Todo contenido codificado en
    base64 (o sus primos) es, a todos los efectos, pública.

### Otras funciones útiles en este módulo

- `standard_b64encode(s)`: Utiliza la codificación original. Es equivalente a llamar
  a `base64.b64encode` especificando `altchars=None`, pero deja más patente la
  intención del programador.

- `base64.standard_b64decode(s)`: Igual que el anterior, pero para la decodificación. De igual
  manera usar este formula deja más clara la intención así como el protocolo usado.

- `base64.urlsafe_b64encode(s)`: Utiliza la codificación _safe for URL and filenames_. Es
  equivalente a llamar a `base64.b64encode` especificando `altchars="-_"`, pero deja más
  patente la intención del programador.

- `base64.urlsafe_b64decode(s)`: Equivalente a la anterior, pero para decodificar.

### Micro proyecto: Docodificar una imagen codificada con base 64

En HTML, la forma normal de incluir una imagen es usar al atributo `src`
para indicar la URL de una imagen que queremos incluir en nuestra página
web. Veamos un ejemplo:

```html
<img src="https://pythoncanarias.es/static/commons/img/logo_text.png">
```

![Logotipo Python Canarias](https://pythoncanarias.es/static/commons/img/logo_text.png)

Pero existe otra forma, no tan conocida de incluir una imagen *embebida*
dentro del documento, es decir, que está dentro del documento y no necesita
acceder a un recurso externo. Para eso se usa, como atributo `src`, en vez
de una _URL_, el contenido usando la siguiente expresión:

```
data:<tipo mime describiendo el formato>;<codificacion>, <datos>
```

Como los datos son binarios, pero las páginas _HTML_ son texto, hay que indicar
qué tipo de fichero es (No puedes basarte en la extensión del fichero, `.gif`,
`.png`, etc. porque no hay fichero), así como la codificación usada (`base64`
no es la única codificación posible).
    
Por ejemplo, para codificar un fichero en formato _PNG_, codificado en base 64,
usaríamos:

```
data:image/png;base64, GDAdx4...
```
    
Dentro del fichero [imagen.b64.txt](imagen.b64.txt) hay una imagen en formato
GIF (El tipo MIME es `image/gif`) codificado en base 64. Dentro del archivo solo hay
caracteres imprimibles (Compruébalo si quieres).

**Micro proyecto**: Escribe un programa que lea los contenidos codificados en base
64 de ese fichero, los decodifique, y escriba los _bytes_ resultantes dentro de un fichero
llamado `imagen.gif`. Abre ese fichero con un navegador web y comprueba si se
ve una imagen.

Solución:

```python
import base64

with open('imagen.b64.txt', 'r') as entrada:
    with open('image.gif', 'wb') as salida:
        salida.write(base64.b64decode(entrada.read()))
```
