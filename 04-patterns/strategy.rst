Patrón Estrategia (*Strategy*)
========================================================================

Definición
------------------------------------------------------------------------

.. index:: Strategy
.. index:: Estrategia (Patrón)

El patrón **Estrategia**, (En inglés *Strategy pattern*) es un patrón de
comportamiento que permite seleccionar entre diferentes algoritmos en
tiempo de ejecución.

En vez de usar directamente una implementación de un único algoritmo, el
código acepta instrucciones en tiempo real para usar un algoritmo dentro
de una familia de algoritmos disponibles.

Este patrón permite desacoplar el algoritmo de los clientes que lo usan.
Al **postergar la decisión sobre qué algoritmo usar** al tiempo de
ejecución, en vez de definirlo en tiempo de compilación, se obtiene
una mayor flexibilidad y capacidad de reutilización.

También conocido como
------------------------------------------------------------------------

**Policy Pattern**.

Ejemplos de uso
------------------------------------------------------------------------

Veamos algunos ejemplos.


Ejemplo 1: Validación de datos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una clase que realiza determinadas validaciones sobre un conjunto de
entradas podría usar un patrón estrategia para seleccionar un algoritmo
de validación diferente basándose en el tipo de los datos, en su origen,
en el usuario que introduce los datos, o cualquier otro factor que fuera
relevante.

A veces estos factores no se conocen perfectamente con antelación y
puede que requieran de algoritmos de validación radicalmente diferentes.
Como ventaja adicional, los algoritmos o estrategias de validación
pueden ser reutilizados en diferentes partes del sistema (e incluso en
otros sistemas) sin necesidad de duplicar el código.


Ejemplo 2: IA de juegos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En un diseño de juegos, a lo mejor interesa que la IA de un enemigo use
algoritmos totalmente diferentes, dependiendo del momento.

- Si el enemigo tiene un arma cuerpo a cuerpo y está bien de salud,
  podría seleccionar una estrategia de "Acércate lo máximo al jugador y
  ataca"

- Si tiene un arma a distancia, podría usar esta: "Manten una distancia
  prudencial con el jugador y dispara".

- Por ultimo, si esta mal de salud y/o sin armas podría cambiar a
  "Ignora al jugador, dirígete a la base más cercana para regenerar
  salud, armas y munición".

Obviamente, estos cambios de estrategia tienen que hacerse en tiempo
real, y dependiendo del estado del juego: Salud del enemigo, armamento,
posición del jugador, etc.

Ejercicio 1: Sistema de pedidos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vamos a ver un código que implementa una parte de una sistema de venta y
gestión de pedido. En nuestro -muy, muy simplificado- sistema de
pedidos, estos solo tienen tres características, el **precio**, el
**número de elementos** que se envían y el **peso total**.

íara enviar, se usan 2 sistemas diferentes de trasporte: **Correvelejos**
y **Ooops**.

Queremos calcular el coste adicional de enviar un pedido, pero las dos
empresas usan un sistema diferente:

- **Correvelejos** 1.25 euro por paquete, y 0.25 euros por kilogramo total

- **Ooops** solo cobra por el peso, 3 euros po kilo

Veamos una primera versión del código. Primero usaremos una clase
``Enum`` para asignar un código a cada transportista:

.. code:: python

    from enum import Enum
    
    class Carrier(Enum):
        
        CORREVELEJOS = 1
        OOOPS = 2

Y ahora implementamos una clase para los pedidos, la vamos a llamar
``Order``:

.. code:: python

    class Order:
        
        def __init__(self, price: float, items: int, weight: float):
            self.price = price
            self.items = items
            self.weight = weight
            
        def shipping_cost(self, carrier: Carrier):
            if carrier == Carrier.CORREVELEJOS:
                return self.items * 1.25 + 0.25 * self.weight
            elif carrier == Carrier.OOOPS:
                return self.weight * 3.0
            else:
                raise ValueError("Código de transportista desconocido")
            

Veamos que tal funciona:

.. code:: python

    order = Order(0, 4, 2.5)
    
    print("Correvelejos: ", order.shipping_cost(Carrier.CORREVELEJOS))
    print("Ooops: ", order.shipping_cost(Carrier.OOOPS))

La salida debería ser::

    Correvelejos:  5.625
    Ooops:  7.5


Bien!, parece que funciona...

... Pero el mundo sigue dando vueltas.

Hemos conseguido una nueva empresa de transportes, **Dalehache**.

Esta nueva empresa tiene, por supuesto, otro sistema de cobro
(algoritmo). No cobra por el peso, solo por **el número de paquetes**.

Pero tiene un **número mínimo de paquetes**, así que cualquier envío de
4 paquetes o menos cuesta como si fueran cinco, es decir, 5 euros. A
partir de ahí, se cobra un euro adicional por cada paquete.

Ejercicio 2: Nuevo transportista
------------------------------------------------------------------------

El ejercicio es cambiar el código anterior para trabajar con esta nueva
empresa:

.. code:: python

    class Carrier(Enum):  # Habrá que añadir un nuevo transportista
        CORREVELEJOS = 1
        OOOPS = 2
        
    
    class Order:
        
        def __init__(self, price: float, items: int, weight: float):
            self.price = price
            self.items = items
            self.weight = weight
            
        def shipping_cost(self, carrier: Carrier):  # habrá que tratar aqui el nuevo valor
            if carrier == Carrier.CORREVELEJOS:
                return self.price + (self.items * 1.25 + 0.25 * self.weight)
            elif carrier == Carrier.OOOPS:
                return self.price + (self.weight * 3.0)
            else:
                raise ValueError("Código de transportista desconocido")
            

Solucion:
------------------------------------------------------------------------

Una posible solución podría ser la siguiente:

.. code:: python

    class Carrier(Enum):
        
        CORREVELEJOS = 1
        OOOPS = 2
        DALEHACHE = 3
    
    
    class Order:
        
        def __init__(self, price: float, items: int, weight: float):
            self.price = price
            self.items = items
            self.weight = weight
            
        def shipping_cost(self, carrier: Carrier):
            if carrier == Carrier.CORREVELEJOS:
                return self.items * 1.25 + 0.25 * self.weight
            elif carrier == Carrier.OOOPS:
                return self.weight * 3.0
            elif carrier == Carrier.DALEHACHE:
                return max(self.items, 5)
            else:
                raise ValueError("Código de transportista desconocido")
            

Hagamos otro pequeño test:

.. code:: python

    order = Order(10, 1, 2.5)

    print("Correvelejos: ", order.shipping_cost(Carrier.CORREVELEJOS))
    print("Ooops: ", order.shipping_cost(Carrier.OOOPS))
    print("DaleHache: ", order.shipping_cost(Carrier.DALEHACHE))
    
Salida::

    Correvelejos:  1.875
    Ooops:  7.5
    DaleHache:  5


Problemas con esta solución
------------------------------------------------------------------------

Esta solución presenta algunos problemas, que podríamos resumir en:

- El método ``shipping_cost`` es parte de la clase ``Order``, pero esto
  no es conceptualmente demasiado correcto, porque la verdad es que sabe
  un montón de cosas de los transportes. Podría ser perfectamente un
  método de la clase ``Carrier``. Un pedido debería ser una entidad
  totalmente independiente de que tipo de transportistas existan.

  Las responsabilidades de las clases no están demasiado claras y eso
  rompe el principio de *single responsability* (La **S** de SOLID).

- Además, cuando tuvimos que añadir un nuevo transportista, tuvimos que
  modificar el código de la clase ``Order``. Hemos tenido que modificar
  la clase para los pedidos por una razón -Añadir un nuevo
  transportista- que no debería afectar. Esto rompe el principio de
  *Open / Close* (La **O** de SOLID).

- La clases ``Order`` y ``Carrier`` están demasiado acopladas. En
  concreto, el método ``shipping_cost`` sabe demasiadas cosas de la
  estructura interna de los transportistas. Por ejemplo, sabe que
  actualmente hay tres transportistas, y sabe el sistema de cobro de
  cada uno. Ademas, esta programado para trabajar usando una instancia
  (del transportista), en vez de una interfaz. Esto va contra el
  principio de *Dependency Inversion*, (La **D** de SOLID).

- Por último, esa estructura de ``if ... elif ... else`` deja un mal
  sabor de boca. En general este tipo de estructuras se considera un
  "mal olor", un indicador de que se podría hacer de otra manera.

Ejercicio 2: Aplicar el patrón Strategy
------------------------------------------------------------------------

Vamos a intentar resolver estos problemas con el patrón Estrategia. Como
vemos, cada transportista usa su propio sistema de reglas -> Estrategia
-> Algoritmo para calcular sus precios, así que vamos a hacer una clase
abstracta para todos los transportistas.

.. note::

   Una clase abstracta es una clase de la cual nunca se crea
   ninguna instancia. Solo se usa para derivar por herencia otras
   clases.

Paso 1) Crear una base clase para las estrategias (en este caso,
transportistas):

.. code:: python

    class BaseCarrier:
        
        def carrier_cost(self, order: Order) -> float:
            raise NotImplemented(
                "Las clases derivadas de BaseCarrier"
                " deben implementar este metodo"
            )

Básicamente, esta es una forma de decir: Si una clase deriva de
``BaseCarrier``, está *obligada* a definir un método ``carrier_cost``,
que acepte como parámetro de entrada un objeto de tipo ``Order``, y que
devuelve un número decimal.

.. note::

   Existe una forma incluso mejor de hacer este tipo de
   *contratos* usando las llamadas *Abstract Base Class*, incluidas en
   Python desde la versión 3.4, y que veremos con algo más de detalle en
   la sección dedicada a las librerías estándar.

Ahora, hagamos una clase para cada transportista. Empezamos por el
servicio Correvelejos:

.. code:: python

    class Correvelejos(BaseCarrier):
        
        def carrier_cost(self, order: Order):
            return order.items * 1.25 + 0.25 * order.weight
        

Para Ooops:

.. code:: python

    class Ooops(BaseCarrier):
        
        def carrier_cost(self, order: Order):
            return order.weight * 3.0

Finalmente, la clase para DaleHache:

.. code:: python

    class DaleHache(BaseCarrier):
        
        def carrier_cost(self, order: Order):
            return max(5, order.items)

Vamos a hacer un pequeño test para comprobar que nuestros nuevos
transportistas siguen funcionando (aunque ahora solo nos informan del
coste del transporte, así mejoramos la asignacion de responsabilidades):

.. code:: ipython3

    order = Order(10, 4, 2.5)
    
    correvelejos_carrier = Correvelejos()
    assert correvelejos_carrier.carrier_cost(order) == 5.625
    
    ooops_carrier = Ooops()
    assert ooops_carrier.carrier_cost(order) == 7.5
    
    dalehache_carrier = DaleHache()
    assert dalehache_carrier.carrier_cost(order) == 5

Ahora, podemos modificar el método para calcular el costo de un pedido,
al que ahora se le debe pasar un objeto (de una clase derivada de
``BaseCarrier``) para indicar el transportista:

.. code:: python

    class Order:
        
        def __init__(self, price: float, items: int, weight: float):
            self.price = price
            self.items = items
            self.weight = weight
    
        def shipping_cost(self, carrier: BaseCarrier):
            return self.price + carrier.carrier_cost(self)

Vamos ahora con nuestra habitual batería de test:

.. code:: python

    order = Order(10, 4, 2.5)
    
    assert order.shipping_cost(Correvelejos()) == 15.625
    assert order.shipping_cost(Ooops()) == 17.5
    assert order.shipping_cost(DaleHache()) == 15

Mejoras obtenidas
------------------------------------------------------------------------

- Las clases ``Order`` para los pedidos y las clases de los distintos
  transportistas: ``Correvelejos``, ``Ooops`` y ``DaleHache`` están
  ahora mucho más **desacopladas**.

  En concreto, la clase pedidos no sabe, ni le importa, cuantos tipos de
  transportistas hay, o como realizan internamente sus cálculos. Lo
  único que necesita saber es que tienen que tener un método llamado
  ``carrier_cost`` que acepta como parámetro de entrada una orden y
  devuelve un coste.

- Por su lado, la clases derivadas de ``Carrier`` (clases ``Carriers`` en
  adelante) solo saben, de los pedidos, que tienen los campos públicos
  ``weight`` e ``items``. El conocimiento que tienen las clases una de
  la otra ha disminuido con respecto al código inicial.

- Las clases ``Carriers`` solo se ocupan cada uno de su propia
  estrategia de cálculo de precios. No saben, ni necesitan saber, nada
  una de las otras.

- Añadir un nuevo transportistas es mucho más sencillo ahora. No hay que
  modificar la clase ``Order``, y solo hay que crear una nueva clase
  derivada de ``CarrierBase`` e implementar su algoritmo específico de
  cálculo de precio.

- Las clases ``Carrier`` pueden ser testeadas con muchas más facilidad.
  Se les puede pasar un doble o *mock* para ello: cualquier objeto con
  propiedades públicas ``width`` e ``items`` puede ser usado como si
  fuera un pedido.

- El método ``shipping_cost`` de la clase ``Orden`` no está ahora
  programado para usar una instancia de un ``Carrier``, sino para usar
  la interfaz (O clase base abstracta, en la nomenclatura de Python)
  ``CarrierBase``. Eso significa que puede usar cualquier objeto que
  tenga un método ``carrier_cost`` que acepte como parámetro de entrada
  una orden y devuelve un coste. De esta forma ahora podemos testear las
  clase orden pasándole un doble o mock de un transportista, y el método
  seguirá funcionando con futuros transportistas (Siempre que implementen
  correctamente su algoritmo de cálculo de precios).

- El *feo* árbol de decisiones a base de ``if ... elif ... else`` ha
  desaparecido, para no volver.

- El código, en general, es más sencillo de leer y de modificar.
