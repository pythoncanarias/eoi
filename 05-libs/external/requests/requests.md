Requests es una librería para HTTP, ref:licenciada bajo Apache2 <apache2>, escrita en Python, para seres humanos.

Filosofía
Requests fue desarrollado al estilo PEP 20.

Hermoso es mejor que feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
La legibilidad cuenta.

Ejemplo con requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())

En python 2, un codigo equivalente a esto era bastante mas largo e incomodo
de leer. Es verdad que ahora, con el cambio llevado a las librerias en
Python3, la diferencia ya no es tanta. Aun asi, `requests` llega más lejos
en terminis de comodidad y facilidad de uso.

Si tu programa hace uso extensivo de llamadas a servidores http, seguramente
`requests` te aprotara un codigo mas sencillo y te conviene usarlo, si solo
estas haciendo una unica llamada, igual requests seria demasiado, ya que solo
te ahorrarias un par de lineas, que igual no compensa añadir otra dependencia
a tu codigo.

### Instalar request

pip install request

### Realizar un petición GET

Realizar una petición en Requests muy sencillo.

Comienza importando el módulo de Requests:

>>> import requests

Ahora, intentemos obtener un página web. Para este ejemplo, vamos a obtener el
timeline público de GitHub.:

>>> r = requests.get('https://api.github.com/event')

Ahora, tenemos un objeto Response llamado `r`. Podemos obtener toda la
información que necesitamos a partir de este objeto.

**Ejercicio**: En la propiedad `status_code` podemos acceder al codigo
de respuesta del servidor. Este es el famoso 404 que obtenemos a veces
en el navegador, si intentamos acceder a una pagina que no existe, por ejemplo.

El codigo para "todo ha ido bien" en 200.

Haz un pequenno script para comprobar una serie de paginas web. Has una peticion
de tipo GET para cada direccion y conprueba que el `status_code` de la respuesta
en 200. Imprime un codigo de error en caso contrario.

Puedes usar estas direcciones, o modificarlas a tu gusto

https://www.google.com/
https://github.com/
https://www.parcan.es/

    urls = [
        'https://www.google.com/',
        'https://github.com/',
        'https://www.parcan.es/',
    ]

GET es el tipo de peticion mas frecuente, pero puedes acceder a todos los
verbos HTTP:

r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")


**Ejercicio**: Cambia el codigo del codigo anterior para que use
`head` en vez de `get`. Va mas rapida? por que? Devuelven todas
las paginas el codigo 200?

### Pasar parámetros en URLs

Con frecuencia, debes enviar algún tipo de información en el query string de la
URL. Si estuvieses creando la URL a mano, esta información estaría en forma de
pares llave/valor luego del signo de interrogación en la URL, por ejemplo
httpbin.org/get?key=val. Requests te permite proveer estos argumentos en forma
de diccionario, usando el parámetro en llave (keyword argument) params. Como
ejemplo, si quisieras pasar key1=value1 y key2=value2 a httpbin.org/get, usarías
algo como esto:

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)

Puedes ver que la URL ha sido codificada correctamente imprimiéndola:

print r.url


Nota: cualquier llave del diccionario cuyo valor es `None` no será agregada 
al *query string* del URL.

### Contenido de respuesta

Podemos leer el contenido de la respuesta del servidor. Usemos el listado de
eventos de
GitHub nuevamente:

>>> import requests
>>> r = requests.get('https://api.github.com/events§')
>>> r.text

'[{"repository":{"open_issues":0,"url":"https://github.com/...

Requests automáticamente decodificará el contenido que viene del servidor. La
mayoría de caracteres unicode serán decodificados correctamente.

Cuando ejecutas una petición, Requests tratará de obtener la codificación de la
respuesta basándose en las cabeceras HTTP. La codificación del texto que
Requests encontró (o supuso), será utilizada cuando se acceda a `r.text`. Puedes
conocer la codificación que `Requests` está utilizando, y cambiarla, usando la
propiedad r.encoding:

>>> r.encoding
'utf-8'
>>> r.encoding = 'ISO-8859-1'


### Contenido de respuesta JSON

Hay un decodificador de JSON incorporado en Requests:

>>> import requests
>>> r = requests.get('https://api.github.com/events')
>>> r.json()


Si la decodificación falla, r.json elevará una excepción. Por ejemplo, si la respuesta obtiene un código 401 (No Autorizado/ Unauthorized), intentar `r.json` producirá un error `ValueError: No JSON object could be decoded`.

#Cabeceras personalizadas

Si quieres agregar cabeceras HTTP a una petición, simplemente pasa un dict al
parámetro headers.

Por ejemplo, en el ejemplo anterior no especificamos la cabecera content-type:

    import json
    url = '...'
    payload = {'some': 'data'}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

### Peticiones POST más complicadas

Típicamente, quieres enviar información en forma de formulario, como un
formulario HTML. Para hacerlo, pasa un diccionario al parámetro `data`. Este
diccionario será codificado automáticamente como formulario al momento de
realizar la petición:

>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.post("http://httpbin.org/post", data=payload)
>>> print r.text
{
  ...
  "form": {
    "key2": "value2",
    "key1": "value1"
  },
  ...
}

### Cabeceras de respuesta

Podemos ver las cabeceras de respuesta del servidor utilizando un diccionario:

>>> r.headers
{
    'status': '200 OK',
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json; charset=utf-8'
}

Este diccionario es especial: está hecho únicamente para las cabeceras HTTP. De
acuerdo con el RFC 7230 , los nombres de las cabeceras HTTP no hacen distinción
entre mayúsculas y minúsculas.

Así que podemos acceder a las cabeceras utilizando letras mayúsculas o minúsculas:

>>> r.headers['Content-Type']
'application/json; charset=utf-8'

>>> r.headers.get('content-type')


### Cookies

Si una respuesta contiene Cookies, puedes acceder a ellas rápidamente:

>>> url = 'http://example.com/some/cookie/setting/url'
>>> r = requests.get(url)

>>> r.cookies['example_cookie_name']
'example_cookie_value'

Para enviar tus propias cookies al servidor, puedes utilizar el parámetro cookies:

>>> url = 'http://httpbin.org/cookies'
>>> cookies = dict(cookies_are='working')

>>> r = requests.get(url, cookies=cookies)
>>> r.text
'{"cookies": {"cookies_are": "working"}}'

### Historial y Redireccionamiento

Requests realizará redireccionamiento para peticiones para todos los verbos,
excepto `HEAD`.

GitHub redirecciona todas las peticiones `HTTP` hacia `HTTPS`. Podemos usar el
método `history` de  la respuesta para rastrear las redirecciones. 

La lista `Response.history` contiene una lista de objetos tipo `Request` que fueron
creados con el fín de completar la petición. La lista está ordenada desde la
petición más antigua, hasta las más reciente.

Si estás utilizando GET u OPTIONS, puedes deshabilitar el redireccionamiento usando el parámetro allow_redirects:

>>> r = requests.get('http://github.com', allow_redirects=False)
>>> r.status_code
>>> assert r.history == []


Si estás utilizando HEAD, puedes habilitar el redireccionamento de la misma manera:

>>> r = requests.head('http://github.com', allow_redirects=True)
>>> r.url
>>> assert len(r.history) > 0

**Ejercicio**: Arreglar el script para que realize la peticion HEAD pero con
redireccionamiento

Timeouts

Con el parámetro timeout puedes indicarle a Requests que deje de esperar por una
respuesta luego de un número determinado de segundos:

>>> requests.get('http://github.com', timeout=0.001)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)

`timeout` indica el tiempo máximo que se espera por la respuesta. Si no se produce 
la respuesta dentro de ese periodo se elevará una excepcion.

