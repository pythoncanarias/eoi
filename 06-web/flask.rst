El framework web ``flask``
---------------------------------------

El *Hola, mundo* en flask::

    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def test():
        return "Hello, world"

Para ejecutar esta aplicacion web debemos hacer::

    $ FLASK_APP=main.py flask run
    * Serving Flask app "main.py"
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    127.0.0.1 - - [06/Mar/2020 14:16:06] "GET / HTTP/1.1" 200 -§
    127.0.0.1 - - [06/Mar/2020 14:16:06] "GET /favicon.ico HTTP/1.1" 404 -

Ahora solo tenemnos que abrir un navegador, como Firefox o Chrome, e ir a la dirección que
se menciona en la salida: ``http://127.0.0.1:5000`` para ver el resultado.

JSON Web Tokens y Flask
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En el desarrollo web es muy común, especialmente en aplicaciones de tipo SPA_ (Single Page
Application) se ha popularizado mucho el uso de un estándar llamado JWT_ (*JSON Web Tokens*)
para el tema de la autorizacion y seguridad de la comunicación entre la SPA y el
servidor remoto. En este apartado vamos a construir una aplicacion Flask usando autorizacion JWT.



(JWT) are very popular nowadays. Modern web-development is aimed at
building Single Page Applications (SPA) using latest JavaScript libraries such as Angular, React or
Vue. Because of that reason, JWT becomes a standard of authorization and communication between SPAs
and web servers. In this article, I want to build a Flask web server with JWT authorization.

.. _SPA: https://es.wikipedia.org/wiki/Single-page_application
