Optimización y Puesta en producción
========================================================================

Sobre las app
------------------------------------------------------------------------

Djaogo tiene este concepto de *applications* o *apps*, que se describe
en la documentación de Django como "Un paquete Python que proporciona
una funcionalidad determinada. Vamos a ver un poco más acerca de las
particularidades de este enfoque.

Una de los aspectos más importantes a la hora de añadir funcionalidad
escribiendo nuestras *apps* es el hecho de que las migraciones de Django
estan asociadas o agrupadas por *app*. Si hay referencias de tipo clave
foranea (``ForeignKey``) entre modelos que están en diferentes *apps*,
el sistema de migraciones de Django intentará inferir un grafo de
dependencias de forma que las migraciones puedan aplicarse en el orden
correcto.

Pero, desgraciadamente, el sistema no es perfecto y pueden producirse
errores y espcialmente dependias circulares comopleja, difíciles de
arreglar, sobre todo si además tenemos muchas *apps*.

Por tanto, debemos considerar estos campos de claves foraneas como
potencialmente peligrosos, y una razón para plantearnos si una división
en diferentes *apps* es realmente adecuada.

Unas primeras recomendaciones, personales, sobre el uso de *apps*:

- Si realmente no acabas de ver o no entiendes la necesidad de dividir
  el proyecto en *apps*, ignora el tema y usa una única *app* para tu
  aplicación. No es necesario tener varias *apps*, y siempre se puede
  plantear una división en el futuro, de ser necesario. No es que sea
  trivial, pero merece la pena por mantener, al menos inicialmente, la
  secuencia de migraciones lineal.

- Si realmente quieres crear aplicaciones separadas, sé todo lo
  explícito que se pueda sobre las dependencias entra las *apps* y
  mantenlas siempre al mínimo. Plantearse cada *app* como un futuro
  microservicio puede ayudar a definir y delimitar el alcance de cada
  *app*.

Da nombres explicitos a las tablas
------------------------------------------------------------------------

La base de datos de la aplicación probablemente es mas importante que el
código, vivirá más tiempo, y también es más difícil de cambiar. Sabiendo
esto, perece sensato ser cuidadoso y explicar con detalle el diseño y
las razones que han llevado al esquema de la base de datos. En este
sentido el comportamiento de Django de tomar estas decisiones por
nosotros puede ser inconveniente.

Aunque el diseño de la base de datos esta en su mayor parte definido a
traves de los modelos, hay algunos aspectos que debemos consdsiderar.
Por ejemlo, Django genera automáticamente el nombre de los modelos a
partir del nombre de la *app* y del propio modelo, siquiendo el patrón::

    <nombre de la app>_<nombre del modelo en minusculas>

En vez de usar este esquema predeterminado, podemos definir las tablas
usando nuestro propio sistema de nombres, usando la clase ``Meta`` con
el atributo ``db_table``::

    class MiModelo:
        class Meta:
            db_table = "modelo"

Las relaciones N a N
------------------------------------------------------------------------

El otro aspecto a considerar en el de los campos *ManyToManyFields*.
Django gestiona esas relaciones N a N usando una table generada
automáticamente, lo que quiere decir que toma las decisiones tanto del
nombre de la tabla como de los campos por su cuenta.

En vez de hacer eso, recomiendo crear explicitamente la tabla
intermedia, y unir los tablas manualmente usando el parámetro
``through`` (Véase `Uso de
ManyToManyField.through <https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ManyToManyField.through>`__).
Esto hace el uso de la tabla explícito, permite el acceso a la tabla de
forma directa y elimina ese caracter *oculto* que, personalmente, me
resulta molesto.

Además, facilita el trabajo si en el futuro hubiera que atribuirle
atributos a la tabla intermedia (Aunque se podría argumentar que esto
podría ser un caso claro de optimización prematura).

Estos detalles parecen triviales, pero desacoplar el diseño de la base
de datos de los detalles de implementación de Django es deseable, porque
hay muchas posibilidades de que otros elementos, aparte del ORM de
Django, acaben usando la base de datos. Este sistema también te permite
renombrar los nombres de las clases de los modelos sin que esto afecte a
las tablas, si se diera el caso. Tambien simplifica el dividir en
diferente *apps* o usar un *framework* diferente.

Evitar el uso de *GenericForeignKey*
------------------------------------------------------------------------

Si puedes, evita usar los campos ``GenericForeignKey``. Usarlos implica
perder la capadidad de usar funcionalidad como los *joins* (Véase
`select_related <https://docs.djangoproject.com/en/3.0/ref/models/querysets/#select-related>`__),
dificulta la integridad referencial y te impide usar funcionalidad
adicional como restricciones de claves foraneas y borrados en cascada.
Es probablemente mejor usar tablas separadas, y usar modelos abstractos
si realmente necesitas establecer este tipo de enlaces.

No obstanta, a veces hay situaciones en las que puede ser necesario o al
menos realmente útil tener una tabla que pueda apuntar a distintas
tablas. En esa caso, aun puedes plantearte usar una solución propia, que
no es tan dificil de hacer (Puedes hacerlo solo con dos campos, uno para
el tipo de modelo/tabla y otro para el valor de la clave foranea).

Lo que menos me gusta de las *GenericForeignKey* es que nos hacen
dependientes de la parte del framework llamada ``ontentTypes``, que
almacena identificadores para las tablas en una tabla mapa llamada
``django_contenttypes``.

Esta table tiene ciertas caracteristicas. En primer lugar, usan el
nombre de la app y el nombre de la clase como columnas para mapear un
modelo de Django a un numero entero, que es luego almacenado en un campo
en la tabla que utiliza la *GenericForeignKey*. Si decides cambiar los
nombres de los modelos o de la *app*, debes gestionar estos cambios
manualmente en la tabla.

Esto tambien implica que esta tabla comun que describe el mapeo entre
los modelos va a complicar las cosas si decides separar la aplicacion en
dioferentes servicios y bases de datos.

Igual que recomiendo nombrar explicitamente las tablas, sugiero usar tu
propio (y segurmante mas simple) esquema o sistema para identificar las
tabla: enteros, cadenas de texto o lo que sea, siempre será mejor que
depender de un número asignado al azar por el framework.

Sobre las migraciones
------------------------------------------------------------------------

A partir de Django 1.7, y usas una base de datos, es muy probable que
uses el sistema de migraciones de la base de datos para modificar el
esquema de la misma. Hay algunas recomendaciones a tener en cuenta al
respecto.

Primero, y sobre todo, **manten las migraciones lo mas simples
posibles**. Si hay que hacer tres cambios enla base de datos, no hagas
una migracion con los trers cambios, siempre mejor hacer tres
migraciones separadas, una para cada caso.

Asegurate también de que **tus migraciones son seguras**, en el sentido
de que no van a provocar una caida o una bajada en el rendimiento del
servidor cuando se aplique. Por ejemplo, podemos esperar que el hecho de
añadir una columna no implica demasiado riesgo, pero la operación
contraria, es decir, borrar una columna, puede potencialmente romper la
aplicación, si todavía hubiera código haciendo referencia a esa
columnna.

Incluso si no hay líneas de código que referencien ese campo, cuando
Django recupera un modelo de la base de datos, por ejemplo usando
``Model.objects.get(...)``, internamente se pedirán todos los campos en
una sentencia ``SELECT``, por lo que se producirá un error.

Podemos prevenir esto asegurandonos de que la migracion se ejecuta
despues de que el codigo haya sido desplegado, pero esto implica que los
despliegues deben ser un poco mas manuales (o menos automáticos, según
el punto de vista). Puede ser complicado también si el desarrollo esta
varios commits por delante del despliegue.

**Consolida las migraciones**. A medida que el proyecto acumula más y
más migraciones, estas tardan más en ejecutarse. Las migraciones de
Django se diseñaron para ejecutar de forma incremental todas las
migraciones, desde la primera, para poder obtener el estado interno
actual de la base de datos. Esto no solo hace mas lentos los desplieges,
también ralentiza construir entornos de desarrollo, de pruebas, etc.

Una soluciona esto es hacer periodicamente una limpieza y consolidar el
estado actual de la aplicacion. Esto se puede hacer usando el propio
sistema de gestion de Django o directamente a mano: Borrar todo el
contenido de la tabla ``django_migrations``, borrar todos los ficheros
de migracion, y ejecutar ``manage.py makemigrations`` para crear una
nuevas migración inicial, unica y con el estado actual de la base de
datos.

Evita modelos demasiado grandes
------------------------------------------------------------------------

Django promueve la idea de usar modelos grandes, añadiendo la lógica de
negocio dentro de los modelos. Aunque puede ser conveniente, sobre todo
al principio, esto no escala bien. Con el tiempo, la clase devien en una
clase gigantesca, con mucho código, larga y difícil de leer. A veces se
usan *mixins* para resolvar parcialmente el problema, aunque esten lejos
de representar una solucion ideal.

Estos modelos gigantes nos complicar trabajar con lógica que no
requieren trabajar con un modelo completo traido de la base de datos.
POr ejemplo, quizá ciertas operaciones solo necesitan el valor de la
clave primaria o un subconjunto de atributos almacenados en alguna
cache. Además, esta dependencia jugara en contra nuestra si queremos
cambiar a otro ORM, por ejemplo. Aclopar la logica a nuestros modelos
puede complicar muestro trabajo.

Es mejor, desde mi punto de vista, mantener modelos ligeros y que se
ocupen exclusivamente de los accesos a la capa de base de datos. Para
eso, necesitamos de alguna manera poner nuestro lógica de negocio en un
nivél intermedio entre la capa de acceso a la base de datos y la capa de
presentacion.

Cuidado con las señales (*signals*)
------------------------------------------------------------------------

Las señales de Django son muy útiles para desacoplar eventos de las
acciones asociadas, pero hay un caso que puede ser problemático, las
señales antes y despues de la operacion ``save``. Pueden ser útiles para
cosas pequeñas, pero si empèzamos a añadir demasiada lógica en estas
funciones pueden confundirnos a la hora de seguir el flujo de procesos.

No podemos pasar argumentos ni información propia usando las señanles, y
tampoco podemos hacer, de forma facil, que las señales se activen o no
en determinadas circustancias. El caso típico es cuando queremos hacer
operaciones en bloque sin activar las señales.

La sugenrecia es limitar su uso, poner poco codigo en estas funciones, y
definirlas cerca del modelo al que van asignadas.

Evita que el ORM sea tu metodo principar de aceso a los datos
------------------------------------------------------------------------

Si estas creando y actualizando la base de datos desde diferentes partes
de tu codigo con llamadas directas al ORM, quiza merece la pena que lo
reconsideres. Hay ciertas desventajas:

El principal problema es que no existe ninguna manera clara de realizar
operaciones personalizadas cuando tus modelos son creados o modificados.
Por ejemplo, supongamos que queremos que cada vez que se crea un onjeto
de tipo ``A``, también se cree otro objeto de tipo ``B`` (O que se
guarde un log, o que se verifique ciertas condiciones, etc…). Aparte de
usar señales, la otra opcion seria sobrecargar el metodo ``save`` con un
monton de codigo, una solicion pesada y enrevesada.

Una solucion es establecer un patrón mediante el cual enrutas todas las
llamadas a la base de datos (Crear/actualizar/borrar) a través de una
interfaz que envuelve el ORM. Esto porporciona puntos de entrada donde
poner la logica parsonalizada antes o despues de los cambios en la base
de datos. Además, desacopla un poco tu aplicacion de la interfaz del
modelo Django, lo que facilitaria usar otro ORM distinto en el futuro.

Cuidado al cachear instancias de modelos
------------------------------------------------------------------------

Si cacheas instancia de modelos, recuerda que si se cambia el esquema de
los modelos estos cambios no se reflejaran en la cache. Asegurate de
usar unos tiempos de vida razonablemente cortos.

Implementa, si puedes, una forma de borrar completamente de la cache,
todos las instancias de un modelo, Si puedes, implementa tambien una
forma de invalidar la cache de una instancia cada vez que moditicas los
datos de la misma.

