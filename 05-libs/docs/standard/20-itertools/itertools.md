---
title: El módulo itertools
---

### Contenido del módulo

**`itertools`** implementa una serie de funciones para trabajar con iteradores
o secuencias como elementos básicos. Muchas de estas funciones están inspiradas
por distintas construcciones que podemos encontrar en otros lenguajes como _APL_,
_Haskell_ o _SML_.

Estas utilidades cuentan con la ventaja de ser parte de la librería estándar,
además de ser eficientes y rápidas, al estar implementadas a bajo nivel. Con
estas utilidades se puede formar una especie de *álgebra de iteradores* que
permite construir herramientas más especializadas de forma concisa y eficiente.

Algunas de las funciones de este módulo son:

- `count`
- `cycle`
- `chain`
- `groupby`
- `product`
- `combinations`
- `tee`

### La función `count`

- `count(start, [step])`

La función **count** produce un iterador infinito. Devuelve una cuenta,
empezando por `start` en la primera llamada y cada siguiente invocación con el
valor incrementado por el parámetro opcional `step` (por omisión, 1):


```python
import itertools

for i in itertools.count(10, -1):
    print(i)
    if i == 0:
        break
```

### La función `cycle`

La función **cycle** (`cycle(s)`) es otro iterador infinito. Empieza
devolviendo los elementos de la secuencia `s`, y cuando termina, vuelve a
empezar:


```python
import itertools

colors = itertools.cycle(['red', 'green', 'blue'])
for i in range(7):
    print(next(colors))
```

### La función `chain`

- `chain(s1, s2, ... ,sn)`

**`chain`** Encadena una secuencia detrás de otra:


```python
import itertools

letras = itertools.chain('ABC', 'DEF')
for letra in letras:
    print(letra)
```

### La función `group_by`

- `groupby(s, f)`

Agrupa los elementos de una secuencia `s`, por el procedimiento de aplicar la
función `f` a cada elemento, asignado al mismo grupo a aquellos elementos que
devuelven el mismo resultado.
    
El resultado es otro iterador, que retorna **duplas** (tuplas de dos
elementos). El primer elemento es el resultado de la función, el segundo, un
iterador de elementos correspondientes a ese resultado / grupo.

Si la secuencia no viene ordenada según el criterio de agrupación, es posible
que se devuelvan varias duplas para un mismo valor del resultado de la función.
En el siguiente ejemplo se puede ver más claro:

El siguiente código agrupa una lista de enteros entre pares
e impares:


```python
import itertools

numeros = [12, 34, 2, 44, 83, 94, 64, 21, 7, 33]

def is_even(num):
    return num % 2

# numeros.sort(key=is_even)
for is_even, sublist in itertools.groupby(numeros, is_even):
    print(f"{'Par' if is_even else 'Impar'}:", end=' ')
    print(*sublist, sep=', ')
```

**Ejercicio**: Dada la lista, `nombres`, con los nombres de las tortugas Ninja,
el siguiente programa las muestra agrupados por la primera letra de su nombre.
Cambia el programa para que los agrupe por la **última** letra de su nombre.


```python
import itertools

nombres = ['Donatello', 'Leonardo', 'Michelangelo', 'Raphael']

def ultima_letra(nombre):
    # Pista: tendras que cambiar el código de esta función
    return nombre[0].upper()

nombres.sort(key=ultima_letra)
for (letra, sublist) in itertools.groupby(nombres, ultima_letra):
    print(letra, end=": ")
    print(*sublist, sep=", ")
```

### La función `product`

- `product(p, q, ...)`
  
Devuelve el producto cartesiano de las secuencias que se la pasen como
parámetros. Es equivalente a varios bucles `for` anidados.
  

Por ejemplo:

```python
list(product(A, B))
```

Es equivalente a:

```python
[(x,y) for x in A for y in B]
```

Ejemplo de uso: Listar las combinaciones de las letras `A` y `B` con los
dígitos $1$ al $2$


```python
import itertools

for (letra, numero) in itertools.product('AB', [1,2]):
    print(letra, numero, sep='')
```

**Ejercicio**: Generar todos los valores posibles de una baraja francesa, usando
dos listas, los rangos, de As a Rey, y los palos: corazones, rombos, tréboles y picas.

Solución:

```python
import itertools

rangos = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
palos = ['♠', '♥', '♦', '♣']

# Tu código va aquí
```

### La función `combinations`

- `combinations(s, n)`

Devuelve todas las combinaciones de longitud `n` que se pueden obtener a partir
de los elementos de `s`. Los elementos serán considerados únicos en base a su
posición, no por su valor, así que si cada elemento es único, no habrá
repeticiones dentro de cada combinación. 
 
El número de combinaciones retornadas será de:

$$\frac{n!}{r!(n-r)!}$$

Donde:

$$r \in [0, 1, ..., n]$$

Si `r` es mayor que `n`, no se devuelve ningún valor.

Se entiende mejor con ejemplos:


```python
import itertools

for i in itertools.combinations('ABCD', 1):
    print(''.join(i))
```


```python
import itertools

for i in itertools.combinations('ABCD', 2):
    print(''.join(i))
```


```python
import itertools

for i in itertools.combinations('ABCD', 3):
    print(''.join(i))
```


```python
import itertools

for i in itertools.combinations('ABCD', 4):
    print(''.join(i))
```

### La función `tee`

- `tee(iterable[, n=2])`

Devuelve `n` iteradores independientes, a partir de un único iterable.


```python
import itertools

ia, ib = itertools.tee(range(10), 2)
next(ib)
for i in range(9):
    print(next(ia), next(ib))
```

Lo que hace internamente es similar a:
 
```python
def tee(iterable, n=2):
        it = iter(iterable)
        deques = [collections.deque() for i in range(n)]
        def gen(mydeque):
            while True:
                if not mydeque:             # when the local deque is empty
                    newval = next(it)       # fetch a new value and
                    for d in deques:        # load it to all the deques
                        d.append(newval)
                yield mydeque.popleft()
        return tuple(gen(d) for d in deques)
```

Una vez que `tee` ha empezado, el iterador original no debería
usarse más, porque se corre el riesgo de que el iterador avance sin
que los iteradores derivados sean informados.

Los iteradores devueltos por `tee` no son seguros para ser usados
por diferentes *threads*, incluso aunque el iterador original si lo
fuera. Si intentamos usarlos desde diferentes _threads_, es posible
que se eleve una excepción del tipo `RuntimeError`.

Este función puede que use una cantidad significativa de
almacenamiento, dependiendo de la cantidad de datos temporales
que necesite almacenar.
  
En general, si un iterador hijo va a leer la mayoría de los datos antes
de que otro iterador hijo empiece, resultaría más eficaz usar una lista
en vez de `tee`.

**Ejercicio**: calcular la suma de los tres números sucesivos, desde el cero
hasta el 99, es decir, el primer termino es $0+1+2 = 3$, el segundo es
$1 + 2 + 3 = 6$, ... Y así hasta el último $97 + 98 + 99 = 294$:


```python
import itertools

i0, i1, i2 = itertools.tee(range(100), 3)
next(i1)
next(i2)
next(i2)
for a,b,c in zip(i0, i1, i2):
    print(f"{a} + {b} + {c} = {a+b+c}")
```

### La función `zip_longest`

- `itertools.zip_longest(*iterables, fillvalue=None)`

Retorna un iterador que agrega los elementos de cada uno de los iterables.
Funciona igual que `zip`, pero con la diferencia de que `zip` termina tan pronto
como alguno de sus iteradores termina, mientras que `zip_longest` continua
hasta que el último iterador acaba. Usa el valor definido en `fillvalue` como
sustituto de los valores que ya no pueden suministrar los iteradores agotados.


```python
import itertools

i0, i1 = itertools.tee(range(10), 2)
next(i1)
for a,b in itertools.zip_longest(i0, i1, fillvalue=-1):
    print(f"{a} + {b} = {a+b}")
```
