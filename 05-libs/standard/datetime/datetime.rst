La librería datetime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El módulo ``datetime`` continua donde lo deja ``time``. Proporciona
clases para trabajar con fechas y tiempos, soportando por
ejemplo aritmética de fechas.

La clase *datetime* sirva para trabajar con fechas y horas. Para trabajar con
estos objetos hay que saber que existen dos tipos distintos de
fechas/horas que podemos obtener a partir de esta clase: fechas absolutas y
fechas ingenuas o _naive_.

Una fecha absoluta dispone de toda la información necesaria para poder
determinar, sin ninguna ambigüedad, su valor. Sabe por tanto en que zona horaría
está y, lo que es más complicado, si está activo o  no el horario de verano.

El horario de verano es un acuerdo político, administrado por cada país, por lo
que no puede sorprender que sea cambiante, difícil de entender y caótico.

La ventaja de una fecha/hora absoluta es que no está sujeta a interpretación.
Con una fecha _naive_, por el contrario, no se puede saber con seguridad
a no ser que dispongamos de algun sistema que nos indique la ubicación
geográfica para completar la información.

Una fecha ingenua está, por lo tanto, incompleta. Le falta información necesaria
para que su valor sea indiscutible, lo que dificulta, por ejemplo, hacer
comparaciones.

Determinar si una fecha _naive_ está referida al Tiempo Coordinado Universal
(UTC), la fecha y hora local o la fecha y hora en alguna otra zona horaria
depende por entero del programa, de la misma forma que es responsabilidad del
programa determinar si un número representa metros, micras o litros.

Las fechas/tiempo locales son fáciles de entender y de usar, pero esa falta de
información nos puede dar problemas.

Los tipos disponibles en este módulo son:

- ``datetime.date``

 Una fecha local, que asume que el Calendario Gregoriano siempre ha estado y
 siempre estará vigente. Tiene los atributos: ``year``, ``month`` y ``day``.

- ``datetime.time``

 Una marca de tiempo ideal, no sujeta a ninguna fecha en particular, y que asume
 que cada día tiene exactamente 24*60*60 segundos. Tiene los atributos:
 ``hour``, ``minute``, ``second``, ``microsecond`` y ``tzinfo``.

- ``class datetime.datetime``

 Combinación de fecha y hora, con los atributos: ``year``,
 ``month``, ``day``, ``hour``, ``minute``,
 ``second``, ``microsecond`` y ``tzinfo``

- ``class datetime.timedelta``

 Representa una duración: La diferencia entre dos objetos de
 tipo ``date`` o ``datetime``.

Estos tipos de datos son todos inmutables.
