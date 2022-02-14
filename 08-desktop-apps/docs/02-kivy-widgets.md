---
title: Controles (_Widgets_) Kivi
---

## Widgets

Vamos a empezar viendo los controles más básicos: el botón y la etiqueta.

Vamos a hacer primero un simple programa con un botón y una etiqueta, y que no haga nada.
Empezaremos con en fichero `.kv` para definir nuestro _layout_. En este caso usaremos 
una clase derivada de:

```kivy
WidgetExample:

<WidgetExample@BoxLayout>:
    cols: 3
    Button:
        text: "Pulsame"
    Label:
        text: "Hola, mundo"
```

En Kivy las reglas pueden ser referidas a objetos (instancias) o a clases. Si son objetos
se usa el nombre de la clase, sin mas, seguido de dos puntos. Para las clases, se usa
la forma `<NombreDeLaClase>` o incluso `<NombreDeLaClase@ClasePadre>` si queremos indicar
de que clase deriva. Es decir, que lo que en Kivy sería:

```kivy
<WidgetExample@BoxLayout>:
```

Es equivalente al siguiente código de Python:

```python
class WidgetExample(BoxLayout)
```

Es decir, que podemos definir las clases o bien en el fichero Kivy
o en el de Python, pero no en los dos.

Para este ejemplo, necesitamos los siguientes ficheros:

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

En el código Python no necesitamos definir la clase `WidgetExample`, ya que se
define en el fichero `.kv`. La clase de la App se llama `SampleApp`, así que si
dejamos a Kivy que se encargue él mismo de cargar el fichero `.kv`.

Lo que hace es eliminar el sufijo `App` de la clase (si lo hubiera), pasar el
resto a minúsculas y cargar el fichero con la extensión `.kv`, que en este caso
sería, por tanto, `sample.kv`. En ese fichero, la raíz es la primera regla
definida con nivel 0 de indentación, en este caso `WidgetExamle`.

¿De donde sale el código de la clase `WidgetExample`? Lo genera de forma
automática Kivy usando la información contenida en el fichero `sample.kv`.

Si ejecutamos ahora el programa `sampleApp.py`, deberíamos obtener una ventana
con dos componentes, el primero es un botón, que podemos pulsar (aunque ahora
no haga nada) y una etiqueta, que tampoco hace nada.

![Boton y etiqueta](widgets-01.png)

### Asignar acciones a controles

Vamos a hacer que el botón haga algo. Para ello lo primero que vamos a hacer es
sacar la definición de la clase del fichero Kivy y nos lo vamos a a traer al
fichero Python.  Hecho este cambio, todo debería funcionan igual, pero los
ficheros quedarían así:

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

Ahora, con la clase definida en Python, podemos implementar en primer lugar el
método que queramos para realizar la acción que queremos que haga el botón, y
en el fichero Kivy realizamos el vínculo entre el botón y el método. Es
importante resaltar que el método se va a definir en la clase `WidgetExample`,
no en el botón. Esto será importante después, a la hora de vincularlos.

Podemos llamar a este método como queramos, vamos a usar el nombre `do_click`.

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

si todo ha ido bien, veremos que al pulsar el botón, se imprime el mensaje.

Conviene resaltar dos cosas: La primera es que hemos escrito la llamada
`do_click()` usando los paréntesis, como si fuera directamente código Python.
La segunda es que no hemos usado `self` para realizar la llamada (de hacerlo
así, estaríamos llamando al método `on_click` del botón, que no es lo que
queremos) sino a una variable predefinida `root`, que siempre será una
referencia al *Widget* padre de toda esta jerarquía, en este caso,
`WidgetExample`.

### Propiedades

Vamos a hacer ahora que al pulsar el botón se modifique el texto de la
etiqueta. Para eso vamos a usar unas lo que kivy llama **Propiedades** o
**Properties**. Las propiedades son clases definidas en Kivy que tiene la
particularidad de que emiten eventos cuando cambia de valor. 

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

class WidgetExample(BoxLayout):
    label_text = StringProperty("Hola, mundo")

    def do_click(self):
        print("Botón pulsado")
...
```
Aparentemente sería lo mismo que si hubiéramos creado 
una cadena de texto "Hola, mundo", pero internamente han pasado
más cosas:

1) se ha creado un evento, en este caso `on_label_text`, que se emitirá cada
   vez que el texto de `label_text` cambie.

2) Internamente se ha implementado un patrón conocido como Observador
   o *Observer*, que básicamente nos permite vincular (*bind*) los cambios en
   esta propiedad a los métodos o funciones que queramos, usando el método
   `bind`.  Cuando se produzcan cualquier cambio de su valor, se ejecutaran los
   procedimientos vinculados a ese cambio, utilizando el evento definido
   antes.

Seguimos ahora con los cambios en el programa. Una vez definida la propiedad,
modificamos el fichero Kivy, y cambiamos el atributo `text` de la
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

Con esto le estamos diciendo a kivy que el texto de la etiqueta debe ser el
contendo de la propiedad `label_text`, **incluso si este cambia en el futuro**.
Esto es la gran ventaja (y el propósito) de que las propiedades emitan eventos
cuando sus valores cambian; permitir a Kivy enterarse de esos cambios y
reflejarlo en el texto de la etiqueta de forma automática.

Vamos a cambiar ahora el código del método `on_click`:

```python
    def do_click(self):
        self.label_text = "Alguien ha pulsado el botón!" 
```

La característica de que estos dos valores esten relacionados de forma que
cuando se cambia el valor en la propiedad, el cambio se propaga o se refleja en
la otra, se llama *binding* o *vínculo*. Se die que los dos valores están ahora
**vinculados**.

Aunque es la primera vez que hablamos de propiedades, en realidad ya las hemos
usado antes. Por ejemplo, cuando usamos el evento `on_press`, este evento está
disponible porque en el botón se ha definido una propiedad `press`.  Al crear
una propiedad, se cera automaticamente el evento encargado de notificr que el
valor de la propiedad ha cambiado.

Otro ejemplo podría ser el texto de las etiquetas. el atributo `text` está
definido como una propiedad, así que cualquier cambio en el texto de una
etiqueta origina un evento `on_text`, que nosotros podemos utilizar, por
ejemplo, desde python, ligandolo a algun metodo o funcion nuestro que actuara
cuando el texto de la etiqueta cambie.

![Eran propiedades todo el tiempo](scooby-doo-properties.png)

**Ejercicio:** Cambiar el programa para que se muestre en el texto de la
etiqueta el número de veces que se ha pulsado el botón.

### Cambiar tipografía, color y tamaño de los controles

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
colo solido. Como el color por defecto es gris, por ejemplo, si definimos un
colo rojo lo que obtendremos será un colo rojo oscuro, mezcla del gris original
y del nuevo color.

Podemos conseguir un botón del color exacto que deseamos de dos formas, o bien
reemplazamos la imagen de fondo del botón por una imagen que sea blanco puro
(basta con un _bitmap_ de unos pocos píxeles), usando las  propiedades
`background_normal` y `background_down`, que son los colores a usan para el
botón normal y pulsado respectivamente.

### La propiedad `disabled`

Esta propiedad nos permite activar o desactivar rápidamente cualquier control.
Normalmente el aspecto del _widget_ se modifica para indicar este estado
desactivado, y cualquier interacción con el usuario queda anulada. 

El valor por defecto de esta propiedad es, lógicamente, `False`, es decir, que
por defecto cualquier *widget* que creemos estará activo.

### Uso de la funcion `builder`

Hasta ahora hemos visto dos maneras de definir la interfaz del programa, bien
usando un fichero `.kv` con un nombre predeterminado, o creando la interfaz
directamente desde Python. Pero hay una clase `kivy.lang.builder.Builder` que
nos permite dos opciones intermedias: Usar ficheros `.kv` con cualquier nombre
que queramos, o usando un valor de cadena de texto en Python que contenga
código `kvlang`.

El método `load_string` nos proporciona la capacidad de interpretar un contenido
en formato _kvlang_, como el que podríamos encontrar en un fichero `.kv`, pero
desde una _string_. Por ejemplo:

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
con el constructor y devuelve el _widget_ raíz.

### ToogleButton o botón de estado

El siguiente *widget* o control que vamos a ver es el **tootleButton**. En
principio es igual a un botón cualquiera, pero cuando se pulsa la primera vez
se queda en estado "pulsado", y cuando lo pulsamos otra vez se vuelve a poner
en estado normal.

Veamos un ejemplo. Nada más rápido y fácil que añadir un `ToogleButton` a lo
que ya tenemos y ver que pasa. Vamos a modificar el fichero Kivy para que la
clase raíz, `root` o principal, `widgetExample`, incluya un `ToogleButton`:

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

Ejecutemos ahora el programa y veamos el resultado.

metodo `do_state`. truco pasar el propio widget. Cambiar textos
ON y OFF. Usar size?hit y width para fijar el tamaño del widget

**Ejercicio:** Podemos habilitar y desabilitar un botón
con el atributo `disabled`

### El control _Switch_

El control `Switch` puede estar en dos estados, activo o inactivo, como si
fuera un interruptor mecánico. El usuario puede desplazarlo a la
derecha/izquierda para activarlo/desactivarlo.

La propiedad `active` es un valor lógico que podemos leer o modificar para
trabajar con el control.

Nótese que este _widget_ espera un gesto de desplazamiento para cambiar de
estado. Si preferimos que el cambio se haga simplemente con un toque, sería
mejor usar el control `ToogleButton`.

### El atributo _Canvas_

Todos los controles o _widgets_ se representan internamente usando un objeto
`canvas` (Instancia de `kivy.graphics.Canvas`), objeto que podemos interpretar
o bien como un área de dibujo o como un conjunto de instrucciones de dibujo.
Son numerosas las instrucciones que podemos aplicar o añadir a un _canvas_,
pero podemos agruparles en dos tipos principales:

- Instrucciones de contexto

- Instrucciones de vértices

Las instrucciones de contexto no dibujan nada, pero su efecto es modificar los
resultados que se obtienen con las instrucciones de vértices. Entre las
instrucciones de vértices podemos encontrar las órdenes típicas como líneas,
rectángulos, círculos, etc.

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
instrucciones importa. Ciertas operaciones, como el cambio de color, escala, etc. son
globales y afectan a las ordenes posteriores.

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


### El control _CheckBox_

El control _CheckBox_ es un botón de dos estados, que puede estar marcado o desmarcado,
Si el control _CheckBox_ está incluido en un grupo (_Group_) se convierte de forma
automática en un _RadioButton_. De forma similar al control `ToogleButton`, solo un _RadioButton_ de los incluidos en el grupo puede estar marcado.

Un ejemplo de uso:

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

