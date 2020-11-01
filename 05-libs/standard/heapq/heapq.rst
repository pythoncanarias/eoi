El módulo ``heapq``: Implementacion del algoritmo *Heap Sort*
--------------------------------------------------------------

.. index:: heap

El módulo ``heapq`` implementa un algoritmo llamada *Heap Sort* pensado
para ser usado con las listas de Python. Un **heap** o montículo es una
estructura de datos en forma de árbol en la cual los nodos hijos mantienen
una relacion de ordenacion con respecto a sus padres. Un *heap* binario
se puede representar usando una lista organizada de tal manera que los hijos
del elemento que ocupa la ñosición :math:`N` estáan en las posiciones :math:`2N+1`
y :math:`2N+2`. Esta disposición permite reorganizar los *heaps* internamente, de
forma que no hace falta relocalizar tanta memoria a la hora de añadir o eliminar
elementos.

Un *maximun heap* garantiza que el nodo padre siempre contendrá un valor superior 
aal de cualquiera de sus hijos. Un *minimal heap*, por el contrario, siempre cumplira
que el valor del padre sera menor que el de cualquiera de sus hijos. La implementación
de este módulo es de tipo *minimal*.

Esta estructura nos permite tener una lista de la cual siemper sera muy rápido extraer
el elemento de mayor valor, por lo que se utiliza especialmente para mantener listas
de elementos con prioridades.

Crear un *Heap*

Hay dos maneras de crear un *heap*, con las funciones ``heappush()`` y ``heapify()``.

heapq_heappush.py
import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

heap = []
print('random :', data)
print()

for n in data:
    print('add {:>3}:'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)

Cuando se usa ``heappush()``, el ordenamiento del heap se mantiene a medida que se van incluyendo
nuevos valores.

Si los daots están en memoriam es más eficiente usar 
`heapify()` y reorganizar los elementos de la lista en primer
lugar.  El resultado de construir un heap elemento a elemento es el mismo que crear la lista sin
ordenar y luego llamar a ``heapify()``.

Una vez que el *heap* está organizado correctamente, se puede usar `headpop` para retirar
el elemento con el valor más bajo.

.. index:: nlargest (heapq)
.. index:: nshortest (heapq)

heapq tambien incluye dos funciones ``nlargest`` y ``nsmallest`` para examinar un iterable y encontrar 
un rango que comprenda los valores mas máximos y mínimos que encuentre.

Ver también:

- Standard library documentation for heapq
- Wikipedia: Heap (data structure) – A general description of heap data structures.
- Priority Queue – A priority queue implementation from Queue in the standard library.
