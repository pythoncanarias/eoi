---
title: Mas controles y Layouts de Kivi
---

## PageLayout

La clase `PageLayout` sirve  para crear una disposición de múltiples páginas, añadiendo además una animación para el paso entre las páginas. Todos los _widgets_ que contenga se tratarán como una página, así que ocuparán el máximo de espacio disponible.
es por esto que `PageLayout` no hace ningún caso a ninguna de las siguientes propiedades: `size_hint`, `size_hint_min`, `size_hint_max` o `pos_hint`.

Veamos un simple ejemplo con tres páginas

```python
--8<--
docs/page-layout-example.py
--8<--
```

Las transiciones entre páginas se realizan con un movimiento de arrastre en los
laterales de las páginas, enlos casos en los que proceda. Por ejemplo, la
ultima página no permite seguir avanzando y la primera no permite retroceder,
como es lógico. Como cada componente deltro del _layout_ va a ser una página
completa, es conveniente que sea a su vez un _layout_ copntendor que a su vez
contenga todos los controles que necesita.


**Ejercicio**: Cambia en el programa anterior para unsar `Label` en vez de
`Button` y comprueba que pasa.


**Ejercicio**: Cambiar color de fondo de los botones para poder apreciar mejor el cambio de pagina


## Ejemplos de uso de Button

Vamos a vincular un boton para que ejecute un método, usando el fichero Kv.
Partiremos del primer ejempo que estudiamos cunado vimos los _layouts_, los
ficheros `simple.kv`:

```kivy
--8<--
docs/simple.kv
--8<--
```

Y `simple.py`:

```kivy
--8<--
docs/simple.py
--8<--
```


### Asignar acciones a controles

Vamos a hacer que el botón haga algo. Para ello lo primero que vamos a hacer es
sacar la definición de la clase del fichero Kivy y nos lo vamos a a traer al
fichero Python.  Hecho este cambio, todo debería funcionan igual, pero los
ficheros quedarían así:

`simpleclick.kv`:

```kivy
--8<--
docs/simpleclick.kv
--8<--
```


Y `simpleclick.py`:

```python
--8<--
docs/simpleclick.py
--8<--
```

Ahora, con la clase definida en Python, podemos implementar en primer lugar el
método que queramos para realizar la acción que queremos que haga el botón, y
en el fichero Kivy realizamos el vínculo entre el botón y el método. Es
importante resaltar que el método se va a definir en la clase `MainLayout`, no
en el botón. Esto será importante después, a la hora de vincularlos.

Podemos llamar a este método como queramos, en este ejemplo hemos sado el
nombre `click`.  si todo ha ido bien, veremos que al pulsar el botón, se
imprime el mensaje.

Conviene resaltar dos cosas:

La primera es que hemos escrito la llamada `click()` usando los paréntesis,
como si fuera directamente código Python.  recordemos que todo lo que va a la
derecha de `:` debe ser una expresión Python.

La segunda es que no hemos usado `self` para realizar la llamada (de hacerlo
así, estaríamos llamando al método `click` del botón, que no es lo que queremos
porque ni siquiera está definido) sino a una variable predefinida `root`, que
siempre será una referencia al *Widget* padre de toda esta jerarquía, en este
caso, `MainLayout`.

## Propiedades

Vamos a hacer ahora que al pulsar el botón se modifique el texto de la
etiqueta. Para eso vamos a usar algo que aun no habiamos visto y que kivy llama
**Propiedades** o **Properties**. Las propiedades son clases definidas en Kivy
que tiene la particularidad de que **emiten eventos** cuando cambia de valor. 

Las propiedades están definidas en el módulo `kivy.properties` y en general
usamos un tipo diferente para cada tipo de dato que queremos usar como
propiedad. Por ejemplo, tendríamos `NumericProperty` para valores numéricos, o
`BooleanProperty` para valores booleanos.

Vamos a crear una propiedad para guardar el texto de la etiqueta. Para
propiedades de tipo textos usamos la clase `kivy.properties.StringProperty`. La
definiremos en la propia clase, como si fuera una variable de clase (solo se
incluye la parte cambiada del fichero Python, la importación y la declaración
de `label_text` como `StringProperty`):

```python
...
from kivy.properties import StringProperty
...

class MainLayout(BoxLayout):
    message = StringProperty("Hola, mundo")

    def click(self):
        ...
...
```

Aparentemente sería lo mismo que si hubiéramos creado una cadena de texto
"Hola, mundo", pero internamente han pasado más cosas:

1) se ha creado automáticamente un evento, en este caso `on_message`, que se
emitirá cada vez que el texto de `message` cambie.

2) Internamente se ha implementado un patrón conocido como Observador o
*Observer*, que básicamente nos permite vincular (*bind*) los cambios en esta
propiedad a los métodos o funciones que queramos, usando el método `bind`.
Cuando se produzcan cualquier cambio de su valor, se ejecutaran los
procedimientos vinculados a ese cambio, utilizando el evento definido antes.

Seguimos ahora con los cambios en el programa. Una vez definida la propiedad,
modificamos el fichero Kivy, y cambiamos el atributo `text` de la etiqueta para
que use la nueva propiedad `message`:

```kivy
MainLayout:
    ...
    Label:
        text: root.message
```

Con esto le estamos diciendo a kivy que el texto de la etiqueta debe ser el
contenido de la propiedad `message`, **incluso si este cambia en el futuro**.
Esto es la gran ventaja (y el propósito) de que las propiedades emitan eventos
cuando sus valores cambian; permitir a Kivy enterarse de esos cambios y
reflejarlo en el texto de la etiqueta de forma automática.

Vamos a cambiar ahora el código del método `on_click`:

```python
    def click(self):
        self.message = "Alguien ha pulsado el botón!" 
```

El código final debería quedar asi, el `simpleprop.kv`:

```kivy
--8<--
docs/simpleprop.kv
--8<--
```


Y `simpleprop.py`:

```python
--8<--
docs/simpleprop.py
--8<--
```

La característica de que estos dos valores esten relacionados de forma que
cuando se cambia el valor en la propiedad, el cambio se propaga o se refleja en
la otra, se llama *binding* o *vínculo*. Se die que los dos valores están ahora
**vinculados**.

Dijimos antes que es la primera vez que vemos las propiedades, en realidad esto
es mentira; ya las hemos usado antes, muchas veces. Por ejemplo, cuando usamos
el evento `on_press`, este evento está disponible porque en el botón se ha
definido una propiedad `press`.  Al crear una propiedad, se crea
automaticamente el evento encargado de notificr que el valor de la propiedad ha
cambiado.

Otro ejemplo podría ser el texto de las etiquetas. el atributo `text` está
definido como una propiedad, así que cualquier cambio en el texto de una
etiqueta origina un evento `on_text`, que nosotros podemos utilizar, por
ejemplo, desde Python, ligandolo a algún método o función nuestro que actue
cuando el texto de la etiqueta cambie.

![Eran propiedades todo el tiempo](scooby-doo-properties.png)

**Ejercicio:** Cambiar el programa para que se muestre en el texto de la
etiqueta el número de veces que se ha pulsado el botón.

## Cambiar tipografía, color y tamaño de los controles

Podemos cambiar varios aspectos visuales de los controles, y el sitio más
cómodo es el fichero `.kv`. Vamos a cambiar la tipografía, el color y el tamaño
de la fuente de la etiqueta. Descarga un fichero `.ttf` y guardalo en una
carpeta que llamaremos `fonts`. en mi caso voy a usar la fuente LCD.ttf.

Ahora, editamos el fichero kivy (solo se muestran las lineas cambiadas):

```kivy
    Label:
        text: root.label_text
        font_name: "fonts/LCD.ttf"
        font_size: "72dp"
        color: "#88FF88"
```

Y sin hacer ningun cambio en el codigo Python, vemos que tenemos
nuestro contador con los cambios estéticos que hemos indicado:

![Contador](widgets-02.png)

El código por el momento está así:

Fichero `sampleApp.py`:

```python
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class WidgetExample(BoxLayout):

    counter = 0
    label_text = StringProperty(str(counter))
    
    def do_click(self):
        self.counter += 1
        self.label_text = str(self.counter)
    

class SampleApp(App):
    pass


def main():
    app = SampleApp()
    app.run()

if __name__ == "__main__":
    main()
```

Y el fichero `sample.kv`:

```kivy
WidgetExample:

<WidgetExample>:
    cols: 3
    Button:
        text: "Púlsame"
        on_press: root.do_click()
    Label:
        text: root.label_text
        font_name: "fonts/LCD.ttf"
        font_size: "72dp"
        color: "#88FF88"
```

### Cambiar el color del botón

Los botones en Kivy son grises por defecto, pero podemos ajustar el color
especificando la propiedad `background_color`, usando una tupla de tres valores
para especificar un color, indicando los valores de rojo, verde y azul como
números entre 0 y 1, o una tupla de cuatro valores si queremos añadir
transparencia.

Pero hay que tener en cuenta que `Button.background_color` en realidad es más
bien cono una iluminación o un tintado que se hace sobre el botón, más que un
color sólido. Como el color por defecto es gris, si definimos un color rojo
intenso, lo que obtendremos será un rojo oscuro, mezcla del gris original
y del nuevo color.

Podemos conseguir un botón del color exacto que deseamos de dos formas, o bien
reemplazamos la imagen de fondo del botón por una imagen que sea blanco puro
(basta con un _bitmap_ de unos pocos píxeles), usando las  propiedades
`background_normal` y `background_down`, que son los colores a usan para el
botón normal y pulsado respectivamente.


## El control _Switch_

El control `Switch` puede estar en dos estados, activo o inactivo, como si
fuera un interruptor mecánico. El usuario puede desplazarlo a la
derecha/izquierda para activarlo/desactivarlo.

La propiedad `active` es un valor lógico que podemos leer o modificar para
trabajar con el control.

Nótese que este _widget_ espera un gesto de desplazamiento para cambiar de
estado. Si preferimos que el cambio se haga simplemente con un toque, sería
mejor usar el control `ToogleButton`.


## El atributo _Canvas_

Todos los controles o _widgets_ se representan internamente usando un objeto
`canvas` (Instancia de `kivy.graphics.Canvas`), objeto que podemos interpretar
o bien como un área de dibujo o como un conjunto de instrucciones de dibujo.
Son numerosas las instrucciones que podemos aplicar o añadir a un _canvas_,
pero se agrupan en dos tipos principales:

- Instrucciones de contexto

- Instrucciones de vértices

La diferencia entre los dos grupos es que las instrucciones de contexto no
dibujan nada, pero su efecto es modificar los resultados que se obtienen con
las instrucciones de vértices. Entre las instrucciones de vértices podemos
encontrar las órdenes típicas como líneas, rectángulos, círculos, etc.

Todos los controles incluyen su propio _canvas_, que usan internamente para
representarse a si mismos. Podemos también crear nuestro propios objetos
_canvas_, si lo necesitamos.

El siguiente código accede al `canvas` del control `MyWidget` y dibuja un
rectángulo dentro:

```python
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

kvWidget = """
MyWidget:
    orientation: 'vertical'
    canvas:
        Color:
            rgb: (255, 0, 0)
        Rectangle:
            size: self.size
            pos: self.pos
"""

class MyWidget(BoxLayout):
    pass

class CanvasApp(App):

    def build(self):
        return Builder.load_string(kvWidget)

CanvasApp().run()
```

El atributo `canvas` funciona como una lista: se compone de una secuencia de
ordenes que se ejecutan una detrás de la otra. Por lo tanto, el orden de las
instrucciones importa. Ciertas operaciones, como el cambio de color, escala,
etc. son Instrucciones de contexto y por tanto afectan a las ordenes
posteriores.

```
with self.canvas:
    Line(points=[(0, 0), (1,1)], width=2)
    Line(circle)
    Line(rectangle)
    Rectangle Ellipse
```

*Ejercicio* : Pintar lineas horizontal/vertical en medio de la ventana

#### Las propiedades ´canvas.before´ y ´canvas.after´

Además de las instrucciones contenidas en un objeto _canvas_, estos objetos
contiene dos subconjuntos adicionales, `canvas.before` y `canvas.after`, que
también están organizados en forma de listas de instrucciones.

Las instrucciones en `canvas.before` se ejecutan, como su nombre indica, justo
antes de las instrucciones principales. De forma equivalente, las instrucciones
contenidas en `canvas.after` se ejecutan justo después de las principales.
Teniendo esto en cuenta, es fácil ver que todo lo dibujado por instrucciones en
`canvas.before` se representará en pantalla en un segundo plano o plano de
fondo, mientras que aquellas en `canvas.after` so mostrarán en un plano
superior, encima de todo lo dibujado anteriormente.

