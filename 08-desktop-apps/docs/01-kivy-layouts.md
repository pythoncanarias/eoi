---
title: Kivy layouts
---
## Introducción a kivy
![Logo de Kivy](Kivy_logo.png)

Como vimos antes, hay dos dosas que diferencian a Kivy de la matoría de otros 
frameworks:

1) En vez de imitar o utilizar los controles nativos de la plataforma, de forma
que nuestras aplicaciones sean lo mas pareciadas posiblesa aplicaciones nativas,
kivy abraza el concepto opuesto: las aplicaciones kivy se parecen todas entre
si, independientemente de la platforma que hay por debajo, y los controles son
todos especificos.

2) Define un a lenguaje propio, llamado a menudo **kvlang**, con el proposito de
definir la organizaci'on, disposicióon o *layout* de los controles en las
pantallas. No es estrictamente necesario usar este lenguaje, pero es verdad que
muchas de los pasos a dar para definir la disposicion en pantalla se simplifica
mucho usandolo.

Vamos a partir del programa "hola, mundo" en kivy que vimos antes para dividirlo
en dos, el programa en si y el fichero con extension `.kv` que define la
disposicion de la interfaz:

```python
from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):

    def build(self):
        self.btn = Button(
           text="Hello World",
           size_hint=(0.4,0.05),
           pos_hint={'x': 0.3, 'y': 0.5}
           )
        return self.btn


def main():
    app = MainApp() 
    app.run()
```

Lo primero que necesitamos saber es que kivy tiene una regla por defecto para
vincular el programa python con el fichero .kv a utilizar para la disposicion  o
*layout*. Tampoco es estríctamente necesrio seguir esta regla, solo es una
ayuda, pero la mayoria de los programas lo hacen asi porque resulta muy comodo.

La regla es la siguiente: Dentro de nuestro programa, habrá un unico elemnto,
que representa la aplicacion, y que será o bien una instancia de la clase `App`
directamente o, mas frecuentemente, una clase derivada de `App` (En el código de
ejemplo, es la clase `MainApp`).  En ese caso, kivy tomara el nombre de la
clase, le quitara en sufijo `App` si lo tuviera, pasara el resto a minúsculas (En nuestro
caso, `main`), y buscará un fichero con ese mismo nombre y extenisión '.kv' (En
nuestro caso `main.kv`).

Vamos entonces a guardar el fichero de ejemplo como `main.py`. Ahora
vamos a especificar la disposicion de nuestros controles en
un fichero,

```kvlang
{% include 'main.kv' %}
```

y en otro `main.py`:

```python
{% include 'main.py' %}
```

Ya no hace falta que importemos `Button`, pues será instanciado a parit del ficher `.kv`. La 
uncion `builder` tampoco hace falta, ya que se creara 
atomáticamnte siguiendo la regla antes descrita.

Fichero kivy -> reglas

parte izquierda: identificadores
parte derecha: codigo python
nuncas se usa =

**Ejercicio**: Añadir un control de tipo Label con el texto "Que tal"

Añadir Label. Que pasa? Error. Solo un widget en el raiz.

Definir Layouts -> Widgets especializados en contenter otros widgets

### BoxLayout

Ejemplo BoxLayout

```python
{% include 'boxlayout.py' %}
```

Fichero kivy:

```python
{% include 'boxlayout.kv' %}
```


**Ejercicio**: Añadir un par mas de botones. Ver que el orden se corresponde con
el orden en que se añadieron los *widgets*

### GridLayout

Ver GridLayout
cols o rows

```python
{% include 'gridlayout.py' %}
```

Fichero kivy:

```python
{% include 'gridlayout.kv' %}
```




### StackLayout

Ver StackLayout

```python
{% include 'stacklayout.py' %}
```

Fichero kivy:

```python
{% include 'stacklayout.kv' %}
```


**Ejercicio**: Hacer los botones mas anchos. Añadir mas botones, Ver lo que pasa. Cambiar tamaño de la ventana
Cambiar la orientacion

'lr' vs 'rl'
'tb' vs 'bt'

orientation: "lt-tb"

RelativeLayout

This layout operates in the same way as FloatLayout does, but the positioning properties (pos, x, center_x, right, y, center_y, and top) are relative to the Layout size and not the window size.

Las propiedades `size_hit` y `pos_hist` trabajn con coordenadas proporcionales, de forma que sus valores siempre estan comprendidos entre 0 y 1. La coordenada 0,0 seria la esquina inferior izquierda (kivy usa un sistema de coordenadas diferente al que vimos en Pillow
o en css por ejemplo, aqui el cero para la Y esta aabajo).

La coordenada 1,1 es la ezquina superior derecha.

La propiedad pos_hint es similar, pero en vez de psarle una tupla se le pasa un diccionario, donde dependiendo de la clave ('x' o 'top' por ejemplo) conseguimos uno u otro resultado: `x` se refiere sempre al borde izquierdo

![pos hints](float-pos-hints.png)

In the floatlayout.kv code file, we use two new properties, size_hint and
pos_hint, which work with the proportional coordinates with values ranging from
0 to 1; (0, 0) is the bottom-left corner and (1, 1) the top-right corner. For
example, the size_hint on line 83 sets the width to 40 percent of the current
window width and the height to 30 percent of the current window height.
Something similar happens to the pos_hint but the notation is different: a
Python dictionary where the keys (for example, 'x' or 'top') indicate which part
of the widget is referenced. For instance, 'x' is the left border. Notice that
we use the top key instead of y in line 88 and right instead of x in line 91.
The top and right properties respectively reference the top and right edges of
the Button, so it makes the positioning simpler.

Aunque estas propiedades simplifican mucho el posicionamiento, avitando calculos
y haciedo el codigo mas claro, seguimos pudiendo usar los valores `x` w `y`
para posicionar los widgets. Por ejemplo, `{'x': .85, 'y': 0}` pondria la x del control al 86 por cierto del ancho total disponible.

Anadir controles por porgrama

### RelativeLayout

Este *layout* funciona igual que el Floatlayout, pero sus propiedades relativas a la
posicion (`pos`, `x`, `center_x`, `right`, `y`, `center_y` y `top`) tiene como referencia el tamaño del Layout, no el de la ventana.

### PageLayout

PageLAyout.Uso. Cambiar color de los botones para poder apreciar mejor el cambio depagina


