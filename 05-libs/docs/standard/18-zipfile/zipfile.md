---
title: zipfile — Soporte para archivos ZIP
---

### Contenido del módulo

El archivo _ZIP_ es un formato estándar de archivado y compresión de archivos.
El módulo `zipfile` proporciona mecanismos para crear, leer, modificar y listar
archivos ZIP. 


```python
import zipfile
```

### La función is_zipfile

La función `is_zipfile()` devuelve un booleno indicando si el fichero que se le
pasa como parámetro es un archivo ZIP o no.

**Ejercicio**: Hacer un pequeño script para listar los ficheros del directorio
actual. Usar alguna indicación visual para destacar aquellos que sean archivos
`zip`. Usa `zipfile.is_zipfile` para descubrir si un fichero es o no un archivo
`zip`.

Solución:

```python
import os
import zipfile

for filename in os.listdir("."):
    flag = zipfile.is_zipfile(filename)
    print(f"- {filename} {'<-- Este es un ZIP' if flag else ''}")
```

Copia el siguiente fichero: [`files.backup`](files.backup) donde tengas el
programa anterior y vuelve a ejecutarlo. Si todo ha ido bien, veras que lo
detecta como un fichero `zip` entre los listados, a pesar de que no tiene 
la extensión `.zip`. El fichero se llama `files.backup`. Vamos a seguir usando
el módulo `zipfile` para leer su contenido.

### La clase ZipFile

La clase ``ZipFile`` nos permite trabajar directamente con un archivo ZIP.
Tiene métodos para obtener información sobre los ficheros contenidos en el
archivo, así como para añadir nuevos ficheros a un archivo.

Para crear una instancia de `ZipFile`, especificamos un modo igual que hacemos
con los ficheros normales. Así, para abrir un fichero `zip` para leer sus
contenidos, usaremos el modo `r`. Usaremos `w` para crear el archivo nuevo (O
truncar uno ya existente), `a` para añadir o `x` para crear y añadir contenidos
de forma exclusivo.

Otro parámetro que podemos usar al crear un archivo `.zip` es `compression`, con
el cual indicaremos el algoritmo de compresión que queremos. Puede tomar los
valores `ZIP_STORED`, `ZIP_DEFLATED`, `ZIP_BZIP2` o `ZIP_LZMA`. El valor por
defecto es `ZIP_STORED`

El parámetro `compresslevel` determina el nivel de compresión y sus posibles
valores son, por tanto, función del algoritmo de compresión seleccionado. Para
`ZIP_STORED` o `ZIP_LZMA` no tiene efecto ninguno.  Si se usa `ZIP_DEFLATED`,
los valores posibles son enteros en el rango de $0$ a $9$ (Son los mismos
valores que usa `zlib`). Cuando se usa `ZIP_BZIP2` se aceptan enteros en el
rango $1$ a $9$.

La clase `ZipFile` también actúa como un gestor de contexto (*context
manager*), por lo que sus instancias pueden ser usadas con la sentencia `with`.

Para leer los nombres de los ficheros contenidos dentro del archivo ZIP,
podemos usar el método `namelist`, que nos dará un listado de los ficheros
incluidos en el archivo. Ejecuta el código siguiente para ver el contenido:


```python
import zipfile

with zipfile.ZipFile('files.backup', 'r') as zf:
    for filename in zf.namelist():
        print(filename)
```

La salida debería ser:

```
COPYING
LindenHill.otf
LindenHill-Italic.otf
```

### La clase `ZipInfo`

Vamos a obtener un poco más de información de estos ficheros. Para ello
podemos usar el método `getinfo(name)`. Este nos devuelve un objeto 
de tipo `ZipInfo` que contiene información sobre el fichero:

```python
import zipfile

with zipfile.ZipFile('files.backup', 'r') as zf:
    for filename in zf.namelist():
        info = zf.getinfo(filename)
        print(filename, 'pesa', info.file_size, 'bytes')
```

La salida debería ser:

```
COPYING pesa 1058 bytes
LindenHill.otf pesa 120992 bytes
LindenHill-Italic.otf pesa 86760 bytes
```

Otra forma sería usando el método `infolist` que nos devuelve directamente
una lista de objetos `ZipInfo`. Como el nombre del fichero está incluido
en la información que almacena esta clase, es una forma un poco más
directa de conseguir la información:
    
```python
import zipfile

with zipfile.ZipFile('files.backup', 'r') as zf:
    for info in zf.infolist():
        print(info.filename, 'pesa', info.file_size, 'bytes')
```

La salida, ahora:

```
COPYING pesa 1058 bytes
LindenHill.otf pesa 120992 bytes
LindenHill-Italic.otf pesa 86760 bytes
```

Ya solo nos faltaría poder leer el contenido de cada fichero. Es
fácil e intuitivo, porque la clase nos proporciona un método `open`
para abrir el archivo y leer su contenido:


```python
import zipfile

with zipfile.ZipFile('files.backup', 'r') as zf:
    with zf.open('COPYING', 'r') as f:
        print(f.read(250).decode('utf-8'))
```

La salida:

```
Copyright (c) 2010 Barry Schwartz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limit
```

### Crear un archivo zip

Como dijimos antes, los objetos que nos devuelve la clase ZipFile son como
archivos:

```python
import zipfile

with zipfile.ZipFile('backup.zip', 'a') as zf:
    with zf.open('ejemplo.txt', 'w') as f:
        f.write(b"Este el el ejemplo")
```


### Otros métodos interesantes

- `extract(member, path=None, pwd=None)`

Extrae un fichero del archivo ZIP a un directorio externo (el directorio
actual, si no se especifica). El atributo `member` puede ser el nombre del
fichero o un objeto del tipo `ZipInfo`. `path` especifica el directorio
destino. `pwd` es la contraseña a usar si el fichero estaba cifrado.


```python
import zipfile

with zipfile.ZipFile('backup.zip', 'a') as zf:
    zf.extract('LindenHill.otf', '.')
```

- `extractall(path=None, members=None, pwd=None)`

Extrae todos los contenidos del archivo ZIP a un directorio externo.  El
parámetro `path`, igual que en el método `extract` indica el directorio
destino, y si no se especifica, por defecto tomará el directorio actual. El
parámetro `members` es opcional, y permite especificar, mediante una lista de
nombres u objetos `ZipInfo`, un subconjunto de los contenidos a extraer. `pwd`
es, de nuevo, la contraseña a usar si los ficheros estuvieran cifrados.

- `printdir()`

Imprime una tabla de  los contenidos del archivo en la salida estándar.

- `setpassword(pwd)`

Define el valor de `pwd` como el nuevo valor por defecto de la contraseña
a usar para extraer contenidos cifrados.

- `read(name, pwd=None)`

Devuelve el contenido en *bytes* del archivo que se indica como parámetro. El
parámetro `name` puede ser el nombre del fichero, o bien un objeto de tipo
`ZipInfo`. El archivo ZIP debe estar abierto en modo `r` (*read*) o `a`
(*append*). `pwd` es la contraseña usada para cifrar el fichero, y si se
especifica, su valor sobreescribe el valor establecido de forma global con
`setpassword`.

- `testzip()`

Lee todos los ficheros del archivo ZIP, y comprueba sus valores de CRC y las
cabeceras de los archivos. Devuelve el nombre del primer fichero incorrecto, o
`None` si todos están bien.

- `write(filename, arcname=None, compress_type=None, compresslevel=None)`

Escribe el fichero especificado por `filename`, con el nombre especifica en
`arcname` (a veces nos puede interesar que el nombre no sea exactamente el
mismo que la ruta original, por ejemplo en _Windows_ no se puede incluir la
letra del disco duro. Si no se especifica, se usará el valor de `filename`,
pero sin la letra del disco duro ni los directorios intermedios usados para
indicar el fichero. Si se indica un valor para `compress_type` se usara este en
ves del nivel por defecto del archivo. De la misma manera, `compresslevel`
sobreescribirá, si se especifica, el valor por defecto. Para poder realizar
esta operación el archivo tiene que abrirse en modo `w`, `x` o `a`.

- `writestr(zinfo_or_arcname, data, compress_type=None, compresslevel=None)`

Sirve para escribir contenidos a partir de datos en memoria, especificados en
el parámetro `data`, y no del sistema de archivos. Los parámetros son
equivalentes a los de `write`.  `zinfo_or_arcname` es o un nombre de fichero o
una instancia de `ZipInfo`. En este último caso, se ha de especificar
obligatoriamente un nombre, fecha y hora. Si se usa un nombre, la fecha y hora
se tomarán del momento actual. Para poder realizar esta operación el  archivo
tiene que abrirse en modo `w`, `x` o `a`.

## Atributos disponibles en un objeto ZipFile

- `filename`

El nombre del archivo ZIP

- `debug`

El nivel de *debug* a usar. Puede variar de $0$ (valor por defecto; sin salida)
a $3$ (El valor de máxima información). La salida se escribe a `sys.stdout`.

- `comment`

Un comentario asociado con el archivo ZIP. No puede exceder de 65535 bytes. Se
puede asignar si se abrió el archivo en modo `w`, `x` o `a`.

**Micro proyecto**: Hacer un _script_ para almacenar en un archivo `archivo.zip` todo
los ficheros del directorio actual que tengan la extensión `ipynb`.


Solución:

```python
import zipfile
import os

with zipfile.ZipFile('archivo.zip', 'w') as zf:
    for fn in os.listdir('..'):
        _, ext = os.path.splitext('../' + fn)
        if ext == ".py":
            print(f"Guardando {fn}")
            zf.write('../'+fn)
```
