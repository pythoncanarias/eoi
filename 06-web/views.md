Vistas
======

Una vista es una función o una clase de python normal, pero que debe
cumplir los siguientes requisitos:

> -   Admite como parámetro una variable de tipo `HttpRequest`. La
>     función puede aceptar más de un parámetro, en ese caso la variable
>     de tipo `HttpRequest` ha de ser obligatoriamente la primera.
> -   Devuelve una instancia del tipo `HttpResponse`.
