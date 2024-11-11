El patrón Adapter (Adaptador)
-----------------------------

Motivación
~~~~~~~~~~

Convierte la interfaz de una clase en otra interfaz que es la que
esperan los clientes. Permite que cooperen clases que de otra forma no
podrían por tener interfaces incompatibles.

También conocido como
~~~~~~~~~~~~~~~~~~~~~

-  *Wrapper* (Envoltorio)

Motivación
~~~~~~~~~~

A veces una clase o función no pueden reutilizarse, porque su interfaz
no coincide con la interfaz específica que requiere la aplicación.

Pensemos, por ejemplo, en un editor de dibujo que permita que los
usuarios dibujen y ubiquen elementos gráficos (líneas, polígonos, texto,
etc.) en dibujos y diagramas.

La abstracción fundamental del editor de dibujo es el objeto gráfico,
que tiene una forma modificable y que puede dibujarse a sí mismo. La
interfaz de los objetos gráficos está definida por una clase abstracta
llamada ``Shape``.

El editor define una subclase de ``Shape`` para cada tipo de objeto
gráfico: una clase ``LineShape`` para las líneas, otra ``PolygonShape``
para los polígonos, etcétera.

Las clases de formas geométricas elementales, como ``LineShape`` y
``PolygonShape`` son bastante fáciles de implementar, ya que sus
capacidades de dibujado y edición son intrínsecamente limitadas. Pero
una subclase *Texto* que pueda mostrar y editar texto es
considerablemente más difícil de implementar, ya que incluso la edición
básica de texto implica actualizaciones de pantalla complicadas y
gestión de búferes.

A su vez, un librería comercial de interfaces de usuario podría
proporcionar una clase ``TextView`` sofisticada para mostrar y editar
texto. Lo que nos gustaría sería poder reutilizar ``TextView`` para
implementar ``TextShape``, pero la librería no se diseñó con las clases
``Shape`` en mente. Por tanto, no podemos usar los objetos ``TextView``
y ``Shape`` de manera intercambiable.

Podríamos cambiar la clase ``TextView`` para que se ajustase a la
interfaz ``Shape``, pero no tenemos el código fuente de la librería.

Incluso aunque así fuese, no tendría sentido cambiar ``TextView``; no
deberíamos tener que adoptar interfaces específicas del dominio sólo
para que funcione una aplicación.

En vez de eso, podríamos definir ``TextShape`` para que adapte la
interfaz ``TextView`` a la de ``Shape``. Podemos hacer esto de dos
maneras:

1) Heredando la interfaz de ``Shape`` y la implementación de
   ``TextView``

2) Componiendo una instancia ``TextView`` dentro de una ``TextShape``

Ambos enfoques se corresponden con las versiones de clases y de objetos
del patrón *Adapter*. Decimos entonces que ``TextForm`` es un adaptador.

Cuándo usar este patrón
~~~~~~~~~~~~~~~~~~~~~~~

-  Si se quiere usar una clase existente y su interfaz no concuerda con
   la que necesita.

Ejemplo de implementacion
~~~~~~~~~~~~~~~~~~~~~~~~~

Supongamos que tenemos una serie de clases que hacen un analisis de
nuestra maquina, y un script que muestra el estado general del sistema,
con el siguiente codigo:

.. code:: ipython3

    class CPU:
    
        def info(self):
            return 'Intel i8 6 cores'
    
    class Memory:
        
        def info(self):
            return '64 GB'
    
    print("Information on this computer:")
    for Cls in (CPU, Memory):
        instance = Cls()
        print(f" - {Cls.__name__}: {instance.info()}")



.. parsed-literal::

    Information on this computer:
     - CPU: Intel i8 6 cores
     - Memory: 64 GB


Nuestra interfaz para estos objetos que devuelven informacion del
sistema es, basicamente, que se puedan crear instancias sin ningun
parámetro y que tengan un metodo ``info`` que devuelva la informacion
requerida.

Ahora, supongamos que tenemos una libreria como ``socket``, que me
permite descubrir el nombre de la maquina:

.. code:: ipython3

    import socket
    
    socket.gethostname()




.. parsed-literal::

    'nova'



El problema es que las ingterfaces no coinciden. ``socket`` es un
módulo, no una clase. ``gethostname`` es una función, no un método, y
además su nombre no corresponde con ``info``.

PAra estos casos nació el patrón *Adapter*. Solo necesitamos una nueva
clase *adaptadora* que use nuestro esquema de llamadas para realizar las
llamadas a la interfaz de ``socket``.

.. code:: ipython3

    import socket
    
    class Hostname:
        def __init__(self):
    
            self.gethostname = socket.gethostname
            
        def info(self):
            return self.gethostname()
    
    
    print("Information on this computer:")
    for Cls in (CPU, Memory, Hostname):
        instance = Cls()
        print(f" - {Cls.__name__}: {instance.info()}")


.. parsed-literal::

    Information on this computer:
     - CPU: Intel i8 6 cores
     - Memory: 64 GB
     - Hostname: nova


**Ejercicio**: La librería estándar ``sys`` tiene una función llamada
``platform`` que nos da informacion acerca del sistem operativo en que
se esta ejecutando Python. Podriamos incluir esta informacion en nuestro
listado, pero de nuevo, la interfaz no concuerda. ¿Puede escribir un
adaptador para integrar esa información en nuestro script

.. code:: ipython3

    import sys
    
    sys.platform




.. parsed-literal::

    'linux'



.. code:: ipython3

    # %load adapter.py
    import sys
    import socket
    
    
    class CPU:
    
        def info(self):
            return 'Intel i8 6 cores'
    
    
    class Memory:
    
        def info(self):
            return '64 GB'
    
    
    class Hostname:
        def __init__(self):
            self.hostname = socket.gethostname()
    
        def info(self):
            return self.hostname
    
    
    class Platform:
    
        def info(self):
            return sys.platform
    
    
    print("Information on this computer:")
    for Cls in (CPU, Memory, Hostname, Platform):
        instance = Cls()
        print(f" - {Cls.__name__}: {instance.info()}")



.. parsed-literal::

    Information on this computer:
     - CPU: Intel i8 6 cores
     - Memory: 64 GB
     - Hostname: nova
     - Platform: linux


