---
title: Pillow - Tratamiento de imágenes
---
## Introducción a Pillow

La librería **Pillow** es un *fork* de la libreria **PIL** (*Python Image
Library*). Con __pillow__ añadimos a Python la capacidad de procesar imágenes.  


###  Instalacion de Pillow

Se instala con pip.

```shell
!pip install pillow
```

Y se importa ocon el nombre `PIL`, para mantenre retrocompatibilidad con la
librería orginal.

```python
import PIL
```

### Características más importantes

- **Acepta múltiples formatos**: Pillow soporta muchos formatos de archivos
usados para almacenaminto de imágenes, entre otros BMP (*Windows Bitmaps*),
EPS (*Encapsulated Postscript*), GIF (*Graphics Interchange Format*),
ICO (*Windows Icons*), JPEG (*Joint Photographic Experts Group*), PNG
(*Portable Network Graphic*), TGA (*Truevision Graphics Adapter*),
TIFF (*Tagged Image File Format*)...

- **Un sistema muy eficiente** para representar las imágenes en memoria. La
  librería está diseñada para permitir un acceso rápido y eficiente a los
  pixels de las imágenes, lo que permite usarlo como una base de desarrollo
  para procesar imágenes.

- **Varios algoritmos** habituales del procesamiento de imágenes ya vienen
incluidos en la librería.

Algunos usos posibles de esta librería:

- Archivado y proceso de imágenes por lotes. La librería permite crear
  *thumbnails*, convertir entre formatos, rotar, cambiar el tamaño, 
  imprimir imágenes, etc.

- Presentar imágenes. La versión actual incluye una interfaz Tk, asi 
  como controles que pueden ser usados en otros sistemas de ventanas
  como PythonWin.

- Proceso de imágenes: La librería incluye operaciones básicas de
  modificación de imagenes, que funciona a nivel de pixels, y operaciones
  de más alto nivel, como filtros, nucleos de convolución y conversiones
  del espacio de colores.

- Análisis y síntesis de imágenes

### Primeros pasos: Usando la clase Image

La clase más importante dentro de la librería es la clase `Image`, definida
en el módulo con el mismo nombre. Podemos crear instancias de esta clase de
diversas formas, bien leyendo las imagenes de un fichero, procesando
otras imágenes, o creando una imagen desde cero.

Pare cargar una imagen desde disco, usamos la función `open()` dentro
del módulo `Image`:


```python
from PIL import Image

im = Image.open("incredibles.png")
```

En Jupyter notebook, podemos usar directamente la imagen como salida de una celda, solo hay que incluir la instancia al final de una celda.


```python
from PIL import Image

im = Image.open("incredibles.png")
im
```

![png](incredibles.png)


Si tiene éxito, la función devuelve un objeto de tipo `Image`. Podemos examinar
atributos de la instancia para obtener información adicional de la imagen:


```python
from PIL import Image

im = Image.open("incredibles.png")
print(im.format, im.size, im.mode)
```

La salida deberia ser:

```
PNG (600, 300) RGB
```


- El atributo `format` identifica el formato usado para almacenar la imagen (Si
la imagen no se ha creado a partir de un fichero, `format` vale `None`). 

- El atributo `size` es una dupla que contiene el ancho y alto de la imagen, en _pixels_.

- El atributo `mode` nos permite saber el número y nombre de las
bandas de la imagen, así como el tipo de pixel y la profundidad. 

Algunos valores habituales de `mode` son: __`L`__ (De luminancia) para imagenes
en escala de grises, __`RGB`__ para imagenes en color real, con 24 bits de
profundidad, y __`CMYK`__, que indica una imagen preparada para usarse en sistemas
de impresión.

Una vez que tenemos la instancia de la imagen, podemos usar los diferentes métodos definidos en la clase para procesar y
manipular las imágenes.

Por ejemplo, podemos mostrar la imagen llamando al métdodo `show`.


```python
from PIL import Image

im = Image.open("incredibles.png")
im.show()
```

**Pregunta**: ¿Cuál es el tamaño de la imagen `leon.jpg`? ¿Y cuál es su modo?

![León](leon.jpg)

```python
from PIL import Image

im = Image.open("leon.jpg")
print('Tamaño de la imagen:', im.size)
print('Modo de la imagen:', im.mode)
```

La salida del programa es:

```
Tamaño de la imagen: (640, 960)
Modo de la imagen: RGB
```


### Teoría del Color

El ojo humano dispone de una serie de células especializadas en recibir la luz,
llamados conos. Hay tres tipos distintos de conos: los sensibles a la luz roja,
los sensibles a la luz azul y los sensibles a la luz verde.

En realidad, solo vemos esos tres colores, llamados __colores primarios__. En
resto de colores se obtiene como combinación de dos o más colores primarios.
Por ejemplo, el violeta sería un __color secundario__, resultado de detectar a
la vez tanto rojo como azul. Sumando el rojo y el verde obtenemos el amarillo.

Los colores primarios rojo, verde y azul funcionan como tales en un sistema
aditivo, es decir, un sistema que *suma* los colores, como la pantalla de
ordenador. En un sistema sustractivo, como el que utilizan los pintores al
mezclar los pigmentos en su paleta, los colores se *restan*. En un sistema
sustractivo, los colores primarios serían Magenta (que absorbe el verde),
Amarillo (que absorbe el azul) y Cyan (que absorbe el rojo).

#### Modelo RGB

Así tenemos entonces los tres colores primarios del modelo RGB: rojo,
verde y azul o lo que es lo mismo con sus nombres en inglés; _Red_,
_Green_, _Blue_. Este sistema se basa en sumar la luz, de forma que la
composición de los tres colores daría el blanco.

#### Modelo CMYK

En el modelo CYM los tres colores primarios son Cián (*Cyan*), Amarillo
(*Yellow*) y Magenta (*Magenta*) y la mezcla de estos tres colores a partes
iguales da como resultado el color negro, debido a que cada adición sustrae
luz. Este modelo es el utilizado en la industria gráfica y las artes visuales.

Pero conseguir el color negro, el más barato, a base de mezclar las tintas de
colores, mucho mas caras, es de genero tonto. Así que lo que se hace en este
mdelo es añadir el negro como color aparte, que se representa con la K final,
aunque estrictamente hablando no es necesario.
 

#### Modelo HSV

Por completar, veremos el modelo HSV (del inglés *Hue*, *Saturation*, *Value* –
Matiz, Saturación, Valor), también llamado HSB (*Hue*, *Saturation*,
*Brightness* – Matiz, Saturación, Brillo), define un modelo de color en
términos de sus componentes.

![Modelo HSV](./HSV.png)

Em modelo HSV está diseñado desde el punto de vista de la utilidad. Es muy útil
usar la ruleta de color HSV para elegir un color. En ella el matiz se
representa por una región circular; una región triangular separada, puede ser
usada para representar la saturación y el valor del color. Normalmente, el eje
horizontal del triángulo denota la saturación, mientras que el eje vertical
corresponde al valor del color. De este modo, un color puede ser elegido al
tomar primero el matiz de una región circular, y después seleccionar la
saturación y el valor del color deseados de la región triangular.

En lo que a nosotros respecta, como estamos usando pantallas de ordenador y,
por tanto, estamos generando la luz mediante un sistema aditivo, el modelo RGB
es el que nos interesa usar.

En resumen, todos los colores se obtienen como combinación de tres posibles
valores. Por lo tanto, para representar una imagen en color, solo tenemos que
almacenar los componentes rojo, verde y azul de cada punto que compone la
imagen. Al igual que con las coordenadas, que podemos guardar en forma de tupla
de dos elementos, los colores se pueden expresar en forma de trios o tuplas de
tres elementos, cada uno indicando, por orden, el componente rojo, verde y azul
del color.

Normalmente se usan un *byte*, o sea, 8 bits, para indicar cada componente del
color, lo que nos da 256 tonalidades de rojo, 256 tonalidades de verde y 256
tonalidades de azul, y todas sus combinaciones, que son 256x256x255 o, lo que
es lo mismo:

$$ 2^{24} = 16777216 $$

16.777.216 colores diferentes son muchos colores. En la práctica, esto es muchisimo más preciso de lo que el ojo humano puede percibir, por lo que a veces se llama a este esquema *True Color*.

También podemos definir colores usando una cuadrupla, una tupla de cuatro valores. Los tres primeros valores corresponden a los componentes RGB del color, en el cuarto se especifica la opacidad (lo contrario de transparencia) del color, también llamada __*alfa*__, __*valor alfa*__ o __*canal alfa*__.

Esto nos permite crear colores traslúcidos, que pueden dejar pasar parte de la luz que emiten los objetos que están detras de ellos. Un valor alfa de 255 se entiendo como totalmente opaco, una alfa de 0 es totalmente transparente; en la práctica, invisible.

### Leer imagenes desde un fichero

La librería soporta, como vimos antes, muchos formatos diferentes. Para leer y
obtener una imagen desde cualquiera de estos tipos de fichero, solo tenemos que
usar la función `open` en el módulo `Image`, como hicimos antes.

No tienes que preocuparte por qué tipo de fichero es, porque la librería lo
determina automáticamente basandose en el propio contenido del fichero.

### Guardar una imagen a fichero

Para guardar un fichero, usamos el método `save` de la propia imagen. Al
salvar la imagen, es importante el nombre del fichero, porque la librería determinará
el tipo del fichero a partir de la extensión del mismo, asi que si se usa el 
nombre `imagen.jpg` se usará un formato diferente que si usamos `imagen.png`.

**Ejecicio**: Convertir la imagen `leon.jpg` a un fichero de tipo PNG.

**Pista**: El mecanismo seria leer la  imagen a memoria, y luego salvarla pero
usando el nombre `leon.png`. La libreria usará la extensión para decidir
que formato de almacenamiento debe usar.

```python
from PIL import Image

img = Image.open("leon.jpg")
img.save("leon.png")
```

**Pregunta**: Como podríamos hacer para cambiar 4000 ficheros de tipo GIF que
tenemos en una carpeta a PNG? No hace falta escribir el programa, solo
describir lo que haríamos

### Crear *thumbnails* o (Para aficionados a la fotografia, copias de contacto)

Podemos usar el método `thumbnail` de la imagen para hacer una versión escalada
y más pequeña. El método acepta como parámetro una dupla o tupla de dos
elementos, que especifican el tamaño máximo de ancho y alto, respectivamente.

El escalado se hace manteniendo la proporción original de la imagen, así que
probablemente el _thumbnail_ solo tendrá el tamaño indicado en la tupla para el
ancho o para el alto. El otro valor se calculará automáticamente. Eso si,
tenemos la garantía de que el ancho y alto del *thumbnail* siempre será menores o
iguales que los máximos indicados.


```python
from PIL import Image

leon = Image.open("leon.jpg")
size = (200, 200)
leon.thumbnail(size)
leon.show()
```

![Leon thumbnail](leon.tn.png)


Una cosa a destacar es que el método `thumbnail` no nos devuelve una nueva
imagen, sino que modifica la imagen original, lo que se suele conocer como
modificación *in place*. La mayoría de las funciones y métodos **no** funcionan
así, sino que devuelven una nueva imagen creada a partir de la original.

Otra cosa que conviene saber es que la librería decodifica y carga la imagen __solo__
cuando no tiene más remedio (Esto se conoce como comportamiento *lazy*).

Esto significa que, cuando abrimos la imagen con open, le lee la cabecera del
fichero para determinar el formato y obtener información como el modo, el
tamaño y demás propiedades, pero el resto de los datos no se leen a no ser que
alguna operación de procesamiento lo requiera (como el método `thumbnail` que
usamos antes).

Por tanto abrir una imagen es siempre una operación muy rápida, y totalmente
independiente del tamaño el fichero o del tipo de compresión usado para
almacenar la imagen.

**Ejercicio**: Escribir un pequeño _script_ que liste las imágenes en el
directorio actual (puedes usar `os.listdir`)  que muestre sus dimensiones (El
ancho y alto, que puedes obtener como una tupla en la propiedad `.size` de la
imagen, y el modo de la imagen (que puedes obtener del método `.mode`).


```python
import PIL
import os

IMAGE_EXTENSIONS = [".png", ".jpg", ".gif", ".webp"]
for fn in os.listdir():
    name, ext = os.path.splitext(fn)
    if ext in IMAGE_EXTENSIONS:
        im = PIL.Image.open(fn)
        print(fn, im.size, im.mode)
```
 Cuya salido podría ser:

```
leon.png (640, 960) RGB
DandelionDM_800x665.jpg (800, 665) RGB
HSV.png (347, 347) RGBA
blue-lion.png (550, 340) RGB
incredibles.png (600, 300) RGB
rectangle.png (450, 643) RGBA
PrimroseDM_1000x390.jpg (1000, 390) RGB
SilverweedDM_800x460.jpg (800, 460) RGB
leon.tn.png (133, 200) RGB
incredibles.webp (600, 300) RGB
fondo.jpg (1280, 719) RGB
mixed.png (341, 512) RGB
croma.png (640, 360) RGBA
elastigirl.png (461, 314) RGB
leon.jpg (640, 960) RGB
```

Puedes filtrar el tipo de ficheros que puedes listar, usando `os.path.splitext(filename)`
y comprobando que la extensión esté en una lista predeterminada, como esta:

```python
    IMAGE_EXTENSIONS = [".png", ".jpg", ".gif", ".webp"]
```

O puedes utilizar las excepciones. Para usar las excepciones, necesitas saber que si se
intenta abrir un fichero de algo que no es un fichero de imagen (un fichero `.py`, por
ejemplo) se elevará la excepción `IOError`. Podemos simplemente capturarla, ignorar
este fichero y pasar al siguiente.


```python
{% include 'external/pillow/lista-imagenes.py' %}
```

### Cortar, pegar y mezclar imágenes

La clase `Image` contiene métodos que te permiten manipular partes de una
imagen. Podemos, por ejemplo, extraer un sub-rectangulo de una imagen, usando
el método `crop`. El parámetro de entrada es una cuádrupla (tupla de cuatro
elementos), que contiene, en este orden:

- valor minimo de `x`, o `left`
- valor minimo de `y`, o `upper`
- valor máximo de `x`, o `right`
- valor máximo de `y`, o `bottom`


```python
from PIL import Image

leon = Image.open("leon.jpg")
box = (150, 320, 280, 440)
region = leon.crop(box)
region
```

![Partede una imagen](leon-crop.png)

Como vemos, el tamaño de la imagen respeta las dimensiones usadas para el
recorte.

```python
leon.size, region.size
```




    ((640, 960), (130, 120))



Observa que en este caso no se transforma la imagen original, como en `thumbnail`, sino que
se crea una imagen totalmente nueva. En el siguiente diagrma se muestra el significado de cada
uno de los valores de la 4-tupla.

![crop](rectangle.png)

El sistema de coordenadas de Pillow pone el origen (0, 0) en la esquina superior izquierda.
Como las coordenadas empiezan en cero, es bueno pensar que las posiciones apuntan
a los valores entre los pixel, y no a los pixels en si. Por tanto, la imagen
recortada tiene un tamaño de 150xs150 pixels exactamente.


```python
from PIL import Image

with Image.open("leon.jpg") as leon:
    box = (150, 300, 300, 450)
    region = leon.crop(box)
    
region
```




![png](output_69_0.png)



### Procesar la imagen y pegarla de nuevo

Vamos a realizar algun cambio en esta nueva imagen. En este caso vamos
a usar el método `transpose` para rotar la imagen 180 grados. Después, 
pegaremos esta imagen rotada en la imagen original, usando el metodo `.paste`
de la misma.


```python
from PIL import Image

leon = Image.open("leon.jpg")
box = (150, 300, 300, 450)
region = leon.crop(box)
region = region.transpose(Image.ROTATE_180)
leon.paste(region, box)
leon.show()
```

Al pegar la imagen, indicamos la imagen a pegar y el rectangulo donde pegarla, y
el tamaño de las dos debe ser el mismo, si no se elevará un error. Además, no se puede
pegar una imagen de forma que ocupe más que el tamaño de la imagen original.

no tenemos que preocuparnos, sin embargo, si los modos de la imagen pegada y destino
no coinciden, la libreria hara las conversiones necesarias automaticamente.

### Descomponer una imagen en color en RGB

El método `split` nos permite dividir una imagen en los canales básicos rojo, verde y azul (R, G, B), devolviendos
tres imagenes, cada una de las cuales contienen los valores para cada banda o color. Podemos
reunificar esas tres imagenenes de nuevo con la función `merge`.


```python
from PIL import Image

leon = Image.open("incredibles.png")
red, green, blue = leon.split()
green
```




![png](output_74_0.png)



El metodo `merge` espera dos parámetros, el primero es el modo (es este caso, `RGB`) y luego las
tres bandas con las que debe remezclar la imagen, en forma de tupla de tres elementos). Si mezclamos las
bandas en el orden correcto, obtenemos la misma imagen.

**Ejercicio**: Mezcla las tres bandas obtenidas antes (`red`, `green`, `blue`) ejecuntando
    la siguiente celda, y comprueba que volvemos a tener la imagen original. Despues, cambia el orden
    de las bandas (`blue`, `green`, `red`, por ejemplo) y observa el efecto


```python
from PIL import Image
from PIL.ImageChops import invert, lighter, add

im = Image.open("incredibles.png")
im.thumbnail((512, 512))

red, green, blue = im.split()
rebuild = Image.merge("RGB", (red, green, blue))
rebuild
```




![png](output_77_0.png)




```python
from PIL import Image
from PIL.ImageChops import invert, lighter, add

im = Image.open("leon.png")


red, green, blue = im.split()
rebuild = Image.merge("RGB", (blue, red, green))
rebuild.thumbnail((550, 550))
rebuild.save('/tmp/green-lion.png')
```

### Transformaciones geométricas

Podemos realizar algunas transformaciones geométricas sencillas
incluidas en la propia clase `Image`. Por ejemplo, `resize` nos 
permite cambiar el tamaño de la imagen. Al contrario que `thumbnail`, no
respetara las proporciones actuales, si el nuevo tamaño no la hace, y
no hace el cambio *in place*, sino que crea una nueva imagen con el nuevo tamaño:
    
    


```python
from PIL import Image

leon = Image.open("leon.jpg")
deformed = leon.resize((560, 220))
deformed
```




![png](output_80_0.png)



Para rotar las imágenes, podemos usar el método `rotate` o, como hicimos antes, `transpose`. Este
último puede ser usado también para reflejar la imagen a lo largo de su eje vertical u horizontal.

    out = im.transpose(Image.FLIP_LEFT_RIGHT)
    out = im.transpose(Image.FLIP_TOP_BOTTOM)
    out = im.transpose(Image.ROTATE_90)
    out = im.transpose(Image.ROTATE_180)
    out = im.transpose(Image.ROTATE_270)
  

  
Usando el *flag* `expand` (por defecto a False), podemos indicar si queremos 
expandir la imagen paa que la rotación se produzca con
o sin perdida.


```python
from PIL import Image

leon = Image.open("leon.jpg")
leon.thumbnail((240, 240))
rotated = leon.rotate(45, expand= False)
rotated
```




![png](output_83_0.png)



### Transformaciones de color

La libreria nos permite convertir imagenes entre diferentes modos.


```python
from PIL import Image

leon = Image.open("leon.jpg")
leon.thumbnail((220, 220))
leon = leon.convert("L")
leon
```




![png](output_85_0.png)



### Mejora de las imágenes

Hay varioas métodos y módulos que nos permites mejorar las imágenes.

#### Filters

En el módulo `ImageFilter` vienen una serie de filtros predefinidos, que
se pueden usar directamente como parámetros del método filter.
Tambien tienen estos filtros ya configurados y listos para usar:

- `BLUR`
- `CONTOUR`
- `DETAIL`
- `EDGE_ENHANCE`
- `EDGE_ENHANCE_MORE`
- `EMBOSS`
- `FIND_EDGES`
- `SHARPEN`
- `SMOOTH`
- `SMOOTH_MORE`


```python
from PIL import Image
from PIL import ImageFilter

leon = Image.open("leon.jpg")
leon = leon.crop((0, 340, 550, 680))
l2 = leon.filter(ImageFilter.SMOOTH)
l2
```




![png](output_89_0.png)




```python
!ls
```

    Allura-Regular.ttf	 HSV.png	    pillow.ipynb
    blue-lion.png		 incredibles.png    pillow.md
    cambia-formato.py	 incredibles.webp   PrimroseDM_1000x390.jpg
    creditos.md		 leon.jpg	    rectangle.png
    croma.png		 leon.png	    rectangle.svg
    cuadricula.py		 lista-imagenes.py  rojo.py
    DandelionDM_800x665.jpg  mixed.png	    SilverweedDM_800x460.jpg
    elastigirl.png		 PaperFlowers.ttf
    fondo.jpg		 payaso.py


**Ejercicio** Prueba distintos filtros en la celda anterior.

### Operaciones puntuales

El metodo `point` se usa para transofmrar los valores de pixels de una 
imagen de manera individulal. Acepta como argumento una funcion que se
aplicara a todos los pixels de la imagen.


```python
from PIL import Image

leon = Image.open("leon.jpg")
leon = leon.crop((0, 340, 550, 440))
leon.point(lambda x: x*1.2)
```




![png](output_93_0.png)




```python
from PIL import Image

leon = Image.open("leon.jpg")
leon = leon.crop((0, 340, 550, 680))
r, g, b = leon.split()
r = r.point(lambda x: 0 if x < 128 else 255)
g = g.point(lambda x: 0 if x < 128 else 255)
b = b.point(lambda x: 0 if x < 128 else 255)
rebuild = Image.merge("RGB", (r, g, b))
rebuild
```




![png](output_94_0.png)



**Ejercicio** Usa la función `split` para obtener los tres canales RGB de la imagen. 
Con el método `point` sube un poco (multiplica por $1.2$) el canal de rojo), y baja un poco los valores de los canales verde y azul (Por ejemplo, multiplícalos por $0.85$). Combina de nueve los canales RGB en una nueva figura y muéstrala como resultado de la celda


```python
# %load rojo.py
from PIL import Image

leon = Image.open("leon.jpg")
leon.thumbnail((350, 450))# 
r, g, b = leon.split()
r = r.point(lambda x: x*1.25)
g = g.point(lambda x: x*0.85)
b = b.point(lambda x: x*0.85)
rebuild = Image.merge("RGB", (r, g, b))
rebuild
```




![png](output_96_0.png)



Podemos conseguir una imagen en colores planos usando una funcion que agrupe
les valores, por ejemplo, de 0 a 64 se convierten en 0, de 65 a 128 serían 65, 
de 129 a 193 serían 125, de 194 para arriba serian 255.


```python
from PIL import Image

leon = Image.open("leon.jpg")
leon = leon.crop((0, 340, 550, 680))
leon.point(lambda x: (x // 64) * 64)
```




![png](output_98_0.png)



### El módulo ImageEnhance

Una forma aun mas avanzada de tratamiento de imágenes se puede encontrar en
el módulo `ImageEnhance`. Podemos crear  un objeto de tipo `Color`, `Contrast`,
`Brightness` o `Sharpness` a partir de la imagen y probarla con distintos
valores.


```python
from PIL import Image
from PIL import ImageEnhance

leon = Image.open("leon.jpg")
leon = leon.crop((0, 340, 550, 680))

enhancer = ImageEnhance.Color(leon)

enhancer.enhance(1.5)
```




![png](output_100_0.png)



**Ejercicio**: Cambia el valor de 2.2 a otros a ti criterio para que veas el efecto en la
    imagen final. Cambia tambien si quieres a otro tipo de *enhancer* y varia de nuevo
    el valor.

### El módulo ImageDraw: Dibujar sobre la imagen

Para dibujar sobre una imagen podemos usar el modulo `ImageDraw`.


Es ste modulo nos posibilita hacer dibujos desde cero, o anotar o retocar
imagenes preexistentes, o incluso generar graficos bajo demanda para la web.

Para poder dibujar sobre la imagen, tenemos que crear un objeto, a veces llamado
*canvas* o lienzo, a partir de la imagen. Dibujamos usando este objeto, y no sobre la
imagen original, pero este objeto se encargara de reflejar estos cambios en ella.

Veamos un ejemplo:


```python
from PIL import Image, ImageDraw

leon = Image.open("leon.jpg")
leon.thumbnail((400, 400))
width, height = leon.size
draw = ImageDraw.Draw(leon)
draw.line((0, 0, width, height), fill=(255, 120, 120), width=12)
draw.line((width, 0, 0, height), fill="coral", width=8)
leon
```




![png](output_103_0.png)




```python
im = Image.open("leon.png")
max_width, max_height = im.size
draw = ImageDraw.Draw(im)

for width in range(40, max_width, 100):
    draw.line((width, 0, width, max_height), fill=(23, 56, 199), width=12)
for height in range(60, max_height, 100):
    draw.line((0, height, max_width, height), fill=(23, 56, 199), width=12)
im
```




![png](output_104_0.png)



### Colores

Para especificar colores, se pueden usar números o tuplas. Para imágenes
en modo `1`, `L` e `I` solo valen los enteros. Si el mode es `F` se deben
usar numeros on coma flotante (*float*). Para RGB se puede usar un numero
o un tupla; si se usa un numero se tomara como el valor rojo. Si el modo
es `P` es que usa un paleta de colores, y se usa un entero cpmo indice de la
paleta.

Desde la version 1.1.4 tambien se pueden usar nombres como `silver` o `navy`
Puedes ver el estandar de nombres de colores para HTML aqui:

https://en.wikipedia.org/wiki/Web_colors#HTML_color_names

*Ejercicio*: Cambia los colores y ancho de las lineas en el ejercicio anterior. ¿Cómo
harias para dibujar una cuadricula?

Ademas de dibujar lineas, tenemos las siguientes funciones definidas en el objeto draw.

- `arc(xy, start, end, fill=None, width=0)`

Dibuja un arco (una porcionde un circulo) entre los angulos indicados `start` y `end`. el
parametro `xy` es un rectangulo que define el rectangulo que inscribe el arco


```python
from PIL import Image, ImageDraw

im = Image.new("RGB", (200, 200), 'white')
draw = ImageDraw.Draw(im)

draw.arc((10, 10, 191, 191), 0, 45, fill="cyan", width=18)
draw.arc((10, 10, 191, 191), 45, 123, fill="coral", width=18)
draw.arc((10, 10, 191, 191), 123, 360, fill=(33, 66, 99), width=18)
im
```




![png](output_108_0.png)



- `chord(xy, start, end, fill=None, outline=None, width=1)`

Como el arco, pero dibuja una linea recta que une los puntos finales.


```python
from PIL import Image, ImageDraw

im = Image.new("RGB", (200, 200), 'white')
draw = ImageDraw.Draw(im)

draw.chord((10, 10, 191, 191), 0, 45, fill="cyan", outline="black")
draw.chord((10, 10, 191, 191), 45, 123, fill="coral", outline="black")
draw.chord((10, 10, 191, 191), 123, 360, fill="pink", outline="black")
im
```




![png](output_110_0.png)



- `line(xy, fill=None, width=0, joint=None)`

Dibuja una linea entra las cordenadas indicadas por `xy`

El parámetro `joint` es el conector entre una secuencia de lineas, puede
ser `curve` o `None`.


```python
import random
from PIL import Image, ImageDraw

im = Image.new("RGB", (400, 200), 'silver')
draw = ImageDraw.Draw(im)
for _ in range(10):
    x0 = random.randrange(401)
    y0 = random.randrange(201)
    p0 = (x0, y0)
    x1 = random.randrange(401)
    y1 = random.randrange(201)
    p1 = (x1, y1)
    draw.line(
        (p0, p1),
        fill=random.choice(['red', 'navy', 'yellow', 'green', 'black', 'white', 'blue']),
        width=random.choice([2, 4, 6, 8])
    )
im
```




![png](output_112_0.png)



**Ejercicio**: Usa un objeto `Draw` para meter al leon en una jaula. O, dicho de otra manera, dibuja con `line` una rejilla de lineas blancas. Tendras que usar
dos bucles, uno para dibujar las lineas verticales y otro para las horizontales. No te preocupes de que las barras coincidan exactamente con el tamanño de la imagen ni nada de eso, simplmente dibuja las lineas con una separacion fija, 32 pixels, por ejemplo.


```python
# %load cuadricula.py
from PIL import Image, ImageDraw

leon = Image.open("leon.jpg")
leon.thumbnail((400, 400))
width, height = leon.size
draw = ImageDraw.Draw(leon)
for x in range(0, width, 32):
    draw.line((x, 0, x, height), fill="white", width=5)
for y in range(0, height, 32):
    draw.line((0, y, width, y), fill="white", width=5)
leon

```




![png](output_114_0.png)



- `pieslice(xy, start, end, fill=None, outline=None, width=1)`

Como `arc` pero dibuja todas las líneas exteriores e interiores
. El parámetro `xy` es una tupla de cuatro elementos indicando la
posición del recuadro que contendrá el arco. Los parámetros `start` y `end` se especifican en grados. Un valor de $0$ se corresponde con la posición de las $3$ en el reloj (Horisontal apuntando hacia la derecha), así que si queremos hacer nuestro gráfico de tarta empezando en la posición de las 12 tenemos que empezar en $-90$.




```python
from PIL import Image, ImageDraw

im = Image.new("RGB", (200, 200), 'white')
draw = ImageDraw.Draw(im)

draw.pieslice((10, 10, 191, 191), 0, 45, fill="cyan")
draw.pieslice((10, 10, 191, 191), 45, 123, fill="coral", outline="white", width=1)
draw.pieslice((10, 10, 191, 191), 123, 360, fill="pink")
im
```




![png](output_116_0.png)



**Ejercicio:** Modificar el ejemplo anterior para que el primer gráfico, en azul, empieze en la posición de las 12.


```python
from PIL import Image, ImageDraw

im = Image.new("RGB", (200, 200), 'white')
draw = ImageDraw.Draw(im)

draw.pieslice((10, 10, 191, 191), -90, -45, fill="cyan")
draw.pieslice((10, 10, 191, 191), -45, 23, fill="coral", outline="white", width=1)
draw.pieslice((10, 10, 191, 191), 23, 270, fill="pink")
im
```




![png](output_118_0.png)



- `point(xy, fill=None)`

Dibuja un punto (un pixel individual) o puntos en las coordenadas `xy` (Que puede
ser una tupla para indicar un punto o una tupla o lista de tuplas para multiples puntos)




```python
import random
from PIL import Image, ImageDraw

im = Image.new("RGB", (200, 200), 'silver')
draw = ImageDraw.Draw(im)
for _ in range(10000):
    x = random.randrange(0, 201)
    y = random.randrange(0, 201)
    draw.point((x, y), random.choice(['red', 'navy', 'yellow', 'green', 'black', 'white', 'blue']))
im
```




![png](output_120_0.png)



- `polygon(xy, fill=None, outline=None)`

Dibuja un polígono. dibuja las lineas que unen cada dos puntos consecutivos, y luego una
linea para unir el primero con el ultimo.




```python
import random
from PIL import Image, ImageDraw

im = Image.new("RGB", (200, 200), 'silver')
draw = ImageDraw.Draw(im)
points = [
    (10, 10),
    (180, 10),
    (98, 44),
    (190, 190),
    (44, 114),
    (10, 180),
]
draw.polygon(points, fill='#336699', outline="red")
im
```




![png](output_122_0.png)



- `rectangle(xy, fill=None, outline=None, width=1)`

Dibuja un rectangulo.


```python
import random
from PIL import Image, ImageDraw

im = Image.new("RGB", (200, 200), 'silver')
draw = ImageDraw.Draw(im)
draw.rectangle([10, 10, 190, 40], fill='#336699')
im
```




![png](output_124_0.png)



- `text(xy, text, fill=None, font=None, anchor=None, spacing=4, align="left", direction=None, ...)`

Dibuja texto

Los parámetros son:

- `xy` Esquina superior izquierda del texto
- `text` Texto
- `fill` Color de relleno
- `font` Fuente a usar
- `spacing` Si el texto contiene vrias líneas, el número de pixels entre líneas.
- `align` Alinecion de l texto: `left`, `center` o `right`
- `direction` Direccion del texto: `rtl` (*right to left*), `ltr` (*left to right*) o `ttb` (*top to bottom*). 


```python
!ls
```

    Allura-Regular.ttf	 HSV.png	    pillow.ipynb
    blue-lion.png		 incredibles.png    pillow.md
    cambia-formato.py	 incredibles.webp   PrimroseDM_1000x390.jpg
    creditos.md		 leon.jpg	    rectangle.png
    croma.png		 leon.png	    rectangle.svg
    cuadricula.py		 lista-imagenes.py  rojo.py
    DandelionDM_800x665.jpg  mixed.png	    SilverweedDM_800x460.jpg
    elastigirl.png		 PaperFlowers.ttf
    fondo.jpg		 payaso.py



```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open("incredibles.png")
im.thumbnail((450, 300))
draw = ImageDraw.Draw(im, "RGBA")
draw.rectangle([80, 170, 300, 222], fill='#336699')
font = ImageFont.truetype("PaperFlowers.ttf", size=40)
draw.text((100, 170), "Have a nice Day!", font=font, fill="white")
im

```




![png](output_127_0.png)



- `textsize(text, font=None, spacing=4, direction=None, ...)`

Devuelve el tamaño que ocupará el texto pasado como parámetro si se dibuja en la imagen.


```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open("incredibles.png")
im.thumbnail((450, 300))
WIDTH, HEIGHT = im.size
draw = ImageDraw.Draw(im, "RGBA")
txt = f"{WIDTH}x{HEIGHT} pixels"
width, height = draw.textsize(txt)
print(width, height)
x = (WIDTH // 2) - (width//2)
y = (HEIGHT // 2) - (height // 2)
print(x, y)
rect = (x, y, x+width, y+height)
draw.rectangle(rect, fill='#336699')
draw.text((x, y), txt, fill="white")
im

```

    84 11
    183 107





![png](output_129_1.png)



- `ellipse(xy, fill=None, outline=None, width=1)`

Dibuja una elipse dentro del rectangulo `xy`


```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open("incredibles.png")
lienzo = ImageDraw.Draw(im, "RGBA")
lienzo.ellipse((260, 50, 330, 120), fill="red", width=2)
im
```




![png](output_131_0.png)



**Ejercicio**: Usa un objeto `Draw` para dibujar una nariz de payaso (Un circulo rojo) en el hocico de leon (O, si prefieres, dibuja con `ellipse` un circulo completo en una imagen de tu eleccion)


```python
# %load payaso.py
from PIL import Image, ImageDraw

leon = Image.open("leon.jpg")

width, height = leon.size
x, y = width //2, height // 2
y += 80
rect = (x-55, y-55, x+55, y+55)
draw = ImageDraw.Draw(leon)
draw.ellipse(rect, fill=(255, 0, 0), width=3)
leon.thumbnail((250, 350))
leon
```




![png](output_133_0.png)



### Llamadas de bajo nivel

Podemos usar los métodos `getpixel` para obtener el valor de un pixel determinado.

`getpixel` capta un único parámetro, pero este es una tupla de dos elementos, las coordenadas
x e y del pixel cuyo valor queremos obtener. En una imagen `RGB`, será una tupla de tres
elementos con las componentes rojo, verde y azul.

**Pregunta**: Cuales son los valores R, G, B del pixel en la posicion 100, 100, en el fichero `leon.jpg`
   


```python
from PIL import Image

leon = Image.open("leon.jpg")
print(leon.getpixel((100, 100)))

```

    (216, 231, 250)


Para trabajar a bajo nivel, leyendo y modificando pixels, lo recomendado es usar
el __método__ `load` de la imagen, que nos da un mapa que nos permite acceder y modificar
los pixels accediendo por índice, como si fueran una matriz.


```python
from PIL import Image

leon = Image.open("leon.jpg")
mapa = leon.load()
print(mapa[100,100])
```

    (216, 231, 250)


Pero este mapa nos deja modificar los valores, simplemente asignando un valor:
    
    mapa[x,y] = (red, green, blue)

**Ejercicio**: Cambiar a cero los valores R, G, B del pixel en la posicion 100, 100, en el fichero `leon.jpg`


```python
from PIL import Image

leon = Image.open("leon.jpg")
mapa = leon.load()

x = 100
y = 100

for xx in range(-10, 11):
    for yy in range(-10, 11):
        mapa[x+xx, y+yy] = (0, 0, 0)

mapa[x-1, y] = (255, 0, 0)
mapa[x, y-1] = (255, 0, 0)
mapa[x, y] = (255, 0, 0)
mapa[x, y+1] = (255, 0, 0)
mapa[x+1, y] = (255, 0, 0)

leon.crop((0,0, 500, 300))
```




![png](output_140_0.png)



**Miniproyecto**: Usar la siguiente foto y pegar la imagen del presentador
    
![Croma](./croma.png)

sobre este fondo

![Fondo](./fondo.jpg)

PAra poder hacer esto, necesitamos saber un par de cosas:
    
- **Cómo crear una imagen de cero**

Usamos la funcion `Image.new`. Hay que pasarle tres parámetros, el modo ("RGB" o "L"), el tamaño
de la imagen (en forma de tupla width, height) y el color de fondo.


```python
from PIL import Image

im = Image.new("L", (90, 90), "red")
im
```




![png](output_143_0.png)



**Pregunta**: Cambiar el modo a "L". ¿Qué color conseguimos? ¿Por qué?

Saber que el metodo `paste` acepta un parametro opcional, una **máscara**. Una mascara es una imagen
con una sola banda (Tonos de grises, si queremos). Al pegar una imagen sobre otra
con paste, si incluimos una imagen como mascara, -que tiene que ser del mismo tamaño que la imagen pegada- 
se sigue el siguiente metodo: si la mascara esta en blanco, se "pega" el pixel, pero si esta en negro, se ignora.
Si esta en algun tono de gris, se pega pero usando el tono de gris como canal alfa u opcidad.

Es decir, que con un 50% de gris (128 en nuestra escala de $0..255$), el pixel se pega pero con un 50 por ciento de su valor, y el otro 50 por ciento  se coge de la imagen de fondo

Asi que vamos a dividir el problema en dos: Primero obtener la mascara:
        
- Crea una nueva imagen desde cero, la mascara, con modo `L`, del mismo tamano que la imagen del presentador. Podemos obterner la imagen con el metodo `size`. Pon como solor de fondo `white`.

Examinar cada uno de los pixeles
de la imagen del presentador. Para cada pixel, si el nivel de verde es superior al de rojo y azul
sumandos, (El componente verde es, por tanto, muy fuerte), por el pixel equivalente en la mascara
a negro (esto es, a cero).

Recuerda que la mascara solo tiene una banda o canal, no como las imagenes
RGB que tienen tres. Por lo tanto, se asigna un solo valor, no una tupla). Si no cumple esta condicion, dejalo como estaba (blanco, si pusiste "white" al crearla).


```python
from PIL import Image, ImageFilter

im = Image.open("croma.png")
(width, height) = im.size

mask = Image.new("L", (width, height), 255)
mask

```




![png](output_149_0.png)




```python
from PIL import Image, ImageFilter

im = Image.open("croma.png")
source = im.load()
(width, height) = im.size

mask = Image.new("L", (width, height), 255)
mask

map_mask = mask.load()

for y in range(height):
    for x in range(width):
        (red, green, blue, _) = source[x,y]
        if green > blue + red:
            map_mask[x,y] = 0
        else:
            map_mask[x,y] = 128
mask = mask.filter(ImageFilter.BLUR).filter(ImageFilter.BLUR)        
mask
```




![png](output_150_0.png)



Con la mascara ya calculada, podemos cortar y pegar usandola para eliminar
todo el verde de la imagen original


```python
from PIL import Image


im = Image.open("croma.png")
fondo = Image.open("fondo.jpg")
fondo = fondo.resize(im.size)
fondo.paste(im, mask)
fondo
```




![png](output_152_0.png)



**ejercicios**: 

- Al crear la máscara, en vez de usar blanco puro para las partes que queremos transparentes, usa un tono de gris y repite el proceso. ¿Por qué pasa eso?

- Cuando creas la mascara, añade un filtro blur a la misma, para que los bordes no sean tan duros. Repite el proceso. Funciona mejor el croma

- Si combinas los dos efectos, obtienes una imagen fantasmal, traslucida y con un brillo verde


```python

```
