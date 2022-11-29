---
title: Kivy layouts
---

## Introducción a kivy Layouts

![Logo de Kivy](Kivy_logo.png)

Como vimos antes, hay dos cosas que diferencian a _Kivy_ de la mayoría de
_frameworks_:

1) En vez de imitar o utilizar los controles nativos de la plataforma, de forma
que nuestras aplicaciones sean lo más parecidas posibles a aplicaciones nativas,
se abraza el concepto opuesto: las aplicaciones _kivy_ se parecen todas entre
si, independientemente de la plataforma que hay por debajo, y los controles son
todos específicos.

2) Define un a lenguaje propio, llamado a menudo **kvlang**, con el propósito
de definir la organización, disposición o *layout* de los controles en las
pantallas. No es estrictamente necesario usar este lenguaje, pero es verdad que
en muchos casos se simplifica mucho esta parte.

Vamos a empezar modificando el programa "hola, mundo" en _kivy_,que vimos en el
tema anterior. Vamos a dividirlo en dos, el programa en si y un fichero con
extensión `.kv` que define la disposición o _layout_ de la interfaz:

Este sería el código Python inicial:

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

Lo primero que necesitamos saber es que Kivy tiene una regla por defecto para
vincular el programa Python con el fichero .kv a utilizar para la disposición
o *layout*. Tampoco es estrictamente necesario seguir esta regla, solo es una
ayuda, pero la mayoría de los programas lo hacen así, porque resulta muy
cómodo.

La regla es la siguiente: Dentro de nuestro programa, habrá un único elemento,
que representa la aplicación, y que será o bien una instancia de la clase `App`
directamente o, mas frecuentemente, una instancia de una clase derivada de
`App` (En el ejemplo, es la clase `MainApp`).  En ese caso, Kivy tomara el
nombre de la clase, le quitara en sufijo `App` si lo tuviera, pasará el resto a
minúsculas (En nuestro caso, `main`), y buscará un fichero con ese mismo nombre
y la extensión '.kv'. En nuestro ejemplo, buscará un fichero llamado `main.kv`.

Vamos entonces a guardar el fichero de ejemplo como `main.py`. Ahora vamos a
especificar la disposición de nuestros controles en un fichero,

```kvlang
{% include 'main.kv' %}
```

y en otro `main.py`:

```python
{% include 'main.py' %}
```

Algunas cosas a tener en cuenta:

1) Ya no hace falta que importemos `Button`, pues será instanciado a partir del
fichero `.kv`.

2) El método `builder` tampoco hace falta. Normalmente es el encargado de
construir el _layout_ de la aplicación en el inicio, pero en este caso se
generará también de forma automática a partir del contenido del fichero
`main.kv`.

### Estructura de los ficheros `.kv`

Fichero kivy -> reglas

parte izquierda: identificadores
parte derecha: codigo python
nunca se usa =


**Ejercicio**: Añadir un control de tipo _Label_ con el texto "Que tal"

Añadir Label. Que pasa? Error. Solo es posible tener un único elemento
raiz.

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


**Ejercicio**: Hacer los botones más anchos. Añadir más botones, Ver lo que pasa. Cambiar tamaño de la ventana
Cambiar la orientación.

'lr' vs 'rl'
'tb' vs 'bt'

orientation: "lt-tb"

### El _layout_ RelativeLayout

Este control funciona de forma similar al `FloatLayout`, pero las propiedades
relativas a la posición (`pos`, `x`, `center_x`, `right`, `y`, `center_y` y
`top`) son relativas al tamaño del control, no al tamaño de la ventana.

Las propiedades `size_hit` y `pos_hist` trabajan con coordenadas
proporcionales, de forma que sus valores siempre están comprendidos entre $0$ y
$1$. La coordenada $0, 0$ serían las correspondientes a la esquina inferior
izquierda (Kivy usa un sistema de coordenadas diferente al que vimos en
_Pillow_ o en _CSS_ por ejemplo, aquí el cero para la coordenada `Y` está
abajo).

La coordenada $1, 1$ corresponderían con la esquina superior derecha.

La propiedad `pos_hint` es similar, pero en vez de pasarle una tupla se le pasa
un diccionario, donde dependiendo de la clave ('x' o 'top' por ejemplo)
conseguimos uno u otro resultado: `x` se refiere siempre al borde izquierdo.

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


