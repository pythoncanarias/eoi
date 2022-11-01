## El patrón prototipo

### Proposito

Especifica los tipos de objetos a crear por medio de una instancia prototípica,
y crea nuevos objetos copiando dicho prototipo.

### Motivación

A veces, necesitamos una copia exacta de un objeto. Por ejemplo, supongamos
que estamos escribiendo una aplicacion para gestionar recetas. Un usuario
puede encontrar una receta de bizcocho y, después de hacerle algunos cambios, 
quiere compartirla con otro usuario. Pero que es lo que se deberia
compartir. ¿Queremos que si el primer usuario sigue experimentado esta
receta, el segundo usuario vea tambien estos cambios? No deberia la receta
compartida mantenerse intacta, sin verse alterado por posteriores experimentos
sobre la original? 

En otros casos, la creación de un objeto puede ser muy costosa
en terminos de tiempo de CPU, memoria o cualquier otro recurso.

Ambos problemas pueden solucionarse usando el patrón Prototipo. LA idea
es permitir crear nuevos objetos en base a un objeto previamente existente.
Cada copia se denomina un __clon__, porque empieza como una copia 
exacta del prototipo, aunque posteriormente su estado puede cambiar, obviamente.
El momento en que se haga el clonado es importante, porque determina el
contenido del clon.

Hay que hacer notar la diferencia entre una copia y una referencia.
Con una referencia el comportamiento es distinto; una alteración hecha
por el poseedor de una referencia es visible para el poseedor de otra
referencia. Con este patron, cada clon es un nuevo objeto con vida independiente
de la del prototipo.

Implementacion

En python, es muy facil crear una copia completa de un objeto, solo
tenemos que usar la funcion `deepcopy` definida en el módulo `copy`
de la librería estándar.

### Ejemplos de uso

Hay muchas aplicaciones y librerías de Python que usan este prototipo, pero
generalmente ni se menciona por estar incuida la capacidad de copia
total en la propia librería.

Una aplicación que usa prototipos es la [Python Visualization Toolkit
(VTK)](https://vtk.org/). VTK es sistema de precesamiento y representacion de
gráficos en 3D. Usan el patrón Prototipo para crear clones de elementos
geométricos como puntos, líneas, etc.

Otro proyecto es [music21](https://web.mit.edu/music21/), un conjunto de
utilidades para ayudar a estudiantes e interesados a responder preguntas
sobre música de forma rápida y sencilla. Internamente usa prototipos para
copiar notas musicales y partituras.

**Ejercicio**

El siguiente fragmento de codigo funciona, pero es muy lento. Cada vez
que creamos un nuevo enemigo, el proceso de creacion de la IA es demasiado
complejo y largo, y toma unos tres segundos (simulado en el codigo con
la llamada a `time.sleep(3)`. Soluciona el problema usando el patron 
prototipo.
