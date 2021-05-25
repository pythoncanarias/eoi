---
title: os. Llamadas al sistema operativo
---

Este módulo da acceso a llamadas del sistema operativo sobre el que se
está ejecutando el intérprete de Python. A nivel de diseño, las llamadas
que funcionana en todos los sistemas usan y devuelven la misma interfaz,
independiente del S.O. Por ejemplo, la función <span
class="title-ref">stat</span> siempre devuelve información sobre un
fichero con el mismo formato, independientemente de la plataforma
aunque, obviamente, las llamadas realizadas al sistema operativo sean
diferentes.

Las funciones que solo están disponibles para un determinado sistema
operativo estan en submódulos aparte.

### os.name

Indica el sistema operativo sobre el que se esta ejecutando el interprete de
Python. Los valores posibles son: 'posix', 'nt' y 'java'.  Para más información
de este tipo, véase también `sys.platform` y `os.uname`.

### os.environ

La variable `environ` es un diccionario que contiene las variables de
entorno definidas en el sistema operativa. Los valores se obtiene la primera
vez que se importa el módulo, por lo que no reflejaran los cambios hechos
después.

### os.getenv

La función `getenv(key, default=None)` retorna el valor de la variable de
entorno especificado como clave (`key`), si existei en `os.environ`, o el valor
en `default` si no existe. Tanto `key`, como `default` deben ser cadenas de
texto.

### os.listdir

La función `os.listdir(path='.')` devuelve una lista conl los nombres de los
ficheros y directorios contenidos dentro de la ruta indicada por `path`. La
lista no está ordenada y no incluye las entradas especiales `.` ni `..`.

### os.walk

La función `os.walk(top, topdown=True, onerror=None, followlinks=False)`
devuelve un iterador que nos permite examinar todo un sistema de archivos. Para
cada directorio y subdirectorio en la raíz (indicada por `top`), incluyendo la
propia raíz, el iterador devuelve una tupla de tres elementos (normalmente
llamados `dirpath`, `dirnames` y `filenames`); `dirpath` es una cadena de
texto, la ruta del directorio, `dirnames` es una lista con los nombres de los
subdirectorios dentro de `dirpath` (excluyendo los nombres especiales `.`
y `..`) y `filenames` es una lista de nombres de los ficheros que **no** son un
directorio en `dirpath`. En cualquier momento podemos tener una ruta absoluta a
un archivo `f` en `filenames` haciendo `os.path.join(top, dirpath, f)`.

### os.mkdir

La función `os.mkdir(path)` crea el directorio especificado en `path`. Si el
directorio ya existe, se eleva una excepción de tipo `FileExistsError`.

### os.is_dir

La función `is_dir(path)` devueve `True` si la ruta pasada como parámetro
es un directorio o un enlace simbólico que apunta a un directorio. Devuelve
`False` si la entrada es o apunta a otro tipo de archivo, o si no existe.

### os.is_file

La función `is_file(path)` devuelve `True` si la ruta pasado como
parámetro es un archivo o un enlace simbólico que apunta a un archivo. Devuelve
`False` si la entrada es o apunta a un directorio o a otra entrada que no sea
un archivo, o si ya no existe.


El submodulo `os.path` (cargado automáticamente) incluye funciones de
ayuda para trabajar con rutas de archivos.

Algunas de las funciones y atributos de este módulo son:

### os.path.getsize

La función `os.path.getsize(path)` devuelve el tamaño, en bytes, del fichero
cuya ruta se la pasa como parámetro.

### os.path.getmtime

La función `os.path.getmtime(path)` devuelve el momento de la última
modificación del archivo. El valor es en tiempo unix: el número de
segundos desde la medianoche UTC del 1 de enero de 1970. Vease el
módulo `time`.

### os.path.splitext

La función `os.path.splitext(path)` devuelve una tupla de dos elementos.
En la primera posición va la ruta completa del fichero, sin
extensión, y en la segunda va la extension, de forma que:

```python
root, ext = os.path.splitext(path)
assert path == root + ext
```

**Ejercicio**: Calcular cuanto ocupan todos los ficheros de tipo Python en
un determinado directorio, incluyendo sus subdirectorios, si los
hubiera. Listar los nombres absolutos, es decir, incluyendo la ruta
desde la raíz, así como el espacio total que ocupan en disco.

**Solución**:

```python

import os

acc = 0
for (dirpath, dirnames, filenames) in os.walk('.'):
    for filename in filenames:
        if filename.lower().endswith('.py'):
            fullname = os.path.join(dirpath, filename)
            size = os.path.getsize(fullname) 
            acc += size
            print(fullname, size)
print('Bytes totales:', acc)
```
