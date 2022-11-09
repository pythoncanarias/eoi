---
title: Para aprender más de Django
topic: Desarrollo Web
---
## Para aprender más de Django


### Autentificación de peticiones web

Existe una *middleware* ya incluido por defecto en Django para gestionar
un sistema de autentificación de usuarios. Cuando este *middleware* de
sesiones está instalado, se añade automáticamente a cada objeto
`request` un atributo `user`.

Si el usuario se ha identificado en el sistema, el valor de `user` sera
una instancia del modelo `auth.User` para dicho usuario. Si no ha habido
autentificación, `user` es una instancia de `AnonymousUser`. En
cualquier caso, siempre podemos comprobar en que situación estamos
accediendo a la propiedad `is_authenticated` de `request.user`. En el
primer caso valdra `True`, en el segundo `False`:

```python
if request.user.is_authenticated:
    # El usuario está autentificado
    # request.user es una instancia de auth.User
    ...
else:
    # No hay usuario
```

#### Como permitir validarse al usuario

Para poder permitirle a un usuario ya existente acceder a la web de forma
autenticada, necesitamos verificar su identidad y crear una nueva sesión. Para
ello podemos usar la función `login` (En `django.contrib.auth`):

```python
login(request, user, backend=None)
```

La función `login` acepta un objeto de tipo `HttpRequest` y una instancia de la
clase `auth.User`. Almacena el identificador de usuario en una sesión, usando
el sistema de Django de sesiones. Si la sesion contuviera algun dato definido
mientras no estaba asociada con ningún usuario, al asignar la sesion al usuario
dichos datos se mantienen. Esto es util, por ejemplo, para poder mantener un
carrito de la compra y no perder esa información si el usuario se valida en
medio de la compra.

Para permitir al usuario acceder desde una vista, obtenderemos tipicamente el
identificador de usuario y la contraseña de un formulario. Usamos
`authenticate` para validar que la combinacion es correcta. Si lo fuera,
authenticate nos devuelve la instancia del usuario, y a continuacion usamos
`login` para vincular la sesión actual (normalmente una sesion anónima) con el
usuario:

```python
from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
```

#### Limitar accesso en base al usuario

Podemos comprobar facilmente si el usuario esta identificado en el
sistema (Es decir, que tiene una sesión asociada al usuario) con una llamada al
método `is_authenticated` del objeto `user`, así que una primera forma podría
ser:

```python
def my_view(request):
    if not request.user.is_authenticated:
        return render(request, 'myapp/login_error.html')
    # ...
```

En el ejemplo anterior, mostramos una plantilla con un mensaje de error,
pero podemos hacer cualquier otra cosa, como por ejemplo redirigir el
navegador hacia la página de autentificación o *login*.

Como este comportamiento es muy habitual, django incorpora un decorador
que realiza todo ese procedimiento por nosotros, el decorador
`login_required` (En `django.contrib.auth.decorators`).

Este decorador hace lo siguiente:

- Si el usuario no está identificado, se le redirige a la dirección definida en

  la variable `settings.LOGIN_URL` (Si no se ha definido, su valor por defecto
  es `accounts/login/`). Incuira en la redirección un parámetro `next`
  con la url a la que se queria acceder inicialmente, de forma que podemos usar
  es valor para redirigirlo a la página que quería ver, una vez se haya
  identificado.

- Si el usuario está identificado, se ejecuta la vista. El codigo de la vista
  puede tener la confianza de que el usuario está identificado.

Si usamos clases basadas en vistas, podemos usar la clase *Mixin*
`LoginRequiredMixin` para obtener el mismo resultado. Los mixin siempre
deberiar estar a la izquierda de la clase principal de la que derivamos la
vista, pero para este en particular, debería ser el primero por la izquierda:

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
```

### Optimización y Puesta en producción

#### Sobre las app

Django tiene este concepto de *applications* o *apps*, que se describe
en la documentación como \"Un paquete Python que proporciona una
funcionalidad determinada\". Vamos a ver un poco más acerca de las
particularidades de este enfoque.

Una de los aspectos más importantes a la hora de añadir funcionalidad
escribiendo nuestras *apps* es el hecho de que las migraciones de Django
están asociadas o agrupadas por *app*. Si hay referencias de tipo clave
foranea (`ForeignKey`) entre modelos que están en diferentes *apps*, el
sistema de migraciones de Django intentará inferir un grafo de
dependencias de forma que las migraciones puedan aplicarse en el orden
correcto.

Pero, desgraciadamente, el sistema no es perfecto y pueden producirse
errores y espcialmente dependencias circulares complejas, difíciles de
arreglar, sobre todo si además tenemos muchas *apps*.

Por tanto, debemos considerar estos campos de claves foraneas como
potencialmente peligrosos, y una razón para plantearnos si una división
en diferentes *apps* es realmente adecuada.

Unas primeras recomendaciones, personales, sobre el uso de *apps*:

- Si realmente no acabas de ver o no entiendes la necesidad de dividir el
  proyecto en *apps*, ignora el tema y usa una única *app* para tu aplicación.
  No es necesario tener varias *apps*, y siempre se puede plantear una división
  en el futuro, de ser necesario. No es que sea trivial, pero merece la pena
  por mantener, al menos inicialmente, la secuencia de migraciones sencilla.

- Si realmente quieres crear aplicaciones separadas, sé todo lo explícito que
  se pueda sobre las dependencias entra las *apps* y mantenlas siempre al
  mínimo. Plantearse cada *app* como un futuro microservicio puede ayudar a
  definir y delimitar el alcance de cada *app*.

#### Da nombres explicitos a las tablas

La base de datos de la aplicación probablemente es mas importante que el
código, vivirá más tiempo, y también es más difícil de cambiar. Sabiendo esto,
perece sensato ser cuidadoso y explicar con detalle el diseño y las razones que
han llevado al esquema de la base de datos. En este sentido el comportamiento
de Django de tomar estas decisiones por nosotros puede ser inconveniente.

Aunque el diseño de la base de datos esta en su mayor parte definido a traves
de los modelos, hay algunos aspectos que debemos consdsiderar.  Por ejemlo,
Django genera automáticamente el nombre de los modelos a partir del nombre de
la *app* y del propio modelo, siquiendo el patrón:

```
<nombre de la app>_<nombre del modelo en minusculas>
```

En vez de usar este esquema predeterminado, podemos definir las tablas
usando nuestro propio sistema de nombres, usando la clase `Meta` con el
atributo `db_table`:

```python
class MiModelo:
    class Meta:
        db_table = "modelo"
```

#### Las relaciones N a N

El otro aspecto a considerar en el de los campos *ManyToManyFields*.
Django gestiona esas relaciones N a N generando una tabla intermedia de
forma automática, lo que quiere decir que toma las decisiones tanto del
nombre de la tabla como de los campos por su cuenta.

En vez de hacer eso, recomiendo crear explicitamente esa tabla
intermedia, y unir los tablas manualmente usando el parámetro `through`
(Véase [Uso de
ManyToManyField.through](https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ManyToManyField.through)).

Esto hace el uso de la tabla explícito, permite el acceso a la tabla de
forma directa y elimina ese comportamiento *oculto* que, personalmente,
me resulta molesto.

Además, facilita el trabajo si en el futuro hubiera que atribuirle
atributos a la tabla intermedia (Aunque se podría argumentar que esto
podría ser un caso de optimización prematura).

Estos detalles parecen triviales, pero desacoplar el diseño de la base
de datos de los detalles de implementación de Django es deseable, porque
hay muchas posibilidades de que otros elementos, aparte del ORM de
Django, acaben interactuando con la base de datos. Este sistema también
te permite renombrar los nombres de las clases de los modelos sin que
esto afecte a las tablas, si se diera el caso. Tambien simplifica el
dividir en diferente *apps* o usar un *framework* diferente.

### Evita el uso de *GenericForeignKey*

Si puedes, evita usar los campos `GenericForeignKey`. Usarlos implica perder la
capadidad de usar funcionalidad como los *joins* (Véase
[select\_related](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#select-related)),
dificulta la integridad referencial y te impide usar funcionalidades
adicionales como restricciones de claves foraneas y borrados en cascada.  Es
probablemente mejor usar tablas separadas, y usar modelos abstractos si
realmente necesitas establecer este tipo de enlaces.

No obstante, a veces hay situaciones en las que puede ser necesario o al menos
realmente útil tener una tabla que pueda apuntar a distintas tablas. En esa
caso, aun puedes plantearte usar una solución propia, que no es tan difícil de
implementar (Puedes hacerlo solo con dos campos, uno para el tipo de modelo/tabla y
otro para el valor de la clave foranea).

Lo que menos me gusta de las *GenericForeignKey* es que nos hacen dependientes
de la parte del framework llamada `ContentTypes`, que almacena identificadores
para las tablas en una tabla mapa llamada `django_contenttypes`.

Esta table tiene ciertas caracteristicas. En primer lugar, usan el nombre de la
app y el nombre de la clase como columnas para mapear un modelo de Django a un
numero entero, que es luego almacenado en un campo en la tabla que utiliza la
*GenericForeignKey*. Si decides cambiar los nombres de los modelos o de la
*app*, debes gestionar estos cambios manualmente en la tabla.

Esto tambien implica que esta tabla comun que describe el mapeo entre los
modelos va a complicar las cosas si decides separar la aplicación en diferentes
servicios y bases de datos.

Igual que recomiendo nombrar explicitamente las tablas, sugiero usar tu propio
(y seguramante más simple) esquema o sistema para identificar las tabla:
enteros, cadenas de texto o lo que sea, siempre será mejor que depender de un
número asignado al azar por el framework.

### Sobre las migraciones

A partir de Django 1.7, si usas una base de datos, es muy probable que uses el
sistema de migraciones de la base de datos para modificar el esquema de la
misma. Hay algunas recomendaciones a tener en cuenta al respecto.

Primero, y sobre todo, **manten las migraciones lo más simples y atómicas
posibles**. Si hay que hacer tres cambios en la base de datos, no hagas una
única migración que incluya los tres cambios, mejor haz tres migraciones
separadas, una para cada caso.

Asegurate también de que **tus migraciones son seguras**, en el sentido de que
no van a provocar una caida o una bajada en el rendimiento del servidor cuando
se aplique. Por ejemplo, podemos esperar que el hecho de añadir una columna no
implica demasiado riesgo, pero la operación contraria, es decir, borrar una
columna, puede potencialmente romper la aplicación, si todavía hubiera código
haciendo referencia a esa columnna.

Incluso si no hay líneas de código que referencien ese campo, cuando Django
recupera un modelo de la base de datos, por ejemplo usando
`Model.objects.get(...)`, internamente se pedirán todos los campos en una
sentencia `SELECT`, por lo que se producirá un error.

Podemos prevenir esto asegurandonos de que la migración se ejecuta después de
que el código ha sido desplegado, pero esto implica que los despliegues deben
ser un poco más manuales (o menos automáticos, dependiendo del punto de vista).
Puede ser complicado también si el desarrollo esta varios *commits* por delante
del despliegue.

**Consolida las migraciones**. A medida que el proyecto acumula más y más
migraciones, estas tardan más en ejecutarse. Las migraciones de Django se
diseñaron para ejecutar de forma incremental todas las migraciones, desde la
primera, para poder obtener el estado interno actual de la base de datos. Esto
no solo hace mas lentos los desplieges, también ralentiza construir entornos de
desarrollo, de pruebas, etc.

Una solucion para esto es hacer periodicamente una limpieza y consolidar el
estado actual de la aplicacion. Esto se puede hacer usando el propio sistema de
gestion de Django o directamente a mano: Borrar todo el contenido de la tabla
`django_migrations`, borrar todos los ficheros de migracion, y ejecutar
`manage.py makemigrations` para crear una nuevas migración inicial, unica y con
el estado actual de la base de datos.

Si puedes, haz que las migraciones sean reversibles.

### Evita modelos demasiado grandes

Django promueve la idea de usar modelos grandes, añadiendo la lógica de negocio
dentro de los modelos. Aunque puede ser conveniente, sobre todo al principio,
esto no escala bien. Con el tiempo, la clase devien en una clase gigantesca,
con mucho código, larga y difícil de leer. A veces se usan *mixins* para
resolvar parcialmente el problema, aunque esten lejos de representar una
solucion ideal.

Estos modelos gigantes nos complicar trabajar con lógica que no requieren
trabajar con un modelo completo traido de la base de datos.

Por ejemplo, quizá ciertas operaciones solo necesitan el valor de la clave
primaria o un subconjunto de atributos almacenados en alguna cache. Además,
esta dependencia jugara en contra nuestra si queremos cambiar a otro ORM, por
ejemplo. Aclopar la logica a nuestros modelos puede complicar muestro trabajo.

Es mejor, desde mi punto de vista, mantener modelos ligeros y que se ocupen
exclusivamente de los accesos a la capa de base de datos. Para eso, necesitamos
de alguna manera poner nuestro lógica de negocio en un nivél intermedio entre
la capa de acceso a la base de datos y la capa de presentacion.

#### Cuidado con las señales (*signals*)

Las señales de Django son muy útiles para desacoplar eventos de las
acciones asociadas, pero hay un caso que puede ser problemático, las
señales antes y después de la operación `save`. Pueden ser útiles para
cosas pequeñas, pero si añadimos demasiada lógica en estas funciones pueden
confundirnos a la hora de seguir el flujo de procesos.

No podemos pasar argumentos ni información propia usando las señanles, y
tampoco podemos hacer, de forma fácil, que las señales se activen o no
en determinadas circustancias. El caso típico es cuando queremos hacer
operaciones en bloque sin activar las señales.

La sugerencia es limitar su uso, poner poco código en estas funciones, y
definirlas cerca del modelo al que van asignadas.

#### Evita que el ORM sea tu metodo principal de aceso a los datos

Si estás creando y actualizando la base de datos desde diferentes partes de tu
código con llamadas directas al ORM, quiza merece la pena que lo reconsideres.
Hay ciertas desventajas:

El principal problema es que no existe ninguna manera clara de realizar
operaciones personalizadas cuando tus modelos son creados o modificados.  Por
ejemplo, supongamos que queremos que cada vez que se crea un onjeto de tipo
`A`, también se cree otro objeto de tipo `B` (O que se guarde un log, o que se
verifique ciertas condiciones, etc.). Aparte de usar señales, la otra opción
sería sobrecargar el método `save` con un montón de código, una solución pesada
y complicada.

Una solucion es establecer un patrón mediante el cual enrutas todas las
llamadas a la base de datos (Crear/actualizar/borrar) a través de una interfaz
que envuelve el ORM. Esto proporciona puntos de entrada donde poner la lógica
personalizada antes o después de los cambios en la base de datos. Además,
desacopla un poco tu aplicación de la interfaz del modelo Django, lo que
facilitaria usar otro ORM distinto en el futuro.

### Cuidado al cachear instancias de modelos

Si cacheas instancia de modelos, recuerda que si se cambia el esquema de los
modelos estos cambios no se reflejarán en la cache. Asegurate de usar unos
tiempos de vida razonablemente cortos.

Implementa, si puedes, una forma de borrar completamente de la cache, todos las
instancias de un modelo, Si puedes, implementa tambien una forma de invalidar
la cache de una instancia cada vez que moditicas los datos de la misma.


### Recursos para profundizar en Desarrollo web

#### HTML y CSS

- [Best HTML courses in 2020](https://hackr.io/blog/best-html-courses)
- [12 HTML Tags You Don\'t Know](https://jatinrao.dev/12-html-tags-you-dont-know)
- [HTML Reference](https://htmlreference.io/) Es una referencia muy
    buena y fácil de consultar de todas las etiquetas HTML.
- [41 Free HTML and CSS ebooks](https://freefrontend.com/html-css-books/)

#### Tutorial oficial de Django

La página oficial proporciona un tutorial bastante completo, dividido en 7
partes:

- Parte 1: [Requests and
  responses](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)

- Parte 2: [Models and the admin
  site](https://docs.djangoproject.com/en/3.0/intro/tutorial02/)

- Parte 3: [Views and
  templates](https://docs.djangoproject.com/en/3.0/intro/tutorial03/)

- Parte 4: [Forms and generic
  views](https://docs.djangoproject.com/en/3.0/intro/tutorial04/)

- Parte 5:
  [Testing](https://docs.djangoproject.com/en/3.0/intro/tutorial05/)

- Parte 6: [Static
  files](https://docs.djangoproject.com/en/3.0/intro/tutorial06/)

- Parte 7: [Customizing the admin
  site](https://docs.djangoproject.com/en/3.0/intro/tutorial07/)

Tambien tiene estos dos tutoriales avanzados:

- [How to write reusable apps](https://docs.djangoproject.com/en/3.0/intro/reusable-apps/)

- [[Writing your first patch for Django](https://docs.djangoproject.com/en/3.0/intro/contributing/)


#### Tutorial de Django Girls

Excelente tutorial, cubre el desarrollo de una aplicación de *blogs* partiendo
practicamente desde cero, por lo que es una buena oprtunidad de aprender o
refrescar Python. Además, está traducido a español.

- [Tutorial de DjangoGirls](https://tutorial.djangogirls.org/es/)

#### Tango con Django (*Tango with Django*)

Es una guía de desarrollo web con Django y Python. En una descripción
más completa que los tutoriales básicos, en el sentido de que explica
las diferentes tecnologías imncluidas en el proceso.

- [Tango with Django](https://www.tangowithdjango.com/)
- [Repositorio de código](https://github.com/maxwelld90/tango_with_django_2_code)

#### Django tutorial de Real Python
Una colección de tutoriales de nivel intermedio a avanzado, por la gente
de [RealPython](https://realpython.com/), que también son una referencia
muy buena en Pyhon en general (En inglés).

- [Real Python Django tutorials](https://realpython.com/)

### Django packages
---------------

Django packages es un directorio de *apps* reutilizables, herramientas,
añadidos y librerías utilizables en tus proyectos Django.

- [Djangopackages.org](https://djangopackages.org/)

#### Django en producción

- [A tour of Django server setups](https://mattsegal.dev/django-prod-architectures.html)

#### Awesome Django

Recopilatorio de todo tipo de recursos para Django

- [Awesome Django](https://github.com/shahraizali/awesome-django)
