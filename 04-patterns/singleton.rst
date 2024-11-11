El patrón Único (*Singleton*)
-----------------------------------------------------------------------

El patron **Singleton** garantiza que una clase **sólo tenga una
instancia**, y proporciona un punto de acceso global a ella.


Motivación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Muchas veces es importante asegurarse que un determinado recurso se
representa o gestiona con un único objeto. Ejemplos típicos son una
conexión a una base de datos, el acceso a una cola de impresión que
gesiona multiples impresoras, el gestor de ventanas, etc.

Una forma sencilla y rapida de tener un unico objeto o variable de un
determinado tipo. y que su acceso sea sencillo, es hacer dicha variable
global a toda la aplicacion, e inicializarla, si fuera necesario, al
principio de la ejecución del programa. Pero hay varios problemas con
este enfoque:

1.- Sabemos ya por experiencia que las variables globales son peligrosas
y deberian evitarse en lo posible.

2.- Tener esa variable global no garantiza que no se puedan crear *otra*
variable del mismo tipo. En algunos sistemas eso seria un problema.

3.- Estamos obligados a realizar la inicializacion y configuracion del
objeto, pero quiza este no vaya a ser usado. Por ejemplo, la cola de
impresion puede que no sea necesaria, porque no es necesario mandar nada
a imprimir durante la ejecución del programa. Usando una variable
global, debemos inicializarla siempre, por si acaso.

Una solucion mejor es hacer que la clase sea responsable de esta única
instancia. La clase puede garantizar que no se crea ninguna otra
instancia (interceptando las peticiones para crear nuevos objetos, o
prohibiendolas), y a la vez puede proporcionar un medio sencillo de
acceder a la instancia. En eso consiste el patrón Singleton.

Participantes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En la implementación con clases, una clase ``Singleton`` que permite a
los clientes acceder a una única instancia, usando un método de clase.
Su responsabilidad es crear una única instancia cuando sea necesario, y
asegurarse de que solo se puede acceder a esa instancia.

Colaboraciones
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los clientes acceden al *Singleton* exclusivamente a través del método
definido para ello.

Consecuencias
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los beneficions más destacados son:

-  Acceso controlado a la única instancia. La clase ``Singleton``
   encapsula su única instancia y tiene un control absoluto sobre su
   acceso.

-  Espacio de nombres reducido. El patrón Singleton evita contaminar el
   espacio de nombres global.

-  Se puede crear subclases de la clase ``Singleton``.

-  Permite un número variable de instancias. El patrón hace que sea
   fácil cambiar de opinión y permitir más de una instancia de la clase
   ``Singleton``.


Implementación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En otros lenguajes se pueden definir funciones privadas, lo que hace más
facil el proceso de evitar que se puedan crear mas objetos a partir de
la clase.

Python tiene una filosofia diferente, más abierta. No implementa
atributos ni propiedades privadas. Unicamente existe la convención
(totalmente voluntario, por tanto) de usar como primer caracter del
nombre de un atributo o método que queremos designar como privado el
caracter subrayado (``_``).

Ahora, esto es, como se ha dicho, una mera convencion, y no hay
mecanismos en el lenguaje para impedir el acceso a estas variables con
el subrayado delante:

**Ejercicio**: Usa la clase ``A`` definida en la celda siguiente para
verificar que la convencion de usar el caracter ``_`` como primer
caracter del nombre es eso, una convención y, por tanta, podemos
modificar el atributo ``_name`` sin ningún problema.

.. code:: python3

   class A:

       def __init__(self, name):
           self._name = name

       def __str__(self):
           return self._name


   a = A('Álfa')
   print(a)

::

   Álfa

Veamos varias formas de implementar este patrón en Python.

Vamos a implementar un simple contador, pero queremos que sea un
*Singleton*, así que cada vez que pidamos una instancia del mismo, se
obtiene siempre la misma. Para ver que esto es así, asignaremos el valor
inicial del contador a un número al azar entre 0 y 1000000.

Sopongamos que esta operacion en muy costosa y nos interesa que se haga
una única vez, pero también queremos acceder e incrementar ese valor
desde cualquier parte del código:

.. code:: python3

   import random 

   class Accumulator:

       def __init__(self):
           print("Se llama al constructor de la clase Accumulator")
           self.value = random.randrange(1000000)

       def __str__(self):
           return f"Acumulator(value={self.value})"

       def inc(self):
           self.value += 1

   acc = Accumulator()
   print(acc, id(acc))
   acc = Accumulator()
   print(acc, id(acc))

::

   Se llama al constructor de la clase Accumulator Acumulator(value=948634)
   140453826370024 Se llama al constructor de la clase Accumulator
   Acumulator(value=732168) 140453826370192

Vemos que la clase anterior permite crear varias instancias. Veremos
ahora varias maneras de convertir la clase ``Accumulator`` en un
*Singleton*.

Primer método: usar un decorador
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python3

   import random

   def singleton(Cls):
       instances = {}
       def getinstance(*args, **kwargs):
           if Cls not in instances:
               instances[Cls] = Cls(*args, **kwargs)
           return instances[Cls]
       return getinstance

   @singleton
   class Accumulator:
       def __init__(self):
           print("Se llama al constructor de la clase Accumulator")
           self.value = random.randrange(1000000)    
       def __str__(self):
           return f"Acumulator(value={self.value})"   
       def inc(self):
           self.value += 1

   acc1 = Accumulator()
   print(acc1, id(acc1))
   acc2 = Accumulator()
   print(acc2, id(acc2))
   acc2.inc()
   assert acc1.value == acc2.value

::

   Se llama al constructor de la clase Accumulator Acumulator(value=114134)
   140453826381584 Acumulator(value=114134) 140453826381584

-  **Ventajas**

   -  El decorador es sencillo de usar y mas intuitivo que usar herencia
      multiple

-  **Inconvenientes**

   -  Aunque el objeto creado llamando a ``Accumulator`` es un auténtico
      objeto *Singleton*, hemos convertido ``Accumulator`` de una clase
      a una función, que puede que no sea lo que deseamos, por ejemplo,
      si quisieramos llamar a métodos estáticos de ``Accumulator``.

   -  Haciendo “trampa” seguimos siendo capaces crear un nuevo objeto a
      partir del primero, porque este mantiene una referencia a la clase
      a la que pertenece en el atributo ``__class__``

.. code:: python3

   acc3_tricky = acc1.__class__()
   print(id(acc1), id(acc3_tricky))

::

   Se llama al constructor de la clase Accumulator 140453826381584
   140453826369688

Segundo método: Una clase base
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python3

   class Singleton:
       _instance = None
       def __new__(class_, *args, **kwargs):
           if not isinstance(class_._instance, class_):
               class_._instance = object.__new__(class_, *args, **kwargs)        
               print("Se llama al constructor de la clase Accumulator")
               class_._instance.value = random.randrange(1000000)  
           return class_._instance

   class Accumulator(Singleton):
       def __repr__(self):
           return f"Acumulator(value={self.value})" 
       def inc(self):
           self.value += 1

   acc1 = Accumulator()
   print(acc1, id(acc1))
   acc2 = Accumulator()
   print(acc2, id(acc2))
   acc2.inc()
   assert acc1.value == acc2.value
   assert acc1 is acc2

::

   Se llama al constructor de la clase Accumulator Acumulator(value=697223)
   140453820806480 Acumulator(value=697223) 140453820806480

-  **Ventajas**

   -  Es una clase de verdad

-  **Inconvenientes**

   -  Puede que necesites usar herencia múltiple. En ese caso, el método
      **new** podria haber sido reescrito e interferir con el **new** de
      la clase ``Singleton``. Hay que estar pendiente de este detalle.

Tercer método: Usar metaclases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python3

   import random

   class Singleton(type):
       _instances = {}
       def __call__(cls, *args, **kwargs):
           if cls not in cls._instances:
               cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
               print("Se llama al constructor de la clase Accumulator")
               cls._instances[cls].value = random.randrange(1000000)
           return cls._instances[cls]

   class Accumulator(metaclass=Singleton):
       def __repr__(self):
           return f"Acumulator(value={self.value})"
       def inc(self)::::
           self.value += 1

   acc1 = Accumulator()
   print(acc1, id(acc1))
   acc2 = Accumulator()
   print(acc2, id(acc2))
   acc2.inc()
   assert acc1.value == acc2.value
   assert acc1 is acc2

::

   Se llama al constructor de la clase Accumulator Acumulator(value=95839)
   140453820807712 Acumulator(value=95839) 140453820807712

**Ventajas**

-  Es una clase real

-  La herencia multiple no interfiere

-  Es un uso legitimo de las metaclases

**Inconvenientes**

-  Quizá ninguno. Pero si se usa sin entender las metaclases podría ser
   peligroso.

Cuarto método: Usar un módulo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tendríamos por un lado el módulo ``acc`` que gestiona todo lo necesario
para el *Singleton*, y que incluye una función o punto de entrada que se
encarga de la inicializacióni de la instancia la primera vez que es
llamada, y que devuelve a partir de ese momento siempre la misma
instancia.

.. code:: python3

   # acc.py

   import random

   class _Accumulator:

       def __init__(self):
           print("Se llama al constructor de la clase Accumulator")
           self.value = random.randrange(1000000)

       def __repr__(self):
           return f"Acumulator(value={self.value})"

       def inc(self):
           self.value += 1


   def accumulator():
       if accumulator.instance is None:
           accumulator.instance = _Accumulator()
       return accumulator.instance

   accumulator.instance = None

Ahora, desde cualquier otra parte del código, simplemente llamamos a la
función ``accumulator()`` del módulo ``acc``:

.. code:: python3

   import acc

   acc1 = acc.accumulator()
   print(acc1, id(acc1))
   acc2 = acc.accumulator()
   print(acc2, id(acc2))
   acc2.inc()
   assert acc1.value == acc2.value
   assert acc1 is acc2

::

   Se llama al constructor de la clase Accumulator
   Acumulator(value=771707) 140453826830408
   Acumulator(value=771707) 140453826830408

**Ventajas**

-  Es la solución más *Pythónica*

-  Simple es mejor que complejo

**Inconvenientes**:

-  Ninguno


Usos conocidos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  La librería ``logging`` crea el *logger* raíz o *root* solo cuando se
   necesita. Todas las llamadas a ``getLogger``, si no se le pasa un
   parámetro de nombre, devuelven el *logger* raíz. Si es la primera
   llamada, se creará en ese preciso momento. Luego, todas las
   subsiguientes llamadas devuelven ese mismo objeto.

-  Los módulos de por si son una implementación de *Singleton*, porque
   ``import`` crea una única copia de cada módulo, las siguientes
   veces que se realiza la importación simplemente se devuelve el mismo
   objeto. Por eso muchos consideran que usar un módulo para implementar
   un *Singleton* es la solución más *pythónica*.
