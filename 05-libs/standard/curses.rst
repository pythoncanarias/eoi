El módulo ``curses``
--------------------------------------

El módulo ``curses`` nos permite pintar en la pantalla, así como gestinar
eventos del teclado, en terminales basadas en texto. Estas terminales y sus
emulaciones disponen de operaciones como mover el cursor, hacer *scroll* de
pantalla, borrar áreas, usar colores, etc... 

Diferentes terminales usan diferentes funciones para cada una de estas
operaciones, ``curses`` nos permite usarlas con una interfaz común, de forma que
no tenemos que preocuparnos por estas diferencias.

Claro que, ¿por qué preocuparnos por esto? Seguro que en pleno siglo XXI, con
interfaces graficas, realidad virtual y teléfonos inteligentes no hay necesidad
ninguna de usar terminales de texto.

La vardad es que existen nichos donde hacer este tipo de cosas en la consola
siguen siendo de utilidad. Un ejemplo pueden ser dispositibos embebidos
corriendo unix pero sin el sistema de ventanas. Tenemos una parte de este curso
donde veremos IOT (*Internet of Things*) en el que se veran este tipo de
dispositinos. Otro entorno donde pueden herramientas como instaladores de
sistemas operativos o configuradores que deben ser ejecutados antes de que
exista soporte gráfico.  También puede ser de utilidad para acceder a maquinas
remotas, en las que la conexion sea lenta o, por las razones que sea, solo se
pueda acceder con *ssh* y una terminal.

Como usar ``curses``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La librería proporciona una funcionalidad muy básica, que permite al programador
trabajar con una abstrabción de la pantalla dividida en regiones diferentes, que
**no** se solapan. Se puede cambiar el contenido de cada "ventana", añadiendo,
borrando o modificando texto. La libreria no suministra ningun concepto de
interfaz de usuario de los que estamos acostumbrados, como botones, *checkboxes*
o cuadros de diálogo. Existen librerías externas que añaden estas
funcionalidades, como urwind_.

La libreria básicamente en un simple *wrapper* sobre una librería del mismo
nombre escrita en ``C``.

.. note:: La versión de Windows de python no incluye el módulo ``curses``, pero
   existe una version llamada UniCurses_, que se puede instalar como librería
   externa.

Antes de hacer nada, la libreria ``curses`` necesita ser inicializada. Para eso
usamos la función ``initscr()``, que determinará el tipo de terminal en uso,
llamará a cualquier código que el terminal necesite y creara variables y
estructuras internas que se usaran más adelante. Si tiene éxito, devolverá un
objeto que representa la pantalla completa de la terminal. Normalmente se
almacena este valor en una variable llamada ``stdsrc``, imitando el nombre de la
variable correcpondiente en el código en ``C``.

Veamos un primer ejemplo::

    import curses
    stdscr = curses.initscr()

Normalmente, al inicializar ``curses`` vas a querer deactivar el eco de las
pulsaciones de teclas en la pantalla, para que podamos leerlas nosotros y no
afecten directamente a la pantalla. Para hacer eso llamamos a la función
``noecho()``::

    curses.noecho()

También querras reaccionar ente pulsaciones de las techas, sin esperar a que el
usuario pulse la tecla *enter*. Esto se conoce como ``cbreak mode``. Puedes
activarlo con::

    curses.cbreak()

¿Qué pasa con las teclas especiales, como las teclas de cursor, *shitt*, *Home*,
etc. Las terminales suelen usar un código de escape seguido de una secuencia de
*bytes*. Puedes gestionar tu esas secuencias o sencillamente dejar que
``curses`` lo haga por tí, devolviendo directamente las pulsaciones de estas
teclas especiales en forma de valores predefinidos como ``curses.KEY_LEFT``.
Para eso, hay que llamar a la función ``keypad(bool)`` con el parámetro
``True``::

    stdscr.keypad(True)

PAra salir de la aplicación, deberemos desactivar todo lo que hemos activado,
así que normalmente acabaremos llamando al siguiente codigo::

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()

Y finalmente una llamada a ``endwin()`` para restaurar la terminal a su estado
original::

    curses.endwin()

Un problema muy habitual es que nuestro código tenga un problema en tiempo de
ejecución y muera sin haber restaurado la terminal a la normalidad. Puede pasar,
por ejemplo, que lo que escribimos no aparece en la pantalla precisamemte porque
hemos desactivado la opcion de *echo* y nunca volvimos a activarlo. La mayoria
de los desarolladores están de acuerdo en que teclear a ciegas no favorece la
depuración del código. En Python es muy fácil evitar esta situación usando la
funcion ``wrapper``. Su uso se explica con el siguiente ejemplo:

.. literalinclude:: curses/initialization.py

La función ``wrapper`` acepta como parámetro un objeto llamable (Una funcion,
por ejemplo, como en esta caso) y realiza primero todos los pasos de
inicialización explicados antes. Luego invoca el objeto pasado como parametro,
pero dentro de una estructura ``try..except``, para garantizar que tanto si la
ejecución termina con éxito como si se produce cualquier error, la terminal es
devuelta a su estado original. La excepción, si la hubo, se eleva de nuevo para
que podamos examinarla. De esta forma la terminal nunca queda en un estado
inutilizable, y siempre seremos capaces de leer los mensajes de error y trazas
de ejecución de cualquier error que se produzca.

Ejercicio: Copiar y ejecutar el emplo anterior. Comprobar que la excepcion se
muestra en pantalla sin problema. Arreglar el codigo y volver a ejecutar.

Windows and Pads
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Las *Windows* son la abstracción fundamental en ``curses``. Una ``window`` o
ventana representa un área rectangular de la pantalla, y soporta métodos para
mostrar texto, borrarlo, permitir la entrada de datos del usuario, entre otras
cosas.

El objeto ``stdscr``, que obtuvimos al llamar a ``initsrc``, es una ventana que
ocupa todo el area de la pantalla. Para algunos programas esto puyede ser
suficiente, pero otros pueden preferir dividir la pantalla en ventanas más
pequeñas, de forma que se puedad redibujar o limpiar de forma independiente. La
funcion ``newwin`` crea uHana nueva ventana, del tamaño y en la posición
inicada, y devueve la ventana recien creada::

    begin_x, begin_y = 20, 7
    height, width = 5, 40
    win = curses.newwin(height, width, begin_y, begin_x)

Hay una cosa muy importante a tener en cuenta, y es que ``curses`` usa un
sistema de coordenadas un tanto inusual. Las coordinadas siempre han de pasarse
en el orden **y, x**, en vez del habitual **x, y**. Además,las coordenadas
**0,0** se corresponden con la esquina superior izquierda de la pantalla (Fue
una decisión desafortunada que ahora es demasiado tarde para arreglar).

Podemos determinar el tamaño total de la pantalla con las variables (que
``initscr`` habrá inicializado) ``curses.LINES`` y ``curses.COLS``. Los rangos
válidos van, por tanto, desde ``(0, 0)`` hasta ``(curses.LINES - 1, curses.COLS
- 1)``.

La función ``refresh``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando llames a cualquier función que modifique una ventana o la pantalla, los
cambios no se reflejarán de forma automática. Para eso necesitamos llamar a
``refresh`` pasándole como parámetro la referencia a la pantalla.

Esto viene directamente de los lejanos tiempos en que las terminales se
conectaban a 300 baudios. Con una conexión tan lenta, tiene sentido acumular
todos los cambios producidos en la pantalla, ya que nos permite optimizarlos.
Por ejemplo, si escribimos en pantalla y luego la borramos, no hay necesidad de
ejecutar la primera orden porque nunca llega a ser visible.

Esto, en la práctica, no nos complica demasiado la vida. LA mayor parte de los
programas que usan una interfaz gráfica hacen un montón de cosas para,
eventualmente, volver a un estado donde esperan por la siguiente pulsación de
tecla, o algún tipo de entrada por parte del usuario. Lo único que hay que
hacer es asegurarse de que la pantalla se refresca justo antes de quedarse a ls
espera.

.. index:: pad (curses)

Un **Pad**  es un caso especial de ventana. Puede ser mayor que la pantalla, de
forma que solo se muestra una parte del pod en la misma en un determinado
momento. Para crear un *pad* se necesita el ancho y el alto, pero para poder
representarlo en pantalla hay que incluir las coordenadas de un area en la
pantalla donde se mostrará la parte del *pad* quie se verá::

    pad = curses.newpad(100, 100)
    # These loops fill the pad with letters; addch() is
    # explained in the next section
    for y in range(0, 99):
        for x in range(0, 99):
            pad.addch(y,x, ord('a') + (x*x+y*y) % 26)

    # Displays a section of the pad in the middle of the screen.
    # (0,0) : coordinate of upper-left corner of pad area to display.
    # (5,5) : coordinate of upper-left corner of window area to be filled
    #         with pad content.
    # (20, 75) : coordinate of lower-right corner of window area to be
    #          : filled with pad content.
    pad.refresh( 0,0, 5,5, 20,75)

La llamada a ``refresh()`` mostrará una parte del pad en el rectángulo en
la pantalla que va desde la coordenada (5, 5) a la (20, 75). La esquina
superior izquierda de esta seccion muestra la coordenada (0, 0) en el pad. Más
allá de esta diferencia, los *pads* actuan exactamente igual que cualqiuer
otra ventana, y tienen los mismos metodos.

Si tienes múltiples ventanas y *pads* en pantalla, la forma más eficiente de
refrescar consiste en llamar primero al método ``noutrefresh()`` de cada
ventana y al final llamar el método ``doupdate()`` de la pantalla. Eso
evita múltiples modificaciones en pantalla, ya que solo se redibuja 
una vez.

Mostrar texto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La forma más versatil para pintar texto en pantalla es usar el método ``addstr()`` 
de la ventana. Se puede usar de dos maneras:

1) Indicando la posición dentro de la ventana donde queremos escribir
   el texto, en ese caso la llamada es::

    window.addstr(y, x, str[, attr])

2) Sin indicar la posición, en cuyo caso se usara la posición actual
  del cursor. La *signatura* del método es, en este caso::

    window.addstr(str[, attr])
   
El parámetro ``attr`` permite modificar la forma en que se pintan los
caracteres, por ejemplo para usar una tipografia en negrita, texto subrayando,
en colores inversos, o (si la terminal lo soporta) en color. Todas estas
opciones se explicarán con más detalle en una sessión posterior.

Por otro lado, el método ``addch()`` nos permite posicionar un único caracter
(Una cadena de texto con longitud 1, un *bytestring* de longirud 1, o un entero,
que represente un caracter Ascii). Podemos, como en el caso anterior,
especificar la posicion u omitirla, en cuyo caso se pintara en la posicion
actual del cursor::

    window.addch(y, x, str[, attr])
    window.addch(str[, attr])

Se proporcionan ciertos caracteres especiales, codificados con valores
superiores a 255. Por ejemplo, ``ACS_PLMINUS`` codifica el simbolo (±) mientras
que ``ACS_ULCORNER`` es la esquina superior izquierda de una caja (util para
representar bordes), aunque seguramente sea más fácil usar directamente
caracteres unicode.

Como las ventanas recuerdan donde se quedó el cursor después de la última
operación, podemos omitir las coordenadas, como vimos antes. También podemos
mover la posición del cursor con el método ``move(y, x)``. Como algunos
terminales muestran la posición actual usando un cursor intermitente, puede que
te interese posicionar el cursor en alguna parte donde no sea molesto. Si
no estas interesado para nada en este tipo de cursor parpadeante, puedes
llamar a la función ``curs_set(False)`` para hacerlo invisible.

Atributos y color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La libreria permite representar el texto de diferentes formas, como por ejemplo
en texto inverso, o remarcando ciertas palabras. Para eso se usan los atributos
que vimos como ultimo parámetro de las llamadas ``addstr`` y ``addch``. 

Un atributo es sencillamente un número entero, donde cada *bit* representa
un atributo diferente. Aunque se puede intentar usar varios atributos a la
vez, ajustando diferentes *bits*, la verdad es que ``curses`` no garantiza
que todas las posibles combinaciones estén disponibles, ya que depende de las
capacidades de la terminal, asi que es mejor ajustarse en lo posible a los
atributos mas comunes que se sabe que funcionan, algunos de los cuales
veremos aquí.



An attribute is an integer, each bit representing a different attribute. You can
try to display text with multiple attribute bits set, but curses doesn’t
guarantee that all the possible combinations are available, or that they’re all
visually distinct. That depends on the ability of the terminal being used, so
it’s safest to stick to the most commonly available attributes, listed here.


===============  ==============================
Attributo        Descripcion
===============  ==============================
``A_BLINK``      Texto parpadeante
``A_BOLD``       Brillante o en negrita
``A_DIM``        Brillo medio
``A_REVERSE``    Inverso
``A_STANDOUT``   Resaltado
``A_UNDERLINE``  Subrayado
===============  ==============================

Por tanto, para mostear una línea de estado, por ejemplo, en vídeo inverso,
podriamos usar el siguiente código::

    stdscr.addstr(0, 0, "Current mode: Typing mode", curses.A_REVERSE)
    stdscr.refresh()

También podemos usar colores, si la terminal los soporta. Para poder usar los
colores, es necesario llamar a la funcion ``start_color()`` lo mas pronto
posible despues de haber inicializado ``curses`` con ``initscr``, para
inicializar el conjunto de valores por defecto. Una vez ejecutada, la función
``has_colors`` devolverá un *boolean* indicando si se pueden usar colores o no.

Los colores en ``curses`` siempre vienen en parejas, conteniendo en primer lugar
el color a usar para el texto y en segundo lugar el que se debe usar para el
fondo. Se puede examinar los valores definidos para cada valor usando la funcion
``color_pair()``. El siguiente ejemplo muestra un mensaje de texto con la pareja
de colores numero 1::

    stdscr.addstr("Linea de texto en color 1", curses.color_pair(1))
    stdscr.refresh()

Para poder definir un nuevo color (es decir, una pareja de dos colores, uno para
el texto y otro para el fondo), podemos llamar a la funcion ``init_pair(n, f,
b)`` cambia la definicion del color ``n`` a los valores ``f`` para el texto y
``b`` para el fondo. El color ``0`` siempre está predefinido para que se
corresponda a blanco sobre negro, y no se puede cambiar.

Hay 8 colores básicos, inicializados y numerados por ``start_color()``. Los valores son

==========  ================
Color num.  Nombre del color
==========  ================
0           Negro
1           Rojo
2           Verde
3           Amarillo
4           Azul
5           Magenta
6           Cian
7           Blanco
==========  ================

Tambien ``curses`` define constantes para cada uno de estos valores:
``curses.COLOR_BLACK``, ``curses.COLOR_RED``, ..., ``curses.WHITE``.

Por ejemplo, para definir el color 1 como una combinacion de rojo (1) sobre
negro (0), podemos hacer::

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

o::

    curses.init_pair(1, 1, 0)


Ejercicio: Hacer un programa con ``curses`` que muestre los colores en pantalla

Cuando se redefine una pareja de colores, todos los textos en pantalla mostrados
con ese color se actualizan automáticamemte. Algunas terminales tambien permiten
definir nuestros propios valores usando valores RGB. La consola de Linux,
desgraciadamemnte, no lo permite. La llamada a ``can_change_color()`` devolvera
un booleano indicando si esto es posible o no.

Entrada de usuario
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La libreria de C nos proporciona algunos mecanismos de entrad bastante simples,
pero el modulo python añade un control de entrada básico. Otras librerias, como
Urwind_ proporcionan una coleccion de controles o *widgets* mucho mas extensa.

Estas son las dos formas de leer una entrada desde una ventada:

1) El método ``getch()`` refresca la pantalla y queda a la espera de que el
usuario pulse alguna tecla. opcionalmente, puedes incluir unas coordenadas 
a las que el cursor debe moverse despues de la pausa.

2) El método ``getkey`` hace lo mismo, pero convierte el entero que representa a
la tecla pulsada al texto que se ha pulsado. Se
devulven los caracteres individuales en forma de cadenas de caracteres de
longitud 1, y las teclas especiales como por ejemplo las teclas de función
devuelven cadenas de texto mas largas conteniendo un texto como ``KEY_UP`` o
``^G``.

Podemos evitar la pausa usando el método ``nodelay``. Si ejecutamos
``nodelay(True)``, las dos llamadas ``getch`` y ``getkey`` se comportan a partir
de ese momento de forma no bloqueante. Para indicar que no se ha pulsado ninguna
tecla, `getch()`` devuelve el valor especial ``curses.ERR`` (-1) mientras que
``getkey()`` eleva una excepción. Tambien existe una funcion ``halfdelay``, que
se puede usar para definir un periodo de espera o *timeout* (en décimas de
segundo) sobre ``getch()``; si no se produce ninguna entrada durante ese tiempo,
se eleva la excepción.

Los numeros devueltos por ``getch`` son, si estan en el rango de 0 a 255,
representan los codigos ascii de la tecla pulsada. Si el valor fuera mayor de
255, entonces se trada de una tecla especial, como las flechas de movimiento,
página arriba, teclas de función, etc. Existen constantes para poder comparar
esos valores: ``curses.KEY_UPPAGE``, ``curses.KEY_HOME`` o ``curses.KEY_LEFT``.
El bucle princiapl del programa puede ser algo como esto::

    while True:
        c = stdscr.getch()
        if c == ord('p'):
            PrintDocument()
        elif c == ord('q'):
            break  # Exit the while loop
        elif c == curses.KEY_HOME:
            x = y = 0

El submódulo ``curses.ascii`` proporciona ciertas funciones que simplifican este
tipo de comparacions, de forma que sean las legibles. Tambien proporcion
funciones de conversión que aceptan ya sea nuemros enteros o cadenas de texto de
longitud 1 y devuelven el mismo tipo. Por ejempo, ``curses.ascii.ctrl()`` devuelve
el caracter de control correspondiente a su argumento.

El submódulo ``curses.textpad`` proporciona un control de tipo caja de texto,
para conseguir textos completos, y además soporta edición usando teclas de control tipo Emacs.
La clase ``TextBox`` tiene varios métodos que soportan edición con validación de
la entrada, incluyendo el limpiar o no los caracteres extra como espacios al
final o al principio. Este es un ejemplo de uso::

    import curses
    from curses.textpad import Textbox, rectangle

    def main(stdscr):
        stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")

        editwin = curses.newwin(5,30, 2,1)
        rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
        stdscr.refresh()

        box = Textbox(editwin)
        box.edit()  # Let the user edit until Ctrl-G is struck.
        message = box.gather()  # Get resulting contents


Para más información
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si estás interesado en estos temas, estos enlaces pueden ser de utilidad para
profundizar:

- `Writing Programs with NCURSES`: a lengthy tutorial for C programmers.

The ncurses man page

The ncurses FAQ

“Use curses… don’t swear”: video of a PyCon 2013 talk on controlling terminals using curses or Urwid.

“Console Applications with Urwid”: video of a PyCon CA 2012 talk demonstrating some applications written using Urwid.


from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)

.. _urwind: http://urwid.org/
.. _unicurses: https://pypi.org/project/UniCurses/
