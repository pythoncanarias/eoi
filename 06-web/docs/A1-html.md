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
