---
title: El lenguaje de kivy o kvlang
---

## El lenguaje kvlang

A medida que las aplicaciones crecen en complejidad, se hace más y más
complicado definir la construcción de árboles de controles, disposición de
layouts y vinculaciones con las funciones o métodos necesarias. El lenguaje KV
es un intento de simplificar y ayudar en este proceso.

El lenguaje KV, también llamado `kvlang` o «El lenguaje de Kivy», nos permite
crear el arbol de _widgets_ (Controles y _layouts_) de forma declarativa, y
nospermite vincular propiedades entre si o con llamadas a métodos/funciones de
forma más natural. Permite la creación de prototipos rápidos y permite cambiar
de forma ágil las interfaces de usuario sin afectar la funcionalidad, al
imponer una separación clara entre la lógica de la aplicación y la interfaz de
usuario


## Uso del lenguaje Kivy (kvlang)

El lenguaje **kvlang** no es estrictamente necesario, pero es verdad que
en muchos casos se simplifica mucho trabajo usándolo.

Como ya sabemos, podemos organizar la disposión o _layout_ de nuestras ventanas usando Python directamente. No hay nada que podamos hacer en el lenguaje de Kivy que
no podamos hacer con Python, y sin embargo, no es así al reves:
algunas cosas que podremos hacer en Python no podremos hacerlas en kvlang, por
ejemplo, la creación dinámioca de controles.

¿Por qué molestarse en aprender KvLang, entonces? Es conveniente, porque si que
es verdad que algunas cosas son más fáciles de hacer en kvlang que en Python.
Además, al tener la disposición de las ventanas descritas en un fichero y
lenguaje separado ayuda cuando la estructura es compleja.

Vamos a empezar modificando un programa muy sencillo. Vamos a dividirlo en dos,
el programa en si y un fichero con extensión `.kv` que define la disposición o
_layout_ de la interfaz:

Este sería el código Python inicial:

```python
from kivy.app import App
from kivy.uix.button import Button

class SimpleApp(App):

    def build(self):
        return Button(
           text="Hello World",
           size_hint=(0.4,0.05),
           pos_hint={'x': 0.3, 'y': 0.5}
           )

if __name__ == '__main__':
    app = SimpleApp() 
    app.run()
```

Vamos a definir el árbol de controles, en este caso un simple botón, en un
fichero kivy, que tiene una extensión por defecto `.kv`, y que llamaremos
`simple.kv`. Pero el nombre que le hemos dado no es casual, tiene una razón de
ser que requiere antes una explicacion

## Los fichero .kv

Lo primero que necesitamos saber es que Kivy tiene una regla por defecto para
vincular el programa Python con el fichero `.kv` a utilizar para la disposición o
*layout*. Tampoco es estrictamente necesario seguir esta regla, solo es una
ayuda, pero la mayoría de los programas lo hacen así, porque resulta muy
cómodo.

La regla es la siguiente: Dentro de nuestro programa, habrá un único elemento,
que representa la aplicación, y que será o bien una instancia de la clase `App`
directamente o, mas frecuentemente, una instancia de una clase derivada de
`App` (En el ejemplo, es la clase `SimpleApp`).  En ese caso, Kivy tomara el
nombre de la clase, le quitara en sufijo `App` si lo tuviera, pasará el resto a
minúsculas (En nuestro caso, `simple`), y buscará un fichero con ese mismo nombre
y la extensión `".kv"`.

En nuestro ejemplo, todos estos pasos lo llevarán a intentar buscará un fichero llamado `simple.kv`. Así que creado el fichero con ese nombre ya se ha vincula directamente con la clase `App` de nuestro programa.

Vamos entonces a guardar el fichero de ejemplo como `main.py`. Ahora vamos a
especificar la disposición de nuestros controles en un fichero,

En primer lugar el fichero `simple.kv`:

```kvlang
--8<--
docs/simple.kv
--8<--
```

y en otro `simple.py`:

```python
--8<--
docs/simple.py
--8<--
```

**Ejercicio**: Para ver que el `simple.py` está realmente usando el fichero
`simple.kv`, haz una modificación en el fichero `simple.kv`, por ejemplo
ampliar el tamaño y color del texto incluyendo estas líneas:

```
    font_size: '24sp'
    color: [.8, .5, .2, 1]
```

Indentadas bajo la definición del botón.

Algunas cosas a tener en cuenta:

1) Ya no hace falta que importemos `Button` en `simple.py`, pues será instanciado a partir del fichero `.kv`.

2) El método `builder` tampoco hace falta. Normalmente es el encargado de
construir el _layout_ de la aplicación en el inicio, pero en este caso se
generará también de forma automática a partir del contenido del fichero
`main.kv`.

### Estructura de los ficheros


Fichero kivy -> reglas

parte izquierda: identificadores
parte derecha: codigo python
nunca se usa =


**Ejercicio**: Añadir un control de tipo _Label_ con el texto "Que tal"

Añadir Label. Que pasa? Error. Solo es posible tener un único elemento
raiz.

## Otras formas de cargar KV

Además de usar la regla _mágica_ de los nombres (`algoApp` -> `algo.kv`) para
asignar automáticamente un fichero `.kv` a un fichero `.py` (Más propiamente
hablando, a una clase derivada de `kivy.app.App`), existen otras dos formas de
hacerlo, máß explicitas:

### Cargando el contenido desde un fichero .kv arbitrario

Podemos usar el objeto predefinido `Builder` (definido en `kivy.core.builder`
para llamar al método `load_file()`, al cual le pasaremos la ruta de un fichero
`.kv` cualquiera. Esta función devuelve el arbol de controles formado a patir
del fichero, así que solo hay que llamar a esta función en el método `build` y
devolver su resultado:

```python
--8<--
docs/builder-load-from-file.py
--8<--
```

En este ejemplo, la estructura se crea a partir del fichero `builder.kv`:

```python
--8<--
docs/builder.kv
--8<--
```

Que debería resultar el algo como:

![Builder from file demo](builder.png)


### Cargando el contenido desde una variable de texto

Usando igualmente `Builder` podemos llamar a su método `load_string()` con el contenido 
del fichero `.kv` (quizá obtenido pr medio de algun otro ptroceso, desde una
bse de datos, etc.) y de forma similar nos devuelve el árbol de controles.

```python
--8<--
docs/builder-load-from-string.py
--8<--
```
