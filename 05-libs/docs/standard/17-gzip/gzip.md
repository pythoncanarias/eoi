---
title: Compresión de datos con gzip
---

### Contenido del módulo

Este módulo proporciona una interfaz simple para comprimir y descomprimir
ficheros, de la misma forma que los programas GNU `gzip` o `gunzip`. El
algoritmo de compresión es el mismo que usa la librería `zlib`.

EL módulo proporciona una clase, `GzipFile`, y varias funciones convenientes,
como  `open()`, `compress()` y `decompress()`.

La clase `GzipFile` puede leer y escribir ficheros comprimidos en formato gzip,
realizando las tareas de compresión y descompresión de forma automática, por lo
que para nosotros es como si fuera un fichero normal y corriente.

Al contrario que con el formato _ZIP_, el formato _gzip_ solo permite comprimir y
descomprimir un fichero, porque no tiene capacidad de archivado (Es decir, la
posibilidad de añadir varios ficheros dentro del archivo).

Para crear un fichero comprimido con _gzip_, simplemente
lo abrimos con el modo `wb` (`w` para escritura, *write*, `b`
para binario, *binary*):

```python
import gzip
   
content = "Hay mucho contenido aquí.\n".encode('utf-8') * 888
with gzip.open('file.txt.gz', 'wb') as f:
    f.write(content)
```

**Ejercicio**: Usar `cat` o alguna utilidad equivalente para ver el contenido
del fichero `file.txt.gz`.

Un ejemplo  de como leer un fichero comprimido::

```python
import gzip
    
with gzip.open('file.txt.gz', 'rb') as f:
    file_content = f.read().decode('utf-8')
print(file_content[0:100])
```

#### Ejercicio: Comprimir un archivo existente

Comprimir el contenido del fichero [`lorem.txt`](lorem.txt) en un nuevo archivo
`lorem.txt.gz`.

Nota: Los objetos de tipo `GzipFile` incluyen un método `writelines()` que se
puede usar para escribir una lista o secuencia de líneas de texto.


```python
import gzip

with open("lorem.txt", "r") as entrada:
    with gzip.open("lorem.txt.gz", "wb") as salida:
        datos = entrada.read().encode('utf-8')
        salida.write(datos)
```

Usa el siguiente código para comprobar la diferencia de tamaño entre los dos
ficheros.


```python
import glob
import os

for filename in glob.glob("lorem*"):
    size = os.path.getsize(filename)
    print(f"- El fichero {filename} pesa {size} bytes")
```

La salida debería ser algo así como:

```
- El fichero lorem.txt pesa 57060 bytes
- El fichero lorem.txt.gz pesa 22316 bytes
```
