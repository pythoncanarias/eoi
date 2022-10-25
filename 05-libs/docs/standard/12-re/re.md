---
title: re - Expresiones Regulares
---
## Introducción a `re`

La librería `re` permite trabajar con expresiones regulares.

Vamos a realizar primero un ejercicio para entender la necesidad y utilidad de
las expresiones regulares. Vamos a hacer una función que nos permita
identificar si un texto representa un número de teléfono del tipo
`999-999-9999`, como por ejemplo `354-472-5023`, pero lo vamos a hacer sin usar
expresiones regulares.

Vamos a llamar a nuestra función `is_phone`. Vamos a escribir primero
unos cuantos test:

```python
def test_ok():
    assert is_phone('354-472-4237') is True

def test_bad():
    assert is_phone('tururu') is False
    assert is_phone('tururutururu') is False
    assert is_phone('tur-rut-ruru') is False
    assert is_phone('123-rut-ruru') is False
    assert is_phone('123-456-ruru') is False
    assert is_phone('tur-456-9876') is Fals
```

Veamos una primera implementación:

```python
def is_phone(s):
    if len(s) != 12:
        return False
    if not s[:3].isdigit():
        return False
    if s[3] != '-':
        return False
    if not s[4:7].isdigit():
        return False
    if s[7] != '-':
        return False
    if not s[8:].isdigit():
        return False
    return True
```

Bien, todos los test pasan. ¿Pero y si ahora queremos que se acepten
dos formatos, tanto `354-402-4237` como `(354) 402-4237`? Primero vamos
a añadir un test para este nuevo caso:

```python
def test_ok_alt_format():
    assert is_phone('(354) 472-4237') is True
```

Que nuestro código actual, evidentemente no pasa. Reescribimos `id_phone` para
adaptarlo a este nuevo formato:

```python
def is_phone(s):
    if len(s) == 12:
        if not s[:3].isdigit():
            return False
        if s[3] != '-':
            return False
        if not s[4:7].isdigit():
            return False
        if s[7] != '-':
            return False
        if not s[8:].isdigit():
            return False
        return True
    elif len(s) == 14:
        if s[0] != '(':
            return False
        if not s[1:4].isdigit():
            return False
        if s[4] != ')':
            return False
        if s[5] != ' ':
            return False
        if not s[6:9].isdigit():
            return False
        if s[9] != '-':
            return False
        if not s[10:].isdigit():
            return False
        return True
    return False
```

Ya funciona con el nuevo formato. Pero es mucho código, no especialmente
agradable de leer, y tampoco es sencillo (demasiados `if` y niveles de
anidamiento). Es verdad que podríamos haberlo escrito un poco más corto, pero
no mucho más.

Veremos ahora qué son las expresiones regulares y como podemos usarlas
para implementar todo el código de la función en apenas tres líneas:

```python
def is_phone(s):
    pat_telefono = re.compile(r'\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4}')
    return bool(pat_telefono.match(s))
```

### Cómo usar las expresiones regulares

Una **expresión regular** viene a definir un conjunto de cadenas de texto que
cumplen un determinado patrón. Si una cadena de texto pertenece al conjunto de
posibles cadenas definidas por la expresión, se dice que casan o que ha habido
una coincidencia o *match*.

Veamos como usar las expresiones regulares. Primero tenemos que importar el
modulo re:

```python
import re
```

El siguiente ejemplo usa una expresión regular para encontrar números
dentro de una cadena de texto. No hay que preocuparse ahora de lo que
significa el texto `\d+`, eso lo explicaremos en el resto del tema.
Ahora solo hay que entender como se usan.

Primero, a partir del texto que describe el patrón que queremos buscar, `\d+`
en este caso, llamamos a la función `compile` del módulo `re`, se obtiene un
objeto tipo *pattern* (Patrón). Este objeto está especializado en identificar
el patrón que le hemos pasado. Los objetos *pattern* tienen varios métodos
útiles. De todos ellos vamos a usar `search`, que realiza una búsqueda del
patrón en el texto indicado. Si no lo encuentra, devuelve `None`, pero si lo
encuentra, devuelve un objeto de tipo *match*, que, entre otras cosas, nos
indica donde exactamente dentro del texto se encuentra el _subtexto_ que casa con
el patrón:

```python
import re 

patron = re.compile(r"\d+")

s = "Con 100 cañones por banda..."
match = patron.search(s)
if match:
    print('Encontrado', match)
else:
    print('No encontrado')
```

Que produce:

```shell
Encontrado <re.Match object; span=(4, 7), match='100'>
```

!!! note

    No es estríctamente obligatorio usar la función `compile`. Podemos usar una
    función `search`, definida en `re`, a la que le pasamos dos parámetros, el
    primero la cadena de texto que describe la expresión regular, y el segundo
    el texto a buscar. Internamente la función creará el objeto patrón. Yo
    recomiendo compilar primero, porque es más eficiente y de esa forma podemos
    reutilizar el patrón en diferentes sitios.

    Este sería el código del ejemplo usando la función `search` en vez del
    método `search`:

    ```python
        import re

        s = "Con 100 cañones por banda..."
        match = re.search(r"\d+", s)
        if match:
            print('Encontrado', match)
        else:
            print('No encontrado')
    ```

### Cómo definir expresiones regulares

Las expresiones regulares se crean a partir de una cadena de texto en la que
combinamos diferentes expresiones regulares primitivas, combinándolas para
producir expresiones regulares más complejas..

La cadena de texto que define la expresión regular puede incluir **caracteres
normales** o **especiales**. Los caracteres normales solo casan literalmente
consigo mismo. Por ejemplo, la expresión regular `a` solo casa con una `a`.
Los especiales, como `+` o `.` tienen significados diferentes, especiales, que
veremos con más detalle durante este tema.

Algunos de estos caracteres con significados especiales son:

| carácter | Significado |
|----------|-------------|
| `.`      | carácter punto. Casa con cualquier carácter |
| `^`      | Casa con el principio de una _string_ |
| `$`      | Casa con el final de una _string_ |
| `*`      | La expresión regular anterior, repetida 0 o más veces |
| `+`      | La expresión regular anterior, repetida 1 o más veces |
| `?`      | La expresión regular anterior, una o ninguna vez |
| `{n}`    | La expresión regular anterior, repetida _n_ veces |
| `{m,n}`  | La expresión regular anterior, repetida entre _m_ y _n_ veces |
| `\`      | "Escapa" el significado del carácter a continuación, permitiendo así incluir caracteres especiales como `{` o `*` literales. |
| `|`      | Alternancia entre patrones: `A|B` significa que casa con el patrón `A` o con el patrón `B`. Se pueden usar múltiples patrones separados con `|` |
| `[]`     | Sirve para indicar un conjunto de caracteres |


### Resultado de buscar patrones en un texto

Como se explicó antes, el resultado de la función depende de si ha encontrado o
no alguna ocurrencia del patrón en el texto. Si la encontró, se devuelve un
objeto de tipo `Match` (que es un objeto que almacena la información de donde
se ha encontrado). Si no lo encuentra, devuelve `None`.

Entra la información que podemos encontrar en este objeto `Match`, se incluye
el texto que ha encontrado, la expresión regular utilizada y la localización,
dentro del texto buscado, de esa coincidencia.

Veamos un ejemplo, usando como expresión regular `este`. Como en esta expresión
solo hay caracteres normales, se interpreta como esa secuencia de caracteres
literalmente: "Una `e`, seguida de una `s`, seguida de una `t`, seguida de 
una `e`":

```python
import re

pattern = re.compile(r'este')
text = 'Contiene este texto el patrón?'
match = pattern.search(text)
if match:
    print(
        f"Encontrado <{match.group(0)}>"
        f" entre las posiciones {match.start()}"
        f" y {match.end()}"
    )
```

Que produce como resultado:

```shell
Encontrado <este> entre las posiciones 9 y 13
```

**Ejercicio**: Modificar el código previo para que encuentre la palabra
"texto".

En principio, nada que no pudiéramos hacer usando el método `index` de las
cadenas de texto, pero la potencia de las expresiones regulares reside en los
caracteres especiales.

Los veremos ahora con más detalle.

### Los caracteres especiales Corchetes `[` y `]`

Estos caracteres se usan para definir un conjunto de caracteres, de forma que
cualquiera de ellos se acepta como una ocurrencia. El conjunto de los
caracteres se pueden listar individualmente, como por ejemplo, `[abc]`, que
casa con cualquiera de los caracteres `a`, `b` o `c`. Otro ejemplo: `[aeiuo]`
es un patrón que se interpreta como "cualquier vocal". Otro uso muy frecuente
sería `[0123456789]`, que se interpreta como "cualquier dígito".

Se acepta también una forma abreviada que nos permite incluir un rango, usando
el carácter `-`. Por ejemplo, el patrón `[0123456789]` se puede abreviar como
`[0-9]`. El patrón `[0-9A-F]` casa con cualquier dígito y con las letras
`A`, `B`, `C`, `D`, `E` y `F`.

Los caracteres especiales pierden su significado dentro de los
corchetes, por lo que no hace falta escaparlos.

Se puede definir **el complemento del conjunto** incluyendo como primer
carácter `^`. De esta forma, la expresión regular `[^59]` casa con cualquier
carácter, excepto con los dígitos `5` ó `9`.

### El carácter especial interrogación `?`

El carácter especial `?` opera de una forma curiosa. Se debe interpretar como
"El patrón que me precede, 0 o 1 vez". Por ejemplo, el patrón `este?` sería:
"El patrón que me precede (En este caso el literal `e`), cero o una vez". Casa
tanto con la cadena `est` como con la cadena `este`.  Otra forma de leerlo es
"opcionalmente, puede venir el patrón anterior".

### El carácter especial punto `.`

El punto es un carácter especial, por lo que tiene un significado diferente de
"debe ser un punto". En una expresión regular, el carácter `.` significa
"cualquier carácter", es decir, es un comodín, para caracteres. Pero atención,
que solo casa con un único carácter.

Por ejemplo, el patrón regular `est.` casa con `este`, `esta`, `estx`, `est8`,
`est@`, pero no con `est`, porque espera un cuarto carácter, el que sea, pero
no encuentra ninguno.

Podemos combinar las dos expresiones anteriores. Por ejemplo en la expresión
`est.?`, la interrogación se refiere siempre, como vimos antes, a la expresión
regular anterior, que en este caso es el `.` o comodín, de forma que toda la
expresión debe entenderse como "Una `e`, seguida de una `s`, seguida de una
`t`, y luego puede que venga, o no, un carácter cualquiera". En este caso
casaría con `este`, `esta`, `estx`, `est8`, `est@`, etc. pero también con
`est`.

**Ejercicio**: Dado el siguiente código:

```python
import re

pattern = re.compile('te.to')
text = 'Contiene este texto el patrón?'

match = pattern.search(text)
if match:
    print(
        f"Encontrado <{match.group(0)}>"
        f" entre las posiciones {match.start()}"
        f" y {match.end()}"
    )
```

1) Cambiar la variable `text` del programa anterior por "Contiene este
teZto el patrón?". Verificar que sigue encontrado el
patrón.

2) Cambiar la variable `text` por "Contiene este teZXto el
patrón?". ¿Encuentra ahora el patrón? ¿Por qué?

### El carácter especial Asterisco `*`

El carácter especial `*` debe interpretarse como "El patrón anterior,
repetido 0 o más veces". Por ejemplo, el patrón `e*` casa con la
cadena vacía (Ninguna aparición del carácter `e`), con `e` (Una
repetición del carácter 'e'), con `ee` (Dos repeticiones), `eee` (Tres
repeticiones), etc.

Una combinación muy habitual es el patrón `.*`. Esto se interpreta como "Cero o
más repeticiones de la expresión regular que esta justo antes, que en este caso
es cualquier carácter", o lo que es lo mismo, "cualquier carácter, repetido 0 o
más veces". Aun más resumido: "Todo".

Por ejemplo, la expresión regular `BEGIN .* END` sería: "Todo lo que
haya entre la palabra BEGIN (en mayúsculas y seguida de un espacio, ojo a eso)
y `END`:

```python
import re

pattern = re.compile(r'BEGIN .* END')
text = 'BEGIN Cualquier cosa que pongamos aqui vale END'

match = pattern.search(text)
if match:
    print(
        f"Encontrado <{match.group(0)}>"
        f" entre las posiciones {match.start()}"
        f" y {match.end()}"
    )
```

**Ejercicio**: Cambiar el texto entre `BEGIN` y `END`. Ver que cualquier
cosa que ponemos vale.

Veamos el siguiente ejemplo, usando como expresión regular `<.*>`. En
lenguaje natural, lo que quier decir es "cualquier texto, inclusive un
texto vacío, delimitado por los caracteres `<` a la izquierda y `>` a la
derecha":

```python
import re
p = re.compile("<.*>")
s = "<p>Hola mundo soy <b>pepe Garcia</b> tu amigo</p>"
p.findall(s)
```

Resultado:

```
['<p>Hola mundo soy <b>pepe Garcia</b> tu amigo</p>']
```

Con este operador y con el siguiente se produce una ambigüedad, que veremos con
un ejemplo. Supongamos que quiero todo el texto comprendido entre los
caracteres `<` y `>`. La expresión regular sería `<.*>`, hasta aquí todo bien.
Pero ¿qué pasa si buscamos ese patrón en el siguiente texto?:

```
Hola <empieza aqui pero termina en el primer > o en el último >
```

¿Debería devolver el fragmento de texto más pequeño?:

```
<empieza aqui pero termina en el primer >
```

¿O el más grande?:

```
<empieza aqui pero termina en el primer > o en el último >
```

Después de todo, ambos fragmentos cumplen con lo expresado en la expresión
regular: "Un símbolo `<`, luego lo que sea y al final un símbolo `>`". Los
informáticos odiamos la ambigüedad; en este caso se resuelve haciendo que por
defecto, el buscador de la expresión regular intente darnos **la mayor cantidad
posible de texto**. Esto se conoce como modo avaricioso o *Greedy*.

Podemos indicar que queremos el comportamiento contrario, esto es, que nos de
la menor cantidad posible de texto (o modo *non greedy*) añadiendo un carácter
`?` después del asterisco. Veamos el siguiente ejemplo:

```python
import re

pat_greedy = re.compile(r'<.*>')
pat_non_greedy = re.compile(r'<.*?>')

text = 'Hola <empieza aqui pero termina en el primer > o en el último >'

match = pat_grLos veremos ahora con más detalle.eedy.search(text)
if match:
    print(f"En modo greedy encontró: {match.group(0)}")
match = pat_non_greedy.search(text)
if match:
    print(f"En modo non-greedy encontró: {match.group(0)}")
```

Cuya salida debería ser:

```shell
En modo greedy encontró: <empieza aqui pero termina en el primer > o en el último >
En modo non-greedy encontró: <empieza aqui pero termina en el primer >
```

### El carácter especial Suma o Más `+`

Similar a `*`, el carácter especial `+` se interpreta como "El patrón
anterior, repetido 1 o más veces\". Por ejemplo, el patrón `e+` no
casaría con la cadena vacía (Ninguna aparición del carácter `e`, ya que
requerimos al menos una), pero si casaría con `e` (Una repetición de
'e'), con `ee` (Dos repeticiones), `eee` (Tres repeticiones), etc.

Una combinación muy habitual es el patrón `.+`. Esto se leería como
"Una o más repeticiones de la expresión regular que esta justo antes,
que en este caso es cualquier carácter", o lo que el lo mismo,
"cualquier carácter, repetido 1 o mas veces". Aun más resumido:
"Todo, menos la cadena vacía".

De igual forma, por defecto se comporta en modo **greedy** y se puede
cambiar a **non greedy** con el sufijo ?.

### El carácter especial Barra Vertical o Tubería `|`

Se usa en la forma `A|B`, donde `A` y `B` representan expresiones regulares, y
se interpretan como una expresión regular que acepta cualquiera de las dos, es
decir, que casará con cualquier texto que case con `A` o con `B`. Es muy
habitual su uso con los grupos, que veremos más adelante.

Se pueden encadenar. Por ejemplo, el siguiente patrón:

```
este|ese|aquel
```

Casa con cualquier de esas palabras.  Otro ejemplo:

```
pat_psoe = re.compile('PSOE|Partido Socialista Obrero Español')
```

### El carácter especial Acento Circunflejo `^`

El carácter especial `^` se interpreta como "Al principio del texto". Sirve
para buscar textos que empiezan por la expresión regular que venga después.
Por ejemplo, el patrón regular`\^Carthago`solo casaría con un texto que empiece
con la palabra`Carthago`.

**Pregunta**: ¿Tiene sentido que el carácter especial `^`se use en una
expresión regular en otro sitio que no sea al principio? ¿Por qué?

### El carácter especial Dolar `$`

Es el inverso del anterior, este carácter especial se interpreta como "Al final
del texto". Sirve para buscar textos que termina por la expresión regular que
viene justo antes.  Por ejemplo, el patrón regular `Delenda est$` solo casaría
con un texto que termine con las palabras`Delenda est`.

**Pregunta**: ¿Tiene sentido usar el carácter especial `$` en otro sitio que no
sea al final? ¿Por qué?

### Los caracteres especiales Llaves `{` y `}`

Estos caracteres nos permiten especificar el número de veces que se debe
repetir la expresión regular precedente, o definir un rango de repeticiones
válido.  Por ejemplo,`[0-9]{4}`se leería "Cualquier dígito, repetido 4 veces",
o sea que `3622` casa, pero `231` no. El texto `56423` si lo haría, pero solo
los primeros cuatro dígitos, es decir, detectaría `5642`, quedando el`3`fuera.
Si cambiáramos el patrón a `[0-9]{3,4}` se leería "Cualquier dígito, repetido 3
o 4 veces", o esa que `3622` casa, y `231` también, pero `75` no, le falta un
dígito.

**Pregunta**: Como escribirías el patrón para que acepte 2, 3, o 4 dígitos.

**Ejercicio**: Escribir el patrón para encontrar posibles NIF: La regla
(simplificada) sería una secuencia de 7 a 8 dígitos, seguidos de una letra
mayúscula. A modo de ayuda veamos algunos valores que casan con el patrón y
otros que no:

| Texto        | Correcto o incorrecto      |
|--------------|----------------------------|
| `43478329W`  | Correcto                   |
| `434783294W` | Demasiados dígitos         |
| `434783W`    | Pocos dígitos              |
| `43783294`   | Falta la letra             |
| `W33783294`  | Letra en lugar incorrecto  |


### El carácter especial Barra Invertida `\`

El propósito de este carácter especial es doble: Si precede a otro carácter
especial, entonces reconvierte a dicho carácter de especial a normal (Se dice
que escapa el significado del carácter). Esto permite buscar caracteres como
`*`, `[` o `?` de forma literal.

![Doctor Who!](doctor-who.jpg)

Por ejemplo, la expresión `Doctor Who\?` busca literalmente el texto `Doctor
Who?`. Si no escapáramos la interrogación (Es decir, si se usara `Doctor
Who?`), se interpretaría como que la última `o` es opcional, y casaría, por
ejemplo, con `Doctor Wh`, que no es lo que queremos.

El segundo uso es introducir una **secuencia especial**, que explicaremos a
continuación.

!!! warning

    Importante: Recordemos que Python también usa el carácter `\` como su
    propia forma de escapar significados (por ejemplo `\n` es la forma de
    representar un salto de línea). Así que para incluir la barra invertida
    tendriamos que escribirla dos veces. Es por eso que siempre se
    recomiendo usar cadenas de texto `raw` (con una `r` antes de la primera
    comilla).

    Define siempre tus expresiones regulares con cadenas de texto crudas o
    *raw*. Algunos verificadores de código o *linters* incluso disparan una
    alerta si no se hace.

Algunas de las secuencias especiales accesible con `\` son:

- `\b` coincide con una cadena vacía, pero solo al principio de una palabra

- `\B` coincide con una cadena vacía, pero solo si **no** está al principio de
  una palabra. Esto significa que `py\B` casará con `python`, `py3`, `py2`,
  pero no con `py`, `py.` o `py!`. `\B` es el opuesto de `\b`. Veremos esta
  pauta repetida en otras secuencias especiales.

- `\d`: casa con cualquier dígito. Equivalente a `[0-9]`

- `\D`: casa con cualquier carácter que **no** sea un dígito. Equivale a
  `[^0-9]`

- `\s`: Casa con espacios y otros caracteres equivalentes, como tabuladores,
  saltos de linea, etc.

- `\S`: Casa con cualquier cosa que no sean espacios. El opuesto de `\s`

- `\w`: Caracteres que pueden ser partes de una palabra en cualquier lenguaje,
  así como los dígitos del 0 al 9 y el carácter `_`. Equivale a `[a-zA-Z0-9_]`

### Los caracteres especial Paréntesis `(` y `)` (Grupos)

Sirven para indicar el principio y el fin de un grupo. No modifican la
expresión regular, en el sentido que esta sigue casando exactamente igual con
paréntesis o sin ellos, pero sirven para que podamos recuperar, después de una
coincidencia o _match_, los contenidos de estos grupos.

Por ejemplo, supongamos que queremos buscar por indicadores de tareas al estilo
de Jira, que se forman con la estructura: Código de proyecto seguido de un
guión y seguido del numero de tarea. Algunos indicadores válidos podrían ser
`ALPH-1244` o `BE-123`. Supongamos para simplificar que los códigos de proyecto
son siempre letras mayúsculas, el patrón que detecta estos códigos podría ser:

```
[A-Z]+-\d+
```

Comprobemos si funciona:

```python
import re

patron = re.compile(r"[A-Z]+-\d+")
for codigo in ["ALPH-1244", "BEMAC-123", "MZGZ-1", "COVID-12"]:
    if patron.match(codigo):
        print(f"Codigo {codigo} es correcto")
```

Que debería producir el siguiente resultado:

```shell
Codigo ALPH-1244 es correcto
Codigo BEMAC-123 es correcto
Codigo MZGZ-1 es correcto
Codigo COVID-12 es correcto
```

Ahora, si quisiéramos acceder solo al número de la tarea, la forma más
fácil es usar los paréntesis para crear los grupos que nos interesan.

Para ello, cambiamos el patrón de:

```
[A-Z]+-\d+
```

a:

```
[A-Z]+-(\d+)
```

El patrón se comporta exactamente igual que antes, pero los objetos *match*
resultantes de una coincidencia permiten ahora acceder a los grupos definidos
usando los paréntesis. Para ello se usa método `group`, indicando el número de
orden de definición del grupo, siendo el grupo 1 el primer grupo definido.

También se puede usar el grupo 0, y lo hemos utilizado en algún ejemplo
anterior. Este grupo cero está definido siempre y consiste en la totalidad del
texto que haya casado con el patrón. Observa que fácil es ahora conseguir
solo el código del proyecto y el número de la tarea, habiéndolos agrupado
previamente:

```python
import re

patron = re.compile(r"([A-Z]+)-(\d+)")
for codigo in ["ALPH-1244", "BEMAC-123", "MZGZ-1", "COVID-12"]:
    m = patron.match(codigo)
    if m:
        proyecto = m.group(1)
        task_number = int(m.group(2))
        print(f"{m.group(0)}: Tarea número {task_number} del proyecto {proyecto}")
```

Cuya salida debería ser:

```shell
ALPH-1244: Tarea número 1244 del proyecto ALPH
BEMAC-123: Tarea número 123 del proyecto BEMAC
MZGZ-1: Tarea número 1 del proyecto MZGZ
COVID-12: Tarea número 12 del proyecto COVID
```

### El método `split`

Con este método podemos dividir una cadena de texto, usando una expresión
regular para determinas los puntos de corte. Los separadores en si normalmente
no se devuelven, pero podemos forzar a que se incluyan si los agrupamos con
paréntesis.

El siguiente ejemplo muestra como podemos dividir un formato de fecha que
utiliza como separador tanto la barra normal inclinada `/`, la barra invertida
`\`, la barra vertical `|` o el guión:

```python
import re

pat_sep = re.compile(r"[-\\|/]")
print(pat_sep.split("2020-10-19"))
print(pat_sep.split("2020/10/19"))
print(pat_sep.split("2020\\10\\19"))
print(pat_sep.split("2020|10|19"))
```

Que debería producir la siguiente salida:

```shell
['2020', '10', '19']
['2020', '10', '19']
['2020', '10', '19']
['2020', '10', '19']
```

**Ejercicio**: Expresiones regulares para encontrar matrículas de coche.

Escribir una expresión regular para detectar matrículas de coches españolas.

Según el siguiente texto, que describen en el sistema de matriculación vigente
actualmente en España:

> El 18 de septiembre del año 2000 entró en vigor el nuevo sistema de
> matriculación en España, introduciendo matrículas que constan de cuatro
> dígitos y tres letras consonantes, suprimiéndose las cinco vocales y las
> letras Ñ, Q, CH y LL. [...] Si el vehículo es histórico, y se ha matriculado
> con una placa de nuevo formato, aparece primero una letra H en la placa.

Escribir un programa que detecte y liste las matrículas en el siguiente
texto:

```
INSTRUIDO por accidente de circulación ocurrido a las 09:43 entre la
motocicleta HONDA 500, matrícula 0765-BBC  y la motocicleta HARLEY-DAVIDSON ,
matrícula 9866-LPX, en el punto kilométrico 3.5 de la carretera general del
sur, término municipal de ...
```

**Solución**:

Un posible patrón podría ser el siguiente:

```
H?\d{4}-?[BCDFGHJKLMNPRSTVWXYZ]{3}
```

Es verdad que visto así puede asustar un poco, pero solo es cuestión de verlo
por por partes:

- `H?` : Una `H`. Pero como la sigue una interrogación, es opcional.  Recuerda
  que `?` se interpreta como la expresión regular anterior (en este caso la
  `H`), 0 o 1 vez.

- `\d{4}` : El conjunto de los caracteres del 0 al 9 (`[0-9]`), o lo que es lo
  mismo, cualquier dígito, repetido 4 veces (`{4}`), es decir, un número de
  cuatro dígitos.

- `-?` : Un guión, opcional, igual que la `H` para vehículos históricos del
  principio.

- `[BCDFGHJKLMNPRSTVWXYZ]{3}` : Cualquiera de los caracteres del conjunto
  indicado (letras consonantes excepto la `Ñ`, `Q`, `CH` y `LL`), repetido 3
  veces.

Un truco que podemos usar con las expresiones para que a la hora de escribirlas
y leerlas sean más sencillas es usar un parámetro opcional a la hora de
compilar, con el que podemos indicarle que, en el texto que define la expresión
regular, deben ignorarse los espacios (a no ser que se escapen) y los saltos de
linea, y que incluso podemos comentar la expresión regular con el carácter `#`;
todo lo que escribamos a partir de este carácter y hasta el final de la línea
actual será ignorado y no formara parte del patrón.

Así, usando esta constante `re.VERBOSE` como segundo parámetro, podemos
escribir la expresión regular del ejercicio anterior como:

```python
import re 

pat_matricula = re.compile("""
    H?  # La letra H, opcional, se reserva para vehículos históricos
    \d{4}  # Los cuatro dígitos de la matrícula
    -?  # Un guión, opcional. Es decir, aceptamos 0765-BBC o 0765BBC
    [BCDFGHJKLMNPRSTVWXYZ]{3}  # Las cuatro letras, del conjunto de posibles
    """, re.VERBOSE)

assert pat_matricula.match("0765-BBC")
assert pat_matricula.match("9866-LPX")
assert pat_matricula.match("probóscide") is None
```

### El método `sub`

Muchas veces, de lo que se trata es de buscar una texto que siga un patrón y
reemplazarlo por otro. Los objetos `Pattern` tienen un método para realizar
estos cambios de forma sencilla y potente. El método `sub` necesita al menos
dos parámetros, el primero es aquello que queremos poner como sustitución de lo
encontrado por el patrón, y luego el texto sobre el que ejecutar la
transformación. Devuelve el texto transformado.

El segundo parámetro puede ser simplemente el texto que queremos que
sustituya el original. Por ejemplo, el siguiente código reemplaza todas
las vocales por asteriscos:

```python
import re

pat = re.compile(r"[aeiouáéíúóú]", re.IGNORECASE)
texto = "El lémur de cola Anillada (Lemur catta) es un gran prosimio"

print(pat.sub("_", texto))
_l l_m_r d_ c_l_ _n_ll_d_ (L_m_r c_tt_) _s _n gr_n pr_s_m__
```

Pero el segundo parámetro también puede ser una función. A esta función se le
pasa el objeto `match` y debe retornar una cadena de texto. Cualquiera que sea
el resultado será ese el texto que sustituirá el texto original. Esta es una
opción muy potente y con la que es muy fácil cambiar un texto a modo _burleta_,
usando la ayuda de `random`:

```python
import re
import random

pat = re.compile(r"[aeiou]")
texto = "Te he dicho mil veces que no me remedes"

def una_vocal_al_azar(match):
    return random.choice('aeiou')

print(pat.sub(una_vocal_al_azar, texto))
```

Que mostraría algo así como:

```
Ta hu decho mol vaces qua nu mu remudos
```

En este caso no hacemos nada con el objeto `match` pasado a la función,
pero en este segundo ejemplo buscamos números en coma flotante y los
reemplazamos por la fracción equivalente, usando la clase `Fraction`
incluida en el módulo `fractions`:

```python
from fractions import Fraction
import re

pat_decimal = re.compile(r'\d+\.\d+')

def as_fracciones(match):
    num = float(match.group(0))
    f = Fraction(num)
    if f.denominator == 1:
        return str(f.numerator)
    else:
        return f"{f.numerator}/{f.denominator}"

text = f"La suma de 0.25 y 0.25 da como resultado {0.25+0.25}"
print(pat_decimal.sub(as_fracciones, text))
```

Lo que daría como resultado:

```
La suma de 1/4 y 1/4 da como resultado 1/2
```

Podemos, por tanto, realizar cambios dinámicos, basándonos en los textos
encontrado o en cualquier otro dato. En el siguiente ejemplo, más complejo, se
extraen y numeran las notas que encuentre un texto, suponiendo que todas las
notas siguen el formato `NOTA: <lo que sea>.`:

```python
import re

pat_nota = re.compile(r'NOTA: (.+?)\.', re.DOTALL|re.MULTILINE)

counter = 0
notas = []

def numera_notas(match):
    global counter, notas
    counter += 1
    texto_nota = match.group(1).replace('\n', ' ').capitalize()
    notas.append(texto_nota)
    return f"(Véase Nota #{counter})."

text = """
    Indiana es uno de los cincuenta estados de los Estados Unidos NOTA: localizado
    en la región del Medio Oeste (Midwest) del país. Su capital es 
    Indianápolis NOTA: su población es de 829 718 hab. Limita al norte con el lago 
    y el estado de Míchigan, al sur con Kentucky, al este con Ohio y
    con Illinois por el oeste NOTA: cubierta en su mayor parte por llanuras. La 
    palabra Indiana significa «tierras de los indios».
    """

print(pat_nota.sub(numera_notas, text))
for num, nota in enumerate(notas, start=1):
    print(f"- Nota {num}: {nota}")
```

Que produce este resultado:

```
Indiana es uno de los cincuenta estados de los Estados Unidos (Véase Nota #1). Su capital es 
Indianápolis (Véase Nota #2). Limita al norte con el lago 
y el estado de Míchigan, al sur con Kentucky, al este con Ohio y
con Illinois por el oeste (Véase Nota #3). La 
palabra Indiana significa «tierras de los indios».

- Nota 1: Localizado en la región del medio oeste (midwest) del país
- Nota 2: Su población es de 829 718 hab
- Nota 3: Cubierta en su mayor parte por llanuras
```

**Ejercicio:** Buscar en la documentación oficial de Python del módulo
`re` el significado de las opciones `DOTALL` y `MULTILINE`.

**Pregunta:** ¿Qué hace el siguiente programa?:

```python
import os
import re

pat_notebook = re.compile("^[abc].*\.py$")
for files in os.listdir("."):
    if pat_notebook.search(fn):
        print(fn)
```

Hay más cosas que podemos hacer con expresiones regulares, consulta la
[documentación oficial sobre el módulo
re](https://docs.python.org/es/3/library/re.html).
