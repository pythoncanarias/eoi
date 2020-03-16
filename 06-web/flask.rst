El framework web ``flask``
---------------------------------------

.. index:: flask


El *Hola, mundo* en flask::

    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def test():
        return "Hello, world"

Para ejecutar esta aplicacion web debemos hacer::

    $ FLASK_APP=main.py flask run

LA salida debería ser similar a esto::

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



.. _SPA: https://es.wikipedia.org/wiki/Single-page_application
.. _JWT: https://es.wikipedia.org/wiki/JSON_Web_Token
