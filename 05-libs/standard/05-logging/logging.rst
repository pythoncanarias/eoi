``logging``: Registro de actividad
==================================

El módulo ``logging`` define un sistema flexible y homogeneo
para añadir un sistema de registro de eventos o :term:log a
nuestras aplicaciones o librerías. Crear un log es relativamente
fácil, pero la ventaja de usar el API definido en las
librerías estándar es que todos los módulos pueden participar
en un log común, de forma que podamos integrar nuestros mensajes
con los de otros módulos de terceros.

El módulo define una serie de funciones habituales es sistemas
de *logging*: ``debug()``, ``info()``, ``warning()``, ``error()`` y ``critical()``. Cada función tiene un uso dependiendo de la gravedad del
mensaje a emitir; estos niveles, de menor a mayor severidad,
se describen en la siguiente tabla:

======== ===============================================
Nivel    A usar para
======== ===============================================
DEBUG    Información muy detallada, normalmente de
         interes sólo para diagnosticar problemas
         y encontrar errores.

INFO     Confirmación de que las cosas están funcionando
         como deben.

WARNING  Una indicación de que ha pasado algo extraño, o
         en previsión de algún problema futuro (Por
         ejemplo, "No queda mucho espacio libre en
         disco"). El programa sigue funcionando con
         normalidad.

ERROR    Debido a un problema más grave, el programa
         no has sido capaz de realizar una parte
         de su trabajo.

CRITICAL Un error muy grave, indica que el programa es
         incapaz de continuar ejecutándose.
======== ===============================================

Un ejemplo muy sencillo::

    import logging
    logging.warning('¡Cuidado!') # el mensaje sale por pantall
    logging.info('Mira que te lo dije...') # este no aparecerá

Si ejecutamos este código, veremos que solo se imprime
el primer mensaje::

    WARNING:root:¡Cuidado!

Esto es porque el nivel por defecto es ``WARNING``, es decir, que solo
se emiten los mensajes de ese nivel o superior. La idea de usar
niveles es precisamente para poder centrarnos en los mensajes que nos
afectan en un determinado momento.

El mensaje impreso incluye el nivel y la descripción que
incluimos en la llamada. También incluye una referencia
a ``root``, que se explicará más tarde. El formato del
mensaje también es modificable, si queremos.

Lo más habitual es crear el log usando un ficharo de texto::

    import logging
    logging.basicConfig(filename='ejemplo.log', level=logging.DEBUG)
    logging.debug('Este mensaje debería ir al log')
    logging.info('Y este')
    logging.warning('Y este también')

Si abrimos el fichero deberíamos ver::

    DEBUG:root:Este mensaje debería ir al log
    INFO:root:Y este
    WARNING:root:Y este también

Al configurar el nivel como ``DEBUG`` vemos que se han grabado todos
los mensajes. Si subieramos a ``ERROR``, no aparecería ninguno.

El formato por defecto es ``severity:logger name:message``. Podemos
cambiar también el formato de los mensajes, usando el parámetro
``format`` en la llamada a ``basicConfig``::

     import logging

    logging.basicConfig(
        filename='ejemplo.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

Podemos definir distintas instancias de loggers (las funciones que
hemos visto hasta ahora usan el logger por defecto, de nombre
``root``), y usar sus nombres para organizarlos en una jerarquía,
usando puntos ``.`` como separadores, de forma similar a como
organizamos los paquetes. Los nombres pueden ser lo que queramos, pero
es una práctica habitual usar como nombre el del módulo::

    import logging
    logger = logging.getLogger(__name__)

De esta forma el nombre del logger refleja la estructura de paquetes
y módulos que estemos usando, y es muy sencillo de usar.

Tambien podemos usar diferentes gestionadores para notificarnos,
aparte de la consola y el fichero de textos, tenemos notificacines vía
sockets, datagramas UDP, por correo, envios a un demonio syslog,  a un
buffer en memoria y, por supuesto, la posibilidad de crear nuestros
propios manejadores.
