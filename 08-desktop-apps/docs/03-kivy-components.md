---
title: Componentes kivy
---

## RecicleView

El proposito de esta clase es proporcinar un sistema para
visualizar un conjunto de datos grande de forna eficiente, visualizando solo los elementos necesarios para la presentacion.
De este forma el numero de controles necesarios para presentar
los datos se mantiene al minimo.

La vista se genera a partir de la propiedad `data`, que debe consistir en una lista de diccionario. Los datos en el dicianario se usaran para crear el widget necesario para su presentacion.

En este componente se utiliza el patron Modelo/Vista/Controlador, donde:

- Modelo: En este caso el modelo son los diccionarios que se pasan a la lista `data`.


- Vista: El codigo de las vistas esta dividido entre los controles
usados internamente y el propio layout del control

- Controlador: El controlador esta implmentado internamente y se ocupa de
la logica necesaria para que todo funciones, esta definido en 
la clase `RecycleViewBehavior`.

Estas clases son clases abstrabtas y en principio no hay que usarlas directamente, sini que usamos implementaciones ya
preparadas para trabajar. Por defecto se usa la clase `RecycleDataModel` para el modelo, `RecycleLayout` para la
vista y `
RevicleView` para el controlador.

Cuando creamos una instancia de `RecycleView`, se crean automaticamente las clases vista y modelo necesarias. Lo úunico que si tenemos que hacer nosotors en crear el Layout necesario y añadirlo a la clase `RecycleView`.

Veamos un ejemplo que muestra 25 botones:

El codigo python:
```
{% include 'recycle-view-demo.py' %}
```

que usa el fichero kivy `recycle.kv`:

```
{% include 'recycle.kv' %}
```

**Ejercicio**: Cambiar el tamaño de la lista a 1000. Comprueba que aun con un tamaño grande de elemenntos a mostrar, la vista sigue mas o menos igual de agil. Cambiar el control por una etiqueta.

## Scatter

Un control de tipo Scatter esta diseñado para que puedan
se puebda mover, cambiar de tamaño, rotat, etc. mediante
interacciones del usuario (ya sea con un raton o con
gestos en una dispostivio movil o tablet) o por nuestro
propio codigo. Ademas, estas transformaciones ton propiedades, que puene ser usadas para porpagar estos cambios a cuaquier 
otro widget.

from kivy.uix.scatter import Scatter

Vamos a necesitr una par de controles mas: una etiqueta (`Label`)
para mostrar un texto, que ira anclada al contro scatter , y un `FloatLayout` donde podamos poner nuestras instancias de scatter, como nodo raiz de la ventana.

El codigo quedaria mas o menos asi:


from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
Now, instead of making a button we’ll need to instantiate our new widgets.

class TutorialApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text='Hello!',
                  font_size=150)
Note here that the floatlayout and scatter don’t have any special properties set, but we could do stuff like disable the scatter’s touch interaction at this point if we wanted to.

At this point we have three widgets - different to before where we only had a single button! We can only return one of these widgets to be the application’s root widget, so the others will have to be child widgets added to one of the other ones. We do this by adding each widget to a different widget above it.

class TutorialApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text='Hello!',
                  font_size=150)

        f.add_widget(s)
        s.add_widget(l)
        return f
Now everything is added below the floatlayout, which is returned to become the application’s root widget - it will fill the screen (though it has no visual representation so we won’t be able to see it), but we will be able to see the label that we should be able to move around by interacting with the scatter that contains it.


### ScrollView

The ScrollView in Kivy provides a scrollable view. Using scrollview, we can scroll through the x-axis as well as the y-axis on the screen.

First, we will import a new function called runTouchApp(). This function will make our scrollview touch-enabled.

```python
from kivy.base import runTouchApp
```

We will define the scrollView as follows:

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

## Clock

Cocn la clase `kivy.clock.Clock` podemos
programar funciones para que se ejecuten
en determinados momentos. La clase nos proporciona
un método  `schedule_interval` con el cual podemos
indicar que un determinado método o función debe 
ehecutarse cada cierto tiempo. Con esto podemos
hacer un reloj digital con muy poco codigo adicional.

Veamos prrimero el fichero kivy:

```
{% include 'simpleclock.kv' %}
```

Y el codigo python:

```
{% include 'simpleclock.py' %}
```

**Ejercicio:** Usar la fuente incluida
 en [fonts/LED.ttf](./fonts/LEF.ttf)
 para la etiqueta de la hora. Cambiar el codigo 
 para que sea una cuenta atras desde las
 '23:59:29'.

Si devolvemos `False` dentro de la funcion llamada
por el reloj, el mecanismo de llamada automatico
se desactiva, de forma que ya no se repetiora mas.

En principio el callback solo acepta un unico parámetro, que es la diferencia de tiempo en segundos entre la llamada actual y la anterios. Si queremos agregar más parámetros, eresulta muy coveniente el uso de `functools.partial`.

Igualemente, podemos usar lambda para recubrir una funcion
que no acepte ningun parámetro, o escribir una recubrimiento
para ella.


### ScreenManagar

El control `ScreenMananer` esta disenañado para gestionar multiples pantallas.
Por defecto, se muestra una pantalla completa cada vez y se usan unas
transiciones o animaciones básicas para pasar de una pantalla a otra. Las
animaciones básicas pueden ser sustituidas por nuestras propias animaciones, si
lo necesitamos.

Vamos a construir un `ScreenManager` con dos pantallas, a las que asignaremos
un nombre diferente a cada una. **Es obligatorio asignarla  un nombre a cada
pantalla**, ya que se usará ese nombre para identificarlas a la hora de
pasar de una pantalla a otra.

La transición por defecto está definida en la clase `SlideTransition` y tiene
opciones para determinar tanto la direción de la transición como la duración.

Una cosa a tener en cuenta es que la clase `Screen` no muestra nada en la
pantalla, es internamente una subclase de `RelativeView`. Es el control que va
dentro del screen el que se debe encargar de esto, normalmente (pero no
necesariamente) algún tipo de Layout Manager.

En el siguiente ejemplo, creamos un gestor para dos pantallas, la primera
pantalla tiene un boton a la derecha quen os permite pasar a la segunda
pantalla. En esta hay un boton a la izquienrda que realiza la función inversa,
nos permite regresar a la primera pantalla. En cada objeto de tipo `Screen` hay
una referencia al ScreenManager que lo contiene, en el atributo `manager`.

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
