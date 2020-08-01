La librería arrow
-----------------

La librería **arrow** nos facilita trabajar con fechas.

**Arrow** intenta que trabajar, modificar, formatear y convertir fechas
sea más sencillo y amigable que con el paquete de la librería estándar
``datetime``.

Lo hace reimplementando y actualizando la clase datetime, cubriendo
ciertos huecos en la funcionalidad y proporcionando una API más directa
para muchas formas diferentes de crear fechas. A modo de resumen,
intenta que se pueda trabajar con fechas con menos imports y menos
código.

El nombre, *arrow* (Flecha) viene de la expresión *fecha del tiempo*.

Instalar arrow
~~~~~~~~~~~~~~

Se instala simplemente con pip:

.. code:: ipython3

    !pip install arrow

Ventajas de usar arrow
~~~~~~~~~~~~~~~~~~~~~~

Se puede trabajar perfectamente con fechas usando la librería estándar,
pero lo que arrow intenta mejorarla en los siguientes aspectos:

-  Demasiados módulos: datetime, time, calendar, dateutil, pytz, etc.

-  Demasiados tipos: date, time, datetime, tzinfo, timedelta,
   relativedelta, etc.

-  Trabajar con `husos
   horarios <https://es.wikipedia.org/wiki/Huso_horario>`__ (*timezone*)
   y convertir de una zona horaria a otra resulta farragoso y pesado.

-  Las marcas de tiempo (*timestamp*) son abiertas o ingenuas (*naive*)
   por defecto.

-  Existen ciertos huecos en la funcionalidad: Interpretar texto en
   formato ISO 8601, convertir a valores más fáciles de interpretar por
   humanos…

Veremos ejemplos de cada una de estas funcionalidad tal y como las
resuelve ``arrow``.

Crear fechas
~~~~~~~~~~~~

Usando datetime no tenemos muchas opciones para crear fechas, podemos
crearlas pasando los datos que necesitamos, o obtener la fecha de hoy
con ``datetime.date.today`` o el *timestamp* de este momento, con
``datetime.datetime.now`` o ``datetime.datetime.utcnow``.

.. code:: ipython3

    import datetime
    
    fecha = datetime.date(2020, 6, 23)  # 23/jun/2020
    timestamp = datetime.datetime(2020, 6, 23, 12, 0, 0)  # 23/jun/2020, a las 12:00:00
    
    hoy = datetime.date.today()
    ahora = datetime.datetime.now()
    print(fecha, timestamp, hoy, ahora, sep=",")

Con ``arrow`` tenemos las mismas opciones, pero ademas podemos crear una
fecha timestamp a partir del texto en formato ISO 8601. Arrow crea casi
todos las variables con la funcion ``get``. Si se llama a ``get`` sin
parametros nos devolvera la fecha y hora actual, usando la zona horaria
UTC:

.. code:: ipython3

    ### Instalar arrow
    
    !pip install arrow


.. parsed-literal::

    Requirement already satisfied: arrow in /home/jileon/.virtualenvs/eoi/lib/python3.6/site-packages (0.15.5)
    Requirement already satisfied: python-dateutil in /home/jileon/.virtualenvs/eoi/lib/python3.6/site-packages (from arrow) (2.8.1)
    Requirement already satisfied: six>=1.5 in /home/jileon/.virtualenvs/eoi/lib/python3.6/site-packages (from python-dateutil->arrow) (1.14.0)


.. code:: ipython3

    import arrow

.. code:: ipython3

    import arrow
    now = arrow.get()
    ts = arrow.get('2020-06-11T21:23:58.970460+07:00')
    d1 = arrow.get(2020, 3, 3)
    d2 = arrow.get('2020-03-03')
    assert d1 == d2

Si queremos ser más explícitos, tenemos las funciones ``now`` y
``utcnow``. Con ``now`` podemos indicar la zona horaria como una string,
una forma muchos más sencilla que con la librería estándar:

.. code:: ipython3

    print(arrow.utcnow())
    print(arrow.now())
    print(arrow.now('Atlantic/Canary'))


.. parsed-literal::

    2020-04-20T15:55:15.494170+00:00
    2020-04-20T16:55:15.498987+01:00
    2020-04-20T16:55:15.500376+01:00


Además, al contrario que ``datetime``, las fechas y marcas temporales no
son abiertas o *naive* por defecto, sino que tienen definido el huso
horario al que corresponden. Si no se indica nada, por defecto se asigna
UTC. Por eso en la celda anterior los valores deberían ser practicamente
iguales (La diferencia debe estar en la escala de milisegundos).

.. code:: ipython3

    arrow.Arrow.utcoffset?

.. code:: ipython3

    arrow.now('America/Chicago').utcoffset

**Ejercicio**: Sabiendo que la zona horaria de Turquía es
``Asia/Istanbul``, averiguar cual es la diferencia horaria con respecto
a UTC. Este dato esta disponible usando el método ``utcoffset()``.
Puedes ver los `nombres de las zonas horarias en
Wikipedia <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__.

**Plus**: Averiguar la diferencia horaria entre la España peninsular
(zona horaria ``Europe/Madrid``), Alemania (zona horaria
``Europe/Berlin`` e Italia (zona horaria ``Europe/Rome``).

.. code:: ipython3

    # %load diferencia-horaria-turquia.py
    import arrow
    
    now = arrow.now('Asia/Istanbul')
    print(now)
    



.. parsed-literal::

    2020-04-20T19:04:54.205854+03:00


.. code:: ipython3

    # %load diferencia-madrid-berlin-roma.py
    import arrow
    
    now_in_madrid = arrow.now("Europe/Madrid")
    now_in_turkey = arrow.now("Asia/Istanbul")
    now_in_berlin = arrow.now("Europe/Berlin")
    now_in_rome = arrow.now("Europe/Rome")
    
    print("Diferencias horarias respecto a España peninsular:")
    print(" - Turquia:", now_in_madrid.utcoffset() - now_in_turkey.utcoffset())
    print(" - Alemania:", now_in_madrid.utcoffset() - now_in_berlin.utcoffset())
    print(" - Italia:",  now_in_madrid.utcoffset() - now_in_rome.utcoffset())


.. parsed-literal::

    Diferencias horarias respecto a España peninsular:
     - Turquia: -1 day, 23:00:00
     - Alemania: 0:00:00
     - Italia: 0:00:00


Otras formas de crear fechas o marcas temporales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A partir de tiempos UNIX
^^^^^^^^^^^^^^^^^^^^^^^^

Otra posibilidad es crear fechas o marcas temporales a parir de los
`tiempos UNIX o Enotch <https://es.wikipedia.org/wiki/Tiempo_Unix>`__:

.. code:: ipython3

    import arrow, time
    
    print(arrow.get(1487900664))
    print(arrow.get(1367900664.152325))
    print(arrow.get(time.time()))


.. parsed-literal::

    2017-02-24T01:44:24+00:00
    2013-05-07T04:24:24.152325+00:00
    2020-04-20T16:12:24.618538+00:00


A partir de otros objetos ``date`` o ``timestamp``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Observa que con el siguiente ejemplo se consiguen fechas *arrow* y son,
por tanto, completas, con zona horaria UTC por defecto, menos en el
último ejemplo, que forzamos la zona horaria de Francia.

.. code:: ipython3

    import arrow, datetime
    
    print(arrow.get(datetime.date.today()))
    print(arrow.get(datetime.datetime.now()))
    print(arrow.get(datetime.datetime.now(), "Europe/Paris"))


.. parsed-literal::

    2020-04-20T00:00:00+00:00
    2020-04-20T17:14:01.549702+00:00
    2020-04-20T17:14:01.550245+02:00


A partir de una cadena de texto
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Podemos extraer de una texto una fecha o marca temporal, si le indicamos
a la libreria como debe interpretar ese texto:

.. code:: ipython3

    import arrow
    
    arrow.get('2022-04-19 12:30:45', 'YYYY-MM-DD HH:mm:ss')




.. parsed-literal::

    <Arrow [2022-04-19T12:30:45+00:00]>



No hay problema si el dato está incluido dentro de un texto mayor. En el
siguiente ejemplo, además, se especifica el parámetro ``locale`` a
español (Usando la constante ``ES_es``) para estar seguros de que se
interpreta *julio* como el nombre del mes, y no *July*:

.. code:: ipython3

    import arrow
    
    d = arrow.get(
        'Diana, princesa de Gales, nacida el 1 de julio de 1961 en Norfolk, Inglaterra',
        'D [de ]MMMM [de ]YYYY',
        locale="ES_es",
    )
    print(d)


.. parsed-literal::

    1961-07-01T00:00:00+00:00


Podemos usar los siguientes códigos para formatear o para interpretar
una fecha en un texto. No son los mismos valores que usa datetime.

================== ===== =======================================
\                  Token Salida
================== ===== =======================================
Año                YYYY  2000, 2001, 2002 … 2012, 2013
\                  YY    00, 01, 02 … 12, 13
Mes                MMMM  Nombre completo del mes
\                  MMM   Nombre abreviado del mes (tres letras)
\                  MM    Numero del mes, con dos digitos
\                  M     Numoer del mes, con uno o dos digitos
Day of Year        DDDD  001, 002, 003 … 364, 365
\                  DDD   1, 2, 3 … 364, 365
Day of Month       DD    01, 02, 03 … 30, 31
\                  D     1, 2, 3 … 30, 31
\                  Do    1st, 2nd, 3rd … 30th, 31st
Day of Week        dddd  Lunes, Martes, Miércoles…
\                  ddd   Mon, Tue, Wed
\                  d     1, 2, 3 … 6, 7
ISO week date      W     2011-W05-4, 2019-W17
Hour               HH    00, 01, 02 … 23, 24
\                  H     0, 1, 2 … 23, 24
\                  hh    01, 02, 03 … 11, 12
\                  h     1, 2, 3 … 11, 12
AM / PM            A     AM, PM, am, pm
\                  a     am, pm
Minute             mm    00, 01, 02 … 58, 59
\                  m     0, 1, 2 … 58, 59
Second             ss    00, 01, 02 … 58, 59
\                  s     0, 1, 2 … 58, 59
Sub-second         S…    0, 02, 003, 000006, 123123123123…
Timezone           ZZZ   Asia/Baku, Europe/Warsaw, GMT
\                  ZZ    -07:00, -06:00 … +06:00, +07:00, +08, Z
\                  Z     -0700, -0600 … +0600, +0700, +08, Z
Seconds Timestamp  X     1381685817, 1381685817.915482 …
ms or µs Timestamp x     1569980330813, 1569980330813221
================== ===== =======================================

A partir de una cadena de texto en formato ISO 8601
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si tenemos la suerte de que el texto ya viene en formato ISO 8601, se
puede interpretar directamente, sin necesidad de indicar el formato:

.. code:: ipython3

    import arrow
    
    arrow.get('2013-09-30T15:34:00.000-07:00')




.. parsed-literal::

    <Arrow [2013-09-30T15:34:00-07:00]>



Obtener una fecha/timestamp a partir de otra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los objetos ``Arrow`` tienen un método llamado ``replace`` para cambiar
los valores de una fecha, y otro llamado ``shift`` que nos permite
*desplazar* una fecha a lo largo del tiempo. Como los objetos tipo
``Arrow`` son inmutables, tanto ``replace`` como ``shitf`` nos devuelven
un nuevo objeto en la posicion temporal deseada.

El método acepta diferentes unidades de desplazamiento, y lo hace
mediante parametro con nombre, como ``days``, ``months``, ``minutes``,…

**Ejercicio**: Calcular el número de días que faltan para la navidad

**Pista**: primero obtén la fecha actual. Luego crea una nueva fecha
reemplazando el mes por 12 y el día por 25 (``replace``). La diferencia
entre las dos fechas te da el número de días hasta Navidad.

.. code:: ipython3

    # %load dias-hasta-navidad.py
    import arrow
    
    today = arrow.get()
    navidad = today.replace(month=12, day=25)
    print(navidad - today)



.. parsed-literal::

    249 days, 0:00:00


El método shift (desplazar)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Con el método ``shift`` también abtenemos una nueva fecha, pero en vez
de indicar los valores a cambiar, indicamos el desplazamiento, positivo
o negativo, a partir de la fecha original. Por ejemplo, para obtenter la
fecha de mañana, se puede hacer:

.. code:: ipython3

    import arrow
    
    hoy = arrow.get()
    mannana = hoy.shift(days=1)
    print(hoy, mannana, sep=", ")


.. parsed-literal::

    2020-04-20T16:29:20.481298+00:00, 2020-04-21T16:29:20.481298+00:00


**Ejercicio**: Usando ``arrow``, calcular la fecha correspondiente al
día actual, pero dentro de 8 años, 3 meses y 9 días.

.. code:: ipython3

    # %load fecha-futura.py
    import arrow
    
    WEEKDAYS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    
    dia = arrow.utcnow()
    futuro = dia.shift(years=8, months=3, days=9)
    wd = futuro.weekday()
    print(f"El día {futuro.format('D/MMM/YYYY')} cae en {WEEKDAYS[wd]}")



.. parsed-literal::

    El día 29/Jul/2028 cae en sábado


El método ``for_json``
~~~~~~~~~~~~~~~~~~~~~~

El método ``for_json`` devuelve una string en formato ISO, lo que
resulta muy cómodo para incluir fechas y marcas temporales en formato
JSON, que no tiene un tipo de dato especifico para estos datos.

.. code:: ipython3

    import arrow
    
    print(arrow.get(2019, 12, 6).for_json())

Rangos
~~~~~~

A partir de un objeto ``Arrow``, podemos obtener el rango que lo
contiene. El ancho del rango depende de la unidad que se le pase como
parametro al metodo ``span``:

.. code:: ipython3

    import arrow
    
    desde, hasta = arrow.utcnow().span('hours')
    print(desde)
    print(hasta)


.. parsed-literal::

    2020-04-20T16:00:00+00:00
    2020-04-20T16:59:59.999999+00:00


O podemos obtener los limites inferior y superior del rango por
sseparado, conlos metodos ``floor`` y ``ceil``:

.. code:: ipython3

    import arrow
    
    print(arrow.utcnow().floor('hour'))
    print(arrow.utcnow().ceil('hour'))


.. parsed-literal::

    2020-04-20T15:00:00+00:00
    2020-04-20T15:59:59.999999+00:00


El metodo humanize
~~~~~~~~~~~~~~~~~~

**humanize** nos permite obtener una descripción textual, más ambigua
pero muy comoda y apta para un ser humano. Con un ejemplo lo
entenderemos enseguida:

.. code:: ipython3

    import arrow
    
    d = arrow.now().shift(hours=-1)
    print(d.humanize())
    
    d = arrow.now().shift(years=5, months=11, days=1)
    print(d.humanize())


.. parsed-literal::

    an hour ago
    in 5 years


En estos ejemplos hemos forzado el valor de ``locale``. Un **locale** se
refiere a un conjunto de variables de entorno que definen el lenguaje,
país y codificación de caracteres preferida, entre otras cosas (como,
por ejemplo, si las fechas se expresan en el orden día, mes, año o mes,
dia, año).

En los ejemplos se ha ajustado a mano para estar seguros de que los
ejemplos funcionan en cualquier entorno, pero lo recomendado,
obviamente, es que el sistema tenga correctamente definido el ``locale``
para que arrow lo lea del sistema.

**Miniproyecto**: Calcular el número total de viernes y 13 en el año
2020

**Pistas**:
-----------

1. Obtén una fecha para el primer día del año, es decir, a 1 de enero de
   2020. Puedes usar cualquier nombre para esta variable, en estas
   pistas supondré que la has llamado ``dia``.

2. Haz un bucle ``while`` para recorrer todos los días del año. La
   condición de salida es que el año sea distinto del año actual, por lo
   tanto la condición del ``while`` es la contraria:
   (``while d.year == 2020``).

Acuérdate de que para este tipo de bucles es importante asegurarse de
que la variable que provoca la salida del bucle es modificada dentro del
mismo. En este ejemplo, hay que avanzar la variable ``dia`` en cada
iteración (Ver el punto 4).

3. Para cada uno de los días, comprobar si es el 13 (``dia.day == 13``)
   **y** que es viernes (``dia.weekday() == 4``). Si es así, imprímelo.

4. desplaza dia al dia siguiente: ``dia = dia.shift(days=1)``.

.. code:: ipython3

    def Viernes13(year):
        viernes13 = []
        day = arrow.now().replace(day=13,month=1,year=year)
        for i in range(1,13):
            day = day.replace(month=i)
            if day.isoweekday() == 4:
                viernes13.append(day)
        return viernes13
    
    print(Viernes13(1915))


.. parsed-literal::

    [<Arrow [1915-05-13T18:08:34.108930+00:00]>]


.. code:: ipython3

    # %load viernes-trece.py
    #!/usr/bin/env python
    
    import arrow
    
    dia = arrow.get(2020, 1, 1)
    while dia.year == 2020:
        if dia.day == 13 and dia.weekday() == 4:  # Es viernes y trece
            print(dia)
        dia = dia.shift(days=1)
    



.. parsed-literal::

    2020-03-13T00:00:00+00:00
    2020-11-13T00:00:00+00:00


**Extra**: ¿Cuántos días viernes y trece hubo en 2015? ¿Y en 1915?

Libreria alternativas
~~~~~~~~~~~~~~~~~~~~~

-  `Delorean <https://github.com/myusuf3/delorean>`__

-  `Pendulum <https://pendulum.eustace.io/>`__

