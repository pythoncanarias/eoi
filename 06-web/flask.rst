El framework web ``flask``
-----------------------------------------------------------------------

.. index:: flask



El *Hola, mundo* en Flask
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este podria ser el programa más sencillo posible en flask::

    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def test():
        return "Hello, world"

Para ejecutar esta aplicación web debemos hacer::

    $ FLASK_APP=main.py flask run

LA salida debería ser similar a esta::

    * Serving Flask app "main.py"
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    127.0.0.1 - - [06/Mar/2020 14:16:06] "GET / HTTP/1.1" 200 -§
    127.0.0.1 - - [06/Mar/2020 14:16:06] "GET /favicon.ico HTTP/1.1" 404 -

Ahora solo tenemnos que abrir un navegador, como Firefox o Chrome, e ir a la
dirección que se menciona en la salida: ``http://127.0.0.1:5000`` para ver el
resultado.

Activar el modo Debug
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Que flask nos permite ejecutar la propia aplicación es muy cómodo para el
desarrollo, pero tiene una pega: cada vez que realizamos un cambio en el código,
tenemos que reiniciar manualmente. Un modo de resolver esto consiste en activar
el modo *debug*, que automaticamete relanzará el servidor en cuanto detecte
cambios en el código, y además nos proporcionará un entorno de depuración muy
potente cuando se produzca un error.

Para activar este facilidades al desarrollo (incluyendo el modo debug) solo hay
que exportar la variable de entorno ``FLASK_ENV`` con el valor ``development``
antes de ejecutar el servidor::

    $ export FLASK_ENV=development
    $ export FLASK_APP=app
    $ flask run


Trabajar con cookies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Las cookies pueden tener varias propiedades, que
se describen en la siguiente tabla:

========  ==========  ======================================================
key       V. Omisión  Descripción
========  ==========  ======================================================
value     ""          El valor de la cookie
max_age   - (None)    Número de segundos de vida
expires   - (None)    Fecha de expiración de la cookie
path      - (None)    Limita la cookie a una ruta determinada
domain    - (None)    Especifica un dominio que puede leer la cookie
secure    - (False)   Si es verdadero, la cookie solo se servirá sobre HTTPS
httponly  - (False)   Impide acceder a esta cookie desde javascript
samesite  - (False)   Limita la disponibilidad de la cookie al mismo site
========  ==========  ======================================================

Cuando vayamos a definir una cookie, tenemos que pensar en todas estas
propiedades y si nos convienen o no los valores por defecto.

[TODO] Como definir cookies

Se usa el atributo ``cookies`` del  objeto ``request`` para acceder a las
cookies implicadas en la solicitud. Es un diccionario al cual podemos acceder
por el nombre de cada *cookie*, y cuyo contenido es el valor de la misma. Fijate
que, aunue a la hora de definir las cookies tuvimos en cuento un monton de
propiedades, a la hora de leerlas solo nos interesa el valor; todos los demas
valores solo determinan si la *cookie* llega al servidor o no.


JSON Web Tokens y Flask
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En el desarrollo web, especialmente en aplicaciones de tipo SPA_ (*Single Page
Application*), se ha popularizado mucho el uso de un estándar llamado JWT_ (*JSON Web Tokens*)
para resolver el problema de la autorización y seguridad de la comunicación entre la SPA y el
servidor remoto. En este apartado vamos a construir una aplicacion Flask usando autorización JWT.

Vamos a empezar implementado una api de estado que nos informe simplemente de la version
actual de la api. Esto se puede hacer (sin seguridad) muy fácilmente, solo hay que
usar la propia rutina ``jsonify`` incluida en Flask::


    from flask import Flask
    from flask import jsonify

    app = Flask(__name__)

    @app.route('/api/v1/stats')
    def test():
        return {
            "active": True,
            "version": "v1",
        }

Si salvamos el ejemplo anterior en un fichero llamado ``api.py`` y lo ejecutamos
con::

    FLASK_APP=api.py flask run

Si ahora apuntamos un navegador a la dirección ``http://127.0.0.1:5000/api/v1/status``
deberiamos obtener un resultado como este::

    {"active":true,"version":"v1"}

Autenticación de las peticiones
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

el usuario ingresa sus credenciales con éxito, obtiene como resultado un **JSON
Web Token**, que debe almacenar localmente.Vemos que en este modelo, no es en
principio necesario crear una sesion en el lado servidor y luego enviar una
clave de sesion en una cookie.

Ahora, cada vez que se quiere acceder a una ruta protegida o recurso, el cliente
tiene que enviar el JWT, generalmente en el encabezamiento de ``Authorization``
utilizando el esquema ``Bearer``. El contenido del encabezado HTTP se ve de la
siguiente forma::

    Authorization: Bearer eyJhbGci...<snip>...yu5CSpyHI

Este mecanismo de autenticación se denomina *stateless* o sin estado, ya que la
información relativa al usuario no se guarda en el servidor. Cada vez que se
accede a un recurso protegido, se debe incluir el token, que será verificado en
cada petición.


La variable ``request``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: request (flask)

La variable **request** [1]_ almacena los datos relativos a una solicitud web.
En vez de pasar este objeto a cada función que deba responder a la solicitud,
Flask automáticamente introduce el objeto `request` dentro del entorno de la
función vista, manejadores de error y otras funciones que se ejecuten durante la
petición, de forma que tienen acceso al mismo como si fuera una variable global.

Cuando la aplicación Flask empieza a responder a una petición, en primer lugar
crea un objeto de la clase ``Request``, basándose en los datos que le
proporciona el servidor WSGI. Como cada *worker* (Ya sea un *thread*, un proceso
o una corutina) solo maneja una única petición, los datos de la petición se
pueden considerar globales para él, durante la vida de la petición.

.. index:: before_request (flask)

Antes de crear el objeto *request*, Flask llama a las funciónes definides con
``before_request()``. Si alguna de estas funciones devuelve un valor distinto de
``None``, el resto de funciones (si las hubiera) s descartan y el valor retornado 
se convertira en una respuesta (un objeto de la clase *Response*) y se usará
como resultado final. La vista tampoco será invocada.

.. index:: after_request (flask)

De igual manera, todas las funciones registradas con ``after_request`` recibiran
como parámetro de entrada la respuesta, y devolveran un objeto ``Response``, que
podrá ser el mismo que se acepta como parametro, el mismo pero modificado o
incluso un objeto totalmente nuevo de la clase ``Response``.

Al final del proceso de respuesta, el objeto `Request` es eliminado de memoria.
Pero si el servidor está siendo ejecutado en modo desarrollo (La
variable de entorno ``FLASK_ENV`` está definida como ``development``), el objeto
``Request`` no se destruye y puede ser inspeccionado en el *debugger*
interactivo, y eso puede resultar muy útil.


Blueprints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. index:: blueprint (flask)

Flask usa el concepto de **Blueprints_** para hacer componentes para aplicaciones
y también para incorporar patrones comunes dentro de una aplicación o
compartidos por varias aplicaciones. De esta forma se pueden estructurar
aplicaciones más grandes, y se pueden implementar extensiones que se pueden
registrar en un repositorio central de forma que esten disponibles para todo el
sistema. Un objeto *Blueprint* funciona de una forma similar a un objeto de tipo
aplicación de Flask, pero no es exactamente igual. Es mas bien una forma de
contruiro o ampliar una aplicacion.

Los *Blueprints* pueden ser útiles para los siguentes casos:

- Descomponer una aplicación compleja en un conjunto de *blueprints*. El
  proyecto puede instanciar una aplicación, inicializar varias extensiones y
  registrar una coleccion de *blueprints*.

- Registrar un *blueprint* en una aplicacion baju un prefijo URL o un
  subdominio. Los parámetros del prejofo URL o del subdominio se pasan como
  parametros comuntes (con valores por defecto) en todas las funciones de tipo
  vistas dentro del *blueprint*.

- Registrar un mismo *blueprint* en una aplicación bajo diferentes URL

- Proporcionar plantillas, filtros para plantillas, ficheros estáticos y otras
  utilidades usando *blueprints*. No es obligatorio incluir vistas o modelos en
  un *blueprint*.

- Registrar un *blueprint* para que sirva de código de inicialización de una
  extensión.

Los *blueprints* no se deben considerar como aplicaciones completas, que podemos
*enchufar* directamente en Flask, porque no son realmente una aplicación sino un
conjunto de operaciones que pueden ser registradas en una aplicación, incluso
varias veces. Por qué, en vez de usar *blueprints*, no usamos múltiples
aplicaciones? Se puede hacer, pero cada aplicación tendrá una
configueración diferente y será gestionada en el nivel WSGI, lo que dificulta
la comunicación entre ellas.

Con *blueprints*, por el contrario, se proporciona separación a nivel de Flask,
comparten la configuración, y pueden realizar cambios globales a la
aplicación,si es necesario, al registrarse. La desventaja es que no se puede
desregistrar un *blueprint* una vez que la aplicación ha sido creada; para eso
necesitamos destruir y volver a crear la aplicacion, es decir, reiniciar el
servicio.

El Concepto de los *Blueprints*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El concepto básico es que losa blueprints permiten añadir operaciones que pueden
ser ejecutaras cuando se registran en la aplicacion. Flask asocia vistas con
*blueprints* cuando está sirviendo peticiones y generando URLs de un *endpoint*
a otro.

Mi Primer Blueprint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El siguiente código es un ejemplo muy simplificado de lo que se puede hacer con
un *blueprint*, en este caso se limita a representar una plantilla estática::

    from flask import Blueprint, render_template, abort
    from jinja2 import TemplateNotFound

    simple_page = Blueprint('simple_page', __name__,
                            template_folder='templates')

    @simple_page.route('/', defaults={'page': 'index'})
    @simple_page.route('/<page>')
    def show(page):
        try:
            return render_template('pages/%s.html' % page)
        except TemplateNotFound:
            abort(404)

Cuando liganmos una vista con la ayuda del decorador ``@simple_page.route``, el
*blueprint* recuerda que debe registrar la función con el o los URL indicados,
cuando se registre en un moomento posterior. Además, añadira como prefijo el
*endpoint* de la función con el nombre del *blueprint* que se asigno en el
constructor (En este caso, también ``simple_page``). El nombre del *blueprint*
no modifica la URL, solo el *endpoint*.

Ahora, cómo registramos este blueprint? así::

    from flask import Flask
    from yourapplication.simple_page import simple_page

    app = Flask(__name__)
    app.register_blueprint(simple_page)

si comprobamos las reglas registradas en esta aplicacion, nos encontraremos con
esto::

    >>> app.url_map
    Map([<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
    <Rule '/<page>' (HEAD, OPTIONS, GET) -> simple_page.show>,
    <Rule '/' (HEAD, OPTIONS, GET) -> simple_page.show>])

JWT 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Authorization: Bearer eyJhbGci...<snip>...yu5CSpyHI

Este es un mecanismo de autenticación sin estado - stateless- ya que la sesión
del usuario nunca se guarda en el proveedor de identidad o en el proveedor del
servicio. Los recursos protegidos siempre comprobaran si existe un JWT válido en
cada pedido de acceso. Si el token esta presente y es válido, el proveedor del
servicio otorga accesos a los recursos protegidos. Como los JWTs contienen toda
la información necesaria en sí mismos, se reduce la necesidad de consultar la
base de datos u otras fuentes de información múltiples veces. 

.. [5] Se usan *proxies* para acceder tanto al objeto ``request`` como a
    ``session``.  De forma similar a la variable de aplicación (normalmente `app`)
    que almacena el contexto general a nivel de aplicación, y al que también se
    accede a través de un *proxy*. Para más información, vease el patron Proxie.


.. _Blueprints: https://flask.palletsprojects.com/en/1.1.x/blueprints/
.. _SPA: https://es.wikipedia.org/wiki/Single-page_application
.. _JWT: https://es.wikipedia.org/wiki/JSON_Web_Token
