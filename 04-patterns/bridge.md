## El patrón Bridge (Puente)

### PROPÓSITO

Desacopla una abstracción de su implementación, de modo que ambas puedan variar
de forma independiente.

### TAMBIÉN CONOCIDO COMO

Handle/Body (Manejador/Cuerpo)

### MOTIVACIÓN

Cuando una abstracción puede tener varias implementaciones posibles, la forma
más habitual de darles cabida es mediante la herencia. Una clase abstracta
define la interfaz de la abstracción, y las subclases concretas la implementan
de distintas formas. Pero este enfoque no siempre es lo bastante flexible. La
herencia liga una implementación a la abstracción de forma permanente, lo que
dificulta modificar, extender y reutilizar abstracciones e implementaciones de
forma independiente.

Pensemos en la implementación de una abstracción portable Ventana en un toolkit
de interfaces de usuario. Esta abstracción debería permitirnos escribir
aplicaciones que funcionen, por ejemplo, tanto en el Sistema de Ventanas X como
en Presentation Manager de IBM (PM). Mediante la herencia podríamos definir una
clase abstracta Ventana y subclases VentanaX y VentanaPM que implementen la
interfaz Ventana para las distintas plataformas. Pero este enfoque tiene dos
inconvenientes:

1. No es conveniente extender la abstracción Ventana para cubrir diferentes
   tipos de ventanas o nuevas plataformas. Imaginemos una subclase VentanaIcono,
   que especializa la abstracción Ventana para representar iconos. Para admitir
   este tipo de ventanas en ambas plataformas debemos implementar dos nuevas
   clases, VentanaIconoX y VentanaIconoPM. Y lo que es peor, tendremos que
   definir dos clases para cada tipo de ventana. Dar cabida a una tercera
   plataforma requeriría otra nueva subclase de Ventana para cada tipo de
   ventana.

2. Hace que el código sea dependiente de la plataforma. Cada vez que un cliente
   crea una ventana, se crea una clase concreta que tiene una determinada
   implementación. Por ejemplo, crear un objeto VentanaX liga la abstracción
   Ventana a la implementación para X Window, lo que vuelve al código del
   cliente dependiente de dicha implementación. A su vez, esto hace que sea más
   difícil portar el código cliente a otras plataformas.  Los clientes deberían
   ser capaces de crear una ventana sin someterse a una implementación concreta.
   Lo único que tendría que depender de la plataforma en la que se ejecuta la
   aplicación es la implementación de la ventana. Por tanto, el código cliente
   debería crear ventanas sin hacer mención a plataformas concretas.

El patrón Bridge resuelve estos problemas situando la abstracción Ventana y su
implementación en jerarquías de clases separadas. Hay una jerarquía de clases
para las interfaces de las ventanas (Ventana. VentanaIcono, VentanaFlotante) y
otra jerarquía aparte para las implementaciones específicas de cada plataforma,
teniendo a VentanaImp[36] como su raíz. Por ejemplo, la subclase VentanaImpX
proporciona una implementación basada en el sistema de ventanas X Window.



Todas las operaciones de las subclases de Ventana se implementan en términos de
operaciones abstractas de la interfaz VentanaImp. Esto desacopla las
abstracciones ventana de las diferentes implementaciones específicas de cada
plataforma. Nos referiremos a la relación entre Ventana y VentanaImp como un
puente (bridge), porque une a la abstracción con su implementación, permitiendo
que ambas varíen de forma independiente.



APLICABILIDAD

Usa el patrón Bridge cuando:

- quieres evitar un enlace permanente entre una abstracción y su implementación.
  Por ejemplo, cuando debe seleccionarse o cambiarse la implementación en tiempo
  de ejecución.

- tanto las abstracciones como sus implementaciones deberían ser extensibles
  mediante subclases. En este caso, el patrón Bridge permite combinar las
  diferentes abstracciones y sus implementaciones, y extenderlas
  independientemente.

- los cambios en la implementación de una abstracción no deberían tener impacto
  en los clientes: es decir, su código no tendría que ser recompilado.

- (C++) quiera ocultar completamente a los clientes la implementación de una
  abstracción. En C++ la representación de una clase es visible en la interfaz
  de la misma.

- tenga una proliferación de clases como la mostrada en el primer diagrama
  de la sección Motivación. Una jerarquía de clases tal pone de manifiesto la
  necesidad de dividir un objeto en dos partes. Rumbaugh usa el término
  “generalizaciones anidadas” [RBP+91j para referirse a dichas jerarquías de
  clases.

- quiera compartir una implementación entre varios objetos (tal vez usando
  un contador de referencias) y este hecho deba permanecer oculto al cliente. Un
  ejemplo sencillo es la clase String de Coplien [Cop92], donde varios objetos
  pueden compartir la misma representación de una cadena (StringRep).


### CONSECUENCIAS

El patrón Bridge tiene las siguientes consecuencias:

1. Desacopla la interfaz y la implementación. No une permanentemente una
   implementación a una interfaz, sino que la implementación puede configurarse
   en tiempo de ejecución. Incluso es posible que un objeto cambie su
   implementación en tiempo de ejecución.

  Desacoplar Abstracción e Implementador también elimina de la implementación
  dependencias de tiempo de compilación. Ahora, cambiar una clase ya no requiere
  recompilar la clase Abstracción y sus clientes. Esta propiedad es esencial
  cuando debemos asegurar la compatibilidad binaria entre distintas versiones de
  una biblioteca de clases.

  Además, este desacoplamiento potencia una división en capas que puede dar
  lugar a sistemas mejor estructurados. La parte de alto nivel de un sistema
  sólo tiene que conocer a Abstracción y a Implementador.

2. Mejora la extensibilidad. Podemos extender las jerarquías de Abstracción y de
   Implementador de forma independiente.

3. Oculta detalles de implementación a los clientes. Podemos aislar a los
   clientes de los detalles de implementación, como el compartimiento de objetos
   implementadores y el correspondiente mecanismo de conteo de referencias (si
   es que hay alguno).

### IMPLEMENTACIÓN

Al aplicar el patrón Bridge hemos de tener en cuenta las siguientes cuestiones
de implementación:

1. Un único implementador. En situaciones en las que sólo hay una
   implementación, no es necesario crear una clase abstracta Implementador. Éste
   es un caso degenerado del patrón Bridge, cuando hay una relación uno-a-uno
   entre Abstracción e Implementador. Sin embargo, esta separación sigue siendo
   útil cuando un cambio en la implementación de una clase no debe afectar a sus
   clientes existentes, es decir, que éstos no deberían tener que ser
   recompilados, sino sólo vueltos a enlazar.

   Carolan [Car89] usa la expresión “Gato de Cheshire” para describir dicha
   separación. En C++ se puede definir la interfaz de la clase Implementador en
   un fichero de cabecera privado que no se proporciona a los clientes. Esto
   permite ocultar por completo la implementación de la clase a los clientes.

2. Crear el objeto Implementador apropiado. ¿Cómo, cuándo y dónde se decide de
   qué clase Implementador se van a crear las instancias cuando hay más de una?
   Si Abstracción conoce a todas las clases ImplementadorConcreto, puede crear
   una instancia de una de ellas en su constructor; puede decidir de cuál
   basándose en los parámetros pasados a su constructor. Por ejemplo, si la
   clase de una colección admite varias implementaciones, la decisión puede
   estar basada en el tamaño de la colección. Se puede usar una lista enlazada
   para colecciones pequeñas y una tabla de dispersión (hash) para colecciones
   grandes.

   Otro enfoque consiste en elegir inicialmente una implementación
   predeterminada y cambiarla después en función de su uso. Si, por ejemplo, la
   colección crece más allá de un cierto límite, puede cambiar su implementación
   por otra que resulte más apropiada para un gran número de elementos.

   También es posible delegar totalmente la decisión en otro objeto. En el
   ejemplo de la Ventana/VentanaImp se puede introducir un objeto fábrica (véase
   el patrón Abstract Factory (79)) cuya única misión sea encapsular detalles de
   implementación. La fábrica sabe qué tipo de objeto VentanaImp crear para la
   plataforma en uso; una Ventana simplemente solicita una VentanaImp, y
   devuelve el tipo adecuado de ésta. Una ventaja de este enfoque es que
   Abstracción no está acoplada directamente a ninguna de las clases
   Implementador.


3. Compartimiento de Implementadores. Coplien ilustra cómo se puede usar el
   modismo de C++ Handle/Body (Manejador/Cuerpo) para compartir implementaciones
   entre varios objetos [Cop92]. El Cuerpo tiene un contador de referencias que
   es incrementado y disminuido por la clase Manejador. El código para asignar
   manejadores con cuerpos compartidos tiene la siguiente forma general:

    Manejador& Manejador::operator» (const Manejador& otro) {
        otro._cuerpo->Ref();
        _cuerpo->QuitarRef();
        if (_cuerpo->ContadorReferencias() == 0) {
            delete _cuerpo;
        }
        _cuerpo = otro._cuerpo;
        return *this;
    }

4. Uso de la herencia múltiple. Se puede utilizar herencia múltiple en C++ para
   combinar una interfaz con su implementación [Mar91j. Por ejemplo, una clase
   puede heredar públicamente de Abstracción y privadamente de
   ImplementadorConcreto. Pero dado que este enfoque se basa en la herencia
   estática, está asociando permanentemente una implementación a su interfaz.
   Por tanto, no se puede implementar un verdadero Bridge usando herencia
   estática, al menos no en C++.
