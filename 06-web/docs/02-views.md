---
title: Vistas de Django
---

## Vistas de Django

Django define una **vista** o **view** como la forma de encapsular la
lógica responsable de procesar una petición de usuario y de devolver un
resultado. Desde un punto de vista de desarrollo, una vista es una
función o una clase de Python normal, pero que debe cumplir estos dos
requisitos:

- Tiene que admitir como primer parámetro una variable de tipo
  `HttpRequest`. La función puede aceptar más parámetros, pero la
  variable de tipo `HttpRequest` ha de ser obligatoriamente la
  primera.

- Devuelve una instancia del tipo `HttpResponse`.

La respuesta puede ser de cualquier tipo, aunque normalmente es HTML,
pero también puede ser una redirección, un error 404, una documento
JSON, una imagen, o cualquier otro contenido.

Aunque el código de las vistas puede estar en cualquier parte, la
práctica recomendada es ponerlas en un fichero `views.py`.

## Nuestra primera vista dinámica

La siguiente vista, `fecha_actual`, devuelve un documento HTML muy
simplificado en el que mostramos la fecha y hora actuales, es decir, la
fecha y hora en la que se ejecutó la vista:

```python
import datetime
from django.http import HttpResponse

def fecha_actual(request):
    now = datetime.datetime.now()
    page = f"""<html>
<body>
<h1>Qué hora es</h1>
<p>Las {now}</p>
</body>
</html>"""
    return HttpResponse(page)
```

Vamos a comentar esta vista por partes:

- Primero importamos el módulo `datetime` y la clase `HttpResponse`.

- Definimos ahora la función `fecha_actual`. Esta será nuestra vista.
  Vemos que cumple la primera de las condiciones, ya que el primer
  parámetro de la función efectivamente parece esperar un objeto
  `HttpRequest`, normalmente llamado `request`, como en nuestro
  ejemplo.

- El nombre de la función es completamente arbitrario. No tiene que
  seguir ninguna convención específica para que Django lo reconozca
  como una vista ni nada parecido.

- El cuerpo de la vista obtiene la fecha/hora actual, formatea el
  resultado en un HTML simplificado, y finalmente devuelve un objeto
  `HttpRequest` generado a partir del HTML. Cumple así con la segunda
  de las condiciones que pedíamos para que fuera
  una vista.

Recordemos que para poder ver el resultado de la vista, tenemos que
tener una ruta en el fichero `urls.py` apuntando a la misma.

**Ejercicio**: Mapear la ruta 'ahora/' a la vista `fecha_actual`.

### Devolver errores

Podemos devolver errores HTTP desde Django. Existen clases derivadas de
`HttpResponse` para algunos de los códigos de error definidos por el protocolo
HTTP. Recordemos que todos los códigos de HTTP que no esten en el rango de los
200 son códigos de error. Si se devuelve una instancia de estas clases en vez
de una respuesta normal, se usará el código de error correspondiente.

Un ejemplo de uso:

```py
import os
from django.http import HttpResponse, HttpResponseNotFound


def show_file_content(request, filename):
    if os.path.isfile(filename):
        ...
        return HttpResponse("OK File found")

    return HttpResponseNotFound(f"<h1>File {filename} not found</h1>")
```

Este sistema obliga a definir el contenido de la página que se muestra en
el navegador, como hacemos en la última línea del ejemplo. Eso está
bien porque podemos personalizar el mansaje de error, pero normalmente
también queremos que haya una consistencia en el formato de los mensajes de error. Para resolver esto
Django define una excepción proia, `Http404`. Si elevamos una excepción en
cualquier línea de la vista, Django la tratará y devolverá la página de error
estandar, incluyendo además en la respuesta el código de error 404.

Es decir, que el ejemplo anterior podria haberse escrito así:

```py
import os
from django.http import Http404
from django.http import HttpResponse


def show_file_content(request, filename):
    if os.path.isfile(filename):
        ...
        return HttpResponse("OK File found")

    raise Http404(f"File {filename} not found")
```

Podemos definir esta página estándar de error definiendo una plantilla con el
nombre `404.html`, que este disponible para ser cargado por el sistema de
plantillas. Todavía no hemos visto, pero lo estudiaremos en el siguiente tema.
Por ahora basta con saber que en esta plantilla definimos la estructura y
apariencia general de la página de error. Esta plantilla se servira **solo**
cuando la variable `DEBUG` en los ajustes esté puesta a `False`. Cuando `DEBUG`
esté a `True`, se muestra la plantilla de django para los errores.
