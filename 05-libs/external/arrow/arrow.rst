La librería ``arrow``: Trabajar con fechas
---------------------------------------------------

.. index:: arrow

La librería **arrow** proporciona intenta que trabajar, modificar y formatear y convertir fechas sea
más sencillo y amigable que con el paquete de la librería estándar `datetime`. Lo hace reimplementando
y actualizando la clase `datetime`, cubriendo ciertos huecos en la funcionalidad y proporcionando una
API más directa para muchas formas diferentes de crear fechas. A modo de resumen, intenta que se
pueda trabajar con fechas con menos imports y menos código.

El nombre, *arrow* (Flecha) viene de la expresión *fecha del tiempo*.

Ventajas de usar arrow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Se puede trabajar perfectamente con fechas usando la librería estándar, pero lo que
arrow intenta mejorar son los siguientes aspectos de ``datetime``:

- Demasiados módulos: `datetime`, `time`, `calendar`, `dateutil`, `pytz`, etc.

- Demasiados tipos: `date`, `time`, `datetime`, `tzinfo`, `timedelta`, `relativedelta`, etc.

- Trabajar con `husos horarios`_ (*timezone*) y convertir de una zona horaria a otra
  resulta farragoso y pesado.

- Las marcas de tiempo (*timestamp*) son abiertas o ingenuas (*naive*) por defecto.

- Existen ciertos huecos en la funcionalidad: Interpretar texto en formato ISO 8601, convertir
  a valores más cercanos al humano.

Veremos ejemplos de cada una de estas funcionalidad tal y como las resuelve ``arrow``.

Crear fechas
^^^^^^^^^^^^^^^^^^^

Usando `datetime` no tenemos muchas opciones para crear fechas, podemos crearlas pasando
los datos que necesitamos::

    import datetime

    fecha = datetime.date(2020, 6, 23)  # 23/jun/2020
    timestamp = datetime.datetime(2020, 6, 23, 12, 0, 0)  # 23/jun/2020, a las 12:00:00

O obtener la fecha de hoy (``datetime.data.today()``) o el timestamp de este momento
(``datetime.datetime.now`` o ``datetime.datetime.utcnow``)::

    import datetime
    hoy = datetime.date.today()
    ahora = datetime.datetime.now()

Con ``arrow`` tenemos las mismas opciones, pero tambien podemos crear una fecha/timestamp
a partir del texto en formato ISO 8601::

    import arrow
    ts = arrow.get('2020-06-11T21:23:58.970460+07:00')
    d1 = arrow.get(2020, 3, 3)
    d2 = arrow.get('2020-03-03')
    assert d1 == d2

Además, al contrario que ``datetime``, las fechas y marcas temporales no son abiertas
o *naive* por defecto, sino que tienen definido el huso horario al que corresponden.

Obtener una fecha/timestamp a partir de otra
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los objetos ``Arrow`` tienen un método llamado ``replace`` para cambiar los valores
de una fecha, y otro llamado ``shift`` que nos permite *desplazar* una
fecha a lo largo del tiempo. Como los objetos tipo ``Arrow`` son inmutables, tanto ``replace``
como ``shitf``
nos devuelven un nuevo objeto en la posicion temporal deseada. El método acepta diferentes
unidades de desplazamiento, y lo hace mediante parametro con nombre, como `days`, `months`,
`minutes`

Ejercicio: Calcular el número de días que faltan para la navidad


Ejercicio: Usando ``arrow``, calcular el dia de la semana de la fecha correspondiente
al día actual, pero dentro de 89 años, 3 meses y 9 días.

Ver solución: :ref:arrow_01.

.. _husos horarios: https://es.wikipedia.org/wiki/Huso_horario
