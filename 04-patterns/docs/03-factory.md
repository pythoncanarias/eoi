---
title: El patrón Factory
---

### Propósito

Define una interfaz para crear un objeto, pero deja que sean las subclases
quienes decidan qué clase instanciar. Permite que una clase delegue en sus
subclases la creación de objetos.

### Motivación

En programación orientada a objetos, el termino `factory` se refiere a una
clase que es responsable de la creación de objetos de otras clases.
Normalmente la clase que actúa como *factory* tiene un objeto con una serie de
métodos. El cliente llama a alguno de estos métodos con ciertos parámetros.
Internamente, el método crea los objetos y se los devuelve al cliente

Así que la pregunta es: ¿Por qué necesitamos una clase _factory_ aparte, cuando
el cliente podría crear directamente el objeto? La respuesta es que este patrón
proporciona ciertas ventajas que puede que nos sean útiles o necesarias:

- La primera ventaja es que la creación de un objeto puede ser independiente de
  su implementación.

- El cliente no necesita saber nada de las clases que realmente crean el
  objeto. Solo necesita pasar la información que se necesita para crearlo. Esto
  simplifica la implementación del cliente (las clases están menos acopladas)

- Es sencillo añadir otra clase más a la factoría, de forma que se puedan crear
  objetos de una nueva clase. El resto de las clases no se ve afectado. El
  cliente tendrá que aceptar un nuevo parámetro o valor del mismo.

- La factoría también puede reutilizar objetos preexistentes. La clase original
  siempre creará un objeto nuevo.

Hay tres variantes de este patrón:

- **Simple Factory pattern**: Permite crear objetos sin exponer la lógica de
  creación de los mismos.

- **Factory method pattern**: Permite crear objetos sin exponer la lógica de
  creación de los mismos, pero retrasa la decisión de que subclase en concreto
  se usará para crear el objeto.

- **Abstract Factory pattern**: Crea los objetos sin necesidad de especificar
  sus clases. El patrón suministra objetos a partir de otra fabrica, que crea
  internamente.

Pero este patrón es poco útil en Python. Las capacidades dinámicas del lenguaje
y el hecho de que funciones, métodos y clases sean todos objetos de primer
nivel (por tanto, susceptibles de ser pasados como parámetros, almacenados en
estructuras de datos, etc.) lo hacen en la práctica poco recomendable. Un caso
en el que podría tener sentido es cuando la estructura de los objetos que
estamos creando este cambiando muy frecuentemente.

Veremos solo el *Simple Factory pattern*, ya que los demás casos son raramente
aplicables en Python.

### Simple Factory pattern

Esta es la forma más sencilla de este patrón. En este caso, la fábrica es
simplemente una función.

Vamos a suponer que estamos creando un juego y queremos poder crear varios
tipos de enemigos. Tenemos las clases `Soldier` para representar soldados, y
`Tower` para torretas defensivas.

Supongamos que deseamos desacoplar la creación de los enemigos del conocimiento
de estas clases. Puede haber varias razones para esto, pensemos como ejemplo
que estamos probando a cambiar las clases, por ejemplo, podemos decidir que la
clase `Tower` podría muy bien reemplazarse por una clases `Soldier` con
capacidad de desplazamiento cero.

La forma más sencilla sería crear una clase o función _factory_:

```python
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
```

La salida del código anterior sería:

```
Soldier Tower
```

**Ejercicio**: Comprueba que el código anterior es capaz de crear enemigos de
distinto tipo. Cambia el código para que podamos incluir un nuevo tipo de
enemigo, el `mecha`, con capacidad de movimiento $5$, potencia de fuego $50$.

![Mecha from Battletech](img/battletech.jpg)

**Pista**: Tendrás que crear una nueva clase `Mecha`, y modificar la
función `make_enemy` para que pueda crear objetos de esta nueva clase.

```python
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
```
