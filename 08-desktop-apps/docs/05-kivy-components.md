---
title: Componentes kivy
---

## La clase Animation

Las clases `Animation` y `AnimationTransition`, definidas en el módulo
`kivy.animation`, sirven para animar propiedades de los controles. Es necesario
especificar el menos el nombre de una propiedad y un valor final u objetivo.
Para aplicar las animaciones, se realizan dos pasos: Primero se crea y define
la animación, y luego se aplica a un control o _widget_.

Por ejemplo, para animar las propiedades `x` e `y` de un control, tenemos que
crear la animación especificando esas propiedades, y los valores finales que
queremos que tengan después de la animación:

```python
anim = Animation(x=100, y=100)
```

Y luego se aplica la animación a un control determinado:

```python
anim.start(widget)
```

La animación tiene un tiempo de duración, que podemos definir usando el
parámetro `duration`. POr defecto, valdrá $1$ segundo.

Veamos el siguiente ejemplo, donde implementamos un botón que se mueve cuando
lo pulsamos.

```python
--8<--
docs/simple-animation.py
--8<--
```

Y su fichero kivy corespondiente:

```python
--8<--
docs/simple-animation.kv
--8<--
```

Otra propiedad de las animaciones es la `transition`. Si no se indica nada, la
animación se realiza de forma lineal, pero podemos indicar o bien en transición
personalizada o bien una cadena de texto nombres de transiciones ya
predefinidas e incluidas en la clase `AnimationTransition`. Como ejercicio,
hagamos que la transición anterior, en ves de ser lineal, use la transición
definida como 'in_back',

Las animaciones se puede encadenar, para que se ejecuten una después de otra, o
solapar, de forma que empiezan todas a la vez (Y, si tienen la misma duración,
terminar a la vez).

Para encadenar dos animaciones, solo hay que usar el operador `+`. La _suma_ de
dos o más animaciones es una nueva animación, que ejecuta todas las sumadas de
forma secuencial.

Para solapar dos animaciones, se hace de forma similar, pero con
el operador `&`. El resultado es una nueva 
animación, que ejecuta todas las anteriores de forma secuencial


Ejercicio: Cambiar la implementación de `move_it` para que se mueva 
a lugares al azar, y que cambien el fondo del boton tambien al azar, cada vez
que se pulsa el boton. Además, que la animación dure medio segundo, en vez de
uno.

```python
import random

...

    def move_it(self):
        pos_hint = {
            'center_x': random.random(),
            'center_y': random.random(),
            }
        anim_pos = Animation(pos_hint=pos_hint, duration=0.5, transition='out_bounce')

        color = [random.random(), random.random(), random.random(), 1]
        anim_color = Animation(background_color=color, duration=0.5)
        
        anim = anim_pos & anim_color
        
        pb_move = self.ids.pb_move
        anim.start(pb_move)
```



### La clase `RecicleView`

El propósito de esta clase es proporcionar un sistema para visualizar un
conjunto de datos grande de forna eficiente, visualizando solo los elementos
necesarios para la presentación.  De este forma el número de controles
necesarios para presentar los datos se mantiene al mínimo.

La vista se genera a partir de la propiedad `data`, que debe consistir en una
lista de diccionario. Los datos en el diccionario se usarán para crear el
*widget* necesario para su presentación.

En este componente se utiliza el patrón Modelo/Vista/Controlador, donde:

- **Modelo**: En este caso el modelo son los diccionarios que se pasan a la
  lista `data`.

- **Vista**: El código de las vistas está dividido entre los controles usados
  internamente y el propio *layout* del control

- **Controlador**: El controlador está implementado internamente y se ocupa de
  la lógica necesaria para que todo funciones, esta definido en la clase
  `RecycleViewBehavior`.

Estas clases son clases abstractas y en principio no hay que usarlas
directamente, si no que usamos implementaciones ya preparadas para trabajar.
Por defecto se usa la clase `RecycleDataModel` para el modelo, `RecycleLayout`
para la vista y ` RevicleView` para el controlador.

Cuando creamos una instancia de `RecycleView`, se crean automáticamente las
clases vista y modelo necesarias. Lo único que si tenemos que hacer nosotros en
crear el *layout* necesario y añadirlo a la clase `RecycleView`.

Veamos un ejemplo que muestra 25 botones:

El código Python:

```python
--8<--
docs/recycle-view-demo.py
--8<--
```

Que usa el fichero Kivy `recycle.kv`:

```
--8<--
docs/recycle.kv
--8<--
```

**Ejercicio**: Cambiar el tamaño de la lista a 1000. Comprueba que aun con un
tamaño grande de elementos a mostrar, la vista sigue igual de ágil. Cambiar el
control por una etiqueta.

### La clase `Scatter`

Un control de tipo `Scatter` está diseñado para que los elementos que contenga
se puedan mover, cambiar de tamaño, rotar, etc. mediante interacciones del
usuario (ya sea con un ratón o con gestos en una dispositivo móvil o en una
*tablet*) o por nuestro propio código. Además, estas transformaciones son
propiedades, que podemos usar para propagar estos cambios a cualquier otro
*widget*.

Para poder usarlo el primer paso, como siempre, es importarlo:

```python
from kivy.uix.scatter import Scatter
```

Vamos a necesitar una par de controles más: una etiqueta (`Label`) para mostrar
un texto, que irá anclada al control *scatter* , y un `FloatLayout` donde
podamos poner nuestras instancias de *scatter*, como nodo raíz de la ventana.

El código quedaría mas o menos así:

```python
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class TutorialApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text='Hello!', font_size=150)
```

Nótese que no usamos en este ejemplo ninguna de las propiedades del control
*LoatLayout* ni del *Scatter*, pero podemos usarlas como en cualquier otro
control, por ejemplo para desactivarlos e impedir la interacción con el
usuario, por ejemplo.

En este momento disponemos de tres *widgets*. Solo debemos retornar uno de
ellos para que sea usado como el control raíz por la aplicación.  Así que vamos
añadiéndolos en forma de árbol:

```python
class TutorialApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text='Hello!',
                  font_size=150)

        f.add_widget(s)
        s.add_widget(l)
        return f
```

Ahora el resto de los componentes esta almacenado de forma directa o indirecta
como descendientes del componente *FloatLayout*, que ahora ya puede actuar como
el control raíz de la aplicación. Ocupará todo el espacio disponible de la
ventana, pero lo único que podremos ver es la etiqueta, que deberíamos ser
capaces de mover, rotar y escalar.


### El control `ScrollView`

El control `ScrollView` proporciona un área para contener otros controles que
proporciona barras de desplazamiento, en una o en las dos dimensiones posibles.

Vamos a importar la función `runTouchApp()`. Con esta función conseguiremos que
el control se pueda usar con múltiples toques (_Usando más de un dedo_).

```python
from kivy.base import runTouchApp
```

Definiremos las propiedades de `ScrollView`:

```python
from kivy.base import runTouchApp
from kivy.lang import Builder

root = Builder.load_string(r'''
ScrollView:
    Label:
        text: 'Scrollview Example' * 100
        font_size: 30
        size_hint_x: 1.0
        size_hint_y: None
        text_size: self.width, None
        height: self.texture_size[1]
''')

runTouchApp(root)
```

### El control `Clock`

Con la clase `kivy.clock.Clock` podemos programar funciones para que se
ejecuten en determinados momentos. La clase nos proporciona un método
`schedule_interval` con el cual podemos indicar que un determinado método o
función debe ejecutarse cada cierto tiempo. Con esto podemos hacer un reloj
digital con muy poco código adicional.

Veamos primero el fichero _kivy_:

```kivy
--8<--
docs/simpleclock/simpleclock.kv
--8<--
```

Y el código Python:

```python
--8<--
docs/simpleclock/main.py
--8<--
```

**Ejercicio:** Usar la fuente incluida en [fonts/LCD.ttf](./fonts/LCD.ttf) para
la etiqueta de la hora. Cambiar el código para que sea una cuenta atrás desde
las '23:59:29'.

Si devolvemos `False` dentro de la función llamada por el reloj, el mecanismo
de llamada automático se desactiva, de forma que ya no se repite más.

En principio el _callback_ acepta un único parámetro, que es la diferencia de
tiempo en segundos entre la llamada actual y la anterior. Si queremos agregar
más parámetros, resulta muy conveniente el uso de `functools.partial`.

Igualmente, podemos usar lambda para recubrir una función que no acepte ningún
parámetro, o escribir un recubrimiento para ella.


### El control `ScreenManagar`

El control `ScreenMananer` esta diseñado para gestionar múltiples pantallas.
Por defecto, se muestra una pantalla completa cada vez y se usan unas
transiciones o animaciones básicas para pasar de una pantalla a otra. Las
animaciones básicas pueden ser sustituidas por nuestras propias animaciones, si
lo necesitamos.

Vamos a construir un `ScreenManager` con dos pantallas, a las que asignaremos
un nombre diferente a cada una. **Es obligatorio asignarle un nombre a cada
pantalla**, ya que se usará ese nombre para identificarlas a la hora de
pasar de una pantalla a otra.

La transición por defecto está definida en la clase `SlideTransition` y tiene
opciones para determinar tanto la dirección de la transición como la duración.

Una cosa a tener en cuenta es que la clase `Screen` no muestra nada en la
pantalla, es internamente una subclase de `RelativeView`. Es el control que va
dentro del _screen_ el que se debe encargar de esto, normalmente (pero no
necesariamente) algún tipo de _Layout Manager_.

En el siguiente ejemplo, creamos un gestor para dos pantallas, la primera
pantalla tiene un botón a la derecha que nos permite pasar a la segunda
pantalla. En esta hay un botón a la izquierda que realiza la función inversa;
nos permite regresar a la primera pantalla. En cada objeto de tipo `Screen` hay
una referencia al `ScreenManager` que lo contiene, en el atributo `manager`.

Usamos en este código el método `load_string` para cargar la definición de las
pantallas internamente, sin necesidad de usar un fichero externo:

```python
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<MenuScreen>:
    FloatLayout:
        Button:
            text: 'First Screen'
            on_press: root.manager.current = 'settings'
            pos_hint: {'right': 1, 'center_y': 0.5}
            size_hint: (None, None)
            size: ("196dp", "24dp")

<SettingsScreen>:
    FloatLayout:
        Button:
            text: 'Second Screen'
            on_press: root.manager.current = 'menu'
            pos_hint: {'x': 0, 'center_y': 0.5}
            size_hint: (None, None)
            size: ("196dp", "24dp")
""")

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class ScreenManagerApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm


def main():
    app = ScreenManagerApp()
    app.run()

if __name__ == '__main__':
    main()
```

El programa hace lo que tiene que hacer, pero se produce un efecto extraño al
volver a la primera pantalla, porque la animación por defecto es hacia la
derecha. Podemos cambiarlo modificando la propiedad `direction`, dentro del
objeto `transition` del `ScreenManager`. Una posible solución es:

```python
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<MenuScreen>:
    FloatLayout:
        Button:
            text: 'First Screen'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'settings'
            pos_hint: {'right': 1, 'center_y': 0.5}
            size_hint: (None, None)
            size: ("196dp", "24dp")

<SettingsScreen>:
    FloatLayout:
        Button:
            text: 'Second Screen'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
            pos_hint: {'x': 0, 'center_y': 0.5}
            size_hint: (None, None)
            size: ("196dp", "24dp")
""")

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class ScreenManagerApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm


def main():
    app = ScreenManagerApp()
    app.run()


if __name__ == '__main__':
    main()
```
