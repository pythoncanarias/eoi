---
title: 'sys: configuración específica del sistema'
---

Este módulo porporciona acceso a algunas variables usadas o mantenidas
por el propio interprete de Python. Siempre está disponible:

> sys.argv
>
> > la lista de argumentos pasados al script de python. En la posicion o
> > (sys.argv\[0\]) siempre va el nombre del script (depende del S.O.
> > subyacente si incluye el nombre completo, incluyendo la ruta, o no).
>
> > sys.exc\_info()
> >
> > > Esta función devuelve una tupla de tres valores con información
> > > sobre el error que está siendo tratado: Tipo de la excepcion,
> > > valor de la misma y traza de ejecución. Podemos usarla en una
> > > clausula `except` para obtener más información del error. Si se
> > > llama cuando no hay ninguan excepción enmarcha, devuelve una tupla
> > > de tres valores `None`.
>
> sys.path
>
> > Una lista de cadenas de texto que especifican las rutas de búsqueda
> > para los módulos y paquetes de python.
>
> sys.platform
>
> > Un identificador de la version de Python en ejecución

Ejercicio: iHacer un script que imprima por pantalla los datos mas
importantes de la version de python instalada:

> -   Version
> -   Path
> -   Platform
