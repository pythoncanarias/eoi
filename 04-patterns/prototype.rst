El patrón Prototipo (*Prototype*)
------------------------------------------------------------------------

Proposito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Especifica los tipos de objetos a crear por medio de una instancia
prototípica, y crea nuevos objetos copiando dicho prototipo.

Motivación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A veces, necesitamos una copia exacta de un objeto. Por ejemplo,
supongamos que estamos escribiendo una aplicación para gestionar
recetas. Un usuario puede encontrar una receta de bizcocho y, después de
hacerle algunos cambios, quiere compartirla con otro usuario. Pero que
es lo que se debería compartir. ¿Queremos que, si el primer usuario
sigue experimentado esta receta, el segundo usuario vea también estos
cambios?  O debería la receta compartida mantenerse intacta, sin verse
alterado por posteriores experimentos sobre la original?

En otros casos, la creación de un objeto puede ser muy costosa en
términos de tiempo de CPU, memoria o cualquier otro recurso.

Ambos problemas pueden solucionarse usando el patrón Prototipo. LA idea
es permitir crear nuevos objetos en base a un objeto previamente
existente. Cada copia se denomina un **clon**, porque empieza como una
copia exacta del prototipo, aunque posteriormente su estado puede
cambiar, obviamente. El momento en que se haga el clonado es importante,
porque determina el contenido del clon.

Hay que hacer notar la diferencia entre una copia y una referencia. Con
una referencia el comportamiento es distinto; una alteración hecha por
el poseedor de una referencia es visible para el poseedor de otra
referencia. Con este patrón, cada clon es un nuevo objeto con vida
independiente de la del prototipo.

Implementación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En Python, es muy fácil crear una copia completa de un objeto, solo
tenemos que usar la función ``deepcopy`` definida en el módulo ``copy``
de la librería estándar.

Ejemplos de uso
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hay muchas aplicaciones y librerías de Python que usan este prototipo,
pero generalmente ni se menciona por estar incluida la capacidad de copia
total en la propia librería.

Una aplicación que usa prototipos es la `Python Visualization Toolkit
(VTK)`_ . VTK es sistema de procesamiento y representación de gráficos
en 3D. Usan el patrón Prototipo para crear clones de elementos
geométricos como puntos, líneas, etc.

Otro proyecto es `music21`_, un conjunto de utilidades para ayudar a
estudiantes e interesados a responder preguntas sobre música de forma
rápida y sencilla. Internamente usa prototipos para copiar notas
musicales y partituras.

Ejercicio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El siguiente fragmento de código funciona, pero es muy lento. Cada vez
que creamos un nuevo enemigo, el proceso de creación de la IA es
demasiado complejo y largo, y toma unos tres segundos (simulado en el
código con la llamada a ``time.sleep(3)``. Soluciona el problema usando
el patrón prototipo.

.. literalinclude:: problem-prototype.py
   :language: python


.. _music21: https://web.mit.edu/music21/
.. _Python Visualization Toolkit (VTK): https://vtk.org/
