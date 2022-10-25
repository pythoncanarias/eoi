---
title: datetime - Gestión de fechas, horas y timestamps
---
## Introducción a `datetime`

El módulo `datetime` continua donde lo deja `time`. Proporciona clases para
trabajar con fechas y tiempos, soportando por ejemplo aritmética de fechas.

La clase `datetime` sirva para trabajar con fechas y horas. Para trabajar con
estos objetos hay que saber que existen dos tipos distintos de fechas/horas que
podemos obtener a partir de esta clase: **fechas absolutas** y **fechas ingenuas o
naive**.

Una fecha absoluta dispone de toda la información necesaria para poder
determinar, sin ninguna ambigüedad, su valor. Sabe por tanto en que zona
horaría está y, lo que es más complicado, si está activo o no el horario de
verano.

El horario de verano es un acuerdo político, administrado por cada país, por lo
que no es ninguna sorpresa que sea cambiante, difícil de entender y caótico.

La ventaja de una fecha/hora absoluta es que no está sujeta a interpretación.
Con una fecha *naive*, por el contrario, no se puede saber con seguridad a no
ser que dispongamos de algún sistema que nos indique la ubicación geográfica
para completar la información.

Una fecha ingenua está, por lo tanto, incompleta. Le falta información
necesaria para que su valor sea indiscutible, lo que dificulta, por ejemplo,
hacer comparaciones.

Determinar si una fecha *naive* está referida al Tiempo Coordinado Universal
(UTC), la fecha y hora local o la fecha y hora en alguna otra zona horaria
depende por entero del programa, de la misma forma que es responsabilidad del
programa determinar si un número representa metros, micras o litros.

Las fechas/tiempo locales son fáciles de entender y de usar, pero esa falta de
información nos puede dar problemas.

Los tipos disponibles en este módulo son los siguientes:

- La clase `datetime.date` es una clase usada para representar fechas locales,
  que asume que el Calendario Gregoriano siempre ha estado y siempre estará
  vigente. Tiene los atributos: `year`, `month` y `day`.

- La clase `datetime.time` representa una marca de tiempo ideal, no sujeta a
  ninguna fecha en particular, y que asume que cada día tiene exactamente $24
  \times 60 \times 60$ segundos.  Tiene los atributos: `hour`, `minute`,
  `second`, `microsecond` y `tzinfo`.

- La clase `class datetime.datetime` es una combinación de fecha y hora, con
  los atributos: `year`, `month`, `day`, `hour`, `minute`, `second`,
  `microsecond` y `tzinfo`

- La clase `class datetime.timedelta` representa una duración: La diferencia
  entre dos objetos de tipo `date` o `datetime`.

Estos tipos de datos son todos inmutables y se les puede calcular un *hash*,
por lo que se pueden usar como claves en un diccionario.

### Objetos `timedelta`

Un objeto de tipo `timedelta` se utiliza para representar una duración,
o si lo preferimos, la diferencia entre dos fechas o momentos. Podemos
crearlo llamando la constructor de `datetime.timedelta`:

```python
class datetime.timedelta(
    days=0,
    seconds=0,
    microseconds=0,
    milliseconds=0,
    minutes=0,
    hours=0,
    weeks=0,
)
```

**Nota**: Este es uno de los módulos más antiguos de la librería estándar y no
respeta las convenciones PEP8, de ahí que clases como `timedelta`, por ejemplo,
estén en minúsculas en vez de en *CamelCase* (por ejemplo, `TimeDelta`) que
sería lo suyo.

Todos los argumentos del constructor son opcionales y tienen como valor por
defecto 0. Podemos usar para cada uno de estos parámetros valores positivos o
negativos, y valores enteros o decimales. Por ejemplo,para crear una diferencia
horaria de media hora, podríamos hacer:

```python
media_hora = datetime.timedelta(hours=0.5)
```

**Ejercicio**: Crear un `timedelta` para una diferencia de nueve horas y
media. Crear ahora un `timedelta` de media hora y otro de 30 minutos. ¿Son iguales?

El objeto `timedelta` normaliza todos los parámetros de entrada para almacenar
solo días, segundos y milisegundos. Una vez creado un `timedelta`, podemos
acceder a estos atributos `days`, `seconds` y `microseconds` que lo definen.

![Nueve semanas y media](nueve-semanas-y-media.png)

El siguiente ejemplo muestra cuantos días y segundos hay en [nueve
semanas y media](https://www.imdb.com/title/tt0091635/):

```python
import datetime
d = datetime.timedelta(weeks=9.5) 
print(
    "Nueve semanas y media son",
    f"{d.days} días y {d.seconds} segundos",
)
```

Los objetos `timedelta` se pueden operar. Por ejemplo, para obtener un periodo
de 24 horas puede hacerse de diferentes formas:

```python
datetime.timedelta(days=1)
datetime.timedelta(hours=24)
datetime.timedelta(hours=1) * 24
```

**Pregunta** ¿Son todos los periodos calculados en el ejemplo anterior
iguales? Razona la respuesta.

Veremos mas adelante que si restamos objetos de tipo fecha (`date`) o
*timestamp* (`datetime`) obtendremos objetos de tipo `timedelta`.

### Objetos tipo `date`

Los objetos tipo `date` representan una fecha (año, mes y día), en un formato
simplificado que asume que nuestro calendario actual, el [Calendario
Gregoriano](https://es.wikipedia.org/wiki/Calendario_gregoriano) ha estado
vigente desde siempre (Lo cual es mentira, pero nos sirve para cálculos
contemporaneos).

Podemos crear un `date` usando la clase:

```python
class datetime.date(year, month, day)
```

Todos los parámetros son obligatorios. Deben ser enteros positivos y, para
cada uno de ellos, cumplir los siguientes requisitos:

- El año (`year`) debe estar comprendido entre `MINYEAR` y `MAXYEAR`

- El mes (`month`) debe estar comprendido entre 1 y 12

- El día (`day`) debe estar comprendido entre 1 y el número de días del mes que
  se haya especificado.

Si alguno de estos valores no cumple estas condiciones, se elevara una
excepción de tipo `ValueError`.

Tambien se pueden obtener objetos de tipo `date` a partir de ciertos
métodos de clase:

- `datetime.date.today()` devuelve la fecha actual

- `date.fromtimestamp(timestamp)` devuelve una fecha a partir del tiempo unix,
  como por ejemplo el vlor devuelto por `time.time()`.

- `date.fromordinal(ordinal)` devuelve la fecha a partir del número de días a
  partir del 1 de enero del año 1. Dicho con otras palabras, el 1 de enero del
  año 1 es el día 1, el 2 de enero del año 1 es el número 2, etc.

Hay más funciones de este tipo en la documentación oficial.

Lo interesante de las fechas es que podemos operar con ellas como si fueran
numeros. La suma de una fecha y un `timedelta` nos dará una nueva fecha.

**Ejercicio**: Calcular la fecha dentro de 91 días.

La diferencia entre dos fechas nos dará un `timedelta`.

**Ejercicio**: Calcular el número de dias trascorridos desde que la OMS
reconocio como Pandemia la enfermedad conocida como COVID-19.

![11 de marzo de 2020](pandemia.png)

Las fechas se pueden comparar con los operadores `==`, `!=`, `<`, `<=`,
`>` y `>=`.

Otro método interesante es `replace`. Como se comentó antes, las objetos
que define `datetime` son todos inmutables. Esto significa que no podemos
modificar, por ejemplo, una fecha una vez creada. Pero si podemos crear
nuevas fechas a partir de una dada, por ejemplo. El metodo `replace` nos
permite hacer esto mismo:

```python
date.replace(year=self.year, month=self.month, day=self.day)¶
```

La respuesta del método es una nueva instancia, con los atributos cambiados
segun se hayan especificado o no en los parámetros.

**Ejercicio**: Escribir una función `ayer()` que nos devuelva la fecha
de ayer. Puedes usar un `timedelta` para restar un día a la fecha actual.
Escribe otra funcion `primero_de_mes`, que devuelva siempre la fecha del
primer del mes actual. Por ejemplo, el 7 de mayo de 2021 la función debe
retornar un objeto `date` para el 1 de mayo de 2021.
