``os``: Llamadas al sistema operativo
=====================================

Este módulo da acceso a llamadas del sistema operativo sobre el que se está ejecutando el intérprete
de Python. A nivel de diseño, las llamadas que funcionana en todos los sistemas usan y devuelven la
misma interfaz, independiente del S.O. Por ejemplo, la función `stat` siempre devuelve información
sobre un fichero con el mismo formato, independientemente de la plataforma aunque, obviamente, las
llamadas realizadas al sistema operativo sean diferentes. 

Las funciones que solo están disponibles para un determinado sistema operativo estan en submódulos
aparte.

.. index:: os.path

El submodulo ``os.path`` (cargado automáticamente) incluye funciones de ayuda para trabajar con
rutas de archivos.

Algunas de las funciones y atributos de este módulo son:

.. index:: name (os)

- ``os.name`` : El nombre del sistema operativo sobre el que se está ejecutando Python. Algunos
  valores posibles son `posix`, `nt` y `java`. Si se desea más información de este tipo, véase
  también ``sys.platform`` y ``os.uname``

.. index:: environ (os)

- ``os.environ`` : Un diccionario que contiene las variables de entorno definidas en el sistema
  operativa. Los valores se obtiene la primera vez que se importa el módulo, por lo que no
  reflejaran los cambios hechos después.

.. index:: walk (os)

- ``os.walk(top, topdown=True, onerror=None, followlinks=False)`` : Devuelve un iterador que nos
  permite examinar todo un sistema de archivos. Para cada directorio y subdirectorio en la raíz
  (indicada por ``top``), incluyendo la propia raíz, el iterador devuelte una tupla de tres
  elementos (normalmente llamados ``dirpath``, ``dirnames`` y ``filenames``); ``dirpath`` es una
  cadena de texto, la ruta del directorio, ``dirnames`` es una lista con los nombres de los
  subdirectorios dentro de ``dirpath`` (excluyendo los nombres especiales `.` y `..`) y
  ``filenames`` es una lista de nombres de los ficheros que **no** son un directorio en ``dirpath``.
  En cualquier momento podemos tener una ruta absoluta a un archivo ``f`` en ``filenames`` haciendo
  ``os.path.join(top, dirpath, f)``.

.. index:: getsize (os.path)

- ``os.path.getsize(path)`` : Devuelve el tamaño, en bytes, del fichero cuya ruta se la pasa como
  parámetro.

.. index:: getmtime (path)

- ``os.path.getmtime(path)`` : Devuelve el tiempo de la ultima modificación del archivo. El valor es
  en tiempo unix: el número de segundos desde la medianoche UTC del 1 de enero de 1970. Vease el
  módulo ``time``.

.. index:: splitext (path)

- ``os.path.splitext(path)``: Devuelve una tupla de dos elementos (root, ext). En la primera
  posición va la ruta completa del fichero, sin extensión, y en la segunda va la extension, de forma
  que ``path`` == ``root + ext``.

.. note:: Ejercicio: Calcular cuanto ocupan todos los ficheros de tipo Python en un determinado
    directorio, incluyendo sus subdirectorios, si los hubiera. Listar los nombres absolutos, es decir,
    incluyendo la ruta desde la raíz, así como el espacio total que ocupan en disco.

Solución::

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
    ./fibo.py 453
    ./fibo_memoized.py 330
    ./test_ast.py 140
    ./ejercicios/find_zips.py 719
    ./ejercicios/http_server.py 343
    ./ejercicios/find-by-ext.py 887
    Bytes totales: 2872
