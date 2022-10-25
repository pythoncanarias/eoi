---
title: headq - Implementación de *Heap Sort*
---

### Contenido del módilo

El módulo `heapq` implementa un algoritmo llamada *Heap Sort* pensado
para ser usado con las listas de Python. Un **heap** o montículo es una
estructura de datos en forma de árbol en la cual los nodos hijos
mantienen una relación de ordenación con respecto a sus padres. Un
*heap* binario se puede representar usando una lista organizada de tal
manera que los hijos del elemento que ocupa la posición $N$ están en
las posiciones $2N+1$ y $2N+2$. Esta disposición permite reorganizar los
*heaps* internamente, de forma que no hace falta reubicar tanta
memoria a la hora de añadir o eliminar elementos.

Un *maximun heap* garantiza que el nodo padre siempre contendrá un valor
superior al de cualquiera de sus hijos. Un *minimal heap*, por el
contrario, siempre cumplirá que el valor del padre sera menor que el de
cualquiera de sus hijos. La implementación de este módulo es de tipo
*minimal*.

Esta estructura nos permite tener una lista de la cual siempre será muy
rápido extraer el elemento de mayor valor, por lo que se utiliza
especialmente para mantener listas de elementos **con prioridades**.

### Crear un *Heap*

Hay dos maneras de crear un *heap*, con las funciones `heappush()` y
`heapify()`.

```python
import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

heap = []
print('random :', data)
print()

for n in data:
    print('add {:\>3}:'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)
```

Cuando se usa `heappush()`, el ordenamiento del _heap_ se mantiene a
medida que se van incluyendo nuevos valores.

### La función `heapify`

Si los datos están en memoria es más eficiente usar
`heapify()` y reorganizar los elementos de la lista en
primer lugar. El resultado de construir un _heap_ elemento a elemento es
el mismo que crear la lista sin ordenar y luego llamar a `heapify()`.

### La función `heappop`

Una vez que el *heap* está organizado correctamente, se puede usar
`headpop` para retirar el elemento con el valor más bajo.

### Otras funciones

`heapq` también incluye dos funciones: `nlargest` y `nsmallest` para
examinar un iterable y encontrar un rango que comprenda los valores
máximos y mínimos que encuentre.

Ver también:

- [heapq — Algoritmo de colas montículos](https://docs.python.org/es/3/library/heapq.html)

- [Wikipedia - Montículo](https://es.wikipedia.org/wiki/Mont%C3%ADculo_(inform%C3%A1tica))

- [Dab Bader - Priority Queues in Python](https://dbader.org/blog/priority-queues-in-python)
