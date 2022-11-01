---
title: Principios del diseño de patrones
---

## Principios de diseño de patrones

## Qué son los patrones de diseño

Una definición sencilla podria ser la siguiente:

> Un patrón de diseño es un modelo de solución para un determinado
> problema de diseño recurrente o habitual. El patron describe el problema
> y una aproximación general a como resolverlo.

## Historia

Si nos fijamos, el concepto no está limitado al desarrollo de software; se puede aplicar
a cualquie campo donde se puedan encontrar problemas recurrentes. De hecho
los primeros patrones de diseño surgen en la arquitectura, producto del arquitecto
Christopher Alexander, en el libro __The Timeless Way of Building__ y desarrollados 
posteriormente, junto con otros autores, en __A Pattern Language__.

En sus palabras, cada patron "__describe un problema que ocurre infinidad de veces en
nuestro entorno, así como la solución al mismo, de tal modo que podemos utilizar esta
solución un millón de veces más adelante sin tener que volver a pensarla otra vez.__"

## Design Patterns: Elements of Reusable Object-oriented Software

![Desing Patterns, by GoF](./img/design-patterns-book-cover.png)

A principios de la década de 1990 los patrones de diseño entraron en el mundo del desarrollo software con el libro **Design Patterns**, escrito por el llamado _Grupo de los cuatro_ (_Gang of Four_ o _GoF_), compuesto por Erich Gamma, Richard Helm, Ralph Johnson y John Vlissides.

En este libro seminal se recogen 23 patrones de diseño comunes.

Los patrones no son ni principios abstractos, ni soluciones especificas a un problema
particular; son algo intermedio. Un patrón define una _posible_ solución correcta para
un problema de diseño, dentro de un contexto dado, describiendo las cualidades 
invariantes de todas las soluciones.

## Características de los patrones

Para describir bien un patrón, un simple esquema gráfico, aunque es sin duda
útil e importante, no es suficiente. Necesitamos más información para poder
reutilizar el patrón.

Tenemos que reflejar también las decisiones tomadas, las
alternativas y sus posibles costos o inconvenientes. Los ejemplos también son
de mucha ayuda.

En el libro Paterns Design, la Banda de los Cuatro describía y utilizaba
la siguiente plantilla para todos sus patrones:

|   |   |   |
|------------------------|-----------|------------------------|
| Nombre y clasificación | Intención | También conocido como  |
| Motivación | Aplicación | Estructura |
| Participantes | Colaboraciones | Consecuencias |
| Implementación | Código de ejemplo | Usos conocidos |
| Patrones relacionados ||

### Nombre y clasificación

El __nombre del patrón es muy importante__. La idea es que contega la esencia del patrón
en una o dos palabras, para que se convierta en parte del vocabulario
de diseño. La clsificación se explica en la sigiente sección.

### Intención

Unos párrafos que respondan a las siguientes preguntas: ¿Qué hace este patrón? ¿Cuáles
serían las razones para usarlo? ¿Qué problema intenta resolver?

### También conocido como

Algunos patrones se conocen con varios nombres; si fuera el caso se
incluirían en esta sección.

### Motivación

Un escenario que muestra un problema de diseño y la manera en que el
patrón lo resuelve. Esto ayuda a entender las descripciones más
abstractas del patrón.

### Aplicación

¿En qué situaciones se puede aplicar este patrón? ¿Hay algún 
ejemplo de un diseño imperfecto que este patrón podría mejorar?
¿Como podemos identificar estas situaciones?

### Estructura

Una representación gráfica de las clases e interactuaciones del patrón.
Existen muchas notaciones gráficas para esto, pero las más usadas
actualente son OMT object-modeling technique (OMT) y UML (que deriva
en gran parte de OMT)

### Participantes

Las clases y objetos que participan en el diseño, así como sus responsabiidades.

### Collaboraciones

Describe la manera en que los participantes colaboran para llevar a cabo
sus responsabilidades.

### Consecuencias

¿Cómo consigue sus objetivos el patrón? ¿Cuáles son los compromisos
y consecuencias de usarlo? ¿Qué aspectos del sistema se pueden
modificar independientemente?

### Implementacion

¿Qué técnicas, _idioms_ y precauciones hay que considerar cuando
implementamos el patrón en un determinado lenguaje de programación.
¿Permite (o dificulta) el lenguaje algun aspecto del patrón?

### Código de ejempo

Fragmentos de código que ilustren como se puede implementar
el patrón. En el libro original se usaban ejemplos en C++
y en Smalltalk. Obviamente, nosotros usaremos Python.

### Usos conocidos

Ejemplo de uso de estos patrones en sistemas reales.

### Patrones relacionados

¿Qué otros patrones de diseño están relacionados con este? ¿Cuáles
son las diferencias más importantes? ¿Se puede usar este patrón junto
con otros? Si es así, ¿Con cuáles?

## Tipos de patrones de diseño

- De creación
- Estructurales
- De comportamiento

### De creación

Se utilizan cuando queremos crear objetos, pero el proceso de creación depende de 
desiciones y circunstancias que puede que no se conozcan a priori. Estos patrones normalmente resuelven el problema retrasando el proceso de creación de los objetos hasta el tiempo de ejecución.

Algunos Patrones de creación son: *`Singleton`*, *`Builder`*, *`Factory Method`*, *`Object Pool`* y *`Prototype`*.

### Estructurales

Sirven para organizar y conectar nuestras estructuras de datos, funciones y objetos. Normalmente
su busca que estas conexiones permitan interactuar pero reduciendo e incluso eliminanado el
acoplamiento, de forma que podamos cambiar las partes de un programa con un impacto mínimo.

Algunos patrones de este estilo son: *`Decorator`*, *`Adapter`*, *`Bridge`*, *`Facade`*, *`Flyweight`* y *`Proxy`*.

### De comportamiento. 

Fundamentalmente establecen unos comportamientos especificos, en los que nuestros
objetos juegan un papel predeterminado por el patrón para resolver un determinado
problema.

Algunos de ellos son: *`Strategy`*, *`Chain of Responsability`*, *`Command`*, *`Interpreter`*,
*`Iterator`*, *`Memoize`*, *`Observer`*, *`Pub/Sub`* y *`Visitor`*.

### Cómo resuelven los patrones los problemas de diseño

Los patrones de diseño resuelven muchos problemas del diseño OOP, y lo hacen de muchas formas diferentes. A continuación se muestran algunos de estos problemas y cómo los solucionan los patrones.

#### Encontrar los objetos adecuados

Lo más complicado del diseño orientado a objetos es descomponer un sistema en objetos. La tarea es difícil porque entran en juego muchos factores: encapsulación, granularidad, dependencia, flexibilidad, rendimiento, evolución, reutilización, etcétera, etcétera. Todos ellos influyen en la descomposición, muchas veces de formas opuestas.

Las metodologías orientadas a objetos permiten muchos enfoques diferentes.

1) Podemos escribir la descripción de un problema, extraer los nombres y verbos, y crear las correspondientes clases y operaciones. 

2) O podemos centrarnos en las colaboraciones y responsabilidades de nuestro sistema.

3) O modelar el mundo real y traducir al diseño los objetos encontrados durante el análisis.

Siempre habrá discrepancias sobre qué enfoque es mejor. Por ejemplo, el modelado estricto del mundo real conduce a un sistema que refleja la necesidad actual, pero no necesariamente las futuras.

Los patrones de diseño ayudan a identificar abstracciones menos obvias y los objetos que las expresan. Por ejemplo, los objetos que representan un proceso o algoritmo no tienen lugar en la naturaleza, y sin embargo son una parte crucial de los diseños flexibles.

El patrón *Strategy* describe cómo implementar familias intercambiables de algoritmos. El patrón *State* representa cada estado de una entidad como un objeto. Estos objetos rara vez se encuentran durante el análisis o incluso en las primeras etapas del diseño; son descubiertos más tarde, mientras se trata de hacer al diseño más flexible y reutilizable.

#### Determinar la granularidad

Los objetos pueden variar enormemente en tamaño y número. Pueden representar cualquier cosa, desde el hardware hasta aplicaciones completas. ¿Cómo decidir entonces qué debería ser un objeto?

Los patrones de diseño también se encargan de esta cuestión. El patrón *Facade* describe cómo representar subsistemas completos como objetos, y el patrón *Flyweight* cómo permitir un gran número de objetos de granularidad muy fina.

Otros patrones de diseño describen formas concretas de descomponer un objeto en otros más pequeños. Los patrones *Abstract Factory* y *Builder* producen objetos cuya única responsabilidad es crear otros objetos. El patrón *Visitor* y el *Command* dan lugar a objetos cuya única responsabilidad es implementar una petición en otro objeto o grupo de objetos.

#### Especificar las interfaces

Cada operación declarada por un objeto especifica el nombre de la operación, los objetos que toma como parámetros y el valor de retomo de la operación. Esto es lo que se conoce como la **signatura** de la operación. Al conjunto de todas las signaturas definidas por las operaciones de un objeto se le denomina la **interfaz** del objeto.

Dicha interfaz caracteriza al conjunto completo de peticiones que se pueden enviar al objeto. Cualquier petición que concuerde con una signatura de la interfaz puede ser enviada al objeto.

Las interfaces son fundamentales en los sistemas orientados a objetos. Los objetos sólo se conocen a través de su interfaz. No hay modo de saber nada de un objeto o pedirle que haga nada si no es a través de su interfaz. La interfaz de un objeto no dice nada acerca de su implementación —distintos objetos son libres de implementar las peticiones de forma diferente—. Eso significa que dos objetos con implementaciones completamente diferentes pueden tener interfaces idénticas.

Cuando se envía una petición a un objeto, la operación concreta que se ejecuta depende tanto de la petición como del objeto que la recibe. Objetos diferentes que soportan peticiones idénticas pueden tener distintas implementaciones de las operaciones que satisfacen esas peticiones. La asociación en tiempo de ejecución entre una petición a un objeto y una de sus operaciones es lo que se conoce como **enlace dinámico**.

El enlace dinámico significa que enviar una petición no nos liga a una implementación particular hasta el tiempo de ejecución. Por tanto, podemos escribir programas que esperen un objeto con una determinada interfaz, sabiendo que cualquier objeto que tenga la interfaz correcta aceptará la petición.

Más aún, el enlace dinámico nos permite sustituir objetos __en tiempo de ejecución__ por otros que tengan la misma interfaz. Esta capacidad de sustitución es lo que se conoce como **polimorfismo**, y es un concepto clave en los sistemas orientados a objetos. Permite que un cliente haga pocas suposiciones sobre otros objetos aparte de que permitan una interfaz determinada. El polimorfismo simplifica las definiciones de los clientes, desacopla unos objetos de otros y permite que varíen las relaciones entre ellos en tiempo de ejecución.

Los patrones de diseño ayudan a definir interfaces identificando sus elementos clave y los tipos de datos que se envían a la interfaz. Un patrón de diseño también puede decir lo
que __no debemos poner__ en la interfaz.

El patrón *Memento* es un buen ejemplo de esto. Dicho patrón describe cómo encapsular y guardar el estado interno de un objeto para que éste pueda volver a ese estado posteriormente.

El patrón estipula que los objetos deben definir dos interfaces: una restringida, que permita a los clientes albergar y copiar el estado a recordar, y otra protegida que sólo pueda usar el objeto original para almacenar y recuperar dicho estado.

Los patrones de diseño también especifican relaciones entre interfaces. En
concreto, muchas veces requieren que algunas clases tengan interfaces
parecidas, o imponen restricciones a las interfaces de algunas clases. Por
ejemplo, tanto el patrón *Decorator* como *Proxy* requieren que ciertas interfaces
sean idénticas en determinados objetos. En el patrón *Visitor*, la interfaz
Visitante debe reflejar todas las clases de objetos que pueden ser visitados.

#### Diseñar para el cambio

La clave para maximizar la reutilización reside diseñar los sistemas de manera que puedan evolucionar.

Los patrones de diseño ayudan al asegurar que un sistema pueda cambiar de
formas concretas. Cada patrón deja que algún aspecto de la 
estructura del sistema varíe independientemente de los otros, haciendo así al sistema más robusto .

Algunas de las causas comunes de rediseño (junto con los patrones de diseño que lo resuelven) son:

- **Crear un objeto especificando su clase**. Especificar un nombre de clase al crear un objeto nos liga a una implementación concreta en vez de a una interfaz. Esto puede complicar los cambios futuros. Para evitarlo, debemos crear los objetos de forma
indirecta: Ver *Abstract Factory*, *Factory Method* y *Prototype*.

- **Dependencia de operaciones concretas**. Cuando especificamos una
  determinada operación, estamos ligándonos a una forma de satisfacer una
  petición. Evitando ligar las peticiones al código, hacemos más fácil cambiar
  el modo de satisfacer una petición, tanto en tiempo de compilación como en
  tiempo de ejecución. Ver *Chain of Responsibility*, *Command*.

- **Dependencia de plataforma**. Las interfaces externas de los sistemas
  operativos y las interfaces de programación de aplicaciones (API) varían para
  las diferentes plataformas hardware y software. El software que depende de
  una plataforma concreta será más difícil de portar a otras plataformas.
  Incluso puede resultar difícil mantenerlo actualizado en su plataforma
  nativa. Por tanto, es importante diseñar nuestros sistemas de manera que se
  limiten sus dependencias de plataforma. Ver: *Abstract Factory*, *Bridge*.

- **Dependencia de las representaciones o implementaciones**. Los clientes de
  un objeto que saben cómo se representa, se almacena, se localiza o se
  implementa, quizá deban ser modificados cuando cambie dicho objeto. Ocultar
  esta información a los clientes previene los cambios en cascada. Ver
  *Abstract Factory*, *Bridge*, *Memento* o *Proxy*.

- **Dependencias algorítmicas**. Muchas veces los algoritmos se amplían,
  optimizan o sustituyen por otros durante el desarrollo y posterior
  reutilización. Los objetos que dependen de un algoritmo tendrán que cambiar
  cuando éste cambie. Por tanto, aquellos algoritmos que es probable que
  cambien deberían estar aislados. Ver: *Builder*, *Iterator*, *Strategy*,
  *Template Method* y *Visitor*.

- **Fuerte acoplamiento**. Las clases que están fuertemente acopladas son difíciles de reutilizar por separado, puesto que dependen unas de otras. El fuerte acoplamiento lleva a sistemas monolíticos, en los que no se puede cambiar o quitar una clase sin entender y cambiar muchas otras. El sistema se convierte así en algo muy denso que resulta difícil de aprender, portar y mantener.

  El bajo acoplamiento aumenta la probabilidad de que una clase pueda ser
  reutilizada y de que un sistema pueda aprenderse, portarse, modificarse y
  extenderse más fácilmente. Los patrones de diseño hacen uso de técnicas como
  al acoplamiento abstracto y la estructuración en capas para promover sistemas
  escasamente acoplados. Ver: *Abstract Factory*, *Bridge*, *Chain of
  Responsibility*, *Command*, *Facade*, *Mediator* y *Observer*.

- **Incapacidad para modificar clases**. Quizá necesitemos el código fuente y
  no lo tengamos. O tal vez cualquier cambio requeriría modificar muchas de las
  subclases existentes. Los patrones de diseño ofrecen formas de modificar las
  clases en tales circunstancias. Ver *Adapter*, *Decorator* y *Visitor*.


### Bajo acoplamiento

Otro principio básico de diseño es favorecer siempre un bajo
[acoplamiento](https://es.wikipedia.org/wiki/Acoplamiento_(inform%C3%A1tica))
entre objetos que interactuan.

Se dice que dos objetos/módulos tiene un acoplamiento **bajo** o
**débil** cuando pueden interactuar, pero el conocimiento que tienen
cada uno del otro es pequeño.

El acoplamiento se relaciona de forma inversa con la
[cohesión](https://es.wikipedia.org/wiki/Cohesi%C3%B3n_(inform%C3%A1tica)).
Un bajo acoplamiento normalmente se correlaciona con una alta cohesión,
y viceversa. Un bajo acoplamiento permite:

- Mejorar la facilidad de mantenimiento.

- Aumentar las posibilidades de reuso.

- Evitar el efecto onda, en el cual un cambio un una parte de software
  afecta a otras.

#### Herencia frente a Composición

Las dos técnicas más comunes para reutilizar funcionalidad en sistemas orientados a objetos son la herencia de clases y la composición de objetos. 

La herencia de clases permite __definir una implementación en términos de
otra__. A esta forma de reutilización se la denomina reutilización de caja
blanca: con la herencia, las interioridades de las clases padres suelen hacerse
visibles a las subclases.

La composición de objetos es una alternativa a la herencia de clases. Ahora, la
nueva funcionalidad se obtiene __ensamblando o componiendo objetos__. La
composición de objetos requiere que los objetos a componer tengan interfaces
bien definidas. Este estilo de reutilización se denomina reutilización de caja
negr: los detalles internos no son visibles. Los objetos aparecen como "cajas
negras".

Tanto la herencia como la composición tienen sus ventajas e inconvenientes.

La herencia se define en tiempo de compilación y es sencilla de usar. También
hace que sea más fácil modificar una implementación que está siendo
reutilizada. 

Pero la herencia de clases también tiene inconvenientes. En primer lugar, no se
pueden cambiar las implementaciones heredadas en tiempo de ejecución. En
segundo lugar, y lo que generalmente es peor, las clases padre suelen definir
al menos parte de la representación física de sus subclases.

Como la herencia expone a una subclase los detalles de la implementación de su padre, suele decirse que "la herencia rompe la encapsulación". La implementación de una subclase esta tan vinculada a la de su padre que cualquier cambio en la implementación del padre obliga a cambiar la subclase.

La herencia tambien puede dificultar la reusabilidad. Si algún aspecto de la
implementación no resulta apropiada para un nuevo problema, debemos reescribir
o reemplazar la clase padre. Eso limita la flexibilidad y la reutilización.

Una solución a esto es heredar sólo de clases abstractas, ya que éstas
normalmente tienen poca o ninguna implementación.

La composición de objetos se puede definir dinámicamente, en tiempo de
ejecución, a través de objetos que tienen referencias a otros objetos. La
composición requiere que los objetos tengan en cuenta las interfaces de los
otros, lo que a su vez requiere interfaces cuidadosamente diseñadas que no
impidan que un objeto sea utilizado por otros.

Pero hay una ventaja en esto: puesto que a los objetos se accede sólo a través de sus interfaces, no se rompe su encapsulación. Cualquier objeto puede ser reemplazado en tiempo de ejecución por otro del mismo tipo.

Además, como la implementación de un objeto se escribirá en términos de
interfaces de objetos, las dependencias de implementación son notablemente
menores.

La composición de objetos produce otro efecto en el diseño del sistema. Optar
por la composición de objetos frente a la herencia de clases ayuda a mantener
cada clase encapsulada y centrada en una sola tarea.

De esta manera, nuestras clases y jerarquías de clases permanecerán pequeñas y
será menos probable que se conviertan en monstruos inmanejables.

Por otro lado, un diseño basado en la composición de objetos tendrá más objetos
(al tener menos clases), y el comportamiento del sistema dependerá de sus
relaciones en vez de estar definido en una clase.

Esto nos lleva a nuestro siguiente principio del diseño orientado a objetos:

**Favorecer la composición de objetos frente a la herencia de clases.**

Aunque ambos sistemas tiene virtudes y defectos, la experiencia nos dice
que se suele abusar de la herencia como técnica de reutilización, y que 
los diseños suelen ser más reutilizables (y más simples) si dependen 
más de la composición de objetos.

En los patrones de diseño se verá la composición de objetos aplicada una y otra vez.

### Principios SOLID

Los principios SOLID son un grupo de 5 principios, cuyas letras iniciales forman la palabra SOLID. Al traducir 
los principios, por supuesto, se pierde el juego de palabras, asi que los veremos por sus nombres en ingles.

- **S**ingle Responsabiliy
- **O**pen / Close
- **L**iskov Sustitution
- **I**nterface Segregation
- **D**ependency Inversion

### SINGLE RESPONSABILIY (S)

Principio de responsabilidad única: Cada clase debe tener una responsabilidad única
y exclusiva. Si hace la comida, no saca la basura.
  

### OPEN / CLOSE (O)

Principio de abierto para extensión, pero cerrado para modificación: Las clases deben estar
abiertas para ampliación o extensión (Normalmente mediante herencia), pero cerradas para modificación. Esto 
nos permite usar las clases sin correr el riesgo de que cambien, a la vez que nos permite ampliarlas
o modificarlas sin perjudicar a otros usuarios
  

### LISKOV SUSTITUTION (L)

Principio de sustitución de Liskov: Creado por Barbara Liskov, tiene una bonita
formulación matemática:

> Sea $Φ(x)$ una propiedad comprobable de todos los
  objetos $x$ de tipo $T$.  Entonces, $Φ(y)$ debería ser verdadera para todo
  objeto $y$ de tipo $S$ si $S$ es un subtipo o derivado de $T$.

La verdad es que visto así, asusta un poco. Pero en realidad es una idea
sencilla; viene a decir que cualquier objeto que pertenezca a una clase, tiene
que poder ser sustuido por cualquier objeto que pertenezca a una subclase.
  

Quiza un ejemplo sea la mejor forma de verlo: Si tenemos una clase
``Mamiferos``, de la cual derivamos dos clases, ``Perros`` y ``Gatos``,
entonces, en cualquier sitio donde estemos usando una variable de tipo
``Mamífero``, _deberíamos ser capaces de sustituir_ esa variable por una de
tipo ``Gatos``, o una de tipo ``Perros`` (o cualquier otro subtipo o subtipos
posibles, ``Delfines``, ``Dalmatas``,...) sin que se produzca ningun error.  Es
decir, que en las relaciones de herencia, si la clase `B` deriva de `A`,
entonces `B` es un tipo de `A`.
  

### INTERFACE SEGREGATION

Principio de separación de interfaces: Es preferible tener muchas interfaces,
especificas para cada cliente, antes que una unica interfaz de uso general.

### DEPENDENCY INVERSION

Principio de inversión de dependencias, siempre se debe preferir depender de
una abstrabción, antes que de una implementacion.

### El principip de Mínima Sorpresa

El __Principio de la Mínima Sorpresa__ (*Principle of least astonishment*) se
aplica al diseño de interfaces, diseño de *software* y la ergonomía. Establece
que cuando haya un conflicto o ambigüedad entre dos elementos, el
comportamiento ha de ser el que genere la mínima sorpresa por parte del
usuario.

Más informalmente, el principio establece que los componentes de un sistema
deben comportarwse de la forma en que la mayoría de los usuarios esperarían que
se comportase; el comportamiento nunca debería asombrar o sorprender al
usuario.

### El principio No Te Repitas

El principio __No te repitas__ (en inglés *Don't Repeat Yourself* o DRY,
también conocido como Una vez y sólo una) promueve la reducción de la
duplicación, especialmente en computación. Según este principio toda "pieza de
información" nunca debería ser duplicada, debido a que esto incrementa la
dificultad en los cambios y evolución posterior, perjudica la claridad y crea
un espacio para posibles inconsistencias. Los términos "pieza de información"
son usados en un sentido amplio, abarcando:

- Datos almacenados en una base de datos

- Código fuente de un programa de software

- Información textual o documentación

Cuando el principio DRY se aplica de forma eficiente, los cambios en cualquier
parte del proceso requieren cambios en un único lugar.

### Fuente Única de Verdad

El principio de __Fuente única de verdad__, (*Single source of truth* o SSOT) o
__fuente única fiable__ nos dice que debemos estructurar los modelos de
información, y los esquemas de detos asociados de forma que:

**para todo dato, este es gestionado (o editado) en un únido lugar**

Cualquier posible enlace o acceso al mismo (posiblemente en otras tablas de una
base de datos relacional) son unicamente por referencia. Como todas estas
referencias se refieren a la "fuente de verdad", cuando se actualize ese
elemento el cambio se propagara a traves de todo el sistema, sin que exista
posibilidad de que quede copias obsoletas en algún lugar.

## Cómo no usar los patrones de Diseño

Los patrones de diseño **no deberían ser aplicados indiscriminadamente**.

Muchas veces éstos consiguen la flexibilidad y la variabilidad a costa de
introducir niveles adicionales de indirección, y eso puede complicar un diseño
o disminuir el rendimiento.

Un patrón de diseño sólo debería ser aplicado **cuando la flexibilidad que
proporcione sea realmente necesaria**. Las secciones de Consecuencias son las
más valiosas a la hora de evaluar los beneficios y los costes de un patrón.
