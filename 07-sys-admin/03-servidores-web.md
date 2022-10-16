# Servidores web
![computer google](https://images.unsplash.com/photo-1501250987900-211872d97eaa?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80)

# Servidores web

- CGI - Common Gateway Interface
- WSGI - Web Server Gateway Interface
    * Gunicorn
- ASGI - Asynchronous Server Gateway Interface
- NGINX - Servidor web/proxy inverso

## Common Gateway Interface - CGI
- Interfaz de los servidores web que permite intercambiar datos entre los servidores y las aplicaciones externas de manera estandarizada. 
- Con el CGI, no es necesario que todo el contenido de la página HTML esté disponible en el servidor, sino que este se genera de forma dinámica cuando el usuario realiza la solicitud correspondiente a través de la propia página.

**Navegando en la web**

Para comprender el concepto de CGI, veamos qué sucede cuando hacemos clic en un enlace para navegar por una página web o URL en particular.

- El navegador se pone en contacto con el servidor web HTTP y solicita la URL, es decir, el nombre del archivo.
- El servidor web analiza la URL y busca el nombre del archivo. Si encuentra ese archivo, lo devuelve al navegador; de lo contrario, envía un mensaje de error que indica que solicitó un archivo incorrecto.
- El navegador web recibe la respuesta del servidor web y muestra el archivo recibido o el mensaje de error.

Sin embargo, es posible configurar el servidor HTTP para que cada vez que se solicite un archivo en un directorio determinado, ese archivo no se devuelva y en su lugar, se ejecute un programa, y que lo que genere ese programa se envíe de vuelta para que lo muestre su navegador. 

Esta función se llama Common Gateway Interface o CGI y los programas se denominan scripts CGI. Estos programas CGI pueden ser un script de Python, un script PERL, un script de Shell, un programa C o C, etc.

![funcionamiento-cgi](https://www.tutorialspoint.com/python/images/cgiarch.gif)

Usos de Common Gateway Interface
- **Cesta de la compra**: cuando un cliente añade algún producto a la cesta de la compra de una tienda en línea, el script CGI procesa esos datos y, luego, los envía al servidor.
- **Comentarios**: el usuario rellena un campo de comentarios. Cuando hace clic en “Enviar”, el texto se transmite al script CGI, que, a su vez, lo reenvía al servidor.
- **Formularios**: también en el caso de los formularios en línea, como a la hora de enviar algún mensaje o inscribirse en una oferta de trabajo, los datos introducidos son procesados primero por Common Gateway Interface antes de transmitirse al servidor.
- **Estadísticas de páginas web**: cuando las páginas web muestran el tráfico que tienen, la tecnología que lo respalda también recurre al CGI en muchos casos.

y más

## Web Server Gateway Interface - WSGI


- Es una especificación que describe cómo un servidor web se comunica con las aplicaciones web y cómo las aplicaciones web se pueden encadenar para procesar una solicitud.

- WSGI es un estándar de Python descrito en detalle en el [PEP 3333](https://www.python.org/dev/peps/pep-3333/).

<small><a href="https://wsgi.readthedocs.io/">https://wsgi.readthedocs.io/</a></small>

```python
# Python's bundled WSGI server
from wsgiref.simple_server import make_server


def application (environ, start_response):

    # Sorting and stringifying the environment key, value pairs
    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]

    response_body = '\n'.join(response_body)

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body.encode()]

# Instantiate the server
httpd = make_server(
    'localhost', # The host name
    8051, # A port number where to wait for the request
    application # The application object name, in this case a function
)

# Wait for a single request, serve it and quit
httpd.handle_request()
```

![gunicorn logo](https://res.cloudinary.com/practicaldev/image/fetch/s--la4AP0DS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://cdn-images-1.medium.com/max/1024/1%2AU3OFfUPCKV7qMmLRRiiYDA.jpeg)

## Gunicorn

- Gunicorn es un servidor HTTP para sistemas Unix que cumple la especificación WSGI. 
- Nos permite servir una aplicación web con múltiples workers para incrementar el rendimiento de nuestra aplicación.
- Es recomendable para entornos de producción, ya que nunca debemos usar los servidores web integrados en Flask o Django, que tienen como objetivo un entorno de desarrollo.

### Ejercicio de Gunicorn!
Ve a [ejercicios/gunicorn.ipynb](ejercicios/gunicorn.ipynb)

## Asynchronous Server Gateway Interface - ASGI

- _"Es el sucesor espiritual de WSGI"_

- Su función es proporcionar una interfaz estándar entre servidores web, marcos y aplicaciones de Python con capacidad asíncrona.

- Donde WSGI proporcionó un estándar para aplicaciones Python síncronas, ASGI proporciona uno para aplicaciones asíncronas y síncronas, con una implementación de compatibilidad con versiones anteriores de WSGI y múltiples servidores y marcos de aplicaciones.

<small><a href="https://asgi.readthedocs.io/">https://asgi.readthedocs.io/</a></small>

## NGINX

NGINX es un servidor web/proxy inverso ligero de alto rendimiento y un proxy para protocolos de correo electrónico.

Es software libre y de código abierto, licenciado bajo la Licencia BSD simplificada; también existe una versión comercial distribuida bajo el nombre de Nginx Plus

Este software fue lanzado oficialmente en octubre del 2004. El creador del software, Igor Sysoev, comenzó su proyecto en el 2002 como un intento de solucionar el problema C10k. C10k es el reto de gestionar diez mil conexiones al mismo tiempo. 

Hoy en día, los servidores web tienen que manejar un número aún mas grande de conexiones. Por esa razón, NGINX ofrece una arquitectura asíncrona y controlada por eventos, característica que hace de NGINX uno de los servidores más confiables para la velocidad y la escalabilidad.

Actualmente Nginx tiene el 20% de la cuota de mercado de servidores web.

Antes de profundizar más en qué es NGINX, repasemos cómo funciona un servidor web. Cuando alguien hace una solicitud para abrir una página web, el navegador se comunica con el servidor de ese sitio web. Luego, el servidor busca los archivos solicitados para la página y se los envía al navegador. Este es sólo el tipo de solicitud más simple.

El ejemplo anterior también se considera como un hilo sencillo. Los servidores web tradicionales crean un solo hilo para cada solicitud, pero NGINX no funciona de esa manera. Como mencionamos antes, NGINX trabaja con una arquitectura asíncrona y controlada por eventos. Esto significa que los hilos similares se administran bajo un proceso de trabajo, y cada proceso de trabajo contiene unidades más pequeñas llamadas conexiones de trabajo. Toda esta unidad es la responsable de manejar los hilos de las solicitudes. Las conexiones de trabajo entregan las solicitudes a un proceso de trabajo, que también lo enviará a su turno al proceso maestro. Finalmente, el proceso maestro proporciona el resultado de esas solicitudes.

Puede parecer simple, pero una conexión de trabajo puede atender hasta 1024 solicitudes similares. Debido a eso, NGINX puede procesar miles de solicitudes sin ninguna dificultad. También es por eso que NGINX se convirtió en una excelente opción para sitios web con mucho tráfico como comercio electrónico, motores de búsqueda y almacenamiento en la nube.

![diagrama funcionamiento NGINX](https://rockcontent.com/es/wp-content/uploads/sites/3/2020/05/nginx1-1024x596.png)

Lo que hace diferente a Nginx es su arquitectura a la hora de manejar procesos, ya que otros servidores web como Apache crean un hilo por cada solicitud.

Es decir, cada vez que un usuario haga una petición al servidor, por ejemplo entrando en la web, se creará un hilo nuevo.
Nginx funciona de una forma más eficiente gracias a la arquitectura asíncrona basada en eventos, en la que en vez de crear un hilo por cada petición, lo gestiona todo bajo el mismo proceso de trabajo donde se gestionan los diferentes hilos.

Este hilo o proceso de nginx contiene varios microprocesos o llamadas de trabajo. Esto se traduce en un mejor rendimiento de Nginx frente Apache sobre todo en consumo de memoria

**¿Cuáles son las características de NGINX?**

NGINX tiene una arquitectura modular extensible, que facilita la extensión de recursos para aquellos que desean cambiar su código fuente.

- El módulo principal es responsable de manejar la conexión
- El balanceo de carga es un recurso extremadamente importante para aquellos que necesitan un sitio web con alta disponibilidad, ya que permite la distribución de solicitudes de servicio entre servidores.  
De esa manera, cuando hay un aumento en las solicitudes al servidor, como un aumento en el tráfico, NGINX puede dirigir el flujo a otros servidores que están en el archivo de configuración.  
Hay tres posibilidades para la distribución de carga en el NGINX. Puede hacerse por igual entre los servidores configurados, distribuirse al servidor que tiene pocas conexiones en este momento o es posible determinar la dirección IP de cada cliente para cada servidor específico.
- El proxy inverso, por otro lado, es un servidor web que recibe solicitudes de conexión y administra lo que se requerirá en el servidor principal o verifica si la solicitud ya está disponible en caché. NGINX, por lo tanto, ofrece esta característica, que se puede configurar fácilmente en su archivo de configuración.

Cómo instalarlo:

https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04-es

http://nginx.org/en/docs/windows.html

# Siguientes pasos en Administración de Sistemas
![camino](https://images.unsplash.com/photo-1439396874305-9a6ba25de6c6?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80)

- Configuration Management & IaC
    * Fabric y Ansible
- Contenedores & Orquestación
    * Docker & Kubernetes
- Miniproyecto!
