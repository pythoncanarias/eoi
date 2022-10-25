pdb
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El módulo ``pdb`` define un debugger interactivo para programas
Python.

Soporta *breakpoints* y *breakpoints* condicionales,
ejecución paso a paso, inspección de la traza, listado del
codigo fuente y evaluación de código Python arbitrario en el
contexto del programa.

También puede ser llamada bajo el control del programa.

Podemos invocarlo desde la línea de comandos con::

    $ pdb <script.py>

Cuando se sjecuta el debugger, el prompt cambia a ``(Pdb)``. Podemos
consultar una breve ayuda pulsando ``help``. Los comandos más útiles
puende ser:

- h(elp)

Sin argumentosm imprime la lista de posibles
ordener. Si la pasamos una orden como
parámetro, ampliará la información sobre
el mismo.

- w(here)

Imprime la traza, con la actuividad más reciente al final.
Una flecha indica en entorno actual

- s(tep)

Ejecuta la línea actual, parandose en la primera
ocasión que pueda: O bien en la primera línea
de una función que se ha llamado o en la siguiente
línea.

- n(ext)

Continua la ejecución hasta que se alcanza la siguiente
línea en el bloque actual  o retorne de una función. La
diferencia con ``step`` es que ``step`` entrará dentro
del cuerpo de una función, mientras que next la ejecutará
y seguirá hasta la siguiente línea.

- r(eturn)

Ejecuta el resto de la función y retorna.

- c(ont(inue))

Continua la ejecución. Solo se para si encuentra un
*breakpoint* o si termina el programa.

- l(ist) [first[, last]]

Lista el código fuente.


Podemos usar el debugger desde dentro del programa; lo habitual es
ejecuta la siguiente línea antes de llegar al código problemático::

    import pdb; pdb.set_trace()

Nota: Si planeas usar mucho el debugger, te recomiendo que instales
la librería externa [ipdb](https://pypi.org/project/ipdb/)

Esto arrancará en modo debugger justo en esa línea. A partir de hay se
puede avanzar a traves del código con ``s`` o ``n``, o seguir la
ejecucion con ``c``.

Hay muchas más ordenes y usos disponibles. Consulta la documentación
oficial de Python para ver todos las opciones.

