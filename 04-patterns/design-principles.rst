Principios de diseño
========================================================================


Diseñar para el cambio
------------------------------------------------------------------------

La clave para maximizar la reutilización reside diseñar los sistemas de
manera que puedan evolucionar.

Los patrones de diseño ayudan al asegurar que un sistema pueda cambiar
de formas concretas. Cada patrón deja que algún aspecto de la estructura
del sistema varíe independientemente de los otros, haciendo así al
sistema más robusto .

Algunas de las causas comunes de rediseño (junto con los patrones de
diseño que lo resuelven) son:

-  **Crear un objeto especificando su clase**. Especificar un nombre de
   clase al crear un objeto nos liga a una implementación concreta en
   vez de a una interfaz. Esto puede complicar los cambios futuros. Para
   evitarlo, debemos crear los objetos de forma indirecta: Ver *Abstract
   Factory*, *Factory Method* y *Prototype*.

-  **Dependencia de operaciones concretas**. Cuando especificamos una
   determinada operación, estamos ligándonos a una forma de satisfacer
   una petición. Evitando ligar las peticiones al código, hacemos más
   fácil cambiar el modo de satisfacer una petición, tanto en tiempo de
   compilación como en tiempo de ejecución. Ver *Chain of
   Responsibility*, *Command*.

-  **Dependencia de plataforma**. Las interfaces externas de los
   sistemas operativos y las interfaces de programación de aplicaciones
   (API) varían para las diferentes plataformas hardware y software. El
   software que depende de una plataforma concreta será más difícil de
   portar a otras plataformas. Incluso puede resultar difícil mantenerlo
   actualizado en su plataforma nativa. Por tanto, es importante diseñar
   nuestros sistemas de manera que se limiten sus dependencias de
   plataforma. Ver: *Abstract Factory*, *Bridge*.

-  **Dependencia de las representaciones o implementaciones**. Los
   clientes de un objeto que saben cómo se representa, se almacena, se
   localiza o se implementa, quizá deban ser modificados cuando cambie
   dicho objeto. Ocultar esta información a los clientes previene los
   cambios en cascada. Ver *Abstract Factory*, *Bridge*, *Memento* o
   *Proxy*.

-  **Dependencias algorítmicas**. Muchas veces los algoritmos se
   amplían, optimizan o sustituyen por otros durante el desarrollo y
   posterior reutilización. Los objetos que dependen de un algoritmo
   tendrán que cambiar cuando éste cambie. Por tanto, aquellos
   algoritmos que es probable que cambien deberían estar aislados. Ver:
   *Builder*, *Iterator*, *Strategy*, *Template Method* y *Visitor*.

-  **Fuerte acoplamiento**. Las clases que están fuertemente acopladas
   son difíciles de reutilizar por separado, puesto que dependen unas de
   otras. El fuerte acoplamiento lleva a sistemas monolíticos, en los
   que no se puede cambiar o quitar una clase sin entender y cambiar
   muchas otras. El sistema se convierte así en algo muy denso que
   resulta difícil de aprender, portar y mantener.

   El bajo acoplamiento aumenta la probabilidad de que una clase pueda
   ser reutilizada y de que un sistema pueda aprenderse, portarse,
   modificarse y extenderse más fácilmente. Los patrones de diseño hacen
   uso de técnicas como al acoplamiento abstracto y la estructuración en
   capas para promover sistemas escasamente acoplados. Ver: *Abstract
   Factory*, *Bridge*, *Chain of Responsibility*, *Command*, *Facade*,
   *Mediator* y *Observer*.

-  **Incapacidad para modificar clases**. Quizá necesitemos el código
   fuente y no lo tengamos. O tal vez cualquier cambio requeriría
   modificar muchas de las subclases existentes. Los patrones de diseño
   ofrecen formas de modificar las clases en tales circunstancias. Ver
   *Adapter*, *Decorator* y *Visitor*.


Bajo acoplamiento
------------------------------------------------------------------------

Otro principio básico de diseño es favorecer siempre un bajo
`acoplamiento <https://es.wikipedia.org/wiki/Acoplamiento_(inform%C3%A1tica)>`__
entre objetos que interactúan.

Se dice que dos objetos/módulos tiene un acoplamiento **bajo** o
**débil** cuando pueden interactuar, pero el conocimiento que tienen
cada uno del otro es pequeño.

El acoplamiento se relaciona de forma inversa con la
`cohesión <https://es.wikipedia.org/wiki/Cohesi%C3%B3n_(inform%C3%A1tica)>`__.
Un bajo acoplamiento normalmente se correlaciona con una alta cohesión,
y viceversa. Un bajo acoplamiento permite:

-  Mejorar la facilidad de mantenimiento.

-  Aumentar las posibilidades de reuso.

-  Evitar el efecto onda, en el cual un cambio un una parte de software
   afecta a otras.


Herencia frente a Composición
------------------------------------------------------------------------

Las dos técnicas más comunes para reutilizar funcionalidad en sistemas
orientados a objetos son la herencia de clases y la composición de
objetos.

La herencia de clases permite **definir una implementación en términos
de otra**. A esta forma de reutilización se la denomina reutilización de
caja blanca: con la herencia, las interioridades de las clases padres
suelen hacerse visibles a las subclases.

La composición de objetos es una alternativa a la herencia de clases.
Ahora, la nueva funcionalidad se obtiene **ensamblando o componiendo
objetos**. La composición de objetos requiere que los objetos a componer
tengan interfaces bien definidas. Este estilo de reutilización se
denomina reutilización de caja negra: los detalles internos no son
visibles. Los objetos aparecen como “cajas negras”.

Tanto la herencia como la composición tienen sus ventajas e
inconvenientes.

La herencia se define en tiempo de compilación y es sencilla de usar.
También hace que sea más fácil modificar una implementación que está
siendo reutilizada.

Pero la herencia de clases también tiene inconvenientes. En primer
lugar, no se pueden cambiar las implementaciones heredadas en tiempo de
ejecución. En segundo lugar, y lo que generalmente es peor, las clases
padre suelen definir al menos parte de la representación física de sus
subclases.

Como la herencia expone a una subclase los detalles de la implementación
de su padre, suele decirse que "la herencia rompe la encapsulación". La
implementación de una subclase esta tan vinculada a la de su padre que
cualquier cambio en la implementación del padre obliga a cambiar la
subclase.

La herencia también puede dificultar la reusabilidad. Si algún aspecto
de la implementación no resulta apropiada para un nuevo problema,
debemos reescribir o reemplazar la clase padre. Eso limita la
flexibilidad y la reutilización.

Una solución a esto es heredar sólo de clases abstractas, ya que éstas
normalmente tienen poca o ninguna implementación.

La composición de objetos se puede definir dinámicamente, en tiempo de
ejecución, a través de objetos que tienen referencias a otros objetos.
La composición requiere que los objetos tengan en cuenta las interfaces
de los otros, lo que a su vez requiere interfaces cuidadosamente
diseñadas que no impidan que un objeto sea utilizado por otros.

Pero hay una ventaja en esto: puesto que a los objetos se accede sólo a
través de sus interfaces, no se rompe su encapsulación. Cualquier objeto
puede ser reemplazado en tiempo de ejecución por otro del mismo tipo.

Además, como la implementación de un objeto se escribirá en términos de
interfaces de objetos, las dependencias de implementación son
notablemente menores.

La composición de objetos produce otro efecto en el diseño del sistema.
Optar por la composición de objetos frente a la herencia de clases ayuda
a mantener cada clase encapsulada y centrada en una sola tarea.

De esta manera, nuestras clases y jerarquías de clases permanecerán
pequeñas y será menos probable que se conviertan en monstruos
inmanejables.

Por otro lado, un diseño basado en la composición de objetos tendrá más
objetos (al tener menos clases), y el comportamiento del sistema
dependerá de sus relaciones en vez de estar definido en una clase.

Esto nos lleva a nuestro siguiente principio del diseño orientado a
objetos:

**Favorecer la composición de objetos frente a la herencia de clases.**

Aunque ambos sistemas tiene virtudes y defectos, la experiencia nos dice
que se suele abusar de la herencia como técnica de reutilización, y que
los diseños suelen ser más reutilizables (y más simples) si dependen más
de la composición de objetos.

En los patrones de diseño se verá la composición de objetos aplicada una
y otra vez.


Principios SOLID
------------------------------------------------------------------------

Los principios SOLID son un grupo de 5 principios, cuyas letras
iniciales forman la palabra SOLID. Al traducir los principios, por
supuesto, se pierde en algunos casos el juego de palabras, así que los
veremos por sus nombres en ingles.

-  **S**\ ingle Responsabiliy
-  **O**\ pen / Close
-  **L**\ iskov Sustitution
-  **I**\ nterface Segregation
-  **D**\ ependency Inversion

SINGLE RESPONSABILIY (S)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Principio de responsabilidad única: Cada clase debe tener una
responsabilidad única y exclusiva. Si hace la comida, no saca la basura.

OPEN / CLOSE (O)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Principio de abierto para extensión, pero cerrado para modificación: Las
clases deben estar abiertas para ampliación o extensión (Normalmente
mediante herencia), pero cerradas para modificación. Esto nos permite
usar las clases sin correr el riesgo de que cambien, a la vez que nos
permite ampliarlas o modificarlas sin perjudicar a otros usuarios

LISKOV SUSTITUTION (L)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Principio de sustitución de Liskov: Creado por Barbara Liskov, tiene una
bonita formulación matemática:

   Sea :math:`Φ(x)` una propiedad comprobable de todos los objetos
   :math:`x` de tipo :math:`T`. Entonces, :math:`Φ(y)` debería ser
   verdadera para todo objeto :math:`y` de tipo :math:`S` si :math:`S`
   es un subtipo o derivado de :math:`T`.

La verdad es que visto así, asusta un poco. Pero en realidad es una idea
sencilla; viene a decir que cualquier objeto que pertenezca a una clase,
tiene que poder ser sustituido por cualquier objeto que pertenezca a una
subclase.

Quizá un ejemplo sea la mejor forma de verlo: Si tenemos una clase
``Mamifero``, de la cual derivamos dos clases, ``Perro`` y ``Gato``,
entonces, en cualquier sitio donde estemos usando una variable de tipo
``Mamífero``, *deberíamos ser capaces de sustituir* esa variable por una
de tipo ``Gato``, o una de tipo ``Perro`` (o cualquier otro subtipo o
subtipos posibles, ``Delfín``, ``Ajolote``, etc.) sin que se produzca
ningún error. Es decir, que en las relaciones de herencia, si la clase
``B`` deriva de ``A``, entonces ``B`` es un tipo de ``A``.


Separación de interfaces (*Interface Segregation*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Principio de separación de interfaces: Es preferible tener muchas
interfaces, especificas para cada cliente, antes que una única interfaz
de uso general.

Inversión de dependencias (*Dependency Inversion*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Principio de inversión de dependencias, siempre se debe preferir
depender de una abstracción, antes que de una implementación.


El principio de Mínima Sorpresa
------------------------------------------------------------------------

El **Principio de la Mínima Sorpresa** (*Principle of least
astonishment*) se aplica al diseño de interfaces, diseño de *software* y
la ergonomía. Establece que cuando haya un conflicto o ambigüedad entre
dos elementos, el comportamiento ha de ser el que genere la mínima
sorpresa por parte del usuario.

Más informalmente, el principio establece que los componentes de un
sistema deben comportarse de la forma en que la mayoría de los usuarios
esperarían que se comportase; el comportamiento nunca debería asombrar o
sorprender al usuario.


El principio No Te Repitas (DRY - *Don’t Repeat Yourself*)
------------------------------------------------------------------------

El principio **No te repitas** (en inglés *Don’t Repeat Yourself* o DRY,
también conocido como Una vez y sólo una) promueve la reducción de la
duplicación, especialmente en computación. Según este principio toda
"pieza de información" nunca debería ser duplicada, debido a que esto
incrementa la dificultad en los cambios y evolución posterior, perjudica
la claridad y crea un espacio para posibles inconsistencias. El término
"pieza de información" es usado en un sentido muy amplio, abarcando:

-  Datos almacenados en una base de datos

-  Código fuente de un programa de software

-  Información textual o documentación

Cuando el principio DRY se aplica de forma eficiente, los cambios en
cualquier parte del proceso requieren cambios en un único lugar.


Fuente Única de Verdad (SSoT - *Single Source of Truth*)
------------------------------------------------------------------------

El principio de **fuente única fiable**, **Fuente única de verdad** o
*Single source of truth*, nos dice que debemos estructurar los modelos
de información, y los esquemas de datos asociados de forma que:

**para todo dato, este es gestionado (o editado) en un únido lugar**

Cualquier posible enlace o acceso al mismo (posiblemente en otras tablas
de una base de datos relacional) debe ser únicamente por referencia. Como
todas estas referencias se refieren a la "fuente de verdad", cuando se
actualice ese elemento el cambio se propagara a través de todo el
sistema, sin que exista posibilidad de que quede copias obsoletas en
algún lugar.

Cómo no usar los patrones de Diseño
------------------------------------------------------------------------

Los patrones de diseño **no deberían ser aplicados
indiscriminadamente**. Al contrario, requieren un proceso previo de
análisis y reflexión.

Muchas veces éstos consiguen la flexibilidad y la variabilidad a costa
de introducir niveles adicionales de indirección, y eso puede complicar
un diseño o disminuir el rendimiento.

Un patrón de diseño sólo debería ser aplicado **cuando la flexibilidad
que proporcione sea realmente necesaria**. Las secciones de
Consecuencias son las más valiosas a la hora de evaluar los beneficios y
los costes de un patrón.
