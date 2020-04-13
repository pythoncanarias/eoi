SimpleHTTPServer — Simple HTTP request handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Este módulo define una serie de clases que nos permiten  implementar
nuestros propios servidores web. La clase SimpleHTTPRequestHandler
(Definida en el módulo ``http.server``) es un servidor de ejemplo básico que
sirve los ficheros del directorio donde se ha ejecutado, mapeando la
estrucura de directorios como páginas web.

La mayor parte del trabajo, como analizar las peticiones, por ejemplo,
lo hace la clase de la que deriva, ``BaseHTTPServer``, la clase de
ejemplo solo tienen que sobreescribir los métodos ``do_GET()`` y
``do_HEAD()``.

El siguiente programa usa la clase de ejemplo para arrancar un
servidor web básico, escuchando en la máquina local y en el puerto
8000::

    import SimpleHTTPServer
    import SocketServer

    PORT = 8000

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print("serving at port", PORT)
    httpd.serve_forever()

Pero puede ser aun más fácil, usando la opcion ``-m`` en el 
interprete para que ejecute el módulo como si fuera
el programa principal, y opcionalmente indicando el número de
puerto al que se vincula el servidor.

    $ python3 -m http.server 8000


