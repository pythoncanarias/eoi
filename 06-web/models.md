## Modelos en Django

Cuando queremos almacenar y recuperar imformación sobre
nuestras entidades, en Django definimos modelos.

Si venimos de un diagrama E/R, entonces probablemente
cada entidad se representara con un modelo, ypara cada
modelo definiremos una seride de campos (*fields*), que
equivalen a los atributos del modelo E/R.

Las relaciones, si son especialmente importantes
o tiene atributos, tambien pueden ser implementadas con
modelos.

### Nuestro primer modelo

Vamos a implementar nuestro primer modelo. Viendo el diagrama
de E/R que desarrollamos, hay una entidad que parace bastante
sencilla: los poderes. No tienen muchos atributos 
y son sencillos de entender.


Vamos a crear nuestro primer modelo basado en esta entidad.
Vamos a llamar al modelo `Power`. La convencion es usar la
inicial en mayúsuculas, porque es una clase, y se recomienda
usar siempre la forma singular (Es decir, mejor *Power* que
*powers*)

Basicamente son dos atributos, nombre y descripción. Así
que este es nuestro primer modelo:

    class Power(models.Model):
        name = CharField(max_length=32)
        description = CharField(max_length=120)

Vamos a crear el fichero `models.py` dentro de la carpeta
`metas`. Dentro del fichero importamos `django.models` para
poder tener acceso a la clase base `models.Model` y pegamos la
definición aterior. El fichero debería quedar así:

    from django import models
    
    class Power(models.Model):
        name = models.CharField(max_length=32)
        description = models.CharField(max_length=120)



Ahora podemos ejecutar el comando de manage `check` para ver si todo 
ha ido bien. Si todo va bien, el siguiente paso ahora
es crear una migración para crear tablas en la base
de datos que sirvan para el almacenamiento de este
modelo.

Para ello se usa el comand de manage `migrate`, normalmente indicando
la app sobre la que queremos generar las migraciones. Pero primero
veamos las migraciones que tenemos actualmente reconocidas por el
sistema. Hagamos:

    manage.py showmigrations

Y deberiamos obtener algo como:

    admin
    [X] 0001_initial
    [X] 0002_logentry_remove_auto_add
    [X] 0003_logentry_add_action_flag_choices
    auth
    [X] 0001_initial
    [X] 0002_alter_permission_name_max_length
    [X] 0003_alter_user_email_max_length
    [X] 0004_alter_user_username_opts
    [X] 0005_alter_user_last_login_null
    [X] 0006_require_contenttypes_0002
    [X] 0007_alter_validators_add_error_messages
    [X] 0008_alter_user_username_max_length
    [X] 0009_alter_user_last_name_max_length
    [X] 0010_alter_group_name_max_length
    [X] 0011_update_proxy_permissions
    commons
    (no migrations)
    contenttypes
    [X] 0001_initial
    [X] 0002_remove_content_type_name
    metas
    (no migrations)
    sessions
    [X] 0001_initial

Vemos ahí que tenemos aplicadas todas las migraciones, y vemos que nos aparece
nuestras apps `commons` y `metas`, pero sin ninguna migración. (Si no aparece
`commons` o `metas`, es que nos hemos despistado de incluirlas en la variable
`APPLICATIONS` del fichero de ajustes `settings.py`).

El caso es que hemos creado el modelo, y para que ese cambio se refleje en la
base de datos, el método más cómodo es usar migraciones (La otra opcion es
reflejar el cambio nosotros a mano en la base de datos).

Para que django cree la migracion, lo que hace es comprobar la diferencia entre
el ultimo estado de la base de datos y la configuracion actual de los modelos.

Si no coinciden -como es el caso, ya que hay una nueva entidad y por tanto se
necesita una nueva tabla- se crea una nueva migración, marcada como "sin
aplicar".

Para crear la migración, se usa la orden `makemigrations`, como se
dijo anteriormente.

    python manage.py makemigrations metas

Deberíamos obtener algo como esto

    Migrations for 'metas':
    metas/migrations/0001_initial.py
        - Create model Power

¡Felicidades! Has creado tu primera migración. Una nueva consulta
con `showmigrations` deberia mostrarnos esta nueva migración, no aplicada:

    admin
    [X] 0001_initial
    [X] 0002_logentry_remove_auto_add
    [X] 0003_logentry_add_action_flag_choices
    auth
    [X] 0001_initial
    [X] 0002_alter_permission_name_max_length
    [X] 0003_alter_user_email_max_length
    [X] 0004_alter_user_username_opts
    [X] 0005_alter_user_last_login_null
    [X] 0006_require_contenttypes_0002
    [X] 0007_alter_validators_add_error_messages
    [X] 0008_alter_user_username_max_length
    [X] 0009_alter_user_last_name_max_length
    [X] 0010_alter_group_name_max_length
    [X] 0011_update_proxy_permissions
    commons
    (no migrations)
    contenttypes
    [X] 0001_initial
    [X] 0002_remove_content_type_name
    metas
    [ ] 0001_initial
    sessions
    [X] 0001_initial

Ahora podemos aplicarla con `migrate`:

    python manage.py migrate metas

Tipos de campos disponibles
===========================

Django viene con un conjunto de tipos de campos bastante extenso,
veremos con más detalle cada uno de ellos. Los agruparemos según el tipo
de datos que usará la base de datos subyacente para almacenarlos:

Campos numéricos (Enteros o en coma flotante)
---------------------------------------------

- AutoField
- BigIntegerField
- DecimalField
- IntegerField
- FloatField
- PositiveIntegerField
- PositiveSmallIntegerField
- SmallIntegerField

Campos lógicos (booleanos)
--------------------------

> -   BooleanField
> -   NullBooleanField

Fechas y tiempos
----------------

> -   DateField
> -   DateTimeField
> -   TimeField

Texto
-----

> -   CharField
> -   CommaSeparatedIntegerField
> -   EmailField
> -   IPAddressField
> -   GenericIPAddressField
> -   SlugField
> -   TextField
> -   URLField

Ficheros
--------

Los ficheros, en realidad, se almacenan en la base de datos en un campo
de texto variable, pero tiene unas cuantas particularidades que
aconsejan explicarlos aparte

> -   FileField
> -   FilePathField
> -   ImageField

Cuando usamos un campo de tipo `FileField` o `ImageField`, el archivo
que subimos es almacenado por el servidor en el sistema de ficheros, y
lo que se guarda en la base de datos es una ruta parcial al mismo, en un
campo de texto variable. La ruta absoluta en el sistema de ficheros
(accesible mediante el atributo `path` del campo) se compone a partir de
varios elementos:

> -   En primer lugar, el valor que se haya almacenado en la variable
>     `MEDIA_ROOT`, definida en el fichero `settings.py`. Si no se ha
>     modificado, el valor por defecto de esta variable es una cadena de
>     texto vacía, que viene a significar el directorio de trabajo
>     actual.
> -   En segundo lugar, la ruta que se obtiene de evaluar el parámetro
>     `upload_to` con el que se definió el campo. Podemos usar códigos
>     de formateo como los que usamos en `strftime()`; por ejemplo,
>     usando `%Y` conseguimos que en la ruta se sustituya ese código por
>     el año del día es que se ha realizado la carga
> -   En tercer lugar, el nombre original del fichero
>
> Por ejemplo, si la variable `MEDIA_ROOT` se definió como `/var/media`,
> el campo de tipo `FileField` o `ImageField` se definió con el
> parámetro `upload_to` igual a `fotos/%Y/%m/%d` y el nombre del fichero
> original era `mifoto.jpg`, la ruta final (Si se hubiera subido el 27
> de julio de 2013) sería:
>
>     /var/media/fotos/2013/07/27/mifoto.jpg

Definir tu propio tipo de campo de datos
========================================

Si estos tipos de campos no son suficientes, podemos definir nuestros
propios tipos. Los detalles son un poco más complicados, pero en esencia
lo único realmente importante es decirle a django dos cosas: Como se
almacena nuestro tipo de dato en la base de datos (normalmente en un
`VARCHAR`), y a la inversa, como recuperar, a partir de lo almacenado,
el dato original.

Usar los modelos para hacer consultas y trabajar con la base de datos
=====================================================================

El acceso a los modelos almacenados en la base de datos se realiza
mediante un objeto de tipo `Manager` o controlador. Un *manager* es la
interfaz a traves de la cual se comunica el modelo con la base de datos.
Internamente usa comandos SQL, aunque la mayoría de las veces no nos
hace falta llegar a ese nivel, porque los modelos nos proporcionan
métodos que son más fáciles de usar. Existe siempre **al menos un
manager** para cada modelo que definamos.

Por defecto, al crear un modelo se crea un manager asociado a la tabla
correspondiente y se le pone como nombre `objects`:

> python manage.py shell
>
> \>\>\> from metahumans import models \>\>\> print(models.objects)
> \<django.db.models.manager.Manager object at 0x7f8b4710dc50\> \...

Guardar en la base de datos
---------------------------

Podemos salvar un objeto instanciado de un modelo en la base de datos,
simplemente llamando al método `save`. Django es lo suficientemente
listo como para distinguir si debe hacer un `INSERT` (Crear un registro
nuevo) o un `UPDATE` (modificar un registro ya existente):

    from metahumans import models

    4f = models.Team(name='Los Cuatro Fantásticos', slug='4f')
    4f.save()

Para reflejar un cambio del modelo en la base de datos, también usamos
`save`:

    4f.description = 'La primera familia de superhéroes'
    4f.save()

Recuperar de la base de datos
-----------------------------

Para recuperar objetos desde la base de datos, el *manager* puede
devolvernos en algunos casos el propio objeto (por ejemplo, véase el
método `get`), paro por lo normal nos devuelve un objeto de tipo
`QuerySet`, es decir un conjunto de resultados.

La consulta más simple que podemos hacer es pedir todos los objetos:

    teams = model.Team.objects.all()

En el código anterior, `temas` es un `QuerySet`, que no será ejecutado
hasta que no se le pidan datos. Una forma habitual de pedir datos es
usarlo como iterador en un bucle `for`:

    teams = model.Team.objects.all()  # No hay consulta todavía a la BD
    for t in teams:                   # Aqui se realiza la consulta
        print(t.name)

Podemos modificar el `QuerySet` de forma que, cuando se ejecute la
consulta, obtengamos justo los objetos que estamos buscando. Una forma
de modificarlo es con su método `filter`, que viene a ser equivalente a
la clausula `WHERE` en una consulta SQL: definimos las condiciones que
tienen que cumplir los objetos para que se incluyan en el resultado. En
el siguiente código, solo ontendremos los equipos que estén activos:

    team = models.Team.objects.filter(active=True)

También podemos usar el método `exclude`, que funciona al reves que
`filter`; los objetos que cumplan la condicion indicada son excluidos
del resultado. El siguiente código obtiene el mismo resultado que el
anterior, pero usando `exclude` en vez de `filter`:

> team = models.Team.objects.exclude(active=False)

Normalmente los métodos ejecutados sobre un `QuerySet` devuelven un
`QuerySet` transformado, de forma que podemos encadenar métodos. Por
ejemplo, la siguiente consulta devuelve superhérose en activo y con un
nivel de 9:

> peligrosos = models.SuperHero.objects \# Esta barra indica a Python
>
> :   .filter(active=True) \# que la linea continua .filter(level=9)

Un método de `objects` que no devuelve un `QuerySet` es el método `get`,
que siempre devuelve un (y solo uno) objeto. La expresión que usemos
dentro del `get` puede ser cualquiera de las que puedas usar en un
`filter`, pero es responsabilidad tuya que la consulta devuelva una sola
fila de la tabla. Si no devuelve ninguna, `get` elevará una excepción de
tipo `DoesNotExist`; si devuelve más de una, elevará una excepción del
tipo `MultipleObjectsReturned`. Ambas excepciones están definidas en el
propio modelo:

    >>> try:
    ...    sh = models.SuperHero.objects.get(active=True)
    ... except models.SuperHero.MultipleObjectsReturned as err:
    ...     print(err)
    ... 
    get() returned more than one SuperHero -- it returned 17!
    >>>

Normalmente el `get` se usa con la clave primaria para obtener el objeto
que queremos, para eso podemos especificar el nombre de la clave
primaria o, incluso más fácil, usar el parámetro `pk`, que siempre es un
alias de la clave primaria del modelo:

    >>> capi = models.SuperHero.objects.get(pk=3)

Consultas avanzadas
-------------------

Podemos hacer consultas más potentes, usando una notación especial para
los parametros: separando con un doble caracter subrayado el campo y el
operador. Se ve más claro con un ejemplo, el siguiente código devuelve
todos los superheroes con nivel mayor que cinco:

    amenazas = models.SuperHero.objects.filter(level__gt=4)

El nombre del parámetero es `level__gt`, al incluir el doble subrayado,
indicamos que el campo es `level`, y que el operador a usar es `gt` (Más
grande que: *Greater Than*). Otras formas de expresar esta misma
consulta podrían ser:

    amenazas = models.SuperHero.objects.filter(level__gte=5)
    amenazas = models.SuperHero.objects.exclude(level__lt=5)
    amenazas = models.SuperHero.objects.exclude(level__lte=4)

Existen muchos operadores, que están ampliamente descritos en la
documentación de Django, pero resultan especialmente interesantes
`contains` e `icontains` para búsquedas en texto (la *i* de `icontains`
sirve para indicar que la búsqueda no debe considerar como letras
diferentes las mayúsculas de las minúsculas):

    spideramenazas =  models.SuperHero.objects.filter(
        name__icontains = 'spider'
        )

Podemos usar `in` para buscar que el valor este dentro de los indicados
en una lista:

    nenazas = models.SuperHero.objects.filter(
        level__in = [1,2,3]
        )

Y podemos usar `year`, `month`, `day`, `week_day`, `hour`, `minute` y
`second` para hacer consultas usando campos de fecha o *timestamp*:

    creados_2015 = models.SuperHero.objects.filter(created__year=2015)

Un error muy comun es olvidarse de usar los dos caracteres subrayados y
poner solo uno:

    >>> nenazas = models.SuperHero.objects.filter(
    ...     level_in = [1,2,3]
    ...     )
    Traceback (most recent call last):
    ... Blah, blah, blah ...
    FieldError: Cannot resolve keyword 'level_in' into field.

También podemos usar el doble caracter subrayado para hacer una consulta
a un modelo relacionado con el modelo que estamos usaudo. Para ello
usamos la forma:

    <nombre de campo relacionado>__<campo en tabla_relacionad>

Por ejemplo:

    ff = models.SuperHero.objects.filter(team__name='Los 4 Fantásticos')

Consultas con SQL Crudo
-----------------------

En algunos casos las consultas que podemos hacer con los modelos pueden
ser más complicadas que su equivalente en SQL. Existen unos objetos,
`django.db.models.Q`, que nos permiten hacer consultas muy complicadas.
Aun asi, si no vemos mejor opción, podemos hacer directamente la
consulta en SQL usando el método `raw`, que acepta como parámetro una
sentencia SQL y nos devuelve, como es habitual, un `QuerySet`.

POr ejemplo, obtengamos usando `raw` los equipos, con un atributo
añadido indicando cuantos miembros tiene asignados:

    teams = Team.objects.raw('''
        SELECT T.id, T.name, count(*) AS num_members 
          FROM mh_team T
          LEFT JOIN mh_superhero SH ON T.id = SH.team_id
         GROUP BY T.id, T.Name
        ''')
    for t in teams:
        print t.name, t.num_members

Este **no es el método recomendado** para hacer esta consulta. Es mejor
limitar las consultas hechas con SQL puro, ya que suelen depender mucho
del gestor de base de datos que estemos usando. Esto crea unas
dependencias que después pueden ser muy complicadas de deshacer. No
obstante, es una posibilidad que existe y en algunos casos -muy pocos,
en realidad- no tendremos más remedio que usarla.

Si la consulta es tan complicada que ni con el método `raw` podemos
obtener lo que queremos, podemos ignorar totalmente los modelos y hacer
una consulta SQL directamente a la base de datos, usando la variable
`django.db.connection`, que el el handler de la base de datos definida
por defecto:

    # reactivamos todos los superheroes ¡Es la guerra!
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("UPDATE mh_superhero SET active = 1")

Limitar el tamaño del resultado
-------------------------------

Podemos modificar un `QuerySet` para que solo devuelva un número máximo
de resultados, o los resultados comprendidos entre un rango de valores.
Para ello lo usamos como si fuera una lista de Python: usando corchetes,
índice inferior (contado el primero como cero) e índice superior:

    f = models.SuperHero.objects.all()[0:5]
    assert len(list(f)) <= 5

No obstante, un QuerySet no es una lista, una de las diferencias es que
no podemos usar índices negativos.

Limitar el tamaño no ejecuta la consulta; como casi todos los métodos
vistos, devuelve un nuevo `QuerySet` modificado a partir del anterior.
