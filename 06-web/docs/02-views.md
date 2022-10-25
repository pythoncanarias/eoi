---
title: Vistas de Django
---
## Vistas de Django

Django define una **vista** o **view** como la forma de encapsular la
lógica responsable de procesar una petición de usuario y de devolver un
resultado. Desde un punto de vista de desarrollo, una vista es una
función o una clase de python normal, pero que debe cumplir estos dos
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

### Nuestra primera vista dinámica

La siguiente vista, `fecha_actual`, devuelve un documento HTML muy
simplificado en el que mostramos la fecha y hora actuales, es decir, la
fecha y hora en la que se ejecutó la vista:

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
  de las condiciones que pediamos para que fuera
  una vista.

Recordemos que para poder ver el resultado de la vista, tenemos que
tener una ruta en el fichero `urls.py` apuntando a la misma.

**Ejercicio**: Mapear la ruta 'ahora/' a la vista `fecha_actual`.


### Devolver errores

Podemos devolver errores HTTP desde Django. Existen clases derivadas de
`HttpResponse` para algunos de los códigos de error definidos por el
protocolo HTTP. Si se devuelve una instancia de estas clases en vez de
una respuesta normal, se usará el código de error correspondiente.
