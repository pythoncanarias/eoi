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

- Las mascas de tiempo (*timestamp*) son abiertas o ingenuas (*naive*) por defecto.

- Existen ciertos huecos en la funcionalidad: Interpretar texto en formato ISO 8601, convertir
  a valores más cercanos al humano.

Veremos ejemplos de cada una de estas funcionalidad tal y como las resuelve ``arrow``.




.. _husos horarios: https://es.wikipedia.org/wiki/Huso_horario
