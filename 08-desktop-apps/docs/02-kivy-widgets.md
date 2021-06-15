## Widgets

Vamos a empezar viendo los controles mas basicos: el boton y la etiqueta.
Vamos a hacer primero un simpleprograma con un boton y una etiqueta, y quen o haga nada.
Emepezaremos con en fichero `.kv` para definir nuestro _layout_. En este caso usaremos 
una clase derivada de 

```kivy
WidgetExample:

<WidgetExample@BoxLayout>:
    cols: 3
    Button:
        text: "Pulsame"
    Label:
        text: "Hola, mundo"
```

en kivy las reglas pueden ser referidas a objetos (instancias) o a clases. Si son objetos
se usa el nombre de la clase, sin mas, seguido de dos puntos. PAra las clases, se usa
la forma `<NombreDeLaClase>` o incluso `<NombreDeLaClase@ClasePadre>` si queremos indicar
de que clase deriva. Es decir, que lo que en kivy seria:

```kivy
<WidgetExample@BoxLayout>:
```

Es equivalente al siguiente codigo de Python:

```python
class WidgetExample(BoxLayout)
```

Es decir, que podemos definir las clases o bien en el fichero kivy
o en el de Python, pero no en los dos.

Para este ejemplo, necesitalos los siguientes ficheros:

`sample.kv`:

```kivy
WidgetExample:

<WidgetExample@BoxLayout>:
    cols: 3
    Button:
        text: "Pulsame"
    Label:
        text: "Hola, mundo"
```

`sampleApp.py`:

```python
import kivy

from kivy.app import App

class SampleApp(App):
    pass


def main():
    app = SampleApp()
    app.run()

if __name__ == "__main__":
    main()
```

En el codigo Python no necesitamos definir la clase `WidgetExample`, ya que 
se define en el fichero `.kv`. La clase de la App se llama `SampleApp`, asi
que si dejamos a kivy que se encarge él mismo de cargar el fichero .kv, lo que hace es eliminar el sufijo App de la clase (si lo hubiera), pasar el resto a minusculas y cargar el fichero con la extensión .kv, que en este caso seria `sample.kv`. En ese fichero, la raiz es la primera
regla definida a con nivel 0 de identacion, en este caso `WidgetExamle`. De donde sale el código
de la clase `WidgetExample`? Lo genera automaticamente kivy desde el fichero
`sample.kv`, con la información contenida en la líneas tres y siguientes.

Si ejecutamos ahora el programa `sampleApp.py`, deberiamos obtener una ventana
con dos componentes, el primero es un boton, que podemos pulsar (aunque qhora no haga nada)
y una etiqueta que tampovo hace nada.

![Boton y etiqueta](widgets-01.png)

Vamos a hecer que el boton haga algo. Pero lo primero que vamos a hacer es sacar
la defincion de la clase del fichero kivy y nos lo vamos a a traer al fichero python.
Hecho este cambio, todo deberia funcioan igual, pero los ficheros quedarian:

`sample.kv`
```kivy
WidgetExample:

<WidgetExample>:
    cols: 3
    Button:
        text: "Pulsame"
    Label:
        text: "Hola, mundo"
```

El fichero `sample.py`:

```python
import kivy
 
from kivy.app import App

class WidgetExample(BoxLayout):
    pass


class SampleApp(App):
    pass


def main():
    app = SampleApp()
    app.run()

if __name__ == "__main__":
    main()
```

Ahora, con la clase definida en Python, podemos implmentar
en primer lugar el método que queramos para realizar la accion
que queremos que haga el boton, y en el fichero kivy realizamos
el vínculo entre el botón y el método. fijate que el método
se va a definir en la clase `WidgetExample`, no en el boton. Esto será
importante después, a la hora de vincularlos.

Podemos llamar a este método como queramos, vamos a usar el
nombre `do_click`.

El fichero `sample.kv`:

```kivy`
WidgetExample:

<WidgetExample>:
    cols: 3
    Button:
        text: "Púlsame"
        on_press: root.do_click()
    Label:
        text: "Hola, mundo"
```

Y el fichero `samplaApp.py`:

```python
import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class WidgetExample(BoxLayout):
    
    def do_click(self):
        print("Botón pulsado")


class SampleApp(App):
    pass


def main():
    app = SampleApp()
    app.run()

if __name__ == "__main__":
    main()
```

si todo ha hido bien, veremos que al pulsar el botón, se imprime el mensaje.

Conviene resaltar dos cosas: La primera es que hemos escrito la
llamada `do_click()` usando los paréntesis, como si fuera
directamente código Python. La segunda es que no hemos usado
`self` para realizar la llamada (de hacerlo así, estariamos
llamando al método `on_click` del boton, que no es lo que queremos) sino a una 
variable predefinica `root`, que siempre esta referenciando al *Widget* padre
de toda esta jerarquia, en este caso `WidgetExample`.

## Propiedades

Vamos a hacer ahora que al pulsar el boton se modifique el
texto de la etiqueta. Para eso vamos a usar unas lo que kivy 
llama **Propiedades** o **Properties**. Las propiedades
son clases definidas en kivy que tiene la particularidad de que
emiten eventos cuando cambia de valor. las propiedades estan definidas en
`kivy.properties` y en general hay un tipo diferente para cada tipo de dato
que queremos usar como propiedad. Por ejemplo, tendriamos `NumericProperty`
para valores, numéricos, o `BooleanProperty` para valores booleanos.

Vamos a crear una propiedad para guardar el texto de la
etiqueta. Para propiedades de tipo textos usamos la clase
`kivy.properties.StringProperty`. La definiremos en la
propia clase, como si fuera una variable de clase (solo se incluye la
parte cambiada del fichero python, la importacion y la declaracion
de `label_text` como `StringProperty`):

```python
...
from kivy.properties import StringProperty

class WidgetExample(BoxLayout):
    label_text = StringProperty("Hola, mundo")

    def do_click(self):
        print("Botón pulsado")
...
```
Aparentemente seria lo mismo que si hubieramos creado simpleente
la cadena de texto "Hola, mundo", pero internamente han pasado
mas cosas:

1) se ha creado un evento, en este caso `on_label_text`, que se emitira
  cada vez que el texto de `label_text` cambie.

2) Internamente se ha implementedo un patron conocido como Observedor
 o *Observer*, que basicamente nos permite vincular (*bind*) los cambios
en esta propiedad a los metodos o funciones que queramos, usando el método
`bind`.  Cuando se produzcan cualquier cambio de su valor, se ejecutaran los
procedimientos vinculados a ese cambio, utilizando el evento definido
anteriomente.

Seguimos ahora con los cambios en el programa. Una vez definida la propiedad,
modificamos el fichero kivy, y cambiamos el atributo `text` de la
etiqueta para que use la nueva propiedad 'label_text`:

```kivy
WidgetExample:

<WidgetExample>:
    cols: 3
    Button:
        text: "Púlsame"
        on_press: root.do_click()
    Label:
        text: root.label_text
```

Con esto le estamos diciendo a kivy que el texto de la etiqueta
debe ser el contendo de la propiedad `label_test`, **incluso si
este cambia**. Esto es la ventaja (y el propósito) de que las propiedades emitan
eventos cuando sus valores cambian; permitir a kivy enterarse
de esos cambios y reflejarlo en el texto de la etiqueta
de forma automática para nosotros.

Vamos a cambiar ahora el código del método `on_click`:

```python
    def do_click(self):
        self.label_text = "Alguien ha pulsado el botón!" 
```

La característica de que estos dos valores esten relacionados de forma
que cuando se cambia el valor en la propiedad, el cambio se propaga o se refleja
en la otra, se llama *binding* o *vínculo*. Los dos valores están ahora **vinculados**.

Aunque es la primera vez que hablamos de propiedades, en realidad ya las
habiamos usado antes. Por ejemplo, cuando usamos el evento `on_press`, este
evetno esta disponible porque en el boton se ha definido una propiedad `press`.
Al crear una propiedad, se cera automaticamente el evento encargado de notificr
que el valor de la propiedad ha cambiado.

Otro ejemplo podría ser el texto de las etiquetas. el atributo `text` esta
definido como una propiedad, asi que cualquier cambio en el texto
de una etiqueta origina un evento on_text, que nosotros podemos utilizar, por ejemplo, desde python, ligandolo a algun metodo o funcion nuestro que actuara
cuando el texto de la etiqueta cambie.

![Eran propiedades todo el tiempo](scooby-doo-properties.png)

**Ejercicio:** Cambiar el programa para que se muestre en el texto de la
etiqueta el número de veces que se ha pulsado el botón.

### Cambiar tipografía, color y tamaño de los controles

Podemos cambiar varios aspectos visuales de los controles, y el sitio
más cómodo es el fichero `.kv`. Vamos a cambiar la tipografía, el color y el tamaño
de la fuente de la etiqueta. Descarga un fichero `.ttf` y guardalo en una carpeta que llamaremos `fonts`. en mi caso voy a usar la fuente LCD.ttf.

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

El código por el momento esta asi:

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

### Cambiera el color del boton

Los botones en kivy son grises por defecto, pero podemos ajustar el color
especificando la propiedad `background_color`, usando una tupla de tres valores
para expecificar un color, indicando los valores de rojo, verde y azul como
numeros entre 0 y 1, o una tupla de cuatro valores si queremos añadir 
transparencia.

Pero hay que tener encuenta que `Button.background_color` en realidad es más
bien cono una iluminación o un titnado que se hace sobre el botn, mas que un
colo solido. Como el color por defecto es gris, por ejemplo, si definimos un colo rojo lo que obtendremos será
un colo rojo oscuro, mezcla del gris original y del nuevo color.

Podemos conseguir un boton del color exacto que deseamos de dos formas, o bien remmeplazamos la imagen de fondo del botón
por una imagen que sea blanco puro (basta con un bitmap de unos pocos pixeles),
usando las  propiedades `background_normal` y `background_down`, que son los
colores a usan para el boton normal y pulsado respectivamente.

### La propiedad `disabled`

Esta propiedad nos permite actiassert isinstance(w, Widget)
var o desactivar rápidamente cuanlquier
*widget*. Normalemente el aspencto del widget se modifica para incicar este
estado desactivado, y cualquier interaccion con el usuario queda anulada. 

El valor por defecto de esta propedad es, logicamente, `False`, es decir, que
por defecassert isinstance(w, Widget)
to cualquier *widget* que creemos estara activo.


### Uso de la funcion `builder`

Hasta ahora hemos visto dos maneras de definir la interfaz del programa, bien
usando un fiechro `.kv` con un nombre predeterminado, o creando la interfaz
directamente desde python. Pero hay una clase `kivy.lang.builder.Builder` que
nos permite dos opciones intermedias: Unsar ficheros `.kv` con cualquier nombre
que queramos, o usando on valor de acadena de texto en python con código
`kvlang`.

El método load_string nos proporciona la capacidad de interpretar un contenido
en formto kvlang, como el que podriamos encontrar en un fichero `.kv`, pero
desde una strind. Por ejemplo:

```python
import kivy.lang.builder
from kivy.uix.widget import Widget

w = kivy.lang.builder.Builder.load_string('''
Widget:
    height: self.width / 2. if self.disabled else self.width
    x: self.y + 50
''')
assert w.size == [100, 100]
assert isinstance(w, Widget)
```

El otro método es `load_file(filename, ...)`: Procesa un fichero
con el constructor y devuelve el widget raiz (si hay alguno definido)
del mismo:


### ToogleButton o botón de estado

El siguiente *widget* o control que vamos a ver es el **tootleButton**. En principio
es igual a un botón cualquiera, pero cuando se pulsa la primera vez se queda
en esado "pulsado", y cuando lo pulsamos otra vez se vueleve a poner en
estado normal.

Vaamoslo con un ejemplo. Nada más ráfipo y fácil que añadir un `ToogleButton`
a lo que ya tenemos y ver que pasa. Vamos a modificar el fichero kivy para que la clase
root o principal, `widgetExample`:

```kivy
WidgetExample:

<WidgetExample>:
    cols: 3
    ToggleButton:
        text: "Botón de estado"
    Button:
        text: "Púlsame"
        on_press: root.do_click()
    Label:
        text: root.label_text
        font_name: "fonts/LCD.ttf"
        font_size: "72dp"
        color: "#88FF88" 
```

ejecutemos ahora el programa y veamos el resultado.

metodo do_state. truco pasar el propio widget. Cambiar textos
ON y OFF. Usar size?hit y width para fijar el tamaño del widget

**Ejercicio:** Podemos habilitar y desabilitar un boton
con el atributo `disabled`

## Switch

The Switch widget is active or inactive, like a mechanical light switch. The user can swipe to the left/right to activate/deactivate it:
## El atribito Canvas

La clase `Canvas` nos permite dibujar, definiendo varios
métodos para pintar lineas, circulos, etc. Todos los contorles
incluyen su prpio canvas, que usan internamente para
representarse a si mismos. Podemos tambien crear nuestro porpios
objejos canvas, si lo necesitamos.

El siguiente codigo crea un canvez dentro de un `boxLayout`
y dibuja un rectangulo dentro:

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

Canvas es una lista: El orden importa. Ciertas operaciones, como el cambio de color, escala, etc. son globales y fectan
a las ordenes posteriores.

```
with self.canvas:
    Line(points=[(0, 0), (1,1)], width=2)
    Line(circle)
    Line(rectangle)
    Rectangle Ellipse
```

*Ejercicio* : Pintar lineas horizontal/vertical en mediode la ventana

canves.before


canvas.after



### CheckBox

CheckBox is a specific two-state button that can be either checked or unchecked. If the CheckBox is in a Group, it becomes a Radio button. As with the ToggleButton, only one Radio button at a time can be selected when the CheckBox.group is set.

An example usage:

```
from kivy.uix.checkbox import CheckBox

# ...

def on_checkbox_active(checkbox, value):
    if value:
        print('The checkbox', checkbox, 'is active')
    else:
        print('The checkbox', checkbox, 'is inactive')

checkbox = CheckBox()
checkbox.bind(active=on_checkbox_active)
```

