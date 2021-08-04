---
title: La librería zlib
---

### Contenido del módulo

Aunque la capacidad de almacenamiento en los ordenadores sigue incrementándose,
también lo hace la cantidad de datos que queremos almacenar. Para solucionar
esto se inventaron hace tiempo varios **algoritmos de compresión**, que nos
permiten almacenar la misma cantidad de información en menos espacio, teniendo
que usar, eso si, un poco más de tiempo para acceder o modificar la información.

En Python, Los módulos `zlib` y `gzip` nos permiten acceder a estos dos
algoritmos de compresión clásicos, mientras que el modulo `bzip2` usa un
formato y algoritmo algo más moderno.

Siempre trabajamos con un flujo de *bytes*, es decir, que podemos comprimir
información en cualquier formato que nos interese, porque los algoritmos no se
preocupan por el formato, solo "ven" secuencias de bytes.

Los tres módulos incluyen también funciones para trabajar, de forma
transparente, con ficheros comprimidos.

Ademas de las funciones de compresión, habitualmente se usa también el
concepto de **archivado**, esto es, incluir varios archivos dentro de otro, normalmente
para copias de seguridad o trasmisión. 

Estos dos conceptos, compresión y archivado no son lo mismo.

- puedes tener un fichero comprimido, sin archivado (es decir, que solo
esta comprimido un único fichero)

- O se puede tener un archivador sin usar compresión.

Pero normalmente estas dos funcionalidades suelen ir juntas.

Nota: En la librería estándar hay módulos para trabajar con otros formatos de
compresión/archivado, como `tarfile` para trabajar con ficheros *.tar*, usados
frecuentemente en sistemas tipo Unix, o `zipfile` para manipular archivos
*.zip*, un formato muy popular en los entornos *Windows* desde los tiempos del
*MS/DOS* (Ambos sistemas pueden encontrarse ya en cualquier entorno, no
obstante). En este curso no veremos estos módulos, pero es importante que sepan
que están ahí, en caso de que los necesiten.

### El módulo zlib

Como siempre, para poder usarlo tenemos que importarlo:

```python
import zlib
```

Podemos comprimir y descomprimir directamente contenidos en memoria. En el caso
de `zlib`, usamos los métodos **`compress`** y **`decompress`**. Vamos a verlo ejecutando
el siguiente ejemplo.


```python
import zlib

message = """
Hola, me llamo Íñigo Montoya. Tu mataste a mi padre. Preparate a morir
""".encode("utf-8")
print(f"El mensaje original ocupa {len(message)} bytes")
compressed = zlib.compress(message)
print(f"El mensaje comprimido ocupa {len(compressed)} bytes")
```

    El mensaje original ocupa 74 bytes
    El mensaje comprimido ocupa 78 bytes


**Ejercicio**: ¿Notan algo raro en el ejemplo anterior?

![El mensaje comprimido ocupa más que el mensaje sin descomprimir](emosido.jpg)

Efectivamente ¡El mensaje comprimido ocupa más que el mensaje sin descomprimir! Justo
lo contrario de lo que debería pasar! Esto es por varias razones:

- Los algoritmos de compresión trabajan mejor cuanto mas repeticiones de
  símbolos haya (trabajan reduciendo la redundancia)

- Cuanto más contenido, mejor compresión (Más probabilidad de encontrar redundancia)

Vamos a ver que tal funciona con una supuesta secuencia de genes (Solo cuatro
símbolos, `G`, `A`, `T` y `C`):

```python
import zlib

message = b"GGAAATGGTAGGGCTAGATGCCCCTTAGCTCATGCGCTGCGCTCATCAAACCTAGGTTATTAGCACTAACAT"

print(f"El mensaje original ocupa {len(message)} bytes")
compressed = zlib.compress(message)
print(f"El mensaje comprimido ocupa {len(compressed)} bytes")
```

La salida es:

```
El mensaje original ocupa 72 bytes
El mensaje comprimido ocupa 49 bytes
```

### Ejercicio: Descomprimir un mensaje

Hemos recibido el siguiente mensaje, comprimido con `zlib`:

```python
message = b'x\x9c\xf3\xc9WH\xce\xcf+NM/\xcd,.IU\x04\x00,\xcc\x05\xa6'
```

Usa la función `decompress` del modulo `zlib` para leer el mensaje original.

```python
import zlib

message = b'x\x9c\xf3\xc9WH\xce\xcf+NM/\xcd,.IU\x04\x00,\xcc\x05\xa6'
print(zlib.decompress(message))
```


### Compresion/Decompresión incremental

El problema de comprimir en memoria es que nos limita, porque necesitamos
mantener a la vez los datos comprimidos y sin descomprimir.

Para solucionar esto tenemos las clases `Compress` y `Decompress` (Que
obtenemos con las llamadas a `compressobj` y `decompressobj`) que nos permiten
trabajar con los datos de forma incremental y con datos demasiado grandes para
caber en memoria. Podemos obtener un objeto de la clase `Compress` llamando a
la función `compressobj`.

Este ejemplo lee el contenido de un archivo de texto en pequeños trozos (de 64
bytes como máximo) y se los pasa al compresor. Como el algoritmo depende de
cálculos realizados en bloques de tamaño fijo, puede que el compresor no esté
listo para devolver la secuencia de salida comprimida, en ese caso devuelve una
cadena vacía (de ahí el `if` después de la llamada a `compress`)

Cuando ya se han enviado todos los datos, se llama al método `flush` para
forzar al compresor a terminar con el ultimo bloque y devolver el resto de los
datos comprimidos.

```python
import zlib

compressor = zlib.compressobj(wbits=9)

original_size = 0
compressed_size = 0
buffer = bytearray()
filename = "lorem.txt"
print(f"Comprimiento fichero {filename}", end=": ")
with open(filename, 'r') as input:
    while True:
        block = input.read(2048).encode('utf-8')
        if not block:
            break
        original_size += len(block)
        compressed = compressor.compress(block)
        if compressed:
            compressed_size += len(compressed)
            buffer += compressed
            print("█", end="")
        else:
            print("░", end='')
    remaining = compressor.flush()
    compressed_size += len(remaining)
    buffer += remaining
print("[OK]")

p = round(compressed_size * 100.0 / original_size,2)
print(f"Fichero {filename} comprimido con tasa de compresion {p:.02f}")
print("[Tam. original:", original_size)
print("Tam. comprimido:", compressed_size)
```

**Ejercicio**: Descomprimir de memoria

El contenido del fichero "lorem.txt" está ahora en memoria, si se ha ejecutado la calda
anterior, en la variable `buffer`. descomprime el contenido y muestra las primeras
3 líneas de texto. Puedes usar `decompress`.

Recuerda que después de descomprimirlo siguen siendo *bytes*, asi que hay que
decodificarlos para obtener texto. Se codifico originalmente con `utf-8`, asi
que hay que usar el mismo esquema para decodificar.


```python
import zlib

text = zlib.decompress(buffer).decode('utf-8')

for i, line in enumerate(text.split("\n\n")):
    print(f"linea {i}: \"{line}\"")
    if i == 2: 
        break
```
### Checksums

Además de las funciones de compresión y descompresión, se incluyen en `zlib` dos funciones
para calcular *checksums* de los datos, `adler32` y `crc32`. Ambas funciones estan pensadas
para ser usadas unicamente para propositos de verificacion de datos, ya que no se consideran
seguras desde el punto de vista criptográfico.

```python
import zlip

assert zlib.crc32(buffer) == 3465102946
assert zlib.adler32(buffer) == 136868278
