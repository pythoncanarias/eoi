### Propósito

Define una interfaz para crear un objeto, pero deja que sean las subclases
quienes decidan qué clase instanciar. Permite que una clase delegue en sus
subclases la creación de objetos.

### Entender el patron Factory

En programación orientada a obtjetos, el termino `factory` se refiere a una
clase que es reponsable de la creacion de objetos de otras clases.  Normalmente
la clase que actua como *factory* tiene un objeto con una serie de métodos. El
cliente llama a alguno de estos metodos con ciertos parámetros. Internamente, el
método crea los objetos y se los devuelve al cliente

Asi que la pregunta es: ¿Por qué necesitamos una clase *factory* aparte, cuando
el cliente podria crear directamente el objeto? La respuesta es que este patron
proporciona ciertas ventajas que puede que nos sean utiles o necesarias:

- La primera ventaja es que la creacion de un objeto puede ser independiente
  de su implementacion.

- El cliente no necesita saber nada de las clases que realmente crean el objeto.
  Solo necesita pasar la informacion que se necesita para crearlo. Esto
  simplifica la implementacion del cliente (las clases estan menos acopladas)

- Es sencillo añadir otra clase mas a la factoría, de forma que se puedan crear
  objetos de una nueva clase. El resto de las clases no se ve afectado. El
  cliente tendra que aceptar un nuevo parámetro o valor del mismo.

- La factoria también puede reutilizar objetos preexistentes. La clase original
  siempre cfeará un nuevo objeto.

Hay tres variantes de este patrón:

- **Simple Factory pattern**: Permite crear objetos sin exponer la lógica de creación
  de los mismos.

- **Factory method pattern**: Permite crear objetos sin exponer la lógica de creación
  de los mismos, pero retrasa la decisión de que subclase en concreto se usará
  para crear el objeto.

- **Abstract Factory pattern**: Crea los objetos sin necesidad de especificar 
  sus clases. El patron suministra objetos a partir de otra fabrica, que
  crea internamete.

Pero este patron es poco útil en Python, porque las capacidades dinámicas
y el hecho de que tanto funciones, metodos y clases sean objetos de primer
nivel, y por tanto susceptibles de ser pasados como parametros, almacenados
en estructuras de detos, etc. lo hacen en la práctica poco recomendable, a no
ser que la estructura de los objetos que estamos creando este cambiando 
muy frecuentemente.



### Simple Factory pattern

Esta es la forma más sencilla de este patrón. En este caso, la fábrica es
simplemente una función. 

Vamos a suponer que estamos creando un juego y queremos poder
crear varios tipos de enemigos. Tenemos las clases `Soldier` para
representar soldados, y `Tower` para torretas defensivas. 

Supongamos que deseamos desacoplar la creacion de los enemigos
del  conocimiento de estas clases (Quiza querramos cambiar las
clases, por ejemplo, podemos decidir que la clase `Tower` podria
muy bien reemplazarse por una clases `Soldier` con capacidad de
desplazamiento cero).

La forma más sencilla seria crear una clase o funcion *factory*


class Soldier:
    def __init__(self):
        self.movement = 10
        self.power = 10

class Tower:
    def __init__(self):
        self.power = 100

def make_enemy(kind):
    Enemies = {
        'soldier': Soldier,
        'tower': Tower,
    }
    _cls = Enemies(kind)
    return _cls

**Ejercicio**: Comprueba que el código anterior es capaz de crear enemigos 
de distino tipo. Cambia el codigo: para que podamos incluir un nuevo tipo
de enemigo, el 'mecha`, con capacidad de movimiento 5, y potencia de fuego 50.

Pista**: Tendras que crear una nueva clase `Mecha`, y modificar la función
`make_enemy` para que pueda crear objetos de esta nueva clase.

### Factory Method

Con esta variedad, definimos una interfaz para crear objetos, pero en
vez de ser la funcion/objeto/clase la responsable de crear los objetos,
esta responsabilidad es delegada a las subclases, que deciden entonces
que clase debe ser instanciada

La creacion de los objetos es por tanto mediante herencia y no por
instanciacio.

Lo que conseguimos con esto es hacer el diseño mas personalizable. Puede
devolver una misma instancia o subclases en vez de un objeot de un tipo
determinado, como en el *Simple Factory*



The following points help us understand the factory method pattern:

We define an interface to create objects, but instead of the factory being responsible for the object creation, the responsibility is deferred to the subclass that decides the class to be instantiated.
The Factory method creation is through inheritance and not through instantiation.
The Factory method makes the design more customizable. It can return the same instance or subclass rather than an object of a certain type (as in the simple factory method).
### 




For some, Simple Factory is not a pattern in itself. It is more of a concept that developers need to know before they know more about the Factory method and Abstract Factory method. The Factory helps create objects of different types rather than direct object instantiation.

Let's understand this with the help of the following diagram. Here, the client class uses the Factory class, which has the create_type() method. When the client calls the create_type() method with the type parameters, based on the parameters passed, the Factory returns Product1 or Product2:

from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")

class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


## forest factory defined
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()

## client code
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)


