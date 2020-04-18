## La libreria pillow

Pillow es un *fork* de la libreria PIL (*Python Image Library*)
Con __pillow__ añadimos a Python la capacidad de procesar imágenes.

Sus caracterísitcas más importantes son:

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

Pare cargar una imagen desde disco, esamos la función `open()` dentro
del módulo `Image`:


from PIL import Image
im = Image.open("toystory.webp")

Si tiene éxito, la función devuelve un objeto de tipo `Image`. Podemos examinar
atributos de la instancia para obtener información adicional de la imagen:

print(im.format, im.size, im.mode)

El atributo `format` identifica el formato usado para almacenar la imagen (Si
la imagen no se ha creado a a partir de una imagen, `format` vale `None`. El
atrbuto `size` es una dupla que contiene el ancho y alto de la imagen, en
*pixels*. El atributo `mode` nos permite saber el número y nombre de las
bandas de la imagen, así como el tipo de pixel y la profundidad. Algunos
valores habituales de `mode` son: "L" (De luminancia) se usa para imagenes
en escala de grises, "RGB" identifica imagenens en color real con 24 bits de
profuncidad, y "CMYK" indica una imagen preparada para usarse en ssitemas
de impresión.

Una vez que tenemos la instancia de la imageh, podemos usar los diferentes métodos
definidos en la clase para procesar y manipular las imágenes.

Por ejemplo, podemos mostrar la imagen llamando al métdodo `show`.

im.show()


