Introducción a Django
========================================================================

.. figure:: ./img/django.png
   :alt: Django

   Django

Qué es Django
------------------------------------------------------------------------

**Django** es un *framework* para el desarrollo de aplicaciones web,
gratuito y de código abierto (open source) escrito en Python.

Un **framework**, desde el punto de vista informático, es un marco o
estructura conceptual y tecnológica, definida normalmente mediante
módulos concretos de software, y que sirve de base para el desarrollo de
un *tipo* de software.

Suele incluir programas, librerías y otras herramientas para ayudaa a
desarrollar y unir los diferentes componentes de un proyecto.

Django, al ser un framework *para desarrollo web*, nos ayudará a
desarrollar ese tipo de aplicaciones, aplicaciones web. Seria absurdo
intentar usarlo para el desarrollo de una aplicación de terminal, una
app movil, o un sistema operativo.

Diferencia entre librerías y frameworks
------------------------------------------------------------------------

A primera vista, pueden parecer muy similares, al fin y al cabo son,
como una libreria de software, solo un conjunto de módulos que podemos
empezar a usar tan pronto como lo instalemos. De hecho, veremos que
instalaremos Django exactamente igual que cualquier otra librerîa.

La principal diferencia radica en *como se usa* y *quien mantiene el
control*.

-  En el caso de una librería, tú mantienes el control, y tu realiza
   llamadas a la librería cuando estimas conveniente.

-  Con un *framework*, la situación se invierte, y es el propio
   *framework* el que llama a las funciones que tu escribes. El
   framework es el que mantiene el control.

Esto se puede conseguir por la restriccion que el propio framework ha
hecho sobre el **dominio**, es decir, sobre el área de problemas que
soluciona. Decidir que solo te vas a encargar de solucionar el hacer una
web, o que solo vas a dedicar a hacer juegos (para un framework de
desarrollo de juegos) simplifica el framework, por varias razones:

-  El esquema principal o esqueleto de la aplicación ya viene
   determinado. Todas las aplicaciones web se estructuran de una forma
   parecida, de la misma forma que todos los juegos tienen un bucle
   interno que es basicamente igual para todos: Leer controles ->
   modificar estado del juego -> representar estado del juego ->
   repetir.

-  En cada dominio hay una serie de problemas comunes, que se pueden
   resolver e implementar en el *framework* porque hay una probabilidad
   muy alta de que te vayas a encontrar con ese problema, por ejemplo,
   en desarrollo web, gestionar todo el proceso de *login* y *logout*,
   manejo de sesiones, etc.

-  Al restringir las capacidades, puedes presuponer o dar por fijas
   determinadas condiciones, asi como el entorno de ejecución.

-  Elimina muchisimos problemas de los que no te vas a tener que
   preocupar. Ningun framework web se tiene que preocupar de los *frames
   por segundo* que pueda dar.

Instalar django
------------------------------------------------------------------------

Como se comentó antes, instalar django es como instalar cualquier otra
libreria, usando pip.

Vamos a verificar primero la versión de Python que tenemos instalada. Es
recomendable tener Python 3.7 o superior::

    python -V

Si todo está bien, podemos instalar Django::

    pip install django

Si no funciona, prueba con:

    pip3 install django

.. note:: En el resto de la documentacion, solo se hará referencia
   a ``python`` y ``pip``, sin el 3 después. Si lo tienes instalado como
   ``python3`` o ``pip3`` haz el reajuste correspondiente.

Saldra un monton de texto mientras se instala Django y sus dependencias.

Podemos comprobar que django esta corectamente instalando simplemente
intentado importarlo. Si no da error, es que esta instalado::

    $ python -c "import django"

.. note:: La opcion ``-c`` de Python nos permite ejecutar el código python
   que le pasamos como parámetro y luego salir del interprete.

Incluso podremos comprobar la versión instalada con la función
``get_version()``::

    $ python -c "import django; print(django.get_version())"

Deberia devolver algo como esto::

    3.0.5


Nuestra primera aplicación Django: Hola, Mundo
------------------------------------------------------------------------

Es una tradición en el mundo de la informática, a la hora de aprender
un nuevo lenguaje, librería o *framework*, empezar desarrollando la
versión más sencilla que se pueda implementar de un programa que haga
algo. Esta tradición se remonta al famoso libro sobre el lenguaje C,
escrito por Kernighan y Ritchie.

Esto nos permite eliminar toda la complejidad adicional que pueda tener
el lenguaje y centrarnos en una única funcionalidad relativamente
trivial; tradicionalmente, escribir o representar de algún modo
el mensaje «Hola, mundo» (Hello, World).

Además, el programa «hola, mundo» nos permite hacernos una idea rápida
de la sintaxis, la semántica y las particularidades de lo que quiera que
estás aprendiendo.

Para poder trabajar con Django, debemos de hacerlo fuera de Jupyter.
Trabajaremos desde la consola y desde un edior de textos. El primer paso
es abrir la consola en el directorio de trabajo que queremos y comprobar
que tenemos la version de Python correcta instalada y disponible

Para verificar que Django está instalado haremos::

    $ python -c "import django"

De nuevo, la ausencia de mensajes de error es buena noticia. Si diera un
error, instalar django como pip::

    $ pip install django

Ahora, el siguiente paso será crear nuestra aplicación. Django, al
instalarse, he añadido una utilidad muy cómoda que permite crear una
aplicación mínima al toque. Podemos ejecutar esta utilidad haciendo::

    $ django-admin

Si todo ha ido bien, deberíamos ver un resultado como este, en el que la
utilidad nos señala amablemente que no le hemos indicado ninguna acción
a ejecutar, y a continuacón, lista las acciones que podemos ejecutar::

    $ django-admin
 
    Type 'django-admin help <subcommand>' for help on a specific subcommand.
 
    Available subcommands:
 
    [django]
        check
        compilemessages
        createcachetable
        dbshell
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
        makemigrations
        migrate
        runserver
        sendtestemail
        shell
        showmigrations
        sqlflush
        sqlmigrate
        sqlsequencereset
        squashmigrations
        startapp
        startproject
        test
        testserver

De todas esas acciones que podemos hacer, la que nos interesa ahora
mismo es ``startproject``. Esta acción es la que crea una aplicación
básica, o como se dice a veces, el *esqueleto* de una aplicación.

Antes de ejecutar la acción, tenemos que pensar el nombre de la misma,
ya que va a crear un directorio con ese mismo nombre. En este curso
vamos a crear varias aplicaciones diferentes, asi que esta la vamos a
crear con el nombre ``hola``.

Para crear la aplicación, por tanto, ejecutamos::

    $ django-admin startprojec hola

Como es habitual, la falta de mensajes de error es indocativo de que
todo ha ido bien. El resultado de la ejecución es que se ha creado una
carpeta nueva con el nombre de la aplicacion, ‘hola’ en este caso
(habria dado un error si ya existiera una carpeta con ese nombre; esto
es así para evitar destruir un proyecto ya existente por descuido.

**Ejercicio**: Intentar crear nuevamente la aplicación ``hola``.
Describir lo que pasa.

Examinado la aplicacion ``hola``
------------------------------------------------------------------------

Vamos a ver los contenidos que hay en la carpeta recien creada.

Como podemos intuir de lo visto en los temas anteriores, Django es
bastante potente y ámplio. no puede ser de otra manera, ya que el
desarrollo web se ha convertido en una fusión de multiples tecnologías.

Para nuestra versión de Hola, mundo, nos contentaremos con una única
página web,con el texto “hola, mundo”.

Mapeo de urls
------------------------------------------------------------------------

Definicion de vista
------------------------------------------------------------------------
