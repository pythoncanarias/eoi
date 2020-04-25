El módulo traceback
------------------------------------------------------------------------

Este módulo nos permite extraer, formatear e imprimir la traza de ejecución.

La traza de ejecución es el "camino", por así decirlo, que ha seguido el
programa hasta llegar a un determinado punto. Esta traza es la misma que se
muestra cuando se eleva una excepción y nadie la captura.

iEl módulo `traceback` es muy util cuando se quieren mostrar estas trazas y
mensajes de error de forma controlada, por ejempo es lo que hace iPython para
mostrar mensajes de error con coloreado de sintaxis e información adicional.

Contenidos de este módulo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El módulo trabaja con objetos de tipo ``traceback``, que son los
objetos que podemos encontrar en ``sys.last_traceback``, o devueltos
en tercer lugar en la tupla que retorna la función ``sys.exc_info()``.

Algunos métodos utiles en este módulo son:

- ``traceback.print_exc([limit[, file]])``

  Esta llamada obtiene la traza actual y la imprime
  en pantalla (o en un fichero, si se especifica),
  usando el mismo formato que usaría
  por defecto Python si la excepción no se captura.

- ``traceback.format_exc([limit])``

  Es como ``print_exc()``, pero devuelve una cadena
  de texto en vez de imprimirla.
