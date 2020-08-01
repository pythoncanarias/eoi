========================================================================
Vistas de Django
========================================================================

Django define una vista es una función o una clase de python normal,
pero que debe cumplir estos dos requisitos:

-  tiene que admite como primer parámetro una variable de tipo
   ``HttpRequest``. La función puede aceptar más de un parámetro, pero
   la variable de tipo ``HttpRequest`` ha de ser obligatoriamente la
   primera.

-  Devuelve una instancia del tipo ``HttpResponse``.

