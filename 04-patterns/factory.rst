El patrón Factory
-----------------

Propósito
~~~~~~~~~

Define una interfaz para crear un objeto, pero deja que sean las
subclases quienes decidan qué clase instanciar. Permite que una clase
delegue en sus subclases la creación de objetos.

Motivacion
~~~~~~~~~~

En programación orientada a obtjetos, el termino ``factory`` se refiere
a una clase que es reponsable de la creacion de objetos de otras clases.
Normalmente la clase que actua como *factory* tiene un objeto con una
serie de métodos. El cliente llama a alguno de estos metodos con ciertos
parámetros. Internamente, el método crea los objetos y se los devuelve
al cliente

Asi que la pregunta es: ¿Por qué necesitamos una clase *factory* aparte,
cuando el cliente podria crear directamente el objeto? La respuesta es
que este patron proporciona ciertas ventajas que puede que nos sean
utiles o necesarias:

-  La primera ventaja es que la creacion de un objeto puede ser
   independiente de su implementacion.

-  El cliente no necesita saber nada de las clases que realmente crean
   el objeto. Solo necesita pasar la informacion que se necesita para
   crearlo. Esto simplifica la implementacion del cliente (las clases
   estan menos acopladas)

-  Es sencillo añadir otra clase mas a la factoría, de forma que se
   puedan crear objetos de una nueva clase. El resto de las clases no se
   ve afectado. El cliente tendra que aceptar un nuevo parámetro o valor
   del mismo.

-  La factoria también puede reutilizar objetos preexistentes. La clase
   original siempre creará un objeto nuevo.

Hay tres variantes de este patrón:

-  **Simple Factory pattern**: Permite crear objetos sin exponer la
   lógica de creación de los mismos.

-  **Factory method pattern**: Permite crear objetos sin exponer la
   lógica de creación de los mismos, pero retrasa la decisión de que
   subclase en concreto se usará para crear el objeto.

-  **Abstract Factory pattern**: Crea los objetos sin necesidad de
   especificar sus clases. El patron suministra objetos a partir de otra
   fabrica, que crea internamete.

Pero este patron es poco útil en Python, porque las capacidades
dinámicas y el hecho de que tanto funciones, metodos y clases sean
objetos de primer nivel, y por tanto susceptibles de ser pasados como
parametros, almacenados en estructuras de detos, etc. lo hacen en la
práctica poco recomendable, a no ser que la estructura de los objetos
que estamos creando este cambiando muy frecuentemente.

Veremos solo el *Simple Factory pattern*, los demas casos son raramente
aplicables en Python.

Simple Factory pattern
~~~~~~~~~~~~~~~~~~~~~~

Esta es la forma más sencilla de este patrón. En este caso, la fábrica
es simplemente una función.

Vamos a suponer que estamos creando un juego y queremos poder crear
varios tipos de enemigos. Tenemos las clases ``Soldier`` para
representar soldados, y ``Tower`` para torretas defensivas.

Supongamos que deseamos desacoplar la creacion de los enemigos del
conocimiento de estas clases (Quiza querramos cambiar las clases, por
ejemplo, podemos decidir que la clase ``Tower`` podria muy bien
reemplazarse por una clases ``Soldier`` con capacidad de desplazamiento
cero).

La forma más sencilla seria crear una clase o funcion *factory*

.. code:: ipython3

    class Soldier:
        def __init__(self):
            self.movement = 10
            self.power = 10
        def __str__(self):
            return "Soldier"
    
    class Tower:
        def __init__(self):
            self.power = 100
        def __str__(self):
            return "Tower"
    
    def enemy_factory(kind):
        Enemies = {
            'soldier': Soldier,
            'tower': Tower,
        }
        _cls = Enemies[kind]
        return _cls()
    
    s1 = enemy_factory('soldier')
    t1 = enemy_factory('tower')
    print(s1, t1)


.. parsed-literal::

    Soldier Tower


**Ejercicio**: Comprueba que el código anterior es capaz de crear
enemigos de distinto tipo. Cambia el codigo para que podamos incluir un
nuevo tipo de enemigo, el ``mecha``, con capacidad de movimiento
:math:`5`, potencia de fuego :math:`50`.

**Pista**: Tendras que crear una nueva clase ``Mecha``, y modificar la
función ``make_enemy`` para que pueda crear objetos de esta nueva clase.

.. code:: ipython3

    class Soldier:
        
        def __init__(self):
            self.movement = 10
            self.power = 10
            
        def __str__(self):
            return "Soldier"
    
    class Tower:
        
        def __init__(self):
            self.power = 100
            
        def __str__(self):
            return "Tower"
    
    def enemy_factory(kind):
        Enemies = {
            'soldier': Soldier,
            'tower': Tower,
        }
        _cls = Enemies[kind]
        return _cls()
    
    assert enemy_factory("mecha").power == 50


::


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-3-5fb9f33e2b98> in <module>
         24     return _cls()
         25 
    ---> 26 assert enemy_factory("mecha").power == 50
    

    <ipython-input-3-5fb9f33e2b98> in enemy_factory(kind)
         21         'tower': Tower,
         22     }
    ---> 23     _cls = Enemies[kind]
         24     return _cls()
         25 


    KeyError: 'mecha'


