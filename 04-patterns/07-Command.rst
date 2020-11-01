El patrón Command
-----------------

.. index:: command (Pattern)

El patrón **Command** es un patrón de tipo conductual, en el que se usa un objeto para encapsular
toda la información necesaria que permita ejecutar una acción en un momento posterior. La
información que almacena suele incluir, entre otras cosas:

- Un nombre
- Objeto o instancia al que pertenece el método
- Parametros a incluir en la invocación del método

Veamos un ejemplo: consideremos el caso de un software de instalacion de tipo *wizard*, en el que, a
traves de una serie de fases o pantallas se van capturando todas las preferencias del usuario. El
usuario puede avanzar o retrodecer a gusto por las distintas fases, cambiando sus decisiones un
cualquier momento. Solo cuando se llega al final y el usuario da su aprobacion, se ejecutan todos
los pasos que conducen a la instalacion del programa.

Esto se puede resolver muy bien usando este patrón. Una posible solución podria ser crear al
principio de la ejecución del instalador un objeto *Command* que almacene toda la información
relativa a las preferencias del usuario. Las preferencias se van guardando y actualizando en este
objeto. Cuando el usuario finalmente pulse "Instalar" el programa simplemente se invoca el método
`execute` del objeto, que realiza la instalacion acorde a las preferencias que tiene almacenadas.
Hemos encapsulado toda la informacion necesaria para realiza una acción dentro de un objeto
*Command*, que puede ser posteriormente ejecutado.

Otro ejemplo podria ser un spooler de impresión. El spooler puede implementarse con un objeto
`Command` que almacena la información pertinente, como el tamaño de la página (A4, por ejemplo)
si debe imprimirse apaisada u horizontal, tipo de papel, etc. Una vez que el usuario manda a imprimir
un documento, cuando el spooler quiera imprimirlo solo tiene que llamar al método `execute()` del
objeto *Command* y el documento se imprime con las preferencias predefinidas.

Ventajas y desventajas
~~~~~~~~~~~~~~~~~~~~~~

Entre las ventajas de este patrón se pueden destacar las siguientes:

- Desacopla totalmente a las clases que invoca la operacion de los objetos
  que saben como ejecutar la operación

- Es fácil componer una sequencia de *Comands* y tratarlos como a cualquier
  otra estructura de datos, por ejemplo, ponerlos en una cola.

- Es muy fácil añadir una nueva orden o *Command* al sistema sin afectar en absoluto al código
  preexistente.

- Se puede implementar facilmente un sisteme de *rollback* o de deshacer (*undo*). Solo hay que
  almacenar en alguna parte los comandos ejecutados y obligar a las clases *Command* a implementar,
  además del método ``execute``, un método ``undo``, para deshacer lo que se haya hecho en el
  comando execute (No siempre se podrá hacer esto, especialmente si trabajamos con sistemas
  externos)

Las desventajas serian:

- Puede incrementar significativamente el número de clases y objetos que deben trabajar
  juntos para realizar una acción.

- Cada comando individual es una clase, que incremente la complejidad y dificulta la implementación
  y el mantenimiento.

