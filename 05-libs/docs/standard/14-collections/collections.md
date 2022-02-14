---
title: El módulo collections - Otras estructuras de datos
---

### Contenido de este módulo

Este módulo implemente ciertos contenedores especializados a partir de los
básicos: Diccionarios, listas, conjunto y tuplas.

### Tupla con nombres (`namedtuple`)

Un objeto de tipo `namedtuple` se comporta como cualquier tupla, pero
su contenido también puede ser accedido por nombre, además de por posición.

Veamos como crear una tupla para unas coordenadas `x` e `y`:

```python
import collections
import math

Point = collections.namedtuple('Point', ["x", "y"])
p = Point(3, 4)

assert p.x == p[0]
assert p.y == p[1]
```

Esto nos permite, por ejemplo, calcular el módulo con esta expresión:

```python
import math

modulo = math.sqrt(p.x ** 2 + p.y ** 2)
```

En vez de:

```python
import math

modulo = math.sqrt(p[0] ** 2 + p[1] ** 2)
```

### Doble cola (`deque`)

Un objeto de la clase ``deque`` implementa una doble lista encadenada, que es
una estructura de datos similar a una lista pero especializada en añadir o quitar
de los extremos con gran rapidez. En contra, las operaciones que no trabajen
con los extremos serán normalmente más lentas que con una lista normal.

Las dobles colas se crean con la función `deque`, a la que le debemos pasar una
secuencia inicial de elementos (Aunque puede estar vacía, simplemente le
pasamos una lista vacía, por ejemplo).

```python
import collection

q = collections.deque([1, 2, 3])
assert len(q) == 3
assert q.pop() == 3
assert len(q) == 2
```

Los métodos `pop` y `append` funcionan en una doble cola igual que en las
listas, pero mucho más rápido. Vamos a usar el módulo `timeit` para poder
apreciar bien la diferencia de velocidad. Evidentemente, con poco elementos el
rendimiento es similar, la diferencia empieza a notarse con mucha actividad o
muchos elementos. Vamos a crear una lista de un millón de elementos, y luego
vamos a retirar el último elemento, con `pop()`, y a continuación lo insertamos
al principio: Vamos a ver el efecto de estas dos operaciones con pocos
elementos:

```python
l = list(range(10))
assert l == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l.insert(0, l.pop())
assert l == [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
l.insert(0, l.pop())
assert l == [8, 9, 0, 1, 2, 3, 4, 5, 6, 7]
```

Esta operación se denomina **rotación**.

Vamos a realizar esta operación sobre una lista de 1 millón de elementos, y
vamos a repetirlo 1.000 veces, para poder tener una estimación relativamente 
bueno del tiempo que total que le lleva a Python realizar todo este trabajo
usando una lista normal:

```python
import timeit

l = list(range(1000000))
timeit.timeit("l.insert(0, l.pop())", number=1000, globals={'l': l})
```

A mi ordenador le ha tomado aproximadamente $1,8384$ segundos realizar todo el
trabajo.

Ahora, si hacemos lo mismo pero usando una doble cola:

```python
import timeit
import collections

q = collections.deque(range(1000000))
timeit.timeit("q.insert(0, q)", number=1000, globals={'q': q})
```

Ahora, en el mismo ordenador y con la misma carga de trabajo, todo el trabajo se
ha realizado en solo $0.0001$ segundos. Una diezmilésima de segundo. La
diferencia es abismal.

En realidad el rendimiento de las listas normales es bastante bueno, el
problema ocurre cuando añadimos elementos a la lista y llega un momento en
tiene que expandirse para poder alojar más elementos. Este proceso se realiza
de forma automática pero consume tiempo, lo que hace que el rendimiento baja. 

Una gran ventaja de las `deque` es que puede ser usadas por diferentes
_threads_ sin ningún problema, ya que están diseñadas especialmente para eso.

Ver ejemplo _threads_.

### Contador (`Counter`)

Un **`Counter`** es un diccionarios especializado en llevar cuentas; asocia a
cada clave un contador y tienen métodos adicionales para este tipo de
estructura de datos. Es equivalente en otros lengajes al concepto de
``multisets``.


```python
import collections

s = ["aaa", "bbb", "cbb", "bcb", "cbb", "aba", "bbb", "zzz", "bbb", "bbb", "bbb"]
d = collections.Counter(s)
d.most_common(3)
d['bbb']
```

**Pregunta**: ¿Cuántas veces aparece la letra `e` en el siguiente texto: 

> Era el mejor de los tiempos, era el peor de los tiempos. La edad de la
> sabiduría, y también de la locura; la época de las creencias y de la
> incredulidad; la era de la luz y de las tinieblas; la primavera de la
> esperanza y el invierno de la desesperación. Todo lo poseíamos, pero
> nada teníamos, íbamos directamente al cielo y nos perdíamos en sentido
> opuesto.

Solución:

```python
d = collections.Counter("""
Era el mejor de los tiempos, era el peor de los tiempos. La edad de la
sabiduría, y también de la locura; la época de las creencias y de la
incredulidad; la era de la luz y de las tinieblas; la primavera de la
esperanza y el invierno de la desesperación. Todo lo poseíamos, pero
nada teníamos, íbamos directamente al cielo y nos perdíamos en sentido
opuesto.
""")
print(d['e'])
```

La salida debería ser `42`.


**Ejercicio**: Contar las 4 palabras más frecuentes del siguiente texto de los Hermanos Mark:

> - Haga el favor de poner atención en la primera cláusula porque es muy
>   importante. Dice que… la parte contratante de la primera parte será
>   considerada como la parte contratante de la primera parte. ¿Qué tal, está
>   muy bien, eh?
> - No, eso no está bien. Quisiera volver a oírlo.
> - Dice que… la parte contratante de la primera parte será considerada como la
>   parte contratante de la primera parte.
> - Esta vez creo que suena mejor.
> - Si quiere se lo leo otra vez.
> - Tan solo la primera parte.
> - ¿Sobre la parte contratante de la primera parte?
> - No, solo la parte de la parte contratante de la primera parte.
> - Oiga, ¿por qué hemos de pelearnos por una tontería como ésta? La cortamos.
> - Sí, es demasiado largo. ¿Qué es lo que nos queda ahora?
> - Dice ahora… la parte contratante de la segunda parte será considerada como
>   la parte contratante de la segunda parte.
> - Eso si que no me gusta nada. Nunca segundas partes fueron buenas.
> - Escuche: ¿por qué no hacemos que la primera parte de la segunda parte
>   contratante sea la segunda parte de la primera parte?

Solución:

```python
import re

def text_to_words(text):
    pat_seps = re.compile("[-\s!?¿+.,;:]+")
    words = (w.strip().lower() for w in pat_seps.split(text))
    return [w for w in words if w]

text = """\
- Haga el favor de poner atención en la primera cláusula porque es muy importante. Dice que… la parte contratante de la primera parte será considerada como la parte contratante de la primera parte. ¿Qué tal, está muy bien, eh?
- No, eso no está bien. Quisiera volver a oírlo.
- Dice que… la parte contratante de la primera parte será considerada como la parte contratante de la primera parte.
- Esta vez creo que suena mejor.
- Si quiere se lo leo otra vez.
- Tan solo la primera parte.
- ¿Sobre la parte contratante de la primera parte?
- No, solo la parte de la parte contratante de la primera parte.
- Oiga, ¿por qué hemos de pelearnos por una tontería como ésta? La cortamos.
- Sí, es demasiado largo. ¿Qué es lo que nos queda ahora?
- Dice ahora… la parte contratante de la segunda parte será considerada como la parte contratante de la segunda parte.
- Eso si que no me gusta nada. Nunca segundas partes fueron buenas.
- Escuche: ¿por qué no hacemos que la primera parte de la segunda parte contratante sea la segunda parte de la primera parte?
"""

words = text_to_words(text)
print(collections.Counter(words).most_common(4))
```

La respuesta debería ser:

- La palabra más frecuente es **la** (24 veces)

- La segunda palabra más frecuente es **parte** (22 veces)

- La tercera palabra más frecuente es **de** (13 veces)

- La cuarta palabra más frecuente es **primera** (10 veces)


### La clase ``OrderedDict``

Los objetos de tipo ``OrderedDict`` son una subclase del diccionario que
recuerda el orden en que se han añadido sus elementos.

!!! warning 
    En python 3 ya no tiene mucho sentido usar esta clase, porque los
    diccionarios normales también tienen la propiedad de mantener internamente
    el orden en que se crean las entradas. Puede ser interesante solo para Python 2 o
    en aquellos casos en que se quiera resaltar que el orden de
    inserción es muy importate.


```python
d = collections.OrderedDict()
d["tres"] = 3
d["uno"] = 1
d["dos"] = 2
for i in d:
    print(i)
```

Salida:

```
tres
uno
dos
```

### La clase ```defaultdict``

Los objetos de tipo ``defaultdict`` son diccionarios, con la única diferencia
de que si se intenta acceder a una clave inexistente, se llama a una función
indicada por nosotros al instanciar el objeto. El resultado de esa función será
el nuevo contenido de la clave.

En el siguiente ejemplo, el diccionario `tribus` es un diccionario que, por
defecto, llamara a la función `list` cada vez que se intente acceder a una
clave que no exista en el diccionario. El resultado de `list`, si lo llamamos
sin ningún parámetro, es una lista vacía.

Cuando intentamos acceder por primera vez a la entrada `suroeste` (en la tercera línea), como
no existe, se llama a `list`, y su resultado, una lista vacía (`[]`) se asigna
a la clave `suroeste`. Por eso, cuando a continuación hacemos un `append` con el
valor `apache`, no se produce ningún error, ya que en ese momento el
contenido de la entrada `suroeste` es una lista.

```python
tribus = collections.defaultdict(list)
assert 'suroeste' not in d
d['suroeste'].append("apache")
d['suroeste'].append("navajo")
d['suroeste'].append("yuma")
assert 'suroeste' in tribus
assert tribus['suroeste'] == ['apache', 'navajo', 'yuma']
assert tribus['noroeste'] == []
```

**Ejercicio**: Implementar un contador (`Counter`) usando `defaultdict`.

Solucion:

```python
d = collections.defaultdict(int)

d['sioux'] += 1
d['osaga'] += 1
d['sioux'] += 1
d['sioux'] += 1
d['osaga'] += 1
d['kansas'] += 1    

assert d['sioux'] == 3
assert d['osaga'] == 2
assert d['kansas'] == 1
assert d['pawne'] == 0
```

### Referencias

- [Python's deque: Implement Efficient Queues and Stacks](https://realpython.com/python-deque/)
