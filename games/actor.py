#!/usr/bin/env python
# 

"""
# Actor: Una clase para poder tener diferentes tipos de agentes en un juego.

Los actores tienen todos las siguientes características comunes:

 - `x` e `y`: Posicion en el espacio
 - `name`: Nombre del actor
 - `next_action`: Ejemplo de otros atributos comunes

Y acepta de forma opcional estos dos componentes:

 - `brain`
 - `weapon`.

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

        >>> hommer = Actor(10, 20, 'Hommer', brain=HommerBrain())  # Simple brain, no weapons
        >>> hommer.brain.think()

"""

class NullComponent:
    """Null Component. Allow us to call any method on this component
    but do nothing, return always `None`.
    """
    
    def __getattr__(self, name):
        return self
    
    def __call__(self, *args, **kwars):
        return


class Actor:
    """Una clase para poder tener diferentes tipos de agentes en un juego.
    """

    __components__ = ['brain', 'weapon']
    __slots__ = ['x', 'y', 'name', 'next_action'] + __components__
    
    def __init__ (self, x, y, name, **components):
        self.x = x
        self.y = y
        self.name = name
        self.next_action = None
        for name in Actor.__components__:
            setattr(self, name, components.get(name, NullComponent()))
                
    def __str__(self):
        return self.name

    def think(self):
        self.brain.think()
        
    def attack(self, level=10):
        self.weapon.attack(level)


# Components

# Brain components. We don't need common base class, just a `think` method

class HommerBrain:
    
    def think(self):
        print('Duh!')


class SocratesBrain:
    
    def think(self):
        print("Conocete a ti mismo")


# Weapon components. Same as before, just need an `attack` method


class CryAsBaby:
    
    def attack(self, power=10):
        print('Cry with power {}'.format(power))
        

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
    hommer.brain = SocratesBrain()
    hommer.think()  #  must output "Conocete a ti mismo"


if __name__ == '__main__':
    main()
