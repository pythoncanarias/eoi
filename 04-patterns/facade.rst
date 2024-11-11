El patron Façade (Fachada)
========================================================================

Propósito
------------------------------------------------------------------------

Proporciona una interfaz unificada para un conjunto de interfaces de un
subsistema. Define una interfaz de alto nivel que hace que el subsistema
sea más fácil de usar.

Motivación
------------------------------------------------------------------------

Una fachada se refiere generalmente a la parte exterior de un edificio.
También puede referirse a una actitud o comportamiento de una persona
que intenta esconder o disimular su estado real.

Cuando se contempla una fachada, podemos apreciar (o no) el exterior
pero no podemos deducir nada o casi nada de las complejidades de su
estructura interior.

El patrón *Façade* funciona igual; oculta las complejidades de un
sistema y proporciona una interfaz simplificada al cliente.

Los beneficios que nos aporta son:

-  Obtener una interfaz unificada y simplificada para un subsistema o
   conjunto de subsistemas

-  No encapsula al subsistema, pero proporciona un acceso de mayor
   nivel, especialmente para agrupar diferentes componentes.

-  Reduce el acoplamiento entre la implementación y los clientes.

Componentes
------------------------------------------------------------------------

- **Fachada a Facade**: La responsabilidad de esta clase o función es
  envolver un sistema complejo interconectado bajo una única apariencia
  mas sencilla de utilizar.

- **Subsistema**: Representa al subsistema o subsistemas que queremos
  ocultar debajo de la fachada.

- **Cliente**: El cliente interactúa únicamente con la fachada, de forma
  que consigue interactuar con el sistema para conseguir sus objetivos.
  El cliente no necesita preocuparse de las complejidades internas (Por
  ejemplo, parámetros de conexión al subsiste), ni de los componentes
  del subsistema.


Aplicabilidad
------------------------------------------------------------------------

Usaremos el patrón Facade cuando:

- Queramos proporcionar una interfaz simple para un subsistema complejo.
  Aquellos clientes, que necesitan más personalización necesitarán ir
  más allá de la fachada.

- Hay muchas dependencias entre los clientes y las clases que
  implementan una funcionalidad. Se introduce una fachada para
  desacoplar el subsistema de sus clientes, promoviendo así la
  independencia entre subsistemas y la portabilidad.

- Queremos usar una librería externa, pero la envolvemos en un Fachada
  para que podamos usarla más fácilmente a la vez que facilitamos el
  cambio de la librería por otra.


Consecuencias
------------------------------------------------------------------------

El patrón Facade proporciona las siguientes ventajas:

1. Oculta a los clientes los componentes del subsistema, haciendo que el
   subsistema sea más fácil de usar.

2. Promueve un débil acoplamiento entre el subsistema y sus clientes.

3. No impide que las aplicaciones usen las clases del subsistema en caso
   de que sea necesario. De este modo se puede elegir entre facilidad de
   uso y generalidad.


Ejercicios
------------------------------------------------------------------------

**Ejercicio**: Discutir las diferencias entre el patrón Fachada (Façade)
y Adaptador (Adapter)

**Ejercicio**: Supongamos que nuestro código utiliza la API de GitHub
para determinada funcionalidad. Las llamadas se realizan en diferentes
partes del código, y no usan ninguna librería especial, sino haciendo
llamadas a la API rest, unas veces usando ``urllib`` y otras ``requests``.

Queremos solucionar el problema, y el primer paso sera crear una fachada
para todo lo que sea interactura con GitHub. Los subsistemas ``urllib``
y ``requests`` deben quedar ocultos bajo la fachada.

Dibuja un esquema gráfico que muestre el estado del sistema antes y
después de esta refactorización.
