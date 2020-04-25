La libreria ``request``: HTTP para humanos
------------------------------------------------

Requests es una biblioteca HTTP de Python pensada para hacer que las solicitudes HTTP sean más
sencillas y amigables para los humanos.

Ventajas de usar requests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Permite realizar peticiones usando el protocolo HTTP/1.1 muy facilmente. no hay necesidad de añadir
  *query strings* manualmente, ni codificar en forma de formulario los datos enviados en un
  ``POST``. Ciertos temas engorrosos como mantener las conexiones *keep-alive* o mantener
  un *pool* de conexiones se gestionan de forma automática, gracias a ``urllib3``.

- Gestión de *cookies* y *sesiones*, Autentificación *Basic/Digest*

- Varificacion SSL de conexiones https, como las que realiza el navegador.

- Codificación y decodificación automática de los contenidos. Descompresión automatica. Las
  respuestas son por defecto unicode. Subida de ficheros multiparte. Descargas de *Streaming*.

Veamos un ejemplo de uso::

    >>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    >>> r.status_code
    200
    >>> r.headers['content-type']
    'application/json; charset=utf8'
    >>> r.encoding
    'utf-8'
    >>> r.text
    u'{"type":"User"...'
    >>> r.json()
    {u'private_gists': 419, u'total_private_repos': 77, ...}

Ejercicio: 
