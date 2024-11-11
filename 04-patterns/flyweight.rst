El patrón *Flywight* (Peso ligero)
========================================================================

.. index:: Flyweight (Patrón)

Propósito
------------------------------------------------------------------------

Compartir estado para permitir un gran número de objetos de grano fino
de forma eficiente.

Motivación
------------------------------------------------------------------------

Un peso ligero es un objeto con estado compartido, que puede usarse a la
vez en varios contextos. El peso ligero se comporta como un objeto
independiente en cada contexto; esto es, no se puede distinguir de una
instancia del objeto que no esté compartida.

Lo fundamental aquí es la distinción entre estado *intrínseco* y
*extrínseco*.

El **estado intrínseco** se guarda con el propio objeto; consiste en
información que es independiente de su contexto y que puede ser, por
tanto, compartida.

El **estado extrínseco** depende del contexto y cambia con él, por lo
que no puede ser compartido. Los objetos cliente son responsables de
pasar al peso ligero su estado extrínseco cuando lo necesite.

Los pesos ligeros modelan conceptos o entidades que normalmente son
demasiado numerosos como para ser representados con objetos.

Un ejemplo gráfico podría ser un objeto en un videojuego que represente
a un árbol.

Queremos usar varios de estos objetos para representar un bosque, pero
en realidad vemos que gran parte de los atributos, como las texturas a
usar para pintar el árbol, el modelo *mesh* para la estructura básica,
etc. son iguales para todos los objetos. Estos serian atributos
*extrínsecos*.

Otros atributos, como la posición (``x``, ``y``, ``z``), efectos de
escala, rotación, etc. son, sin embargo, propios de cada árbol. Son los
atributos *intrínsecos*.

Con la clase *Flyweight*, las instancias comparten todos los datos
comunes, de forma que el tamaño de la instancia es considerablemente
menor, y el consumo de memoria también se reduce drásticamente,

Aplicabilidad
------------------------------------------------------------------------

Debería aplicarse el patrón cuando se cumpla **todo** lo siguiente:

- Una aplicación utiliza un gran número de objetos.

- Los costes de almacenamiento son elevados debido a la gran cantidad
  de objetos.

- Gran parte del estado del objeto puede hacerse extrínseco.

**Ejercicio**: Volvemos a nuestro juego imaginario. Ahora estamos
probando otro prototipo para la IA. Esto no tarda prácticamente nada en
inicializarse, el problema es que ocupa muchísimo espacio. Y la cosa es
que todos los enemigos usan la misma IA, con lo que cada enemigo ocupa
muchísima memoria.

La siguiente celda define una función que ayuda a calcular el tamaño en
bytes que ocupa una variable, en Python. No es una tarea tan sencilla
como pudiera parecer, pero lo bueno es que puedes usarla sin entender
todos los detalles:

:: code:: python

    import sys
    from types import ModuleType, FunctionType
    from gc import get_referents
    
    # Custom objects know their class.
    # Function objects seem to know way too much, including modules.
    # Exclude modules as well.
    BLACKLIST = type, ModuleType, FunctionType
    
    
    def getsize(obj):
        """sum size of object & members."""
        if isinstance(obj, BLACKLIST):
            raise TypeError('getsize() does not take argument of type: '+ str(type(obj)))
        seen_ids = set()
        size = 0
        objects = [obj]
        while objects:
            need_referents = []
            for obj in objects:
                if not isinstance(obj, BLACKLIST) and id(obj) not in seen_ids:
                    seen_ids.add(id(obj))
                    size += sys.getsizeof(obj)
                    need_referents.append(obj)
            objects = get_referents(*need_referents)
        return size

Usando la función ``getsize``, vemos que los enemigos realmente ocupan
demasiado memoria (Mas considerando lo poco que hacen por ahora):

.. python::

    class IA: 
        def __init__(self):
            self.space = [0] * 1000000
    
    class Enemy:
        IA = None
        
        def __init__(self, name="prototype"):
            self.name = name
            if Enemy.IA is None:
                Enemy.IA = IA()
    
        def __repr__(self):
            return f'Enemy({repr(self.name)})'
    
    for i in range(3):
        e = Enemy(f"enemy_{i}")
        print(f"{e} ocupa {getsize(e)} bytes")
    getsize(Enemy.IA)


    Enemy('enemy_0') ocupa 224 bytes
    Enemy('enemy_1') ocupa 224 bytes
    Enemy('enemy_2') ocupa 224 bytes


Ejercicios
------------------------------------------------------------------------

**Ejercicio**: Resuelve el problema usando el patrón *Flyweight*.
Modifica solo la clase ``Enemy``, la clase ``IA`` no se puede tocar.

**Pregunta**: Cuales son los atributos extrínsecos de la clase ``Enemy`` y
cuáles son los intrínsecos.

**Pregunta**: Que otro patrón podríamos haber usado para garantizar que
solo tenemos una instancia a la vez de la IA?

.. literalinclude:: flyweight.py
  :language: python
