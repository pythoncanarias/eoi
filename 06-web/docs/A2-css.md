---
title: Apéndice 2 - Hojas de estilo CSS
tags: 
    - Desarrollo Web
---

## CSS: Hojas de estilo en cascada

El objetivo de las **Hojas de Estilo en Cascada** (*Cascade Style Sheets*) es
poder definir todos los aspectos visuales de la representación de un
documento HTML de forma independiente y aislada de la representación HTML
en si, que quedaría únicamente para definir la semántica. Es decir, en HTML
especificamos que un determinado fragmento de texto es un párrafo (con
la etiqueta `p`) y  con CSS definimos todos los aspectos estéticos o de
representación: Tipo de letra, tamaño, orientación, color, alineación, etc.

Para ver un buen ejemplo de lo que se puede conseguir cambiando la
especificación de estilos para un mismo documentos, la página [CSS Zen
garden](http://csszengarden.com/) es muy recomendable.

## Cómo especificar estilos

Existe tres maneras de especificar el estilo o representación de nuestro HTML:

- Usando estilos en línea

- Usando una especificación interna

- Usando una referencia a un documento CSS externo


### Especificar estilos en línea

Este forma de aplicar estilos es la más directa pero es la menos recomendable.
Veremos después la especificación mediante una especificación interna (que es mejor)
o usando referencias a documentos externos (Que es todavía mejor).

Usando estilos en línea se limita la definición del estilo al elemento concreto
en el que lo estamos definiendo. Aunque no se recomienda su uso, es la forma
más sencilla y además, los elementos definidos en linea tiene precedencia sobre
las definiciones hechas es especificaciones internas o por referencia, lo cual
puede ser necesario en algunos casos. Pero hay que tener en cuenta que estos
suele ser síntoma de un problema de diseño que estamos parcheando, pero no
arreglando.

En el siguiente ejemplo vamos a cambiar todas las características en el
párrafo de texto que hay en el documento:

 - Cambiaremos el color a verde
 
 - Usaremos la tipografía `Trebuchet MS` (Si el ordenador no tuviera
   esa tipografía disponible, usa la que tenga por defecto dentro 
   de la familia *sans-serif*.
 
 - El tamaño del texto se ajustará a 25 pixels de alto.

Veamos cómo se haría usando estilos en línea:

```html
<html>
 <head>
  <title>Ejemplo de CSS</title>
 </head>
 <body>
  <p style="color: green; font-size: 25px; font-family: 'Trebuchet MS', sans-serif;">
    Hello CSS World
  </p>
 </body>
</html>
```

**Ejercicio**: Añade un segundo párrafo, sin estilos, después del primero.
Comprueba que el estilo definido dentro del primer párrafo no se aplica al
segundo.

Esta forma de especificar los estilos tiene varios problemas:

- Tenemos que repetir todo la especificación del estilo cada vez que queramos
   usarlo

- Esto no solo hace la página más pesada, también gastamos tiempo de CPU en
  recalcular una y otra vez el mismo estilo.

- La gestión de los estilos se complica. Si tenemos 22 párrafos como el del
  ejemplo, y queremos cambiar el tamaño de la fuente a 32 pixels, hay que
  cambiar el estilo en cada uno de ellos.

- La información de representación (CSS) y la semántica están mezcladas en el
  elemento.


### Especificar los estilos de forma interna

Podemos usar las etiquetas `<style>` y `</style>` dentro de un documento HTMl
para definir los estilos a usar en el resto de la página. Este elemento debe ir
dentro de la sección `<head>` del documento.

```html
<!DOCTYPE html>
<html>
 <head>
  <style>
    p {
        color: green;
        font-size: 25px;
        font-family: 'Trebuchet MS', sans-serif;
    }
  </style>
 </head>
 <body>
  <p>Hello CSS World</p>
 </body>
</html>
```

En esta definición obtenemos algunas ventajas. Al definir los atributos de un
párrafo de esta manera, estamos especificando todos los párrafos, de forma que
no tenemos que repetir la misma información en cada elemento de la página.

[ ] **Ejercicio**: Añadir un nuevo párrafo. Comprobar que el nuevo párrafo mantiene
las características definidas en la hoja de estilo. 

Además, aunque estén en el mismo documento, por los menos hemos separado la
especificación de los estilos y el documento. Esto hace también que los estilos
se calculen solo una vez.


### Especificar una hoja de estilos como un documento externo

Este es la forma más recomendable de aplicar estilos a un documento. Para ello
se usa la etiqueta `link` dentro de la estructura `head` del documento. Usamos
el atributo `rel` con el valor `stylesheet` dentro del `link`, y el atributo
`href` debe enlazar con el documento que contenga las reglas de estilo:

```html
<!DOCTYPE html>
<html>
 <head>
  <link rel="stylesheet" type="text/css" href="style.css">
 </head>
 <body>
  <p>Hello CSS World</p>
 </body>
</html>
```


Las ventajas de tener el estilo definido en un documento externo son:

- Podemos reutilizar esta hoja de estilo en otros documentos HTML

- Podemos enlazar a varias hojas de estilo desde un único documento.

- Estas hojas de estilo se pueden cachear. Por ejemplo si definimos una hoja de
  estilos común para todo un _website_, solo se cargará y procesará la primera
  vez.

- No mezclamos los dos lenguajes en un mismo documento

Por ejemplo:

```html
<!DOCTYPE html>
<html>
 <head>
  <link rel="stylesheet" type="text/css" href="estilos.css">
 </head>
 <body>
  <p>Hello CSS World</p>
 </body>
</html>
```

Siendo el documento `estilos.css` el siguiente:

```css
p {
    color: green;
    text-decoration: underline;
    font-size: 25px;
    font-family: 'Trebuchet MS', sans-serif;
}
```


La razón de definir los estilos en la parte `head` es que permite al navegador
obtener la información necesaria para la representación de los elementos antes,
de forma que puede usar la para no tener que representar el elemento dos veces,
lo que resulta molesto para el usuario y hace aparentemente más lenta la carga
de la página.


## Estructura de un documento CSS

Los documentos CSS consisten en una serie de **reglas** (*rules*) que define
como se debe representar un elemento o subconjunto de elementos. La estructura
de las reglas siguen el siguiente patrón:

```css
<selector> { <propiedades> }
```

El selector es el que determina a que elementos de la página se le deben
aplicar las propiedades definidas en la regla. Hasta ahora hemos usado uno 
muy sencillo que es simplemente el nombre de un `tag`; en nuestro caso `p`. Este
sería el caso más sencillo para un selector.

[ ] **Ejercicio**: Escribe una regla para los elementos `H1` que les asigne color
rojo.

Podemos tener múltiples selectores en la misma regla, por ejemplo la siguiente
regla define que la alineación del texto para los elementos `h1` y `h2` debe
hacerse centrada:

```css
h1, h2 {
    text-align: center;
    }
```

Las propiedades normalmente consisten parejas atributo/valor, separados por el
carácter dos puntos: `:`, como en el ejemplo anterior. Normalmente se definen
varios atributos, pero no es obligatorio; el ejemplo anterior, in ir más lejos,
solo define una propiedad.

Los selectores pueden ser más elaborados que simplemente la etiqueta: veamos
algunos selectores básicos en forma de ejemplos:

Ejemplo     | Descripción del selector|
-----------:|-------------------------|
`*`         | Universal. Todos los elementos |
`div`       | De etiqueta. Todos los elementos `div` |
`.blue`     | De clase: Todos los elementos que tengan la clase `blue` |
`#headline` | De identidad: **El elemento** con identificador `headline` |
`[attr]`    | De atributo: Elementos que tengan el atributo indicado (con cualquier valor) |
`[attr='val']`  | De atributo: Elementos con el atributo y el valor indicado |
`[attr~='val']` | De atributo: Elementos con el atributo y **contengan** valor indicado |
`[attr*='val']` | De valor de atributo: Elementos que tengan el atributo y el valor indicado |
`:pseudo-class` | De pseudo-clase: Todos los elementos con la pseudo-clase indicada |
`div > p`   | De descendencia: Todos los párrafos que estén **directamente** dentro de un `div` |
`div p`     | De descendencia: Todos los párrafos que estén dentro de un `div` (Al nivel que sea)|


[ ] **Ejercicio**: Modificar la vista de la lista de tareas. Hacer que el
texto de prioridad alta aparezca en rojo y en negrita (la propiedad para
poner el texto en negrita es: `font-weight: bold;`. Podemos asignar una clase a
un elemento HTML usando el atributo `class`. Por ejemplo, el párrafo:

```html
<p class="saludo">Hola, mundo</p>
```

Tiene la clase `saludo`. Podríamos definir los estilos para esta clase de
párrafos con el selector `p.saludo`o simplemente `.saludo`. El primero se
aplicaría solo a los párrafos con la clase `saludo`, el segundo a cualquier
elemento con la clase `saludo`.

También es posible asignar varias clases a un único elemento, simplemente
hay que ponerlos como una lista de clases separados por espacio. El siguiente
ejemplo muestra un párrafo con las clases `saludo` y `aviso`:

```
<p class="saludo aviso">Hola, mundo</p>
```

## Pseudo-elementos

Los selectores de pseudo-elementos empiezan con dos caracteres `:`. Se
califican como _pseudo_ porque se refieren a elementos a los que normalmente no
podríamos modificar, porque no forman parte del árbol DOM. El ejemplo más claro
es el de `selected`, que nos permite definir el estilo a usar cuando se
selecciona texto para copiar.

Los pseudo-elementos más usado son:

`::after`:

:   Estilos a aplicar al contenido que viene después de un elemento.
    Normalmente se usa la regla `content` para añadir ese contenido, por
    ejemplo:

    ```css
    p::after { content: "after"; }
    ```

`::before`: 

:   Similar a `::after`, pero referido al contenido antes del elemento.


`::first-letter`

:   Estilos a aplicar a la primera letra del elemento

`::first-line`

:   Estilos a aplicar a la primera línea

`::selection`

:   Estilo a aplicar cuando se selecciona texto


## Pseudo-clases (O Pseudo-selectores)

Las pseudo-clases son palabras clave que nos permite seleccionar elementos
basándonos, igual que con los pseudo-elementos, en información que no está en
el documento (y por tanto no es accesible en el DOM) o que no puede ser
accesible usando los selectores anteriores. Esta información puede estar
asociada a cierto estado, a localizaciones, a negaciones de lo anterior o a
lenguajes.

El ejemplo más claro de las pseudo-clases es el referido a los enlaces, tenemos
una pseudo-clase `:visited` para los enlaces que ya han sido visitados, otra
para cuando el puntero del ratón está situado encima del enlace y podemos,
por tanto, hacer _click_ en él, `:hover`. Otros casos muy usados son seleccionar 
un `checkbox` cuando esta seleccionado, `:checked`, o seleccionar el elemento de
un formulario que tenga el foco, ':focus'.

Otras pseudo-clases que pueden ser interesantes son las siguientes:


`:first-child`

:   Estilos a usar para el primer elemento de la lista de elementos hijos
    de un elemento. En el caso de una lista, por ejemplo, el primer
    elemento `<li>`

`:last-child`

:   Similar a `:first-clild`, pero referido al último elemento.

`:nth-child`

:   Para seleccionar una serie de elementos pertenecientes a una
    fila o columna en una lista de elementos o en una tabla. Se
    pasa el número entre paréntesis; `:nth-child(2)` sería el
    segundo hijo.

`:hover`

:   Un enlace, si el cursor está posicionado encima.

`:visited`

:   Un enlace, si la dirección a la que apunta ya ha sido visitada.

`:active`

:   Un enlace activo, es decir, presionado

`:focus`

:   El elemento, normalmente parte de un formulario, que tiene el foco
    en este momento.

`:enabled`

:   Elementos, normalmente parte de un formulario, que están habilitados.


`:disabled`

:   Elementos, normalmente parte de un formulario, que están deshabilitados.

`:default`

:   Elementos, normalmente parte de un formulario, que están seleccionados
    por defecto. Se usa normalmente para elementos de tipo _radio_ o _checkbox_.


`:required`

:   Estilos para los elementos que tienen el atributo `required`

`:optional`

:   Estilos para los elementos que tienen el atributo `optional`

`:read-only`

:   Estilos para los elementos que tienen el atributo `read-only`

`:not()`

:    Invierte el selector

`*`

:    Selecciona todos los nodos dentro del especificado. Por ejemplo
     `table *` selecciona todo el contenido de la tabla.


## Selector por identidad

Para especificar el identificador de un elemento en HTML se usa la propiedad
`id`. En el selector, como vimos antes, usaríamos el prefijo `#`: 

```html
<div id="ejemplo">
    <p>Esto es un texto de ejemplo</p>
</div>
```

Que podría ser seleccionado con:

```css
#ejemplo {
 width: 20px;
}
```

La especificación de HTML no permite que múltiples elementos tengan el
mismo ID.

Algunas propiedades útiles:

- `border`: `border: 1px dotted red;`

- `background`: 
 
 - `background-color: red;`

 - `background-color: #de1205`;

 - `background-color: rgba(0, 0, 0, 0.5);`

 - `background-image: url(logotipo.png);`


## Box model

![Box model](img/box-model.svg)

El modelo de caja o _box model_ es un concepto esencial de la estructura
HTML/CSS. Cada elemento está contenido en un área que define tres capas de
espacio que lo rodea. Los nombres de estas capas son `padding`, `border` y
`margin`.

El modelo de caja también define la posición sobre la que se rota el elemento,
y por defecto esta puesto a `50% 50%`, por lo que todas las rotaciones se
realizaran respecto al punto central. Si queremos que gire, por ejemplo,
sobre la esquina superior izquierda, habría que definir la propiedad
`transform-origin` a `0 0`.

Lo más importante a recordar del modelo de caja de CSS es que las copmponentes
`width` y `height` definen solo la región más interna o `content-box`. Eso
significa que si añadimos valores de `padding`, `border` o `margin`, el espacio
ocupado finalmente por el elemento sera la suma de todos estos valores.

Por ejemplo, si un elemento de 200x100 pixels tiene un `padding` de `2px`, un border
de `1px` y un `margin` de `5px`; el espacio total ocupado será de 216 pixels de
ancho:

$$ 200 + 2 \times 2 + 1 \times 2 + 5 \times 2 = 216 $$

Mientras que el alto será:

$$ 100 + 2 \times 2 + 1 \times 2 + 5 \times 2 = 116 $$

Usando la propiedad `box-sizing` podemos determinar si hay que incluir es
espacio de `padding` y de `margin` en las componentes `width` y `height`. El
valor por defecto es `content-box`, que indica que la altura y anchura final
son la suma de la altura y anchura declarada, mas las componentes del `margin`,
`border` y `padding`. Pero si usamos `border-box`, tanto las componentes de
`padding` como `border` se incluyen en las componentes `width` y `height`.

Para elementos de tipo texto, lo normal es usar el modo `content-box`, mientras
que para componentes de maquetación y ajuste, es más cómodo trabajar en el modo
`border-box`.

## Ajustes de tipografía

### font-family: Fuente

Con `font` podemos definir casi todos los aspectos tipográficos: Podemos usar
la abreviatura `font` para definir cada uno de las siguientes caracteríisticas,
por orden:

| Nombre          | Propiedad                                       |
|:---------------:|-------------------------------------------------|
| `font-family`   | Tipografía                                      |
| `font-size`     | Tamaño                                          |
| `font-stretch`  | Permite estirar o comprimir el texto            |
| `font-style`    | El estilo: itálica/oblicua                      |
| `font-variant`  | Variaciones de la tipografía, p.e. `small-caps` |
| `font-weight`   | Peso: p.e. `bolder`, `120%`                     |
| `line-height`   | Altura de la línea                              |
| `text-decoration` | Subrayado o no                                |

La especificación para la fuente o familia de fuentes a usar sigue una
configuración especial: se pueden especificar varias fuentes, separadas por
coma. Si la primera fuente no está disponible o no puede ser presentada por la
razón que sea, se intentará usar la siguiente, hasta llegar al final. En el
siguiente ejemplo:

```css
font-family: "CMU Bright", Arial, Verdana, sans-serif;
```

Se mostrará la primera que pueda ser utilizada. Es normal acabar la lista
con una especificación general: `serif`/`sans-serif`/`monotype`, que siempre
estará disponible.

### font-size: Tamaño de la fuente

El tamaño de la fuente puede ser definido con `font-size`: Se puede usar un
tamaño fijo, como en este ejemplo:

```css
font-size: 18px;
```

O un tamaño relativo:

```css
font-size: 120%;
```

Las unidades para tamaños fijos puedes ser de diferentes tipos. El tamaño
estándar del texto es `12pt` (puntos), `16px` (pixels) o `1em`. 

El grosor o ancho del texto se puede controlar con `font-weight`: Los valores
`bold`, `bolder`, `light` y `lighter` son habituales, y también valores
numéricos, desde 100 hasta 900, donde el valor normal es 500 o Medio. Los
valores numéricos se corresponden a los valores como se muestra en la tabla:

| Valor | Nombre       |
|:-----:|--------------|
| 100   | Thin         |
| 200   | Extra-light  |
| 300   | Light        |
| 400   | Regular      |
| 500   | Medium       |
| 600   | Semi-bold    |
| 700   | Bold         |
| 800   | Extra-Bold   |
| 900   | Black        |

### text-align: Alineación del texto

Con `text-align` podemos alinear el texto dentro de un contenedor. Los valores
posibles son `left` (Por defecto), `center` y `right`.


## Frameworks CSS

Hay varios _frameworks CSS_ que sirven de ayuda para construir sobre ellos
nuestra página web. Un _Framework CSS_ es un conjunto de estilos y clases
predefinidos, que siguen determinados patrones y proporcionan una base
consistente para una web. Por lo normal incluyen algún sistema de _grid_,
tipografías y elementos de interfaz habituales como botones, formularios,
menús, barras de navegación, etc.

Algunos de ellos son [Booostrap](https://getbootstrap.com/),
[TailWindCSS](https://tailwindcss.com/),
[SemanticUI](https://semantic-ui.com/), [Foundation](https://get.foundation/),
[Pure.css](https://github.com/pure-css/pure) o
[Bulma.css](https://github.com/jgthms/bulma), entre muchos otros. Vamos a ver
este último, a modo de ejemplo.

Las ventajas principales de **Bulma.css** es que es ligero y modular, por lo que se
puede configurar para usar solo los componentes que necesites. Además, no
necesita _javascript_. Es uno de las _frameworks css_ más populares, con una
comunidad muy activa. Además, cuenta con muchas plantillas, integraciones y
ejemplos de uso.

![Usa bootstrap](img/use-bootstrap.svg)

Vamos a descargar la hoja de estilos directamente desde github:

[bulma.css](https://raw.githubusercontent.com/jgthms/bulma/master/css/bulma.css)

Lo descargamos en `comun/static/comun/css/` (Si no existe este direcotorio, lo
crearemos). Podemos ahora reemplazar la plantilla `base.html` por la siguiente:

```html
--8<--
./docs/base.html
--8<--
```

Vemos que Bulma redefine algunos estilos para los componentes base, pero la
mayor parte de las veces define un estilo para cada componente, que tendremos
que añadir para usarlo. Por ejemplo, se define una clase `.table` para que se
la añadamos al componente html `<table>`. 

[ ] **Ejercicio**: Cambiemos la lista de tareas para  que empieze a
usar la clase `table`

### Modificadores

Hay muchos elementos en Bulma que tienes estilos alternativos. La mayoría de
estos estilos se definen con clases que empiezan con los prefijos `is-` o
`has-`. Por ejemplo, tenemos una clase para los botones que se llama `button`:

```html
<button class="button">
  Button
</button>
```

![button](img/button.png)

Añadiendo a laa clase `button` la clase `is-primary`, podemos modificar el
color del botón.

```html
<button class="button is-primary">
  Button
</button>
```

![button](img/button-primary.png)

Bulma define 6 colores principales:


- `is-primary`
- `is-link`
- `is-info`
- `is-success`
- `is-warning`
- `is-danger`

También se puede cambiar el tamaño:

- `is-small`
- `is-medium`
- `is-large`



Y el estilo o estado:

- `is-outlined`
- `is-loading`
- `[disabled]`

Y todos estos modificadores se pueden cambiarm 

