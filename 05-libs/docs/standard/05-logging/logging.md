---
title: logging - Registro de actividad
---

## Introducción a `logging`

El módulo `logging` define un sistema flexible y homogéneo para añadir un
sistema de registro de eventos o **log** a nuestras aplicaciones o librerías.

Crear un log es relativamente fácil, pero la ventaja de usar el API definido en
las librerías estándar es que todos los módulos pueden participar en un log
común, de forma que podamos integrar nuestros mensajes con los de otros módulos.

## Funciones de log

Esta librería define una serie de funciones habituales es sistemas de *logging*:
`debug()`, `info()`, `warning()`, `error()` y `critical()`.  Cada función tiene
un uso dependiendo de la gravedad del mensaje a emitir; estos niveles, de menor
a mayor severidad, se describen en la siguiente tabla:

| Nivel   | A usar para |
|:-------:|-------------|
| `DEBUG` | Información detallada, normalmente de interés sólo para diagnosticar problemas y encontrar errores.
| `INFO`  | Confirmación de que las cosas están funcionando como deben.
| `WARNING` | Ha pasado algo extraño, o en previsión de un problema futuro (Por ejemplo, "No queda mucho espacio libre en disco"). El programa sigue funcionando con normalidad |
| `ERROR` | Debido a un problema grave, el programa es incapaz de realizar parte de su trabajo |
| `CRITICAL` | Un error muy grave, el programa es incapaz de continuar ejecutándose |

Un ejemplo muy sencillo:

```python
import logging
logging.warning('¡Cuidado!')
logging.info('Mira que te lo dije...')
```

Si ejecutamos este código, veremos que solo se imprime el primer
mensaje:

```
WARNING:root:¡Cuidado!
```

Esto es porque el nivel por defecto es `WARNING`, es decir, que solo se emiten
los mensajes de ese nivel o superior. La idea de usar niveles es precisamente
para poder centrarnos en los mensajes que nos afectan en un determinado
momento.

El mensaje impreso incluye el nivel (`WARNING`) y la descripción que incluimos en la
llamada. También incluye una referencia a `root`, que se explicará más tarde.

El formato del mensaje también es modificable, si queremos.

## Configuración del sistema de logs

El sistema para configurar el sistema de _logs_ es muy potente, pero por eso
mismo también puede ser bastante complicado. La forma más sencilla de
configurarlo es con la función `basicConfig`, que nos permite crear un sistema
sencillo de _logs_ con una única llamada. Veamos un ejemplo para uno de los
casos más habituales, crear un _log_ usando un fichero de texto, definiendo el
fichero de destino y el nivel mínimo a partir del cual se tratarán los
mensajes:

```python
import logging

logging.basicConfig(filename='ejemplo.log', level=logging.DEBUG)
logging.debug('Este mensaje debería ir al log')
logging.info('Y este')
logging.warning('Y este también')
```

!!! note "Solo deberíamos realizar una llamada a `basicConfig`"
    
    Una vez realizado la llamada a `basicConfig`, las siquientes llamadas que
    se hagan a la función no tendrán efecto ninguno, porque el sistema ya está
    configurado.  Por ello es conveniente realizar la llamada lo más pronto
    posible, idealmente lo primero que debería hacer el programa.

    Podemos tener sistemas más complicados, incluso hay formas de cambiar
    dinámicamente el sistema de _logs_, pero son más complicadas y fuera
    del alcance de `basicConfig`.
    
Si abrimos el fichero deberíamos ver:

```
DEBUG:root:Este mensaje debería ir al log
INFO:root:Y este
WARNING:root:Y este también
```

Al configurar el nivel como `DEBUG` vemos que se han grabado todos los
mensajes. Si subiéramos el nivel a `ERROR`, no aparecería ninguno.


El formato por defecto es `severity:logger name:message`. Podemos cambiar
también el formato de los mensajes, usando el parámetro `format` en la llamada
a `basicConfig`:

```python
import logging

logging.basicConfig(
    filename='ejemplo.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
```

Hay otros sistema más potentes (y, por tanto, complicados) de configurar el
sistema de _logs_, en la documentación oficial podemos ver una sección completa
dirigida a [configuración del sistema de
logs](https://docs.python.org/3/library/logging.config.html).

Algunos de ellos son `dictConfig`, que nos permite definir el sistema
a partir de un diccionario, `fileConfig`, que usa un fichero de configuración
para
el mismo propósito, y `listen`, que nos permite arrancar un puerto de
comunicaciones, usando `socket`, y se queda a la espera de que cambiemos los
parámetos del sistema de _logs_. Por tanto, permite configurar los _logs_ en
tiempo de ejecución y sin parar el programa.


## Usar varios logs

Podemos definir más de un _logger_ (las funciones que hemos visto hasta ahora
usan el _logger_ por defecto, de nombre `root`), y usar sus nombres para
organizarlos en una jerarquía, usando puntos `.` como separadores, de forma
similar a como organizamos los paquetes o las carpetas. Los nombres pueden ser
lo que queramos, pero es una práctica habitual usar como nombre el del módulo:

```python
import logging
logger = logging.getLogger(__name__)
```

De esta forma el nombre del *logger* refleja la estructura de paquetes y
módulos que estemos usando, y es muy sencillo de usar.

También podemos usar diferentes manejadores para notificarnos, aparte de la
consola y el fichero de textos, tenemos notificaciones vía *sockets*, datagramas
UDP, envíos por correo, envíos a un demonio *syslog*, a un _buffer_ en memoria y, por
supuesto, la posibilidad de crear nuestros propios manejadores.

Al tener los _logs_ organizados en una estructura jerárquica, podemos tener
mucho más control; podemos por ejemplo guardar
todos los mensajes de `logs` que vayan al _logger_ `cuentas.ops` en una base de datos, mientras
que los que vayan al _logger_ `cuentas.usuarios` se muestren en la consola, pero solo para los
niveles de `ERROR` y `CRITICO`, y que todos los mensajes enviados a `cuentas`
(lo que incluiría los enviados a `cuentas.ops`, `cuentas.usuarios`,
`cuentas.trasacciones`, etc.) de nivel `CRITICO` se envién a una determinada
cuenta de correo.
