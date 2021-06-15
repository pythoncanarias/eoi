---
title: arrow - Gesti de fechas
---
## Introduccón a `arrow`

La librería **arrow** nos facilita trabajar con fechas. **Arrow** intenta que
trabajar, modificar, formatear y convertir fechas sea más sencillo y amigable
que con el paquete de la librería estándar `datetime`. 

Lo hace reimplementando y actualizando la clase `datetime`, cubriendo ciertos
huecos en la funcionalidad y proporcionando una API más directa para muchas
formas diferentes de crear fechas. A modo de resumen, intenta que se pueda
trabajar con fechas con menos _imports_ y menos código.

El nombre, *arrow* (Flecha) viene de la expresión *fecha del tiempo*.

### Instalar arrow

Se instala simplemente con pip:

```python
!pip install arrow
```

Y se importa como:

```python
import arrow
```

### Ventajas de usar arrow

Se puede trabajar perfectamente con fechas usando la librería estándar,
pero `arrow` intenta mejorarla en los siguientes aspectos:

- Demasiados módulos: `datetime`, `time`, `calendar`, `dateutil`, `pytz`, etc.

- Demasiados tipos: `date`, `time`, `datetime`, `tzinfo`, `timedelta`, `relativedelta`, etc.

- Trabajar con [husos horarios](https://es.wikipedia.org/wiki/Huso_horario) (*timezone*) y
    convertir de una zona horaria a otra resulta farragoso y pesado.
    
- Las marcas de tiempo (*timestamp*) son abiertas o ingenuas (*naive*) por defecto.
    
- Falta funcionalidad: Interpretar texto en formato ISO 8601, convertir a
  valores más fáciles de interpretar por humanos...

Veremos ejemplos de cada una de estas posibles mejoras tal y como las
resuelve `arrow`.

### Crear fechas

Usando `datetime` no tenemos muchas opciones para crear fechas, podemos
crearlas pasando los datos que necesitamos, o obtener la fecha de hoy con
`datetime.date.today` o el *timestamp* de este momento, con `datetime.datetime.now`
o `datetime.datetime.utcnow`. 

```python
import datetime

fecha = datetime.date(2020, 6, 23)  # 23/jun/2020
timestamp = datetime.datetime(2020, 6, 23, 12, 0, 0)  # 23/jun/2020, a las 12:00:00

hoy = datetime.date.today()
ahora = datetime.datetime.now()
print(fecha, timestamp, hoy, ahora, sep=",")
```
Con `arrow` tenemos las mismas opciones, pero ademas podemos crear una
fecha `timestamp` a partir del texto en formato ISO 8601. `Arrow` crea casi
todos las variables con la función `get`. Si se llama a `get` sin
parámetros nos devolverá la fecha y hora actual, usando la zona horaria UTC:


```python
import arrow

now = arrow.get()
ts = arrow.get('2020-06-11T21:23:58.970460+07:00')
d1 = arrow.get(2020, 3, 3)
d2 = arrow.get('2020-03-03')
assert d1 == d2
```

Si queremos ser más explícitos, tenemos las funciones `now` y `utcnow`. Con `now` podemos
indicar la zona horaria con una `string`, una forma muchos más sencilla que con la librería
estándar:


```python
print(arrow.utcnow())
print(arrow.now())
print(arrow.now('Europe/Madrid'))
```

Además, al contrario que `datetime`, las fechas y marcas temporales no son
abiertas o *naive* por defecto, sino que tienen definido el huso horario al que
corresponden. Si no se indica nada, por defecto se asigna UTC. Por eso en la
celda anterior los valores deberían ser prácticamente iguales (La diferencia
debe estar en la escala de milisegundos).





**Ejercicio:** Sabiendo que la zona horaria de Turquía es `Asia/Istanbul`,
averiguar cual es la diferencia horaria con respecto a UTC. Este dato esta
disponible usando el método `utcoffset()`. Puedes ver los [nombres de las zonas
horarias en Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

Ejemplo de uso de `utcoffset`:

```python
arrow.now('America/Chicago').utcoffset()
```
Produce algo como:

```
datetime.timedelta(days=-1, seconds=68400)
```

**Plus**: Averiguar la diferencia horaria entre la España peninsular (zona
horaria `Europe/Madrid`), Alemania (zona horaria `Europe/Berlin` e Italia
(zona horaria `Europe/Rome`).

**Soluciones:**

```python
{% include 'external/arrow/diferencia-horaria-turquia.py' %}
```

```python
{% include 'external/arrow/diferencia-madrid-berlin-roma.py' %}
```

    Diferencias horarias respecto a España peninsular:
     - Alemania: 0:00:00
     - Italia: 0:00:00


### Otras formas de crear fechas o marcas temporales

#### A partir de tiempos UNIX

Otra posibilidad es crear fechas o marcas temporales a partir de 
los [tiempos UNIX o Enotch](https://es.wikipedia.org/wiki/Tiempo_Unix):


```python
import arrow, time

print(arrow.get(1487900664))
print(arrow.get(1367900664.152325))
print(arrow.get(time.time()))
```

Que produce:

```
2017-02-24T01:44:24+00:00
2013-05-07T04:24:24.152325+00:00
2021-06-15T19:02:29.039913+00:00
```

#### A partir de otros objetos `date` o `timestamp`

Observa que con el siguiente ejemplo se consiguen fechas *arrow* y son, por tanto, completas, con zona
horaria UTC por defecto, menos en el último ejemplo, que forzamos la zona horaria de Francia.


```python
import arrow, datetime

print(arrow.get(datetime.date.today()))
print(arrow.get(datetime.datetime.now()))
print(arrow.get(datetime.datetime.now(), "Europe/Paris"))
```

Salida:

```
2021-06-15T00:00:00+00:00
2021-06-15T20:03:33.645496+00:00
2021-06-15T20:03:33.645565+02:00
```

#### A partir de una cadena de texto

Podemos extraer de una texto una fecha o marca temporal, si le indicamos
a la librería como debe interpretar ese texto:


```python
import arrow

arrow.get('2022-04-19 12:30:45', 'YYYY-MM-DD HH:mm:ss')
```

No hay problema si el dato está incluido dentro de un texto mayor. En el
siguiente ejemplo, además, se especifica el parámetro `locale` a español
(Usando la constante `ES_es`) para estar seguros de que se interpreta *julio*
como el nombre del mes, y no *July*:


```python
import arrow

d = arrow.get(
    'Diana, nacida el 1 de julio de 1961 en Norfolk, Inglaterra',
    'D [de ]MMMM [de ]YYYY',
    locale="ES_es",
)
print(d)
```

Podemos usar los siguientes códigos para formatear o para interpretar una fecha en un texto. No son
los mismos valores que usa `datetime`.

|               | Token   | Salida                                 |
|--------------:|---------|----------------------------------------|
| Año           | YYYY    | 2000, 2001, 2002 … 2012, 2013          |
|               | YY      | 00, 01, 02 … 12, 13                    |
| Mes           | MMMM    | Nombre completo del mes                |
|               | MMM     | Nombre abreviado del mes (tres letras) |
|               | MM      | Número del mes, con dos dígitos        |
|               | M       | Número del mes, con uno o dos dígitos  |
| Day of Year   | DDDD    | 001, 002, 003 … 364, 365               |
|               | DDD     | 1, 2, 3 … 364, 365                     |
| Day of Month  | DD      | 01, 02, 03 … 30, 31                    |
|               | D       | 1, 2, 3 … 30, 31                       |
|               | Do      | 1st, 2nd, 3rd … 30th, 31st             |
| Day of Week   | dddd    | Lunes, Martes, Miércoles...            |
|               | ddd     | Mon, Tue, Wed                          |
|               | d       | 1, 2, 3 … 6, 7                         |
| ISO week date | W       | 2011-W05-4, 2019-W17                   |
| Hour          | HH      | 00, 01, 02 … 23, 24                    |
|               | H       | 0, 1, 2 … 23, 24                       |
|               | hh      | 01, 02, 03 … 11, 12                    |
|               | h       | 1, 2, 3 … 11, 12                       |
| AM / PM       | A       | AM, PM, am, pm                         |
|               | a       | am, pm                                 |
| Minute        | mm      | 00, 01, 02 … 58, 59                    |
|               | m       | 0, 1, 2 … 58, 59                       |
| Second        | ss      | 00, 01, 02 … 58, 59                    |
|               | s       | 0, 1, 2 … 58, 59                       |
| Sub-second    | S…      | 0, 02, 003, 000006, 123123123123…      |
| Timezone      | ZZZ     | Asia/Baku, Europe/Warsaw, GMT          |
|               | ZZ      | -07:00, -06:00 … +06:00, +07:00, Z     |
|               | Z       | -0700, -0600 … +0600, +0700, +08, Z    |
| Seconds  (ts) | X       | 1381685817, 1381685817.915482 …        |
| ms or µs (ts) | x       | 1569980330813, 1569980330813221        |


#### A partir de una cadena de texto en formato ISO 8601

Si tenemos la suerte de que el texto ya viene en formato ISO 8601, se puede
interpretar directamente, sin necesidad de indicar el formato:


```python
import arrow

arrow.get('2013-09-30T15:34:00.000-07:00')
```

### El método `replace`

Los objetos `Arrow` tienen un método llamado `replace` para cambiar los valores
de una fecha, y otro llamado `shift` que nos permite *desplazar* una fecha a lo
largo del tiempo. Como los objetos tipo `Arrow` son inmutables, tanto `replace`
como `shitf` nos devuelven un nuevo objeto en la posición temporal deseada. 

El método acepta diferentes unidades de desplazamiento, y lo hace mediante
parámetro con nombre, como `days`, `months`, `minutes`,...

**Ejercicio:** Calcular el número de días que faltan para la navidad.

**Pista:** Primero consigue la fecha actual. Luego crea una nueva fecha
reemplazando el mes por 12 y el día por 25 (`replace`). La diferencia entre las
dos fechas te dará el número de días hasta Navidad.

**Solución:**

```python
{% include 'external/arrow/dias-hasta-navidad.py' %}
```

### El método `shift` (desplazar)

Con el método `shift` también obtenemos una nueva fecha, pero en vez de indicar
los valores absolutos a cambiar, indicamos el desplazamiento, positivo o negativo, a
partir de la fecha original. Por ejemplo, para obtener la fecha de pasado mañana, se
puede hacer:


```python
import arrow

hoy = arrow.get()
day_after_tomorrow = hoy.shift(days=2)
print(day_after_tomorrow)
```

**Ejercicio:** Usando `arrow`, calcular el día de la semana de la fecha
correspondiente al día actual, pero dentro de 8 años, 3 meses y 9 días.

**Solución:**

```python
{% include 'external/arrow/fecha-futura.py' %}
```

### El método `for_json`

El método `for_json` devuelve una _string_ en formato ISO, lo que resulta muy cómodo para
incluir fechas y marcas temporales en JSON, que no tiene un tipo de dato especifico
para estos datos.


```python
import arrow

print(arrow.get(2019, 12, 6).for_json())
```

### El método `span`. Cálculo de rangos

A partir de un objeto `Arrow`, podemos obtener el rango que lo contiene. El
ancho del rango depende de la unidad que se le pase como parámetro al método
`span`:
  

```python
import arrow

desde, hasta = arrow.now('Europe/Madrid').span('days')
print(desde)
print(hasta)
```

O podemos obtener los límites inferior y superior del rango por separado, con
los métodos `floor` y `ceil`:


```python
import arrow

print(arrow.utcnow().floor('hour'))
print(arrow.utcnow().ceil('hour'))
```

### El metodo `humanize`

**humanize** nos permite obtener una descripción textual, más ambigua pero más cómoda
para un ser humano. Con un ejemplo lo entenderemos enseguida:


```python
import arrow

d = arrow.now().shift(hours=-1)
print(d.humanize(locale='es_ES')

d = arrow.now().shift(years=5, months=11, days=1)
print(d.humanize(locale='es_ES'))
```

Produce:

```
hace una hora
en 5 años
```

En estos ejemplos hemos forzado el valor de `locale`. Un __locale__ se refiere
a un conjunto de variables de entorno que definen el lenguaje, país y
codificación de caracteres preferida, entre otras cosas (como, por ejemplo, si
las fechas se expresan en el orden día, mes, año o mes, día, año). 

En los ejemplos se ha ajustado a mano para estar seguros de que los ejemplos
funcionan en cualquier entorno, pero lo recomendado, obviamente, es que el
sistema tenga correctamente definido el `locale` para que `arrow` lo lea del
sistema.

**Miniproyecto:** Calcular el número total de viernes y 13 en el año 2020

**Pistas:**

1. Hay que comprobar los días 13 de cada mes. Eso significa que podemos hacer un bucle
con valores desde 1 hasta 12 para probar cada mes, ya que $1$ es enero y $12$
es diciembre.

2. Dentro del bucle, consigue la fecha para el día 13 del mes que te indica el bucle y del año
investigado, es decir, 2021.

3. Comprobar si la fecha calculada en el paso previo es viernes (`dia.weekday() == 4`). 
Si es así, imprímelo.


```python
{% include 'external/arrow/viernes-trece.py' %}
```

Solo hubo uno, el 13 de mayo.


**Ejercicion Extra:** ¿Cuántos viernes y trece hubo en 2015? ¿Y en 1915?

### Librerías alternativas

- [Delorean](https://github.com/myusuf3/delorean)

- [Pendulum](https://pendulum.eustace.io/)

- [dateutils](https://dateutil.readthedocs.io/en/stable/)

