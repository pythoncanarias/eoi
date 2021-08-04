El paquete urllib
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El paquete urllib incluye modulos especificos para abrir y trabajar
con direcciones de internet (URLs)

Dentro de este paquete, se encuentran los siguiente módulos:

- ``urllib.request`` usado para abri y lerr URLs

- ``urllib.error`` contiene las exceprciones usadas por ``urllib.request``

- ``urllib.parse`` para analizar y descompones en partes las URLs

- ``urllib.robotparser`` para procesar ficheros de tipo `robots.txt`


La función más usada del módulo ``request`` es la siguiente::

    urllib.request.urlopen(url[, data][, timeout])

Que abre la url indicada, dandonos un objeto similar a un fichero.

En el parámetro opcional ``data`` podemos incluir información
adicional  que requieren ciertas peticiones web, especialmente
``POST``. Si se incluye, ``data`` debe estar formateada con el
estándar  ``application/x-www-form-urlencoded``, algo que podemos
conseguir usando la función ``urllib.parse.urlencode()``, que acepta como
parámetro un  diccionario o una secuencia de parejas (2-tuplas), y
deveulve una string en dicho formato.

El otro parámetro opcional, ``timeout``, indica el tiempo en segundos
que debemos esperar antes de descartar por imposible una conexión.

El objeto devuelto, además de comportarse como un archivo, dispone de
tres métodos adicionales:

- ``geturl()``

  Devuelve la URL del recurso recuperado. Esto se utiliza
  noprmalmente para determinar si ha habido alguna clase de
  recirección.

- ``info()``

  Devuelve la meta-información sobre el recurso solicitado, como
  las cabeceras, en forma de una instancia de la clase
  ``mimetools.Message``.

- ``getcode()``

  Devuelve el código de estado del protocolo HTTP de la
  respuesta.

Ejemplo: Salvar una página de Internet en un fichero local::

    import urllib2

    url = 'http://www.python.org/'
    f = urllib2.urlopen(url)
    with open('python.html', 'w') as salida:
        for linea in f.readlines():
            salida.write(linea)
    f.close()
