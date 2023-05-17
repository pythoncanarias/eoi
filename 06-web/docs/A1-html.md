---
title: Apéndice 1. HTML
tags:
    - web
---

## Introducción a HTML

HTML es un lenguaje de marcado que nace junto con el protocolo HTTP en los 90 y
da lugar a lo que actualmente conocemos como la _Web_.

En sus inicios, HTML era relativamente limitado, orientado a la creación de
artículos científicos. En la actualidad, la responsabilidad de la
**representación** de los elementos se ha transferido a las hojas de estilo, y
su labor principal es definir la estructura del documento.

## Las etiquetas HTML

La sintaxis de HTML está compuesta por **etiquetas** o **_tags_** (que se
marcan con los símbolos `<` y `>`, y atributos. Muchas de las etiquetas sirven
para definir un fragmento o porción del contenido, por lo que vienen en
parejas, una para poder marcar el princiio y otra el final. La marca de inicio,
el contenido interior y la marca final, todo junto, se consideran **un
elemento HTML**.

Cada etiqueta HTML tiene un proposito específico. Veamos algunos ejemplos:


| Etiqueta    | Proposito                                             |
|:-----------:|-------------------------------------------------------|
| `<html>`    | Incluye todo el documento. Es el elemento raiz        |
| `<head>`    | Incluye metainformacion sobre el documento            |
| `<script>`  | Incluye contenido ejecutable, normalmente javascript  |
| `<title>`   | Define el título del documento                        |
| `<body>`    | Cuerpo o centenido del documento                      |
| `<p>`       | Define un párrafo de texto                            |
| `<h1>`      | Define un encabezado de nivel 1                       |

### Estilos por defecto

In HTML many tags are assigned a ”default” CSS style even if you didn’t specify
it yourself.  For example, using two <span> tags in a row, will not generate a
line break.  But two <div> tags in a row will. This is simply because span
tag’s default CSS ”display” style is set to ”inline-block”, which perpetuates
any text added after it just to the end of the previous tag. But <div> tag’s
default ”display” property style is ”block”, which will drop content added to
your HTML doc- ument immediately after the <div> tag right below it, based on
the height of that <div> element.


## Comentarios HTML

Se puede comentar código HTML con las marcas `<!--` y  `-->`, al principio y
final respectivamente del texto a comentar. Todo lo que se encuentre entre
estas marcas no sera procesado ni formará parte del resultado final que
aparezca en la pantalla. Son útiles especialmente para desarrollo.

## Declaración de contenido HTML


Con HTML5, solo es necesario esta declaración al principio de la página:

```
<!doctype html>
```

Antes de HTML5, solía ser algo así:

```
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">
```

¡Algo hemos avanzado!


## Formularios

Las etiquetas `<form>` y `</form>` delimitan un formulario. Los atributos más
importantes de `form` son `action` y `method`. Con `action` definimos la ruta
a la que el formularioenviará los datos. Con `method`, cuyos valores posibles
son `GET` y `POST`, definimos como se envian los datos. Para formularios, lo
normal es usar `POST`

Los controles de los formularios son casi todos elementos `<input>` con
distintos valores del parámetro `type`. En principo HTML define los siguientes

### Botón de envio o de _submit_

La forma de obtener este contro es usando el valor `submit` en el parámetro
`type`. Un eemplo podria ser:

```html
<input type="submit" name="ok" value="buscar">
```

### Contraseña

La forma de obtener este contro es usando el valor `password` en el parámetro
`type`. Un ejemplo podría ser:

```html
<input type="password" name="passwd">
```

Con una caja de texto de tipo `password`, cuando el usuario teclee algo dentro,
solo apareceran asteríscos, aunque internamente se esté almacenando la
información para ser enviada pasteriormente. LA idea es impedir que otras
personas puedan leer esta información mietras se escribe.

### El elemento `textarea`

Este control es específico para aceptar textos grandes, de varias líneas.
El control acepta cualquier longitud de texto, pero podemos limitar
esa cantidad con el parámetro `maxlength`. De igual manera, podemos exigir una
cantidad **m inima** de texto con `minlength`. Dos de los atributos más usados
con este control son `cols` y `rows`, que nos permiten definir el ancho y alto
del control, en número de caracteres.

Un ejemplo de `textarea`, con su etiqueta asociada:

```html
<label for="txt-asunto">Describa su problema
<textarea name="asunto" id="txt-asunto" cols="60" rows="8">
</textarea>
</label>
```




### Recuadro de texto

### Select

Este control muestra un selector que nos permite elegir entre diferentes
posibilidades. Se usa la etiqueta `<select>`, con un atributo `name` para poder
obtener despues el valor, y acaba con el correspondiente `</select>`. En medio,
podemos poner todas las etiquetas `<option>...</option>` que queramos, cada una
de ellas proporcionando un valor particular. 

```html
<p>
<label for="cb-ninja">Seleccion tu tortuga ninja / artista famoso del renacimiento italiano:
<select name="ninja" id="cb-ninja">
<option value="leo">Leonardo</option>
<option value="mike">Michelangelo</option>
<option value="don">Donatello</option>
<option value="ralph">Raphael</option>
</select>
</label>
</p>
```

Otros componentes de un formulario, que no son estrictamente hablando
componentes, seria las etiquetas, `label`, y los confuntos de controles o `fieldset`


### Etiquetas o `label`

El componente `<label>` esta pensado específicamente para etiquetar los
distintos componentes de un formulario. Usa un parámetro `for` en el que
se debe incluir el `id` del control al que la etiqueta está asociado.

```html
<label for="name">Nombre del usuario:
<input type=text" name="name" id="name">
</label>
```

Los valores del atributo `for` de la etiqueta y el `id` del control deben
ser iguales. Aunque en este ejemplo los atribiitos `name` e `id` del control
tienen el mismo valor, `label` solo presta atencion al campo `id`.

Asignar etiquetas descriptivas a los componentes de un formulario es muy
importante, especialmente como ayuda a personas con visibilidad reducida.

### Fieldset

El elemento `<fieldset>` sirve para agrupar varios controles y etiquetas
dentro de un formukario, a efectos visuales.
Dentro puede/debe contener in elemento `legend` que es una descripción
del tipo de controles que hay en el agrupamiento.

Un ejemplo:

```html
<form>
  <fieldset>
    <legend>Elige tu monstruo favorito</legend>

    <input type="radio" id="kraken" name="monster" value="K">
    <label for="kraken">Kraken</label><br>

    <input type="radio" id="mummy" name="monster" value="M">
    <label for="mummy">La momia</label><br>

    <input type="radio" id="vampire" name="monster" value="V">
    <label for="vampire">Vampiro</label>
  </fieldset>
</form>
```

Como casi todos los controles, puede tener el atributo `disabled`, lo que puede
resultar muy útil porque desabilita todos los controles dentro del `fieldset`,
no hay que desabilitarlos uno por uno.

## Resumen de marcas

| Etiqueta | Descripción |
|:--------:|-------------|
| a        |   Enlace |
| abbr     | Abreviatura |
| article  | Artículo |
| aside    | Nota al margen |
| audio    | Embebe un sonido, o un canal de audio |
| b        | fragmento de texto en negrita |
| blockquote | Representa una cita o fragmento extraido de otra fuente |
| body     | Cuerpo del documento |
| br       | Salto de línea |
| button   | Botón |
| canvas   | Área que puede ser usada para dibujar, normalmente con javascript |
| caption  | Define el titulo o texto asociado de una tabla |
| cite     | Una cita o referencia a otra fuente externa |
| code ||
| col ||
| colgroup ||
| dd  | Texto de la definición |
| del | Texto marcado como borrado |
| details ||
| dfn ||
| dialog  | Una sección que representa un cuadro de diálogo |
| div | Division general |
| dl  | Lista de definiciones |
| dt  | Termino de la definición |
| em  | fragmento de texto enfatizado (Por defecto, en cursiva o itálicas) |
| embeb   | Embebe una aplicación texterna, normalmente contenido multimedia como audio o vídeo |
| fieldset    | Cunjunto de campos de un formulario, agrupados |
| figcaption ||
| figure ||
| footer ||
| form ||
| h1  | Encabezado de nivel 1 |
| h2  | Encabezado de nivel 2 |
| h3  | Encabezado de nivel 3 |
| h4  | Encabezado de nivel 4 |
| h5  | Encabezado de nivel 5 |
| h5  | Encabezado de nivel 6 |
| head    | Seccion de metadatos del documento |
| header ||
| hgroup ||
| hr ||
| html    | Documento html |
| i   | fragmento de texto en cursiva o itálicas |
| iframe ||
| img ||
| img  | Imagen embebida |
| input ||
| ins | Texto marcado como insertado |
| kbd | Texto marcado como entrada de teclado |
| label ||
| legend ||
| li  | Elemento de lista |
| main ||
| map ||
| mark ||
| menu ||
| menuitem ||
| meta ||
| meter ||
| nav ||
| noscript ||
| object ||
| ol  | Lista ordenada |
| optgroup ||
| option ||
| output  | Texto que representa el producto de un cálculo |
| p   | Marcan un párrafo |
| param ||
| picture ||
| pre ||
| progress ||
| q ||
| s ||
| samp ||
| script  | Código ejecutable, normalmente en javascript  |
| section | Sección |
| select ||
| small ||
| source  | Define fuentes alternativas para elementos multimedia como `audio` o `video` |
| span    | Fragmento general de texto |
| strong   | fragmento de texto resaltado (Por defecto, en negrita) |
| style ||
| sub 	| Defines subscripted text. |
| summary 	| Defines a summary for the <details> element. |
| sup 	| Defines superscripted text. |
| svg 	| Embed SVG (Scalable Vector Graphics) content in an HTML document. |
| table   | Tabla |
| tbody 	| Groups a set of rows defining the main body of the table data. |
| td  | Celda de tipo datos |
| template 	| Defines the fragments of HTML that should be hidden when the page is loaded, but can be cloned and inserted in the document by JavaScript. |
| textarea 	| Defines a multi-line text input control (text area). |
| tfoot 	| Groups a set of rows summarizing the columns of the table. |
| th  | Celda de tipo columna |
| thead | Groups a set of rows that describes the column labels of a table. |
| thead | Cabecera de una tabla |
| time 	| Represents a time and/or date. |
| tr  | Fila de una tabla |
| track 	| Defines text tracks for the media elements like <audio> or <video>. |
| tt  | Texto en fuente de ancho fijo |
| u 	| Displays text with an underline. |
| ul  | Lista no ordenada |
| var 	| Define una variable. |
| video 	| Embeds video content in an HTML document. |
| wbr 	| Represents a line break opportunity. |



Fuente: [List of HTML5 Tags/Elements - Tutorial Republic](https://www.tutorialrepublic.com/html-reference/html5-tags.php)
