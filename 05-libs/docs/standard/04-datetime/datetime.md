---
title: datetime - Gestión de fechas, horas y marcas temporales
---

## Introducción a `datetime`

El módulo `datetime` continua donde lo deja `time`. Proporciona clases para
trabajar con fechas y tiempos, soportando por ejemplo aritmética de fechas.

La clase `datetime` sirva para trabajar con fechas y horas. Para trabajar con
estos objetos hay que saber que existen dos tipos distintos de fechas/horas que
podemos obtener a partir de esta clase: **fechas absolutas** o **aware** y **fechas
ingenuas o naive**.

Una fecha absoluta dispone de toda la información necesaria para poder
determinar, sin ninguna ambigüedad, su valor. Sabe por tanto en que zona
horaria está y, lo que es más complicado, si está activo o no el horario de
verano.

El horario de verano es un acuerdo político, administrado por cada país, por lo
que es inconstante, difícil de entender y caótico.

La ventaja de una fecha/hora absoluta es que no está sujeta a interpretación.
Con una fecha _naive_, por el contrario, no se puede saber con seguridad a no
ser que dispongamos de algún sistema que nos indique también la ubicación geográfica
para completar la información.

Una fecha ingenua está, por lo tanto, incompleta. Le falta información
necesaria para que su valor sea indiscutible, lo que dificulta, por ejemplo,
hacer comparaciones.

Determinar si una fecha _naive_ está referida al Tiempo Coordinado Universal
(UTC), la fecha y hora local o la fecha y hora en alguna otra zona horaria
depende por entero del programa, de la misma forma que es responsabilidad del
programa determinar si un número representa metros, micras o litros.

Las fechas/tiempo locales son fáciles de entender y de usar, pero esa falta de
información nos puede dar problemas.

## Tipos de datos

!!! warning "datetime es uno de los módulos más antiguos de la librería estándar"

    De ahí que no respete las convenciones PEP8, y clases como `date` estén en
    minúsculas en vez de en *CamelCase* (es decir, `Date`) que sería lo suyo.

Los tipos disponibles en este módulo son los siguientes:

- **date**: La clase `datetime.date` es una clase usada para representar fechas
  locales, que asume que el Calendario Gregoriano siempre ha estado y siempre
  estará vigente (_Spoiler_: No es verdad). Tiene los atributos: `year`,
  `month` y `day`.

- **time**: La clase `datetime.time` representa una marca de tiempo ideal, no
  sujeta a ninguna fecha en particular, y que asume que cada día tiene
  exactamente $24 \times 60 \times 60$ segundos (_Spoiler_: No es verdad).
  Tiene los atributos: `hour`, `minute`, `second`, `microsecond` y `tzinfo`.

- **datetime**: La clase `datetime.datetime` es una combinación de fecha y
  hora, con los atributos: `year`, `month`, `day`, `hour`, `minute`, `second`,
  `microsecond` y `tzinfo`

- **timedelta**: La clase `datetime.timedelta` representa una duración: La
  diferencia entre dos objetos de tipo `date` o `datetime`.

Estos tipos de datos son todos inmutables y se les puede calcular un *hash*,
por lo que se pueden usar como claves en un diccionario.


## Los objetos de tipo `time`

Los objetos de tipo `time` sirven para representar un momento del día (con
precisión de hasta microsegundos, si nos hace falta), de forma independiente
del día.

Podemos crearlos usando directamente la clase:

```
import datetime

t1 = datetime.time(hour=8, minute=30)  
t2 = datetime.time(12, 30, 0)  # Podemos pasar los valores por orden
t3 = datetime.time(12)         # los valores no pasados se ponen a 0
```

Los parámetros son `hour`, `minute`, `second` y `microsecond`, pero no es
necesario especificarlos todos, porque tienen un valor por defecto de $0$.
También podemos especificar la zona horaria con `tzinfo`, pero dejaremos eso
para cuando veamos los objetos de tipo `datetime.datetime`.

Una vez creado el objeto, podemos acceder a esas propiedades de forma
independiente:

```
import datetime

t = datetime.time(hour=8, minute=30)  
print('Hora:', t.hour)
print('Minutos:', t.minute)
print('Segundos:', t.second)
```

Los objetos de tipo `time` se puede comparar entre ellos, si son del mismo tipo
, es decir, si ambos son _naive_ o si ambos tienen definida una zona horaria
(aunque no sea la misma zona horaria). Si intentamos comparar tiempos _naive_
con _aware_, se elevará una excepción de tipo `ValueError`.

!!! warning 'Desde la versión 3.3, se puede comparar la igualdad'

    Desde la version 3.3, se puede comparar una fecha _naive_ con una
    no _naive_ sin que se produzca error, siempre y cuando la comparación
    sea exclusivamente la igualdad. El cualquier caso, la camparación
    develvera siempre `False`.

Otras formas de crear objetos de tipo `time`:
\
- `fromisoformat` crea una instancia de `time` a partir de una cadena de texto,
  en el formato estándar para fechas/hora. Por ejemplo
  `time.fromisoformat('04:23:01')` o `time.fromisoformat('04:23:01.000384')` o
  incluso `time.fromisoformat('04:23:01+04:00')`, que nos crea una objeto de
  tipo `time` _aware_, porque le hemos indicado la diferencia con UTC, 4 horas.
  Igualmente, tiene el método inverso `isoformat` que hace lo contrario, crea
  una cadena de texto en formato estándar a partir de una instancia de `time`.

- El método `replace` (que veremos que también tienen las clases `date` y
  `datetime`) funciona devolviendo una nueva instancia de `time`, con alguno
  de los valores reemplazados por los valores que pasamos como parámetros. Este
  método es muy útil porque, como se comentó al principio, todas
  las instancias de las clases `time`, `date`, `datetime` y `timedelta` son
  **inmutables**.

```python
import datetime

t1 = datetime.time(12, 0, 0)  # t1 vale 12:00:00, el mediodía
t2 = t1.replace(hour=18)      # t2 son las 6 de la tarde
```


## Variable de tipo fecha (`date`)

Los objetos tipo `date` representan una fecha (año, mes y día), en un formato
simplificado que asume que nuestro calendario actual, el [Calendario
Gregoriano](https://es.wikipedia.org/wiki/Calendario_gregoriano) ha estado
vigente desde siempre (Lo cual es mentira, pero nos sirve para cálculos
contemporáneos).

La forma más sencilla de crear una fecha es usando directamente 
la clase `datetime.date`:

```python
import datetime
fecha = datetime.date(2022, 10, 26)
```

Todos los parámetros son obligatorios. Deben ser enteros positivos y, para
cada uno de ellos, cumplir los siguientes requisitos:

- El año (`year`) debe estar comprendido entre `MINYEAR` y `MAXYEAR`

- El mes (`month`) debe estar comprendido entre 1 y 12

- El día (`day`) debe estar comprendido entre 1 y el número de días del mes que
  se haya especificado.

Si alguno de estos valores no cumple estas condiciones, se elevará una
excepción de tipo `ValueError`.

Una vez creada la fecha, podemos acceder a cada uno de estos valores 
de forma independiente:

```python
import datetime

d = datetime.date(2022, 10, 26)
print('Año:', d.year)
print('Mes:', d.month)
print('Dia:', d.day)
```

Pero instanciar directamente desde la clase no es la única manera de crear
objetos de tipo fecha o `date`. También se pueden obtener a partir de ciertos
métodos:

- `datetime.date.today()` devuelve la fecha actual

- `date.fromtimestamp(timestamp)` devuelve una fecha a
  partir del tiempo Unix, como por ejemplo el valor devuelto por `time.time()`.

- `fromisoformat(str)` crea una fecha a partir de una cadena de texto en
  formato ISO 8601, es decir `YYYY-MM-DD`, por ejemplo
  `datetime.date.fromisoformat('2022-10-26')`.

- `date.fromordinal(ordinal)` crea una fecha a partir del número de días desde
  el principio del año. Dicho con otras palabras, 1 nos devolverá la fecha del
  1 de enero, 2 nos devolverá el 2 de enero, 32 nos devolverá el 1 de febrero,
  etc.

- Otro método interesante para crear fechas es `replace`. Como se comentó
  antes, las objetos `date` son inmutables. Esto significa que no podemos
  modificarlos una vez creados. Pero si podemos crear nuevas fechas a partir de
  una existente, y el método `replace` nos permite hacer esto mismo.
  Podemos cambiar el día, mes y/o año usando los parámetros `day`, `month` y
  `year`.

  La respuesta del método es una nueva variable `date`, con los atributos
  cambiados según se hayan especificado, o no, en los parámetros (Si no
  especificamos el parámetro o le pasamos 0, el valor de la fecha original se
  mantiene).


**Ejercicio**: convierte el siguiente ejemplo:

```python
hoy = datetime.date.today()
primero_de_mes = hoy.replace(day=1)¶
```
en una función `obtener_primero_de_mes`, que devuelva siempre la fecha del
primer del mes actual. Por ejemplo, si llamamos a la función el 7 de mayo de
2021 la función debe retornar un objeto `date` para el 1 de mayo de 2021.

```
import datetime

def obtener_primero_de_mes():
    ...  # Tu código va aqui
```

Las fechas, independientemente de como se hayan creado, se pueden comparar,
igual que los números, con los operadores `==`, `!=`, `<`, `<=`, `>` y `>=`.


[ ] **Ejercicio** Escribir un programa que nos diga si hoy es nuestro cumpleaños.
Necesitas obtener la fecha de hoy (`datetime.date.today()`), crear una fecha
con el día y mes de tu cumpleaños pero el año actual (puedes usar el método
`replace`) y luego compararlas. Si son iguales, es tu cumpleaños.

**Extra Bonus**: En caso de que no sean iguales, imprimir un mensaje indicando si
la fecha todavía no ha llegado o si ya se pasó.

Otros métodos interesantes de los objetos tipo fecha son los siguientes:

- `toordinal()` es la contraria de `fromordinal`, nos devuelve el numero de
  días contados desde el 1 de enero con respecto a esa fecha.

- `weekday()` nos devuelve un código numérico para indicar el día de la semana,
  desde $0$ a $6$, donde $0$ representa el lunes y $6$ el domingo. La función
  `isoweekday()` es similar, pero usa otra codificación, en el rango $1$ a $7$,
  donde $1$ es el lunes y $7$ el domingo.

- `isoformat()` devuelve una cadena de texto representado la fecha en formato
  ISO 8601, es decir `YYYY-MM-DD`. El la inversa de la ya vista
  `fromisoformat(str)`. `datetime.date(2022, 10, 2) == '2022-10-02'`

Hay más funciones de este tipo en la documentación oficial.

Una cosa interesante de las fechas es que podemos operar con ellas, como si
fueran números. Veremos más adelante que la resta de dos fechas nos dará un
objeto de tipo `timedelta`, y que la suma de una fecha y un `timedelta` nos
dará una nueva fecha.


## Objetos de tipo marca temporal o `datetime`

Los objetos de tipo `datetime.datetime` son una combinación de fecha (`date`) y
tiempo (`time`), de forma que son los más adecuados para representar un momento
determinado en una fecha determinada. Asume las mismas simplificaciones que
estas dos clases, es decir, asume que siempre ha estado vigente el calendario
Gregoriano (_Spoiler_: No es verdad) y que un día se compone exactamente de 24
horas de 60 minutos, cada uno compuesto de 60 segundos (_Spoiler_: no es
verdad).

Podemos crearlos directamente usando la clase:

```
import datetime

dt = datetime(2022, 10, 26, 12, 0, 0)
```

Aceptando todos los parámetros de fechas y tiempos: `year`, `month`, `day`,
`hour`, `minute`, `second`, `microsecond` y `tzinfo`. Por defecto todos los
valores son $0$, y si no se especifica la zona horaria, creara una marca
temporal `naive`.

O, al igual que con `date` y `time`, existen otras formas de construir marcas
temporales. Por ejemplo `datetime.datetime.now(tz_info=None)` nos devuelve el
momento actual (_naive_ o _aware_ dependiendo de si le hemos pasado o no
información de la zona horaria).

Desde la versión 3 es mucho más fácil trabajar con marcas temporales, porque se
ha incorporado un nuevo modulo llamado `zoneinfo`. Con él podemos trabajar con
las zonas temporales usando nombres claves, fáciles de usar.  Por ejemplo, si
queremos crear una marca temporal, sita en España pero en terreno peninsular,
podemos hacer:

```
import datetime
import zoneinfo

tz_info = zoneinfo.ZoneInfo('Europe/Madrid')
ahora = datetime.datetime.now(tz_info)
print(ahora)
```

Pero si queremos crear una marca temporal sita en las islas canarias, haríamos:

```
import datetime
import zoneinfo

tz_info = zoneinfo.ZoneInfo('Atlantic/Canary')
ahora = datetime.datetime.now(tz_info)
print(ahora)
```

También podemos crear una marca temporal a partir de una cadena de texto en
formato ISO, con `fromisoformat`, aunque para _parsear_ cadenas de texto
existen otras librerías de terceros como `dateutil`, `arrow` y otras, más
potentes.

```
import datetime

naive_date = datetime.datetime.fromisoformat('2011-11-04 00:05:23.283')
aware_date = datetime.datetime.fromisoformat('2011-11-04 00:05:23.283+02:00')
print(naive_date, aware_date)
```

**Ejercicio**: Comprobar que si creamos dos marcas temporales con exactamente
el mismo valores, pero diferentes zonas horarias, nos devuelve dos valores
`datetime` que **no** son iguales.

```
import datetime
import zoneinfo

tz_peninsula = zoneinfo.ZoneInfo('Europe/Madrid')
tz_canarias = zoneinfo.ZoneInfo('Atlantic/Canary')

dt_peninsula = datetime.datetime(2022, 10, 26, 12, 0, 0, tzinfo=tz_peninsula)
dt_canarias = datetime.datetime(2022, 10, 26, 12, 0, 0, tzinfo=tz_canarias)
print('Península:', dt_peninsula)
print('Canarias:', dt_canarias)
print(dt_peninsula == dt_canarias)
```

Pero si los creamos con una hora de diferencia, son comparables aunque no estén
en la misma zona horaria:

```
import datetime
import zoneinfo

tz_peninsula = zoneinfo.ZoneInfo('Europe/Madrid')
tz_canarias = zoneinfo.ZoneInfo('Atlantic/Canary')

dt_peninsula = datetime.datetime(2022, 10, 26, 12, 0, 0, tzinfo=tz_peninsula)
# Una hora menos en canarias...
dt_canarias = datetime.datetime(2022, 10, 26, 11, 0, 0, tzinfo=tz_canarias)
print('Península:', dt_peninsula)
print('Canarias:', dt_canarias)
print(dt_peninsula == dt_canarias)
```


## Objetos `timedelta`

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

Todos los argumentos del constructor son opcionales y tienen como valor por
defecto $0$. Podemos usar para cada uno de estos parámetros valores positivos o
negativos, y valores enteros o decimales. Por ejemplo,para crear una diferencia
horaria de media hora, podríamos hacer:

```python
media_hora = datetime.timedelta(hours=0.5)
```

**Ejercicio**: Crear un `timedelta` para una diferencia de nueve horas y media.
Crear ahora un `timedelta` de media hora y otro de 30 minutos. ¿Son iguales?

El objeto `timedelta` normaliza todos los parámetros de entrada para almacenar
solo días, segundos y milisegundos. Una vez creado un `timedelta`, podemos
acceder a estos atributos `days`, `seconds` y `microseconds` que lo definen.

El siguiente ejemplo muestra cuantos días y segundos hay en [nueve
semanas y media](https://www.imdb.com/title/tt0091635/):

![Nueve semanas y media](nueve-semanas-y-media.png)

```python
import datetime
d = datetime.timedelta(weeks=9.5) 
print(
    "Nueve semanas y media son",
    f"{d.days} días y {d.seconds} segundos",
)
```

Los objetos `timedelta` son consistentes, esto es, producen el mismo valor aun
si se han construido de formas diferentes. Por ejemplo, para obtener un periodo
de 24 horas puede hacerse de diferentes formas:

```python
import datetime

datetime.timedelta(days=1)
datetime.timedelta(hours=24)
datetime.timedelta(hours=1) * 24
```

**Pregunta** ¿Son equivalentes los periodos calculados en el siguiente
ejemplo? Razona la respuesta.

```python
import datetime

delta_1 = datetime.timedelta(hours=1.5)
delta_2 = datetime.timedelta(hours=1) + datetime.timedelta(minutes=30)
```

Veremos a continuación que si restamos objetos de tipo fecha (`date`) o
marca temporal (`datetime`) obtendremos objetos de tipo `timedelta`.


### Sumas y diferencias entre fechas

La diferencia o resta entre dos fechas nos dará un `timedelta`.

**Ejercicio**: Calcular el número de días trascurridos desde que la
Organización Mundial de la Salud reconoció como Pandemia la enfermedad conocida
como **COVID-19** (Necesitarás crear dos fechas, la de hoy y la de la
declaración, y restarlas para obtener  un `datetime.timedelta`).

![11 de marzo de 2020](pandemia.png)
- Fuente: [Pandemia de COVID-19 - Wikipedia, la enciclopedia libre](https://es.wikipedia.org/wiki/Pandemia_de_COVID-19#Declaraci%C3%B3n_de_pandemia)

También podemos sumar una variable de tipo `timedelta` a una fecha para obtener
una nueva.

```python
>>> import datetime
>>> hoy = datetime.today()
>>> tres_dias = datetime.timedelta(days=3)
>>> dentro_de_tres_dias = hoy + tres_dias
```

[ ] **Ejercicio**: Escribir una función `ayer()` que nos devuelva la fecha
de ayer. Puedes usar un `timedelta` para restar un día a la fecha actual.

**Ejercicio**: Escribir una función `principio_siguiente_mes(fecha)` que nos devuelva la fecha
del primer día del mes sigiuente al de la fecha pasada como parámetro. Observa
que un simple `replace` puede fallar, porque si partimos del 30 de enero,
e intentar obtener una fecha convirtiendo el mes a febrero, nos dará un
error, ya que no existe el 20 de febrero. Puedes usar un `timedelta` para sumar
un día a la fecha hasta que el mes cambie.


**Miniproyecto:**

Mejorar el siguiente código para mostrar una fecha y hora en formato para
humanos. 

Bonus: Imprimir un marca si el fichero ha sido creado hace menos de 24 horas

```
import os

for filename in os.listdir():
    ts_modificado = os.path.getctime(filename)
    print(filename, ts_modificado)
```

