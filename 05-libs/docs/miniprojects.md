Las siguientes propuestas sirven como miniproyecto para la parte de Librerías. **No hay que hacerlos todos, solo uno de ellos**. Elige el que más te apetezca. Obviamente, si quieres hacer más de uno, para prácticar, no hay problema.

## Rampas de color

Utilizando la librería Pillow, crea una imagen en color (modo `RGB`), de
$256x256$ pixel, de forma que, para cada posible pixel en la posición $x$ e $y$ 
de la imagen, las componentes roja (`'r'`), verde (`'g'`) y azul ('`b`') cumplan
las siguientes condiciones:

- La componente roja debe ser igual a x
- La componente verde debe ser igual a y
- La componente azul debe ser igual a la media de los valores x y y

Por ejemplo, el pixel en la posición 13, 27 debería tener las siguientes
componentes de color:

- Rojo: 13
- Verde: 27
- Azul: 20

La imagen que deberiamos obtener deberia ser igual que esta:

![ramp](ramp.png)

## Etiquetar imágenes

Utilizando la librería Pillow, lee un fichero de tipo imagen, cuyo nombre se
pasa como parámetro en la línea de comandos (estará en `sys.argv[1]`). Obten el
ancho y el alto en pixels de la imagen (Propiedad `size` de la image).
Utilizando las funciones definidas en `ImageDraw` (Concretamente, las funciones
`ImageDraw.text` para "dibujar" el texto e `ImageDraw.textlength` para saber
cuanto espacio (ancho en _pixels_) ocupará el texto antes de pintarlo),
pinta en la esquina inferior izquierda las dimensiones en pixels de la imagen,
en la forma "<ancho> x <alto>".

Guarda la nueva imagen con un nuevo nombre, compuesto a partir del nombre
original, pero anteponiedo la cadena de texto `"-stamped"` entre el nombre del
fichero en si y la extensión. Recuerda que en `os.path` hay una función
especifica que divide un nombre de fichero precisamente en estas dos, partes,
`os.path.splitext`:

```python
>>> os.path.splitext('hola.png')
('hola', '.png')
```

Por ejemplo, si ejecutamos el programa sobre la siguiente imagen (`img001.png`):

![Montañas](img001.png)

Debería de crear una nueva imagen `img001-stamped.png`, tal que así:

![Montañas sellada](img001-stamped.png)

## Estadisticas de trabajo

Usando las funciones definidas en el módulo `os`, hacer un programa que muestre
una gráfico de barras mostrando el número de ficheros modificados o creados en
los siete días anteriores (Puedes obtener la fecha actual con la librería
estándar `datetime` o con la librería externa que también vimos, `arrow`. Luego
tendrás que obtener la fecha de hace 7 días, puedes usar `datetime.timedelta` o
el método `shift` si usas `arrow`).

Las funciones `os.path.getmtime` y `os.path.getctime` te darán la fecha y hora
en los que cada fichero ha sido creado / modificado, pero en tiempo
Unix (Segundos desde el 1 de enero de 1970), asi que tendrás que convertirlos a
objetos de tipo `datetime.datetime` o `arrow.Arrow` según la librería que
decidas utilizar (En cualquiera de los dos casos, es mejor que termines trabajando con objetos de tipo `date`, sin la información horaria, ya que para este caso esa informaciónno es necesaria y simplemente molestaria).

No hace falta complicarse con el grafico, un simple grafico de barras mostrado
en la terminal es suficiente. La salida podria ser algo como esto:

```
2022-10-31 ▉
2022-11-06 ▉▉▉
2022-11-07 ▉▉▉▉▉▉▉▉▉
```

Para imprimir la barra, puedes usar el caracter unicode `\u2589` o `▉`, y
recuerda que puedes multiplicar un texto por un número y el resultado es la
cadena repetida tantas veces como ese numero, es decir:

```
>>> print('\u2589' * 12)
▉▉▉▉▉▉▉▉▉▉▉▉
```

Tendrás que llevar la cuenta de los ficheros por cada fecha, lo ideal es un
diccionario. Recuerda que los objetos de tipo `datetime.date` se pueden usar
como claves de un diccionario. Si no lo ves claro, usa una cadena de texto que
represente la fecha, como por ejemplo `2022-10-07`.


## Ayuda a Luke

En la siguiente foto (`luke.png`) podemos ver a nuestro héroe Luke Skywalker a
punto de atacar a los malvados sicarios de Jabba el Hutt.

![Use the force!](luke.png)

El problema es que el sable láser está apagado. Vamos a usar Pillow para añadir
el efecto especial del sable láser.

Para ello sigue la siguiente receta:

- Abre la imagen original con `Image.load`.

- Crea una nueva imagen, del mismo tamaño que la original, pero en modo `RGBA`
  (La `A` significa transparencia), y color por defecto `(0, 0, 0, 0)`. En el
  modo `RGBA` usamos 4 _bytes_ para cada píxel: Rojo, verde, azul y opacidad o
  _alfa_. Un valor alfa de 0 indica nula opacidad, o lo que es lo mismo, máxima
  transparencia. Así que tendremos una nueva imagen, del mismo tamaño que la
  original, pero totalmente transparente. Podemos llamar a esa nueva imagen
  `vfx`, por ejemplo (`VFX` es la abreviatura habitual para los efectos
  visuales).

- Las coordenadas de donde queremos colocar la hoja del sable láser van del
  punto $380, 498$ a $-35, 34$. Vamos a dibujar una línea desde el primer punto
  al segundo, usando la función `line` (No hay problema por dibujar fuera de la
  imagen).

  Recuerda que para usar las funciones de dibujo primero tienes que crear un
  objeto tipo _canvas_ o lienzo desde la imagen que quieres modificar (`vfx` en
  este caso), con `canvas = ImageDraw.Draw(vfx)`. Es este objeto el que tiene
  los métodos para dibujar como `ellipse`, `arc` o `line`.

  Dibuja una línea de color verde intenso (Usa la tupla $(0, 255,
  0)$), entre los puntos indicados, y de un ancho de 24 píxeles.

- Vamos a difuminar ahora esta línea, para hacer el contorno luminoso de la
  hoja. Para eso, usamos el método `filter`, y podemos usar `ImageDraw.BLUR`
  para difuminar la imagen. Como el difuminado es demasiado suave, vamos a
  aplicarlo varias veces, por ejemplo, 18 veces. Recuerda que `filter` nos va a
  devolver el resultado como una nueva imagen, así que normalmente lo que
  hacemos es poner ese resultado en la imagen de partida, algo como
  `vfx = vfx.filter(ImageDraw.BLUR)`. Pero 18 veces. Por favor, no copies la
  línea anterior 18 veces, los bucles `for` y la función `range` son tus
  amigos.

- Vamos a pintar ahora el núcleo brillante de la hoja. Vamos a pintar una linea
  blanca, un poco mas estrecha que la verde original. Necesitas un nuevo objeto
  _canvas_, porque la imagen que tenemos ahora en la variable `vfx` es
  diferente.  Dibuja ahora una línea de color blanco (Usa la tupla $(255, 255,
  255)$), entre los puntos $380, 498$ a $-35, 34$, y de un ancho de 18 píxeles.

- Ahora, necesitamos difuminar la línea blanca, pero esta vez con un difuminado
  suave nos vale. Aplica un nuevo filtro `BLUR` sobre la imagen `vfx`.

- Ahora necesitamos pegar la capa de `vfx` sobre la imagen original, pero no
  podemos usar el método `paste`, porque este no entiende de imágenes
  transparentes, sino que usa el concepto de máscara que vimos en su día.
  
  Pero no hay problema porque podemos usar el método `alpha_composite`, que
  funciona igual, pero respetando el canal alfa. Por lo demás funciona igual
  que `paste`: le pasamos a la imagen original la imagen que queremos pegar
  `vfx`, y como segundo parámetro, las coordenadas. Como las dos imágenes son
  del mismo tamaño, simplemente pegamos en $(0, 0)$,

- Salva la imagen como `Luke-vfx.png`. Deberías tener algo como esto.

![This is the way](luke-vfx.png)

¡A por ellos, Luke!


## Mini gestor de tareas

**Atención**: No vimos ninguna de las dos librerías que se comentan en este ejercicio, así que tendrás que leer un poco sobre ellas en los enlaces incluidos para poder hacer este miniproyecto.

Vamos a crear un programa gestor de tareas, muy sencillo, para ser usado desde  la línea de comandos. Para ello vamos a usar [`argparse`](https://docs.python.org/3/library/argparse.html) de la librería estándar o [`fire`](https://google.github.io/python-fire/guide/) que es una librería de terceros, para gestionar los parámetros en línea.

El programa se llamará `tm.py`, y solo necesita entender dos ordenes, `add` y
`list`.

- La opción `add` nos permitirá añadir una tarea nueva. Necesita un parámetro
  adicional, obligatorio, que sería el título  o descripción de la tarea.
  Ademas, acepta tres parámetros opcionales, que sirven para indicar la
  prioridad. El parámetro `--low` indicara una tarea de baja prioridad,
  `--normal` indica una prioridad normal y `--high` una tarea de alta
  prioridad. Si no se especifica este parámetro, se debe asumir una prioridad
  normal. Si por error se indican varias prioridades, se debe asumir como válida la más alta.

  El programa, para dar de alta la tarea, abrirá en fichero `tasks.csv`
  en modo adición (`a`), y guardará dentro del mismo, en una línea para cada
  tarea, la siguiente información:

  - Fecha y hora en la que se añadió la tarea en formado `YYYY-MM-DD HH:MM:SS`
  - La prioridad, como una de las siguientes opciones: `low`, `normal`, `high`.
  - El texto de la tarea, entre comillas dobles

  Se usará como separador de los campos en este fichero CSV el caracter `;`.

- La otra orden, `list`, mostrara todas las tareas. Acepta también los mismos
  tres parámetros opcionales anteriores, `--low`, `--normal`, `--high`. Si se
  especifica este parámetro, solo se listarán las tareas de la prioridad
  indicada. Si no se especifica nada, se listarán todas.



