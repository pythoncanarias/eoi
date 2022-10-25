#!/usr/bin/env python
# 

"""
# Actor: Una clase para poder tener diferentes tipos de agentes en un juego.

Los actores tienen todos las siguientes características comunes:

 - `x` e `y`: Posicion en el espacio
 - `name`: Nombre del actor
 - `next_action`: Ejemplo de otros atributos comunes

Y acepta de forma opcional estos componentes:

 - `brain`
 - `weapon`.
 - `fly`.

Si el actor tiene definido `brain` entonces puede ejectur la accion `think`, si no
esta definido, `think` aun puede ser llamada pero no va a ejecutar
nada ni devolver nada. Lo mismo con la clase `weapon`, si esta definido
permite realizar ataques con el metodo `attack`, si no, el metodo se
puede invocar pero no hara nada. 

Para añadir un nuevo componente:

1) Añadir el nombre del componente al atributo `__components__` de la clase Actor

2) Para cada _verbo_ (metodo) del componente, definir una forma simplificada para
   llamar directamente desde el actor. Por ejemplo, si definimos el motodo
   `think` asi:

        ```Python
        def think(self):
            self.brain.think()
        ```

    Esto nos permite llamar a `think` desde el propio actor:

        >>> hommer = Actor(10, 20, 'Hommer', brain=HommerBrain())  # Simple brain, no weapons
        >>> hommer.think()
    
    O no definirlo, si preferimos llamar al metodo cualificando con el componente:

        >>> hommer = Actor(10, 20, 'Hommer', brain=HommerBrain())  # Simple brain, no weapon
        >>> hommer.brain.think()

3) Si el componente solo tiene un metodo, quiza mejor usar un componente que solo
define el metodo __call__, para que pueda ser invocado directamente. Vease el ejemplo
del componente Fly.


Todos los componentes se derivan de la clase base Component para poder vincularlos
con el actor con el que estan asociado.
"""


# Components


class Component:

    def __init__(self, owner=None):
        self.owner = owner


class NullComponent(Component):
    """Null Component. Allow us to call any method on this component
    but do nothing, return always `None`.
    """
    
    def __getattr__(self, name):
        return self
    
    def __call__(self, *args, **kwars):
        return


# Brain components. We don't need common base class, just a `think` method

class HommerBrain(Component):
    
    def think(self):
        print('{} says Duh!'.format(self.owner.name))


class SocratesBrain(Component):
    
    def think(self):
        print("{} said: Conocete a ti mismo".format(self.owner.name))


# Weapon components. Same as before, just need an `attack` method

class Weapon(Component):

    def __init__(self, power_level=10, owner=None):
        super().__init__(owner=owner)
        self.power_level = power_level


class CryAsBaby(Weapon):

    def attack(self):
        print('{} cry with power {}'.format(self.owner.name, self.power_level))


class Mjolnir(Weapon):

    def attack(self):
        print('{} use a sledgehammer with power {}'.format(self.owner.name, self.power_level))


# Fly component


class Fly(Component):
    def __call__(self):
        print('{} is flying now'.format(self.owner.name))
        return True


class Actor:
    """Una clase para poder tener diferentes tipos de agentes en un juego.
    """

    __components__ = ['brain', 'weapon', 'fly']
    __slots__ = ['x', 'y', 'name', 'next_action'] + __components__
    
    def __init__ (self, x, y, name, **components):
        self.x = x
        self.y = y
        self.name = name
        self.next_action = None
        for name in Actor.__components__:
            if name in components:
                component = components[name]
                component.owner = self
            else:
                component = NullComponent(self)
            setattr(self, name, component)
                
    def __str__(self):
        return self.name

    def set_component(self, tag, comp):
        comp.owner = self
        setattr(self, tag, comp)

    def think(self):
        self.brain.think()
        
    def attack(self):
        self.weapon.attack()


def main():
    
    hommer = Actor(10, 20, 'Hommer', brain=HommerBrain())  # Simple brain, no weapons
    socrates = Actor(10, 20, 'Socrates', brain=SocratesBrain())  # Awesome brain, no weapons
    trump = Actor(10, 30, 'Donald', weapon=CryAsBaby())  # No brian, weapon is cry-as-a-baby

    hommer.think()  # Must output 'Duh!'
    socrates.think() # Must output "Conocete a ti mismo"
    trump.think()  # No error here, even if trump has no brain. No output.

    hommer.attack()  # Same here, hommer has no weapon, so we do nothing
    socrates.attack()  # Also socrates has no weapon
    trump.attack()  # Trump has a weapon, so he can attack. Output is "Cry with power 10"

    # Change componentes in the instance, in real time
    hommer.set_component('brain', SocratesBrain())
    hommer.think()  #  must output "Conocete a ti mismo"

    # Components can be single callables
    angel = Actor(0, 0, 'Angel', fly=Fly())
    angel.fly()
    hommer.fly()  # Still not

    # You can create an actor adding components in run time 
    thor = Actor(10, 40, 'Thor')
    thor.set_component('brain', SocratesBrain())
    thor.set_component('weapon', Mjolnir(power_level=2500))
    thor.set_component('fly', Fly())

    thor.think()
    thor.attack()
    thor.fly()



if __name__ == '__main__':
    main()
