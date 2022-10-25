Instalar Leaflet

    pip install django-leaflet

Añadir esta dependencia a nuestro fichero `requirements.txt` (o `Pipenv` si
usamos pipenv)

    echo "django-leaflet >> requirements.txt

Añadimos la app a la lista de apps instaladas. Editamos `settings.py`
y la incliomos en la lista `INSTALLED_APPS`

Migramos para que se crean las tablas que necesite la app

    python manage.py migrate


Añadimos el javascript y las hojas de estilo en las paginas en las
que vayamos a usar los mapas. PAra simplificar, los pondremos en la
pagina `base.html`


    {% load leaflet_tags %}
    ...
    <head>
        ...
        {% leaflet_js %}
        {% leaflet_css %}
    </head>

Añadir en la pagina el mapa, indicando un nombre

Add the map in your page, providing a name:

    ...
    <body>
        ...
        {% leaflet_map "yourmap" %}
        ...
    </body>

    
