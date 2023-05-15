---
title: Gestión de contenidos estáticos
---

## Los contenidos estáticos

Hemos visto que Django se especializa en generar contenidos dinámicos, es
decir, páginas web cuyo contenido se crean en el momento en que se solicita,
normalmente a base de obtener información de una base de datos u otras fuentes
y componer un resultado combinando dichos datos con plantillas.

Pero en el desarrollo web hay también contenidos que no son estáticos, en el
sentido de que no cambian con frecuencia. Ejemplos de este tipo de datos
son las imágenes, las hojas de estilo, el código _Javascript_, vídeos, etc.

En principio Django **no se encarga de este tipo de contenidos**. Esto es
razonable porque se especializa precisamente en la parte dinámica, así que
delega el servicio de los contenidos estáticos a programas especializados en
eso mismo, servir contenidos estáticos, es decir, servidores web
_tradicionales_ como Apache, Nginx, IIS, LiteSpeed y otros.

Sin embargo, los autores consideraron que sería una complejidad adicional
excesiva, **para desarrollo**, exigir la incorporación de un servidor web para
servir los contenidos estáticos, así que incluyeron en Django un servidor de
contenidos estáticos, que en principio solo se activa si tenemos definido a
nivel global (es decir en el fichero `settings.py`) la variable `DEBUG` a
`True`.

Es importante aclarar que este servidor de estáticos no está pensado para ser
usando nunca en producción, ya que no es nada eficiente y tampoco se ha
realizado un esfuerzo grande en la seguridad, porque como se indicó, solo se
debe usar en la fases de desarrollo.

## Tipos de contenidos estáticos

En Django se divide el tratamiento de los contenidos estáticos en dos partes
diferentes, dependiendo del origen de los ficheros estáticos. Si los ficheros
son originados por nosotros mismos (Por ejemplo, una hoja de estilos CSS o una
imagen a usar como logo en las páginas web) eso se gestiona principlamente con
las variables `STATIC_URL` y `STATIC_ROOT`. Ambas variables tienen significados
diferents, pero relacionados.

El otro tipo de contenidos estáticos es el que no es gestionados por nosotros,
sino por nuestros usuarios. Por ejemplo, si tenemos una red social, nos
interesa que el usuario pueda subir una foto suya para su perfil. Este tipo de
contenidos se gestionan con otras dos variables en la configuración,
`MEDIA_URL` y `MEDIA_ROOT`.

## Contenidos estáticos propios

Vamos a empezar con los contenidos estáticos que generamos nosotros. Por
ejemplo, vamos a ver como definir una hoja de estilos que podemos usar en
nuestras plantillas para ofrecer un estilo unificado. Pero veamos primero
las variables `STATIC_` y su significado.

Ambas variables indican como acceder a los contenidos estáticos, pero la
diferencia es que una de ellas (`STATIC_URL`) indica como acceder a estos
contenidos **en forma de URL**, es decir, accediendo a través del servidor web,
mientras que la otra (`STATIC_ROOT`) indica como acceder a esos contenidos en
el sistema de ficheros local.

Por ejemplo, con la siguiente configuración:

```
STATIC_URL = '/static/'

STATIC_ROOT = '/var/web/static-content/
```

Si yo creo un fichero `logo.png` en la ruta `/var/web/static-content/`, es
decir, que el fichero está en `/var/web/static-content/logo.png`, entonces el
servidor web (el que ejecutamos con el comando `runserver`) nos servirá en
fichero en la URL 'http://localhotst:8000/static/logo.png'); siempre y cuando
en el fichero `settings.py` tengamos la variable `DEBUG` a `True`.

**Ejercicio**: Crea un directorio `static` en la misma carpeta del proyecto.
Modifica el fichero `settings.py` para definir las variables `STATIC_*` de la
siguiente forma:

```
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = '/static/'
```

Copia el fichero logo.png:

![Taskmaster Logo](./img/logo.png)

Al nuevo directorio recién creado, `static`.

Comprueba que, con el valor de `DEBUG` a True, el servidor de desarrollo sirve
la imagen en
[`http://localhost:8000/static/logo.png`](http://localhost:8000/static/logo.png).
Prueba a cambiar el valor de `DEBUG` a ver que pasa.

Vuelve a poner `DEBUG` a `True`. Cambia ahora la variable `STATIC_URL` a
`/ficheros/estaticos/` y comprueba que la URL anterior yo no funciona, pero con
[`http://localhost:8000/ficheros/estaticos/logo.png`](http://localhost:8000/ficheros/estaticos/logo.png) si que debería verse el logo.

## La orden `collecstatic`

Django proporciona un mecanismo para gestionar los contenidos estáticos, y es
precisamente una de las `apps` que nos ha incluido por defecto cuando se creó
el proyecto con `startproject`. Si revisamos las aplicaciones incluidas en la
variable `INSTALLED_APPS`, veremos una con el nombre 'django.contrib.staticfiles'.

Esta `app` nos incluye, entre otros, un comando llamada `collectstatic`,
que podemos ver listado en las opciones disponibles si llamamos a `manage.py`
sin ningún parámetro:

```shell
$ python ./manage.py
...
[staticfiles]
    collectstatic
    findstatic
...
```

¿Qué hace `collectstatic`? Pues recolectar todos los contenidos estáticos que
hayan sido definidos en cada `app` instalados, y asegurarse de que están
copiados tal cual en `STATIC_ROOT` y, por tanto, servidos en la web a partir de
`STATIC_URL`.

¿Cómo sabe que contenidos son estáticos, de entre todos los
archivos que puede haber dentro de cada `app`? Pues usa un sistema parecido
al de las plantillas, todo lo que esté dentro de una carpeta que se llame
`static` se copiará tal cual en `STATIC_ROOT`.

Como esto podría causar problemas de colisiones si varias `apps` usaran el
mismo nombre de recurso, la recomendación de Django es crear una carpeta
`static` y dentro de esta, otra carpeta con el nombre de la `app`, y poner
todos los recursos estáticos en esta última.

Por ejemplo, si tenemos dos `apps` llamadas `alfa` y `beta`, si ambas quisieran
definir un fichero `styles.css`, si ponemos estos contenidos directamente en la
carpeta `static` de cada `app`, tendríamos los estilos de `alfa` en
`alfa/static/styles.css` y los de `beta` en `beta/static/styles.css`. Pero como
la orden `collectstatic` se limita a copiar los ficheros que encuentra **dentro**
de las carpetas `static` al directorio al que apunte `STATIC_ROOT`, acabaríamos
con los dos ficheros `static` en la misma ruta: `{STATIC_ROOT}/styles.css`.

Esto no pasa si seguimos la recomendación de Django. Los ficheros de estilos
estarían en `alfa/static/alfa/styles.css` y `beta/static/beta/styles.css`, con
lo cual acabarán en rutas diferentes: `{STATIC_ROOT}/alfa/styles.css` y
`{STATIC_ROOT}/beta/styles.css` y no habría conflicto.

## La etiqueta `static`

La `app` 'django.contrib.staticfiles' también incluye un `tag` para las
plantillas de Django especial para facilitar la inclusión de recursos
estáticos. Para poder usar esta etiqueta especial hay que cargarla en la
plantilla, poniendo una orden `load` al principio de la plantilla.

```html
{% raw %}
{% load static %}
{% endraw %}
```

Ahora, cuando queramos hacer referencia a un contenido estático, por ejemplo
`tasks/css/styles.css`, que estaría dentro de la carpeta `static` de la `app`
`tasks`, podemos usar el _tag_ `static` para que el sistema añada
automáticamente el prejijo definido en `STATIC_URL`. De esta forma, si en
un futuro se cambiara el prefijo en el fichero `settings.py` no necesitamos
cambiar ninguna de las plantillas.

```html
{% raw %}
<link rel="stylesheet" type="text/css" href="{% static 'tasks/css/styles.css' %}">
{% endraw %}
```

**Ejercicio**: Mueve el fichero `logo.png` a una carpeta `static` dentro de la
_app_ tasks. Vamos a crear a su vez carpetas diferentes para imágenes `img` y
para hojas de estilo `css`, asi que el fichero `logo.png`, al ser una imagen,
debemos guardarlo en `tasks/static/tasks/img/logo.png`. Ya de paso, crear un
fichero de estilos en `tasks/static/tasks/css/styles.css`. Pasar los contenidos
dentro de la página HTML al fichero de estilos y enlazar desde  la plantilla.


