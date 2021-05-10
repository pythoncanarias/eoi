La libreria requests
====================

Requests es una librería para HTTP escrita en Python, para seres
humanos.

Se diseño desde el principio siguiendo muy de cerca algunos de
los principios de estilo PEP 20:

- Hermoso es mejor que feo.

- Explícito es mejor que implícito.

- Simple es mejor que complejo.

- Complejo es mejor que complicado.

- La legibilidad cuenta.

Se instala con ayuda del comando ``pip``:

.. code:: bash 

    pip install requests


.. code:: ipython3

    import requests

Ejemplo con requests

.. code:: ipython3

    r = requests.get('http://localhost:8000')
    print(r.status_code)
    for nm in r.headers:
        print(nm, ':', r.headers[nm])
    print(r.encoding)
    #print(r.text)


.. parsed-literal::

    200
    Server : SimpleHTTP/0.6 Python/3.6.9
    Date : Tue, 21 Apr 2020 18:21:22 GMT
    Content-type : text/html; charset=utf-8
    Content-Length : 672
    utf-8


En python 2, un codigo equivalente a esto era bastante mas largo e
incomodo de leer. Es verdad que ahora, con el cambio llevado a las
librerias en Python3, la diferencia ya no es tanta. Aun asi,
``requests`` llega más lejos en terminis de comodidad y facilidad de
uso.

Si tu programa hace uso extensivo de llamadas a servidores http,
seguramente ``requests`` te aportara un código más sencillo y te
conviene usarlo, si solo haces una unica llamada, igual
solo te ahorrarías un par de lineas extra,
lo que no compensaría añadir otra dependencia.


Realizar un petición GET
------------------------

Realizar una petición en Requests muy sencillo.

Comienza importando el módulo de Requests::

     import requests

Ahora, intentemos obtener un página web. Para este ejemplo, vamos a
obtener el timeline público de GitHub::

    r = requests.get('https://api.github.com/events')
    data = r.json()

Ahora, tenemos un objeto Response llamado ``r``. Podemos obtener toda la
información que necesitamos a partir de este objeto.

**Ejercicio**: En la propiedad ``status_code`` podemos acceder al codigo
de respuesta del servidor. Este es el famoso 404 que obtenemos a veces
en el navegador, si intentamos acceder a una pagina que no existe, por
ejemplo.

El codigo para «todo ha ido bien» en 200.

Haz un pequeño script para comprobar una serie de paginas web. Has una
peticion de tipo GET para cada direccion y conprueba que el
``status_code`` de la respuesta en 200. Imprime un codigo de error en
caso contrario.

Puedes usar estas direcciones, o modificarlas a tu gusto::

   urls = [
       'https://www.google.com/',
       'https://github.com/',
       'https://www.parcan.es/',
   ]

GET es el tipo de peticion mas frecuente, pero puedes acceder a todos
los verbos HTTP:

-  requests.post(“http://httpbin.org/post”)

-  requests.put(“http://httpbin.org/put”)

-  requests.delete(“http://httpbin.org/delete”)

-  requests.head(“http://httpbin.org/get”)

-  requests.options(“http://httpbin.org/get”)

**Ejercicio**: Cambia el código anterior para que use ``head`` en vez de
``get``. Va más rapida? Por qué? Devuelven todas los servidores el
código ``200``?

Pasar parámetros en URLs
------------------------

Con frecuencia, debes enviar algún tipo de información en el query
string de la URL. Si estuvieses creando la URL a mano, esta información
estaría en forma de pares llave/valor luego del signo de interrogación
en la URL, por ejemplo ``httpbin.org/get?key=val``.

Requests te permite proveer estos argumentos en forma de diccionario,
usando el parámetro en llave (keyword argument) params. Como ejemplo, si
quisieras pasar key1=value1 y key2=value2 a httpbin.org/get, usarías
algo como esto:

.. code:: ipython3

    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get("http://httpbin.org/get", params=payload)

Puedes ver que la URL ha sido codificada correctamente imprimiéndola:

.. code:: ipython3

    print(r.url)


.. parsed-literal::

    http://httpbin.org/get?key1=value1&key2=value2


Nota: cualquier llave del diccionario cuyo valor es ``None`` no será
agregada al *query string* del URL.

Contenido de respuesta
----------------------

Podemos leer el contenido de la respuesta del servidor. Usemos el
listado de eventos de GitHub nuevamente:

.. code:: ipython3

    import requests
    r = requests.get('https://api.github.com/events')
    r.json()[2]['id']




.. parsed-literal::

    '12115403054'



Requests automáticamente decodificará el contenido que viene del
servidor. La mayoría de caracteres unicode serán decodificados
correctamente.

Cuando ejecutas una petición, Requests tratará de obtener la
codificación de la respuesta basándose en las cabeceras HTTP. La
codificación del texto que Requests encontró (o supuso), será utilizada
cuando se acceda a ``r.text``. Puedes conocer la codificación que
``Requests`` está utilizando, y cambiarla, usando la propiedad
r.encoding:

.. code:: ipython3

    import requests
    
    r = requests.get('https://google.com/')
    r.encoding




.. parsed-literal::

    'ISO-8859-1'



Contenido de respuesta JSON
---------------------------

Hay un decodificador de JSON incorporado en Requests:

.. code:: ipython3

    import requests
    
    r = requests.get('https://api.github.com/events')
    print(r.json())


Cabeceras personalizadas
------------------------

Si quieres agregar cabeceras HTTP a una petición, simplemente pasa un
dict al parámetro headers.

Por ejemplo, en el ejemplo anterior no especificamos la cabecera
content-type::

   import json
   url = '...'
   payload = {'some': 'data'}
   headers = {'content-type': 'application/json'}
   r = requests.post(url, data=json.dumps(payload), headers=headers)

Peticiones POST más complicadas
-------------------------------

Típicamente, quieres enviar información en forma de formulario, como un
formulario HTML. Para hacerlo, pasa un diccionario al parámetro
``data``. Este diccionario será codificado automáticamente como
formulario al momento de realizar la petición:

(Para este ejemplo, asegurate de tener un serivor local corriendo en
otra terminal, con ``python -m http.server``).

.. code:: ipython3

    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://localhost:8000/post", data=payload)

Cabeceras de respuesta
----------------------

Podemos ver las cabeceras de respuesta del servidor utilizando un
diccionario::

    r.headers
    { ‘status’: ‘200 OK’, ‘content-encoding’: ‘gzip’,
    ‘transfer-encoding’: ‘chunked’, ‘connection’: ‘close’, ‘server’:
    ‘nginx/1.0.4’, ‘x-runtime’: ‘148ms’, ‘etag’:
    ‘“e1ca502697e5c9317743dc078f67693f”’, ‘content-type’: ‘application/json;
    charset=utf-8’ }

Este diccionario es especial: está hecho únicamente para las cabeceras
HTTP. De acuerdo con el RFC 7230 , los nombres de las cabeceras HTTP no
hacen distinción entre mayúsculas y minúsculas.

Así que podemos acceder a las cabeceras utilizando letras mayúsculas o
minúsculas::

    r.headers['Content-Type']
    'application/json; charset=utf-8'
    r.headers.get('content-type')
    'text/html;charset=utf-8'


Cookies
-------

Si una respuesta contiene Cookies, puedes acceder a ellas rápidamente::

    url = 'http://example.com/some/cookie/setting/url'
    r = requests.get(url)
    r.cookies['example_cookie_name']

Para enviar tus propias cookies al servidor, puedes utilizar el
parámetro cookies::

   url = 'http://httpbin.org/cookies'
   cookies = dict(cookies_are='working')
   r = requests.get(url, cookies=cookies)
   r.text

Debería devolver::

   '{"cookies": {"cookies_are": "working"}}'

Historial y Redireccionamiento
------------------------------

Requests realizará redireccionamiento para peticiones para todos los
verbos, excepto ``HEAD``.

GitHub redirecciona todas las peticiones ``HTTP`` hacia ``HTTPS``.
Podemos usar el método ``history`` de la respuesta para rastrear las
redirecciones.

La lista ``Response.history`` contiene una lista de objetos tipo
``Request`` que fueron creados con el fín de completar la petición. La
lista está ordenada desde la petición más antigua, hasta las más
reciente.

Si estás utilizando GET u OPTIONS, puedes deshabilitar el
redireccionamiento usando el parámetro allow_redirects::


    r = requests.get('http://github.com')
    print(r.status_code)
    print(r.history)

    200
    [<Response [301]>]


Si estás utilizando HEAD, puedes habilitar el redireccionamento de la
misma manera::

    r = requests.head('http://github.com', allow_redirects=True)
    print(r.status_code, r.url, r.history)
    
    200 https://github.com/ [<Response [301]>]


**Ejercicio**: Arreglar el script para que realize la peticion HEAD pero
con redireccionamiento

Timeouts
--------

Con el parámetro timeout puedes indicarle a Requests que deje de esperar
por una respuesta luego de un número determinado de segundos.

``timeout`` indica el tiempo máximo que se espera por la respuesta. Si
no se produce la respuesta dentro de ese periodo se elevará una
excepcion.

La clase Session
----------------

Los objetos de tipo Session permiten reusar y compartir determinados
valores y *cookies* entre peticiones que se realizan con esa sesión.
Tambien usae internamente las conexiones reutilizables definidas en la
libreria urllib3. Este objeto esta pensado para ser usado cunaod se
realizan muchas conexiones al mismo host, ya que en este caso, el hecho
de reutilizar la conexión puede suponer un incfremento sigbnificativo de
lrendimiento.

Un objeto de tipo ``Session`` tiene todos los metodos definidos como
funciones en requests.

Veamos un ejemplo en el que vemos como las conexiones realizadas al
mismo host comparten las cookies::

    import requests
    
    s = requests.Session()
    primera = s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
    segunda = s.get('https://httpbin.org/cookies')
    print(segunda.cookies)


    <RequestsCookieJar[]>


Soluciones
----------

Versión final del programa de chequeo de web, usando ``head`` y con el
parametro ``allow_redirecs``::


    import requests
    
    urls = [
        'https://www.google.com/',
        'http://github.com/',
        'https://www.parcan.es/',
    ]
    
    for url in urls:
        r = requests.head(url, allow_redirects=True)
        if r.status_code != 200:
            print(f"Error {r.status_code} al acceder a {url}")

