Patrón Estrategia (Strategy pattern)
------------------------------------

**Estrategia**, (En inglés *Strategy pattern*, a veces *Policy pattern*)
es un patrón de comportamiento, que permite seleccionar entre diferentes
algoritmos en tiempo de ejecución.

En vez de usar directamente una inplementación de un único algoritmo, el
código acepta instrucciones en tiempo real para usar un algoritmo dentro
de una familia de algoritmos disponibles.

Este patron permite desacoplar el algoritmo de los clientes que lo usan.
Al **postergar la decisión sobre qué algoritmo usar** al tiempo de
ejecución, en vez de predefinirlo en tiempo de compilación, se obtiene
una mayor flexibilidad y capacidad de reutilización.

Veamos algunos ejempos.

Ejemplo 1: Validación de datos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~

En un diseño de juegos, a lo mejor interesa que la IA de un enemigo use
algoritmos totalmente diferentes, dependiendo del momento.

-  Si el enemigo tiene un arma cuerpo a cuerpo y está bien de salud,
   podría seleccionar una estrategia de “Acércate lo máximo al jugador y
   ataca”

-  Si tiene un arma a distancia, podría usar esta: “Manten una distancia
   prudencial con el jugador y dispara”.

-  Por ultimo, si esta mal de salud y/o sin armas podria cambiar a
   “Ignora al jugador, dirígete a la base más cercana para regenerar
   salud/rearmarte”.

Obviamente, estos cambios de estrategia tienen que hacerse en tiempo
real, y dependiendo del estado del juego: Salud del enemigo, armamento,
posición del jugador, etc.

## Ejercicio 1: Sistema de pedidos

Vamos a ver un código que implementa una parte de una sistema de venta y
gestión de pedido. En nuestro -muy, muy simplificado- sistema de
pedidos, estos solo tienen tres caractersiticas, el **precio**, el
**número de elementos** que se envian y el **peso total**.

Para enviar, se usan 2 sistemas diferentes de trasporte: Servicio Postal
y UPS.

Queremos calcular el coste adicional de enviar un pedido, pero las dos
empresas usan un sistema diferente:

**Servicio Postal**: cobra 1.25 euro por item, y 0.25 euros por
kilogramo total

**UPS**: solo cobra por el peso, 3 euros / kg

Veamos una primera versión del código. Primero usaremos una clase
``Enum`` para asignar un código a cada transportista:

.. code:: ipython3

    from enum import Enum
    
    class Carrier(Enum):
        
        POSTAL = 1
        UPS = 2

Y ahora implementamos una clase para los pedidos, la vamos a llamar
``Order``:

.. code:: ipython3

    class Order:
        
        def __init__(self, price: float, items: int, weight: float):
            self.price = price
            self.items = items
            self.weight = weight
            
        def shipping_cost(self, carrier: Carrier):
            if carrier == Carrier.POSTAL:
                return self.price + (self.items * 1.25 + 0.25 * self.weight)
            elif carrier == Carrier.UPS:
                return self.price + (self.weight * 3.0)
            else:
                raise ValueError("Código de transportista desconocido")
            

Veamos que tal funciona:

.. code:: ipython3

    order = Order(0, 4, 2.5)
    
    assert order.shipping_cost(Carrier.POSTAL) == 5.625
    assert order.shipping_cost(Carrier.UPS) == 7.5

Bien!, parece que funciona..

… Pero el mundo sigue dando vueltas

Hemos conseguido una nueva empresa de transportes, **DHL**.

Esta nueva empresa tiene, por supuesto, otro sistema de cobro
(algoritmo). No cobra por el peso, solo por **el número de items**.

Pero tiene un **número mínimo de items**, asi que cualquier cantidad de
5 o menos items cuesta 5 euros. A partir de ahí, se cobra un euro
adicional por cada item.

El ejercicio es cambiar el codigo anterior para trabajar con esta nueva
empresa

.. code:: ipython3

    class Carrier(Enum):  # Habrá que añadir un nuevo transportista
        POSTAL = 1
        UPS = 2
        
    
    class Order:
        
        def __init__(self, price: float, items: int, weight: float):
            self.price = price
            self.items = items
            self.weight = weight
            
        def shipping_cost(self, carrier: Carrier):  # habrá que tratar aqui el nuevo valor
            if carrier == Carrier.POSTAL:
                return self.price + (self.items * 1.25 + 0.25 * self.weight)
            elif carrier == Carrier.UPS:
                return self.price + (self.weight * 3.0)
            else:
                raise ValueError("Código de transportista desconocido")
            

Solucion:
~~~~~~~~~

Una posible solucion podria ser la siguiente:

.. code:: ipython3

    class Carrier(Enum):
        
        POSTAL = 1
        UPS = 2
        DHL = 3
    
    
    class Order:
        
        def __init__(self, price: float, items: int, weight: float):
            self.price = price
            self.items = items
            self.weight = weight
            
        def shipping_cost(self, carrier: Carrier):
            if carrier == Carrier.POSTAL:
                return self.price + (self.items * 1.25 + 0.25 * self.weight)
            elif carrier == Carrier.UPS:
                return self.price + (self.weight * 3.0)
            elif carrier == Carrier.DHL:
                return self.price + max(self.items, 5)
            else:
                raise ValueError("Código de transportista desconocido")
            

Hagamos otro pequeño test:

.. code:: ipython3

    order = Order(10, 4, 2.5)
    
    assert order.shipping_cost(Carrier.POSTAL) == 15.625
    assert order.shipping_cost(Carrier.UPS) == 17.5
    assert order.shipping_cost(Carrier.DHL) == 15


### Problemas con esta solución

Esta solución presenta algunos problemas, que podriamos resumir en:

-  El método ``shipping_cost`` es parte de la clase ``Order``, pero esto
   no es conceptualmente demasiado correcto, porque la verdad es que
   sabe un montón de cosas de los transportes. Podria ser perfectamente
   un metodo de la clase ``Carrier``. Un pedido deberia ser una entidad
   totalmente independiente de que tipo de transportistas existan.

   Las responsabilidades de las clases no están demasiado claras y eso
   rompe el principio de *single responsability* (La **S** de SOLID).

-  Además, cuando tuvimos que añadir un nuevo transportista, tuvimos que
   modificar el código de la clase ``Order``. Hemos tenido que modificar
   la clase para los pedidos por una razón -Añadir un nuevo
   transportista- que no debería afectar. Esto rompe el principio de
   *Open / Close* (La **O** de SOLID).

-  La clases ``Order`` y ``Carrier`` están demasiado acopladas. En
   concreto, el metodo ``shipping_cost`` sabe demasiadas cosas de la
   estructura interna de los transportistas. Por ejemplo, sabe que
   actualmente hay tres transportistas, y sabe el sistema de cobro de
   cada uno. Ademas, esta programado para trabajar usando una instancia
   (del transportista), en vez de una interfaz. Esto va contra el
   principio de *Dependency Inversion*, (La **D** de SOLID).

-  Por último, esa estructura de ``if`` … ``elif`` … ``else`` deja un
   mal sabor de boca. En general este tipo de estructuras se considera
   un “mal olor”, normalmente un indicador de que se podria hacer de
   otra manera.

Ejercicio 2: Aplicar el patrón Strategy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vamos a intentar resolver estos problemas con el patron Estrategia. Como
vemos, cada transportista usa su propio sistema de reglas -> Estrategia
-> Algoritmo para calcular sus precios, asi que vamos a hacer una clase
abstracta para todos los transportistas.

--------------

**Nota**: Una clase abstracta es una clase de la cual nunca se crea
ninguna instancia. Solo se usa para derivar por herencia otras clases.
\**\*

Paso 1) Crear una base clase para las estrategias (en este caso,
transportistas)

.. code:: ipython3

    class BaseCarrier:
        
        def carrier_cost(self, order: Order) -> float:
            raise NotImplemented(
                "Las clases derivadas de BaseCarrier"
                " deben implementar este metodo"
            )

Basicamente, esta es una forma de decir: Si una clase deriva de
``BaseCarrier``, está *obligada* a definir un método ``carrier_cost``,
que acepte como parametro de entrada un objeto de tipo ``Order``, y que
devuelve un número decimal.

--------------

**Nota**: Existe una forma incluso mejor de hacer este tipo de
*contratos* usando las llamadas *Abstract Base Class*, incluidas en
Python desde la versión 3.4, y que veremos con algo más de detalle en la
sección dedicada a las librerías estándar. \**\*

Ahora, hagamos una clase para cada transportista. Empezamos por el
servicio postal:

.. code:: ipython3

    class Postal(BaseCarrier):
        
        def carrier_cost(self, order: Order):
            return order.items * 1.25 + 0.25 * order.weight
        

…para UPS:

.. code:: ipython3

    class UPS(BaseCarrier):
        
        def carrier_cost(self, order: Order):
            return order.weight * 3.0

… y, finalmente, la clase para DHL:

.. code:: ipython3

    class DHL(BaseCarrier):
        
        def carrier_cost(self, order: Order):
            return max(5, order.items)

Vamos a hacer un pequeño test para comprobar que nuestros nuevos
transportistas siguen funcionando (aunque ahora solo nos informan del
coste del transporte, asi mejoramos la asignacion de responsabilidades):

.. code:: ipython3

    order = Order(10, 4, 2.5)
    
    postal_carrier = Postal()
    assert postal_carrier.carrier_cost(order) == 5.625
    
    ups_carrier = UPS()
    assert ups_carrier.carrier_cost(order) == 7.5
    
    dhl_carrier = DHL()
    assert dhl_carrier.carrier_cost(order) == 5

Ahora, podemos modificar el método para calcular el costo de un pedido,
al que ahora se le debe pasar un objeto (de una clase derivada de
``BaseCarrier``) para indicar el transportista:

.. code:: ipython3

    class Order:
        
        def __init__(self, price: float, items: int, weight: float):
            self.price = price
            self.items = items
            self.weight = weight
    
        def shipping_cost(self, carrier: BaseCarrier):
            return self.price + carrier.carrier_cost(self)

Vamos ahora con nuestra habitual batería de test:

.. code:: ipython3

    order = Order(10, 4, 2.5)
    
    assert order.shipping_cost(Postal()) == 15.625
    assert order.shipping_cost(UPS()) == 17.5
    assert order.shipping_cost(DHL()) == 15

Mejoras obtenidas
-----------------

-  Las clases ``Order`` para los pedidos y las clases de los distintos
   transportistas: ``Postal``, ``UPS``, ``DHL`` están ahora mucho más
   **desacopladas**.

En concreto, la clase pedidos no sabe, ni le importa, cuantos tipos de
transportistas hay, o como realizan internamente sus cálculos. Lo úniqo
que necesita saber es que tienen que tener un método llamado
``carrier_cost`` que acepta como parámetro de entrada una orden y
devuelve un coste.

Por su lado, la clases drivadas de ``Carrier`` (clases ``Carriers`` en
adelante) solo saben, de los pedidos, que tienen los campos públicos
``weight`` e ``items``. El conocimiento que tienen las clases una de la
otra ha disminuido con respecto al código inicial.

-  Las clases ``Carriers`` solo se ocupan cada uno de su propia
   estrategia de cálculo de precios. No saben, ni necesitan saber, nada
   una de las otras.

-  Añadir un nuevo transportistas es mucho más sencillo ahora. No hay
   que modificar la clase ``Order``, y solo hay que crear una nueva
   clase derivada de ``CarrierBase`` e implementar su algoritmo
   específico de cálculo de precio.

-  Las clases ``Carrier`` pueden ser testeadas con muchas más facilidad.
   Se les puede pasar un doble o *mock* para ello: cualquier objeto con
   propiedades públicas ``width`` e ``items`` puede ser usado como si
   fuera un pedido.

-  El mátodo ``shipping_cost`` de la clase ``Orden`` no está ahora
   programado para usar una instancia de un carrier, sino para usar una
   interfaz (O clase base abstracta, en la nomemclatura de Python). Eso
   significa que puede usar cualquier objeto que tenga un método
   ``carrier_cost`` que acepte como parámetro de entrada una orden y
   devuelve un coste. De esta forma ahora podemos testear las clase
   orden pasandole un doble o mock de un transportista.

-  El “feo” orbol de decisiones a base de ``if ... elif ... else`` ha
   desaparecido, para no volver.

-  El código, en general, es más sencillo de leer y de modificar
