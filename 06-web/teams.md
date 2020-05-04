Django también define una serie de campos para reflejar las
relaciones entre modelos.

La mas usade es `ForeignKey`, que se usa para representar
una relacion uno a muchos ($1$ a $N$). Requiere obligatoriamente
al menos dos parámetros: La clase con la que se quiere relacionar
el modelo y un parametro llamado `on_delete` que explicaremos
mas adelante.

Vamos a crear la relacion 1 a N que teniamos en nuestro diagrama
E/R entre un superheroe (O supervillano) y un equipo. En nuestro
analisis no se permitia que un metahumano fuera parte de mas de
un equipo, pero si se permitia que fuera por solitario, es decir, que
podia no pertener a ningun grupo.

Lo primero que tenemos que hacer es crear el nuevo módelo para el equipo,
vamos a llamarlo `Team`, y por ahora solo nos interesan tres campos,
el nombre del supergrupo, una descripción y el nombre de su base o 
cuartel general. Algo
como esto:

    class Team(models.Model):
        
        class Meta:
            verbose_name = "Equipo"
            verbose_name_plural = "Equipos"

        name = models.CharField(max_length=220)
        description = models.TextField(max_length=4000)
        headquarter =  models.CharField(max_length=100)

    def __str__(self):
        return self.name


Añadimos esta definición al fichero `metahumans/models.py`. Al añadir esta
nueva clase, nuestra base de datos ya no esta en sintonía con nuestro modelos,
asi que habra que crear 
y aplicar una migracion para crear esta tabla.

Vamos a incluir este nuevo modelo en el admin, edita el fichero
`metahumans/admin.py` y añade las siguientes líneas:

    class TeamAdmin(admin.ModelAdmin):
        list_display = ('name', 'headquarter')

    admin.site.register(models.Team, TeamAdmin)

Una cosa nueva que hemos usado en el modelo `Team` es una clase
definida dentro del modelo llamado `Meta`. Esta es una convención
que usa Django para añadir meta-informacion sobre el modelo. En este
caso estamos añadiendo información acerca de cual es el nombre con
el que nos referimos coloquialmente a esta entidad, en dos versiones, para
singular "El equipo" y el plurar "Los equipos".

Una vez creado el nuevo modelo, podemos dar de alta, usando
el admin, a los vengadores, por ejemplo. Puedes
usar esta informacion para crearlo:

- Nombre: Vengadores
- Descripcion: Los heroes más poderosos de la Tierra
- Cuartel general: Torre Stark / Torre vengadores

Ahora, para reflejar la relación 1 a N entre el equipo
y los miembros, tenemos que modificar la clase `MetaHuman`, incluyendo
una referencia a la clase `Team`. 

Modifiquemos `MetaHuman` para que queda algo asi:

    class MetaHuman(models.Model):
        name = models.CharField(max_length=42)
        country = models.CharField(max_length=2, choices=COUNTRIES)
        level = models.IntegerField(default=10)
        active = models.BooleanField(default=True)
        powers = models.ManyToManyField(Power)
        last_update = models.DateTimeField(auto_now=True)
        team = models.ForeignKey(
            Team,
            on_delete=models.PROTECT,
            blank=True,
            null=True,
            default=None,
        )

        def __str__(self):
            return self.name

En el campo `team` hemos creado una referencia al modelo `Team`. Las
opciones `blank`, `null` y `default` nos permiten incluir la posibilidad
de que el metahumano pertenezca a un grupo o no. La opcion `on_delete`, 
que es obligatoria, esta ajustada en este caso a `PROTECT`. Veremos
mas posibilidades para este parametro.

Por ahora, lo que nos interesa saber sobre el valor de `on_delete`
es que nos permite definir el comportamiento del sistema si
se borra una entidad de la clase referenciada; en nuestro caso, que hacemos
con los metahumanos que pertenencen a un grupo si dicho grupo se
borra.

El valor `PROTECT` significa: Si el grupo que quieres borrar tiene
algun metahumano asignado, impide el borrado. Es decir, solo se permite el 
borrado si ningun metahumano esta asignado a este grupo.

Se crea un índice de forma automática para cada clave foranea o
`ForeignKey`. Podemos desabilitar esto usando el parámetro
`db_index` a `False`.

Que está pasando a nivel de base de datos? django añade un campo 
con el nombre del campo que hemos indicado (en nuestro caso, `team`)
pero añadiendole `_id`, de forma que a nivel de base de datos, en 
la table de MetaHuman se habrá creado un nuevo campo `team_id`. En ese
campo se guardará el valor de la clave primaría del equipo, cuando
se asigne este superheroe al mismo.

Pero Normalmente, no tenemos que preocuparnos de este campo, a no ser
que estemos trabajando directamente al nivel de base de datos. Si
usamos el ORM, siempre trabajaremos directamente con el atribute `team`.

Vamos a asignar uno de nuestros superheroes a nuestro recien
creado grupo de Los Vengadores, pero no lo vamos a hacer con
el admin, vamos a hacerlo directamente desde Python

Vamos a ejecutar un nuevo comando de `manage.py`, `shell`:

    python manage.py shell

Esto nos abrira un shell de Python, como el normal que tenemos
instalado, pero con la diferencia de que Django se ha inicializado
previamente, de forma que podemos acceder a los modelos. Lo primero
que vamos a hacer es importar `Team` y `MetaHuman`.

    >>> from metahumans.models import Team, MetaHuman

Una vez obtenido acceso a los modelos, vamos a pedirle al modelo
`Team` que nos devuelve un objeto de este tipo. En principio el
primero que encuentre, pero como solo hemos
creado uno, debería devolvernos el de Los vengadores.

    >>> avengers = Team.objects.first()
    >>> print(avengers)
    Vengadores

Dentro de cada modelo hay un gestor, que por defecto tiene el
nombre de `objects` que nos permite realizar operaciones con el
modelo como hacer búsquedas o filtros por determinados valores (una
consulta o *query* en la jerga de base de datos).

En este caso concreto, le hemos pedido que nos devuelve el 
primero, asi que el resultado es una instancia concreta de `Team`.
Lo mas normel con los metodos de `objects`, sin embargo, es que
no devuelvan objetos, sino un tipo especial de datos llamado
`queryset`, que representa un conjunto de instancias y que, entre
otras cosas, podemos iterar (es decir, usar en en for)

Vamos ahora a obtener un heroe cualquiera. Si no has creado 
ninguno todavía, crealo ahora usando el admin. Vamos a conseguir
este heroe de la misma manera que conseguimos el equipo: pidiendole
al gestor `objects` que nos de el primero que encuentre:

    >>> hero = MetaHuman.objects.first()
    >>> print(hero)
    Spiderman

Ya tenemos un heroe (en la variable `hero`) y un equipo en
la variable `avengers`). Para asignar a este heroe a este
equipo, solo hay que usar el nuevo atributo `team` que
definimos en la clase `MetaHuman`:

    hero.team = avengers
    hero.save()

Es importante la llamada al metodo `save`. Los cambios que se
hagan en los modelos en nuestro programa solo existen en la
memoria RAM del ordenador. No se reflejan en
la base de datos hasta que no se llame al método `save`.

Podemos usar ahora el admin para buscar al heroe en cuestion y verificar
que esta, efectivamente, asignado al equipo de Los Vengadores.

#### El argumento `on_delete`

Cuando se borra un objeto que esta referenciado por una `ForeignKey`, django
sigue un comportamiento que esta copiado del comportamiento equivalente
en las bases de datos relacionales. Estas son las opciones
disponibles.

- `CASCADE`: Viene de la expresion *Borrado en cascada*. Significa que, si
  el modelo referencia se borra, se deben borrar tambián las entidades
  que estan asociadas.

  En nuestro caso no tiene mucho sentido, porque
  el equipo puede desaparecer y los heroes, obviamente, seguir existiendo.

  Pero, por ejemplo, si tenemos el típico modelo Factura - Linea de factura,
  donde una (1)  factura esta compuesta por (N) varias lineas, una por cada
  producto, si que podria tener sentido. Al borrar una factura, que se borren
  también todas las líneas de la misma, porque no tiene sentido la
  existencia de una línea de factura existiendo de forma independiente
  a una factura.

- `PROTECT`: El que hemos usado. En nuestro caso, para poder borrar un
  equipo, debemos desasignar todos los miembros que tenga. Solo cuando
  no haya ninguna referencia al equipo podrá borrarse.
  ¶
- `SET_NULL`: Poner el campo de referencia a `NULL`. Tambien podría
  tener sentido en nuestro caso, vendria a decir que si el equipo
  se borra, entonces todos sus componentes pasana a ser *lobos 
  solitarios*. Obviamente, para poder usar esta opcion, el campo debe
  admitir la posibilidad de ser nulo.

- `SET_DEFAULT`: Similar al anterior, pero en vez de asignar `NULL`, se
  asigna a una especie de grupo pr defecto. Para poder usar esto hay
  que especificar el parametro `default`.

- `SET()`: Se asigna al valor de `Foreignkey` en el modelo el valor
  que se le pase como parámetro a `SET`. Se puede pasar un valor
  o bien un *callable*, cuyo valor devuelto se usara como
  clave foranea.

  Por ejemplo, se podria buscar que grupo tiene el minimo
  numero de componentes y asigar los heroes del equipo borrado
  a este. O elegir un equipo al azar, o elegir un equipo dependiendo
  del día de la semana,  o cualquier otra posibilidad que se nos
  ocurra.

- `DO_NOTHING`: Como su nombre indica, no hace nada. Se usa cuando
  queremos dejar que la propia base de datos resuelvas el problema
  con sus propios mecanismos.

Un parametro interesante es la opcion `limit_choices_to`. En nuestro
caso, por ejemplo, si queremos asignar heroes a un grupo seria
deseable que solo me dejara seleccionar heroes que actualmente
no están asociados a ninguno. Se puede usar un diccionario, un modelo
`Q`(que veremos mas adelante) o directamente un *callable* que devuelva
un diccionario o un objeto `Q`.

Una cosa que hay que destacar, especialmente porque tiene
asociado una cierta "magia", es que al incluir el campo 
en el modelo `MetaHuman`, haciendo referencia al modelo
`Team`, es que hemos modificado, en realidad, ambos modelos.

Por un lado, obviamente, el modelo `MetaHuman` tiene ahora un nuevo
atributo `team`, que sera `None` si el personaje no esta
asociado a ningun equipo, o una instancia del equipo al que
está asignado.

Por otro lado, el modelo `Team` tiene ahora un atributo, que 
nosotros no hemos declarado explicitamente, que le permite
realizar la relacion inversa, es decir, le permite obtener
los personajes que estan asociados al equipo.

El nombre de este atributo "magico" se forma con el nombre del modelo que
realizo el enlace, sequido de `_set` todo en minusculas. En nuestro caso, `Team`
tiene un atributo ahora llamado `metahuman_set`. Este atributo es
un objeto tipo `query_set`, es decir, una representacion de los
modelos que referencian a team.

Vamos a asignar en el admin
dos o tres superheroes mas al grupo de los vengadores, y luego vamos
a ejecutar el shell para comprobar el contenido de este atributo, haremos:

    manage.py shell

Y una vez dentro de Python:

    >>> from metahumans.models import Team, MetaHuman
    >>> avengers = Team.objects.first()
    >>> for hero in avengers.metahuman_set.all():
    ...     print(hero)
    Spiderman
    Iron Man

Dentro del bucle for, la variable `hero` no es simplemente en nombre
del su0erheroe, es un objeto de tipo MetaHuman completo.



OneToOneField¶
class OneToOneField(to, on_delete, parent_link=False, **options)¶
A one-to-one relationship. Conceptually, this is similar to a ForeignKey with unique=True, but the “reverse” side of the relation will directly return a single object.

This is most useful as the primary key of a model which “extends” another model in some way; Multi-table inheritance is implemented by adding an implicit one-to-one relation from the child model to the parent model, for example.

One positional argument is required: the class to which the model will be related. This works exactly the same as it does for ForeignKey, including all the options regarding recursive and lazy relationships.

If you do not specify the related_name argument for the OneToOneField, Django will use the lowercase name of the current model as default value.

With the following example:

from django.conf import settings
from django.db import models

class MySpecialUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    supervisor = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='supervisor_of',
    )
your resulting User model will have the following attributes:

>>> user = User.objects.get(pk=1)
>>> hasattr(user, 'myspecialuser')
True
>>> hasattr(user, 'supervisor_of')
True
A DoesNotExist exception is raised when accessing the reverse relationship if an entry in the related table doesn’t exist. For example, if a user doesn’t have a supervisor designated by MySpecialUser:

>>> user.supervisor_of
Traceback (most recent call last):
    ...
DoesNotExist: User matching query does not exist.
Additionally, OneToOneField accepts all of the extra arguments accepted by ForeignKey, plus one extra argument:

OneToOneField.parent_link¶
When True and used in a model which inherits from another concrete model, indicates that this field should be used as the link back to the parent class, rather than the extra OneToOneField which would normally be implicitly created by subclassing.

See One-to-one relationships for usage examples of OneToOneFie
