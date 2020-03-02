El módulo ``itertools``
-----------------------------------------------------------------------

Este módulo implementa una serie de funciones para trabajar con iteradoresr,
que se usan como elementos básicos. Muchas de  estas fnciones están inspiradas
por distintas construcciones que podemos encontrar en otros lenguajes como APL,
Haskell o SML.

Estas utilidades cuentan con la ventaja de ser parte de la librería estándar,
ademásm de ser eficientes y rápidas, al estar implementadas a bajo nivel. Con
estas utilidades se puede formar una especie de *algebra de iteradores* que
permite construir herramientas más especializadas de forma suscinta y eficiente.

Algunas de las funciones de este módulo son:

.. index:: count

* ``count(start, [step])``

  Iterador infinito. Devuelve una cuenta, empezando por ``start`` en la primera
  llamada y cada siguiente invocación con el valor incrementado por el
  parámetro opcional ``step`` ( por omisión, 1)::

    >>> for i in itertools.count(10, -1):
    ...     print(i) ...     if i == 0: break; ...  10 9 8 7 6 5 4 3 2
    1 0

.. index:: cycle

* ``cycle(s)``

  Iterador infinito. Empieza devolviendo los elementos de la
  secuencia ``s``, y cuando termina, vuelve a empezar::

    >>> color = itertools.cycle(['red', 'green', 'blue']) for i in
    >>> range(7):
    ...     print(color.next()) ...  red green blue red green blue
    red
    >>>

.. index:: chain

* ``chain(s1, s2, ... ,sn)``

  Encadena una secuencia detrás de otra::

    >>> l = [c for c in itertools.chain('ABC', 'DEF')] 
    >>> print(l)
    ['A', 'B', 'C', 'D', 'E', 'F']
    >>>

.. index:: groupby

* ``groupby(s, f)``

  Agrupa los elementos de una secuencia ``s``, por el procedimiento
  de aplicar la función ``f`` a cada elemento, asignado al mismo
  grupo a aquellos elementos que devuelven el mismo resultado. El
  resultado es un iterador que retorna duplas (tuplas de dos
  elementos) formadas por el resultado de la función y un iterador de
  todos los elementos correspondientes a ese resultado::

    >>> l = ['Donatello', 'Leonardo', 'Michelangelo', 'Raphael'] f
    >>> = lambda x: x[-1] for (letra, s) in itertools.groupby(l,
    >>> f):
    ...     print(letra) ...     for i in s: print(' -', i) ...  o
    - Donatello
    - Leonardo
    - Michelangelo l
    - Raphael
    >>>

.. index:: product

* ``product(p, q, ...)``

  Devuelve el producto cartesiano de las secuencias que se la pasen
  como parámetros. Es equivalente a varios bucles for anidados; por
  ejemplo::

    product(A, B)

  devuelve el mismo resultado que::

    ((x,y) for x in A for y in B)

  Ejemplo de uso::

      >>> for (letra, numero) in itertools.product('AB', [1,2]):
      ...     print(letra, numero)
      ...
      A 1
      A 2
      B 1
      B 2
      >>>

.. index:: combinations

* ``combinations(s, n)``

  Devuelve todas las combinaciones de longitud ``n`` que se
  pueden obtener a partir de los elementos de ``s``. Los
  elementos serán considerados únicos en base a su posición, no
  por su valor, así que si cada elemento es único, no habra
  repeticiones dentro de cada combinación. El número de
  combinaciones retornadas sera de ``n! / r! / (n-r)!``, donde
  ``r ∈ [0, 1, ..., n]``. Si ``r`` es mayor que ``n``, no se
  devuelve ningún valor.

    >>> for i in itertools.combinations('ABCD', 1): print(''.join(i))
    ...
    A
    B
    C
    D
    >>> for i in itertools.combinations('ABCD', 2): print(''.join(i))
    ...
    AB
    AC
    AD
    BC
    BD
    CD
    >>> for i in itertools.combinations('ABCD', 3): print(''.join(i))
    ...
    ABC
    ABD
    ACD
    BCD
    >>> for i in itertools.combinations('ABCD', 4): print(''.join(i))
    ABCD
    >>>

.. index:: tee

* ``tee(iterable[, n=2])``

  Devuelve ``n`` iteradores independientes, a partir de un único
  iterable. Lo que hace internamente es similar a::

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

  Una vez que ``tee`` ha empesado, el iterador original no deberia ser usado más,
  porque se corre el riesgo de que el iterador avanze sin que los iteradores
  derivados sean informados.

  Los iteradores devueltos por ``tee`` no son seguros para ser usados
  por diferentes *threads* incluso aunque el iterador original si lo
  fuera. Si intentamos usarlos desde diferentes *threads*, es posible+
  que se eleve una excepción del tipo ``RuntimeError``.

  Este función puede que use una cantidad significatica de almacenamiento,
  dependiendo de cuantos datos temporales necesite almacenar. En general, si
  un iterador la mayoría de los datos antes de que otro iterador empiece,
  resultaria más eficaz usar una lista en vez de ``tee``.

  Ejemplo de uso::

    >>> from itertools import tee
    >>> l = list(range(10))
    >>> l
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> a, b = tee(iter(l), 2)
    >>> next(b)

    >>> for i1, i2 in zip(a, b):
    ...     print(i1, i2, i1*i2)
    ... 
    0 1 0
    1 2 2
    2 3 6
    3 4 12
    4 5 20
    5 6 30
    6 7 42
    7 8 56
    8 9 72

  .. note:: Ejercicio: calcular la suma de los tres números sucesivos, desde el cero
      hasta el 99, es decir, el primer termino es 0+1+2 = 3, el segundo es
      1*2*3 = 6, ... hasta el ultimo 97+98+99 = 294
