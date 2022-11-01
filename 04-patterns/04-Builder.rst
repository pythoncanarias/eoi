El patrón Builder
========================================================================

Propósito
------------------------------------------------------------------------

Separa la construcción de un objeto complejo de su representación, de
forma que el mismo proceso de construcción pueda crear diferentes
representaciones.

.. code:: ipython3

    def f(a=-1, b=-1, c=-1, d=-1, e=-1, f=-1):
        
    f(a=2, b=6)
    f(c=3, d=5, e=7, f=8)
    
    
    
    b = BuilderForF()
    b.set_a(2)
    b.set_b(5)
    b.call()

Al contrario que otros patrones creacionales, *Builder* no requiere que
los objetos que vaya a crear tengan que tener una interfaz común.
Podemos crear objetos totalmente diferentes usando el mismo proceso de
construccion.

Motivación
------------------------------------------------------------------------

Es especialmente útil en aquellos casos en lso que tenemos que crear
objeots que adminten múltiples opciones de configuracion. Es habitual
encontralo en clases que tienen un metodo de creacion simple y un serie
de metodos de configuracion, y normalmente soportan llamadas en cadena,
por ejemplo ``someBuilder.set_value_a(1).set_value_b(2).create()``.

The Builder pattern can be recognized in class, which has a single
creation method and several methods to configure the resulting object.
Builder methods often support chaining (for example,

Un lector del formato de intercambio de documentos RTF (Rich Text
Format) debería poder convertir RTF a muchos formatos de texto. Podría
convertir documentos RTF a texto ASCII o a un útil[32] de texto que
pueda editarse de forma interactiva. El problema, no obstante, es que el
número de conversiones posibles es indefinido. Por tanto, tendría que
ser fácil añadir una nueva conversión sin modificar el lector.

Una solución es configurar la clase LectorRTF con un objeto
ConvertidorDeTexto que convierta RTF a otra representación textual.
Cuando el LectorRTF analiza el documento RTF, usa el ConvertidorDeTexto
para realizar la conversión. Cada vez que el LectorRTF reconozca un
token RTF (ya sea texto normal o una palabra de control de RTF), envía
una petición al ConvertidorDeTexto para que lo convierta. Los objetos
ConvertidorDeTexto son responsables de realizar la conversión de datos y
de representar el token en un determinado formato.

Las subclases de ConvertidorDeTexto están especializadas en diferentes
conversiones y formatos. Por ejemplo, un ConvertidorASCII hace caso
omiso de las peticiones de conversión de cualquier otra cosa que no sea
texto sin formato. Por otro lado, un ConvertidorTeX, implementará
operaciones para todas las peticiones, con el objetivo de producir una
representación en TeX con toda la información de estilo que haya en el
texto. Un ConvertidorUtilDeTexto producirá un objeto complejo de
interfaz de usuario que permita al usuario ver y editar el texto.

La clase de cada tipo de convertidor toma el mecanismo de creación y
ensamblaje de un objeto complejo y lo oculta tras una interfaz
abstracta. El convertidor se separa del lector, que es el responsable de
analizar un documento RTF.

El patrón Builder expresa todas estas relaciones. Cada clase de
convertidor se denomina constructor, en el contexto de este patrón, y al
lector se le llama director. Aplicado a este ejemplo, el patrón Builder
separa el algoritmo para interpretar un formato textual (es decir, el
analizador de documentos RTF) de la manera en que se crea y se
representa el formato de destino. Esto permite reutilizar el algoritmo
de análisis de LectorRTF para crear diferentes representaciones de texto
a partir de documentos RTF —basta con configurar el LectorRTF con
diferentes subclases de ConvertidorDeTexto—.

Aplicabilidad
------------------------------------------------------------------------

Úsese el patrón Builder cuando

-  el algoritmo para crear un objeto complejo debiera ser independiente
   de las partes de que se compone dicho objeto y de cómo se ensamblan.

-  el proceso de construcción debe permitir diferentes representaciones
   del objeto que está siendo construido.

Participantes
------------------------------------------------------------------------

-  **Constructor** (ConvertidorDeTexto) especifica una interfaz
   abstracta para crear las partes de un objeto Producto.

-  **Constructor Concreto** (ConvertidorASCII, ConvertidorTeX,
   ConvertidorUtilDeTexto) implementa la interfaz Constructor para
   construir y ensamblar las partes del producto. define la
   representación a crear. proporciona una interfaz para devolver el
   producto (p. ej., ObtenerTextoASCII, ObtenerUtilDeTexto).

-  **Director (LectorRTF)** construye un objeto usando la interfaz
   Constructor.

-  **Producto (TextoASCII, TextoTeX, UtilDeTexto)**

   representa el objeto complejo en construcción. El ConstructorConcreto
   construye la representación interna del producto y define el proceso
   de ensamblaje. Incluye las clases que definen sus partes
   constituyentes, incluyendo interfaces para ensamblar las partes en el
   resultado final.

Colaboraciones
------------------------------------------------------------------------

El cliente crea el objeto Director y lo configura con el objeto
Constructor deseado.

El Director notifica al constructor cada vez que hay que construir una
parte de un producto.

El Constructor maneja las peticiones del director y las añade al
producto.

El cliente obtiene el producto del constructor.

Consecuencias
------------------------------------------------------------------------

Éstas son las principales consecuencias del patrón Builder:

-  Permite **variar la representación interna de un producto**. El
   objeto Constructor proporciona al director una interfaz abstracta
   para construir el producto. La interfaz permite que el constructor
   oculte la representación y la estructura interna del producto.
   También oculta el modo en que éste es ensamblado. Dado que el
   producto se construye a través de una interfaz abstracta, todo lo que
   hay que hacer para cambiar la representación interna del producto es
   definir un nuevo tipo de constructor.

-  **Aísla el código de construcción y representación**. El patrón
   Builder aumenta la modularidad al encapsular cómo se construyen y se
   representan los objetos complejos. Los clientes no necesitan saber
   nada de las clases que definen la estructura interna del producto;
   dichas clases no aparecen en la interfaz del Constructor. Cada
   ConstructorConcreto contiene todo el código para crear y ensamblar un
   determinado tipo de producto.

   El código sólo se escribe una vez; después, los diferentes Directores
   pueden reutilizarlo para construir variantes de Producto a partir del
   mismo conjunto de partes. En el ejemplo anterior de RTF, podríamos
   definir un lector para otro formato distinto de RTF. como por ejemplo
   un LectorSGML, y usar los mismos objetos ConvertidorDeTexto para
   generar representaciones TextoASCII, TextoTeX y UtilDeTexto de
   documentos SGML.

-  **Proporciona un control más fino sobre el proceso de construcción**.
   A diferencia de los patrones de creación que construyen los productos
   de una vez, el patrón *Builder* construye el producto paso a paso,
   bajo el control del director. El director sólo obtiene el producto
   del constructor una vez que éste está terminado. Por tanto, la
   interfaz Constructor refleja el proceso de construcción del producto
   más que otros patrones de creación. Esto da un control más fino sobre
   el proceso de construcción y, por tanto, sobre la estructura interna
   del producto resultante.

Implementación
------------------------------------------------------------------------

Normalmente hay una clase abstracta Builder que define una operación
para cada componente que puede ser creado. La implementación
predeterminada de estas operaciones no hace nada.

Una clase ConstructorConcreto redefine las operaciones para los
componentes que está interesado en crear.

Éstas son otras cuestiones de implementación que hay que considerar:

1. **Interfaz de ensamblaje y construcción**. Los constructores
   construyen sus productos paso a paso. Por tanto, la interfaz de la
   clase Constructor debe ser lo suficientemente general como para
   permitir construir productos por parte de todos los tipos de
   constructores concretos.

Una cuestión de diseño fundamenttal tiene que ver con el modelo del
proceso de construcción y ensamblaje. Normalmente basta con un modelo
según el cual los resultados de las peticiones de construcción
simplemente se van añadiendo al producto. En el ejemplo del RTF, el
constructor convierte y añade el siguiente token al texto que ha
convertido hasta la fecha.

Pero a veces podríamos necesitar acceder a las partes del producto que
ya fueron construidas. En el ejemplo del laberinto que presentamos en el
Código de Ejemplo, la interfaz ``ConstructorLaberinto`` permite añadir
una puerta entre habitaciones existentes. Otro ejemplo son las
estructuras arbóreas, como los árboles sintácticos que se crean de abajo
a arriba. En ese caso, el constructor devolvería nodos hijos al
director, el cual los devolvería al constructor para construir los nodos
padre.

2. **¿Por qué no usar clases abstractas para los productos?** En
   general, los productos creados por los constructores concretos tienen
   representaciones tan diferentes que sería de poca ayuda definir una
   clase padre común para los diferentes productos. En el ejemplo del
   RTF, es poco probable que los objetos TextoASCII y UtilDeTexto tengan
   una interfaz común. Como el cliente suele configurar al director con
   el constructor concreto adecuado, sabe qué subclase concreta de
   Constructor se está usando, y puede manejar sus productos en
   consecuencia.

3. **Métodos vacíos de manera predeterminada en el constructor**. En
   C++, los métodos de creación no se declaran como funciones miembro
   virtuales puras a propósito. En vez de eso, se definen como métodos
   vacíos, lo que permite que los clientes redefinan sólo las
   operaciones en las que están interesados.
