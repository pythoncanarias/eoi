---
title: Modelos en Django
tags:
    - Database
---

## Introducción a los modelos en Django

Cuando queremos almacenar y recuperar imformación sobre nuestras
entidades, en Django definimos **modelos**.

Si venimos de un diagrama E/R, entonces probablemente cada entidad se
representará con un modelo, y para cada modelo definiremos una serie de
de **campos** (*fields*), que equivalen a los atributos del modelo E/R.

Las relaciones, si son especialmente importantes o tiene atributos,
tambien pueden ser implementadas con modelos.

### Nuestro primer modelo

Vamos a implementar nuestro primer modelo. Viendo el diagrama de E/R que
desarrollamos, hay una entidad que parace bastante sencilla: los
poderes. No tienen muchos atributos y son sencillos de entender.

Vamos a crear nuestro primer modelo basado en esta entidad. Vamos a
llamar al modelo `Poder`. La convención es usar la inicial en
mayúsculas, porque es una clase, y se recomienda usar siempre la forma
singular (Es decir, mejor `Poder` que `poderes`)

Básicamente para este modelos solo es necesario un atributos, el
nombre del poder. Así que este es nuestro primer
modelo:

```python
class Poder(models.Model):
    nombre = CharField(max_length=80)
```
        
Vamos a crear el fichero `models.py` dentro de la carpeta `metahumans`.
Dentro del fichero importamos `django.models` para poder tener acceso a
la clase base `models.Model` y pegamos la definición aterior. El fichero
debería quedar así:

```python
from django import models

class Poder(models.Model):
    nombre = CharField(max_length=80)
```

Ahora podemos ejecutar el comando de manage `check` para ver si todo ha
ido bien:

```shell
python manage.py check
```

El siguiente paso, si no hay errores, es crear una migración para crear
tablas en la base de datos que sirvan para el almacenamiento de este
modelo.

Para ello se usa el comando de manage `migrate`, normalmente indicando
la app sobre la que queremos generar las migraciones. Pero primero
veamos las migraciones que tenemos actualmente reconocidas por el
sistema. Hagamos:

```shell
manage.py showmigrations
```

Y deberiamos obtener algo parecido a esto:

```shell
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
contenttypes
[X] 0001_initial
[X] 0002_remove_content_type_name
metahumans
(no migrations)
sessions
[X] 0001_initial
```

La salida muestra que tenemos aplicadas todas las migraciones. Vemos también
que aparece nuestras app `metahumans`, pero sin ninguna migración. (Si no
aparece `metahumans`, es que nos hemos despistado de incluirlas en la variable
`INSTALLED_APPS` del fichero de ajustes `settings.py`).

El caso es que hemos creado el modelo, y para que ese cambio se refleje en la
base de datos, el método más cómodo es usar migraciones (La otra opcion es
reflejar el cambio nosotros a mano en la base de datos).

Para que django cree la migración, lo que hace es comprobar la diferencia entre
el último estado de la base de datos y la configuración actual de los modelos.

Si no coinciden -como es el caso, ya que hay una nueva entidad y por tanto se
necesita una nueva tabla- se crea una nueva migración, marcada como "sin
aplicar".

Para crear la migración, se usa la orden `makemigrations`, como se
explicó anteriormente:

```shell
python manage.py makemigrations metas
```

Deberíamos obtener una salida similar a:

```shell
Migrations for 'metahumans':
metahumans/migrations/0001_initial.py
    - Create model Poder
```

¡Felicidades! Has creado tu primera migración. Una nueva consulta con
`showmigrations` deberia mostrarnos esta nueva migración, no aplicada:

```
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
contenttypes
[X] 0001_initial
[X] 0002_remove_content_type_name
metahumans
[ ] 0001_initial
sessions
[X] 0001_initial
```

Ahora podemos aplicarla con `migrate`:

```shell
python manage.py migrate metahumans
```

Ahora `showmigrations` indica con `[X]` que esa migración ya ha sido
aplicado. Podemos hacer el `migrate` de nuevo. Esta segunda vez no hará
nada, porque el sistema es lo suficientemente listo como para saber que
no debe aplicar la misma migración dos veces. Podemos hacer la operación
de migrate todas las veces que queramos, solo se ejecura realmente en la
primera llamada.

### Opciones comunes para todos los campos

Los siguientes campos estan disponibles para todos los campos. Todos son
opcionales.

- `null` (*bool*): Si se establece a `True`, los valores vacíos se
  almacenaran en la base de datos usando `NULL`, Por defecto es
  `False`.

  El parámetro `blank` también debe estar a `True` para que se
  permitan valores vacíos en el modelo. El parámetro `null` solo se
  refiere al almacenamiento en la bse de datos.

- `blank` (*bool*): Si esta a `True`, se permite que el campo quede
  sin definir o vacio. Por defecto es `False`, es decir, que todos los
  campos por defecto son obligatorios.
  
- `choices` (*sequence of tuples*): Una secuencia de duplas (Tuplas de
  dos elementos). El primer elemento de la tupla se usara como código
  y es el valor que se almacenará en la base de datos, mientras que el
  segundo se usara como descripción, legible por humanos.
  
- `db_column` (*str*): El nombre del campo en la tabla de la base de
  datos. Si no se especifica, se usara el nombre del campo.
  
- `db_index` (*bool*): Si se define como `True`, se creará un índice
  en la base de datos para este campo. Dependiendo del tipo de campo
  tendra un valor por defecto uy otro.
  
- `db_tablespace` (*str*): Para las bases de datos que soportan
  estacios de nombres.
  
- `default` (*Any*): El valor por defecto. Puede ser un valor en si o
  un *callable*. En este segundo caso, se llamará al *callable* cada
  vez que se cree un nuevo registro.

  El valor por defecto no puede ser un objeto mutable, como una
  instancia, una lista, un conjunto, etc. Si se permitirera, todas las
  instancias compartirian ese objeto. Si queremos usar, por ejemplo,
  una lista, la forma mas sencilla es envolver ese valor en un
  *callable*.

  No se pueden usar lambdas para definir valores por defecto, porque
  no pueden ser serializadas por las migraciones.

- `editable` (*bool*): Si esta a `False`, el campo no aparece en el
  admin ni en ningún `ModelForm` derivado de lmodelo. Tambien se
  ingora estos campos a efectos de validación.
  
- `error_messages` (*dict*): Este parámetro permite redefinir el texto
  de los mensajes de error que se pueden originar desde este campo. Es
  un diccionario cuyan claves deben coincidir con los mensajes de
  error que quieres reescribir.
  
- `help_text` (*str*): Texto de ayuda sobre el campo.

- `primary_key` (*bool*): Indica que este canpo es la clave primaria.
  Django limita a los modelos de forma que solo un campo puede ser
  clave primaria.

  Si no se especifica ningún campo para que sea la clave primaria, se
  crea auntomaticamente un campo `id` como autonumérico y clave
  primaria.

  Si definimos un campo como clave primaria, obligatoriamente `null`
  es `False` y `unique` es `True`.

  El campo se comporta ahora como de solo lectura. Si se modifica el
  campo de clave primaria de un objeto y se salva de nuevo se creará
  un nuevo registro.

- `unique` (*bool*) : Si se ajusta a `True`, se prohiben valores
  duplicados para este campo. Esto se fuerza tanto a nivel del modelo
  como de la base de datos, normalmente creando un índice sobre el
  campo.
  
- `unique_for_date` (*str*) : Como el anterior, pero solo para los
  regitros que tienen la misma fecha en el campo indicado.
  
- `unique_for_month` (*str*) : Como el anterior, pero solo para los
  regitros que tienen el mismo mes y año que la fecha en el campo
  indicado.
  
- `unique_for_year` (*str*) : Como el anterior, pero solo para los
  regitros que tienen el mismo año que la fecha en el campo indicaddo.
  
- `verbose_name` (*str*) : Versión del nombre apropiada para un humano.

- `validators` (*list*): Lista de funciones validadoras a aplicar a
  este campo.

### Tipos de campos disponibles

Django viene con un conjunto de tipos de campos bastante extenso,
veremos con más detalle cada uno de ellos. Los agruparemos según el tipo
de datos que usará la base de datos subyacente para almacenarlos:

#### Para almacenar números

- `IntegerField`
- `AutoField`
- `BigIntegerField`
- `DecimalField`
- `FloatField`
- `PositiveIntegerField`
- `PositiveSmallIntegerField`
- `SmallIntegerField`

El campo `IntegerField` es un campo que podemos usar para almacenar
números enteros. Dependiendo de la base de datos que se esté utilizando,
el rango de valores posibles puede variar, pero el rango desde
$-2147483648$ hasta $2147483647$ es soportado por todas las bases de
datos que Django soporta.

El tipo `AutoField` Es un campo numérico similar a `IntegerField`, pero
con la diferencia de que aumentará de valor automáticamente cada vez que
añadamos un nuevo registro o fila a la tabla. Es el que se utiliza de
forma automática para las claves primarias si no lo hemos hecho al
definir el modelo.

El campo `BigIntegerField` almacena enteros también, pero garantiza que
el rango de valores posibles será mayor (Internamente fuerza a usar 64
bits), así que los valores que puede almacenar van desde
$-9223372036854775808$ a $9223372036854775807$.

Tanto el campo `FloatField` como `DecimalField` permiten almacenar
valores numéricos decimales, es decir, los que tienen una parte
*decimal*. La diferencia es que `FloatField` almacena esta información
usando el formato de coma flotante, que es útil para almacenar con la
máxima precisión que la máquina nos pueda dar. `DecimalField`, por otro
lado, limita expresamente la cantidad de dígitos que podemos representar
despues de la coma.

El uso de `DecimalField` es, por tanto, especialmente indicado para
almacenar valores de monedas, en las cuales las subdivisiones llegan
solo hasta un determinado nivel. Por ejemplo, $3.45$ euros tiene sentido
(3 euros y 45 céntimos) pero $3.449$ euros no tiene sentido, no existen
subdivisiones del céntimo. Usaremos `FloatField` cuando queremos
mantener la precisión más alta posible, para cálculos precisos.

**Ejrrcicio**: Comprobar que:

```python
(0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1) - 1.0
```

No da exactamente cero:

```
-1.1102230246251565e-16
```

Un campo `SmallIntegerField` almacena enteros, pero el rango de valores
posibles es inferior al de `IntegerField`. Los límites del rango
dependen de la base de datos usada, pero podemos asumir como seguro el
rango de $-32768$ a $32767$.

Los campos `PositiveIntegerField` y `PositiveSmallIntegerField` son como
`IntegerField` y `SmallIntegerField`, pero con la limitación de que solo
aceptan valores positivos.

#### Para almacenar valores lógicos (booleanos)

- `BooleanField`

Si queremos que acepte, además de `True` y `False`, el valor
[None]{.title-ref}, tendremos que incluir el argumento `null=True`.
Anteriormente habia una clase `NullBooleanField`, pero esta obsoleta y
no desaconseja su uso desde la versión \$2.1\$ de Django.

### Para almacenar fechas y tiempos

- `DateField`

- `DateTimeField`

- `TimeField`

- `DurationField`

Estos campos se usan para añadir a nuestro modelos fechas, tiempos o
marcas temporales (fecha+tiempo). Hay dos parámetros que se suelen usar
mucho con estos tipos de datos:

- `auto_now` ajusta automaticamente el valor del campo al momento o
    dia actual cada vez que el modelo es modificado y almacenado en la
    base de datos. De esta forma obtenemos un campo que registra siempre
    el ultimo momento en que un registro ha sido alterado.
    
- `auto_now_add` ajusta también automáticamente el valor, pero solo la
    primera vez, es decir, cuando el registro se ha creado. Las
    siguientes operaciones que cambien valores en el registro no afectan
    a este valor.

Si usamos estas opciones, no podemos usar `default`, y viceversa, ya que
entran en conflicto.

![CSV no](img/nick-fury-csv-is-shit.png)


**Ejercicio**: Añadir al modelo `Poder` un campo, de uso interno,
que llamaremos `fecha_creacion` para que se almacenen los cambios cada vez
que se añade un nuevo poder.

Recuerda que debes:

1) Modificar el modelo

2) Comprobar que no hay errores (`manage.py check`)

3) Crear la migración (`manage.py makemigrations`)

4) Opcionalmente, comprobar que la migración existe pero no esta
    aplicada (`manage.py showmigrations`)
    
5) Aplicar la migración (`manage.py migrate`)

6) Opcionalmente, comprobar que la aplicacion ha sido aplicada
    (`manage.py showmigrations`)

#### Campos para almacenar ficheros

- `FileField`
- `FilePathField`
- `ImageField`

Cuando usamos un campo de uno de estos tipos, el archivo que subimos es
almacenado por el servidor en el sistema de ficheros, y lo que se guarda en la
base de datos es una *ruta parcial* al mismo, en un campo de texto variable.

La ruta absoluta en el sistema de ficheros (accesible mediante el atributo
`path` del campo) se compone a partir de varios elementos:

- En primer lugar, el valor que se haya almacenado en la variable `MEDIA_ROOT`,
  definida en el fichero `settings.py`. Si no se ha modificado, el valor por
  defecto de esta variable es una cadena de texto vacía, que viene a significar
  el directorio de trabajo actual.

- En segundo lugar, la ruta que se obtiene de evaluar el parámetro `upload_to`
  con el que se define el campo. Podemos usar códigos de formateo como los que
  usamos en `strftime()`; por ejemplo, usando `%Y` conseguimos que en la ruta
  se sustituya ese código por el año del día es que se ha realizado la carga.

- En tercer lugar, el nombre original del fichero.

Por ejemplo, si la variable `MEDIA_ROOT` se definió como `/var/media`, el campo
de tipo `FileField` o `ImageField` se definió con el parámetro `upload_to`
igual a `fotos/%Y/%m/%d` y el nombre del fichero original era `mifoto.jpg`, la
ruta final (Si se hubiera subido el 27 de julio de 2019) sería:

```
/var/media/fotos/2019/07/27/mifoto.jpg
```

Con `FilePathField` podemos limitar la opción del archico a un determinado
directorio o sistema de archivos. Tiene varios parámetros específicos, pero el
primero y obligatorio es la ruta base desde la que se pueden cargar los
ficheros. La opción `match` nos permite también definir una expresión regular
que límite aun más las posibles opciones. Por ejemplo `.*\.txt$` limita las
opciones a ficheros que tengan la extensión `.txt`.

`ImageField` es una especialización de `FileField` que permite almacenar
imágenes. Si la libreria `Pillow` está instalada, esto nos ppropordiona
posibilidades adicionales, como acceder a la anchura y altura en pixels de la
imagen.

#### Campos para almacenar textos

- `CharField`

- `TextField`

- `EmailField`

- `GenericIPAddressField`

- `URLField`

- `SlugField`

Los campos `CharField` y `TextField` son ambos utiles para guardar textos. La
diferencia estriba en el tamaño.

Se espera que `CharField` sea para campos de texto relativamente pequeños (Por
ejemplo, el nombre del puesto en una oferta de trabajo, algo como `Python
Developer`), mientras que en `TextField` se espera guardar cantidades de texto
mayores (De nuevo con el ejemplo de una oferta de empleo, la descripción
completa del puesto, incluyendo deberes y responsabilidades). La app `admin`
reconoce esta diferencia y usa controles diferentes para cada campo.

Los campos `EmailField`, `GenericIPAddressField` y `URLField` son campos de
texto especializados en cada uno de los valores indicados por su nombre. Se
realizan validaciones de forma automática para cada uno de estos campos.

Por último, `SlugField` es un término traido de los periodicos. Es una etiqueta
corta, que se usa normalmente para identificar o discriminar, y que contiene
solo letras, números y los símbolos `_` y `-`. No pueden contener espacios, por
ejemplo. Esto hace que se usan generalente para formar parte de un URL. Una
entrada de un blog, por ejemplo, podria usar un *slug* basado en el titulo para
crear una URL permanente que apunta a dicha entrada.

Igual que un `CharField`, podemos especificar una longitud máxima. Por defecto
es $50$. A nivel de base de datos, se creara también un índice, lo que en la
práctica impide usar valores duplicados y convierte al *slug* en una clave
candidata o al menos en parte de una clave candidata.

A menudo es útil precalcular o establecer un valor inicial de forma automática
al campo *slug* basandonos en otros campos. Se puede definir esto
automaticamente en el admin usando la propiedad `prepopulated_fields`.

Si especificamos `allow_unicode` como `True` (Por defecto es `False`) el campo
aceptará tambien letras `unicode`, como `á`, en vez de limitarse a letras
ASCII.

### Campos para definir las relaciones

Django también define una serie de campos para reflejar las relaciones
entre modelos.

La más usade es `ForeignKey`, que se usa para representar una relacion
uno a muchos ($1$ a $N$). Requiere obligatoriamente al menos dos
parámetros: La clase con la que se quiere relacionar el modelo y un
parámetro llamado `on_delete` que explicaremos más adelante.

Vamos a crear la relación 1 a N que teniamos en nuestro diagrama E/R
entre un superheroe (O supervillano) y un equipo. En nuestro análisis no
se permitía que un metahumano fuera parte de más de un equipo, pero si
se permitía que fuera por solitario, es decir, que podia no pertener a
ningun grupo.

Lo primero que tenemos que hacer es crear el nuevo módelo para el
equipo, vamos a llamarlo `Equipo`, y por ahora solo nos interesan dos
campos, el nombre del supergrupo, y el nombre de su base
o cuartel general. Algo como esto:

```python
class Equipo(models.Model):

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    id = models.AutoField(primary_key=True)  # No es estrictamente necesario
    nombre = models.CharField(max_length=100)
    cuartel = models.CharField(max_length=240, blank=True)  # blank=True significa opcional

    def __str__(self):
        return self.nombre
```

**Nota: Uso de la clase Meta** Una cosa nueva que hemos usado en este modelo
`Equipo` es una clase definida dentro del modelo llamado `Meta`. Esta es una
convención que usa Django para añadir meta-informacion sobre el modelo. En este
caso estamos añadiendo información acerca de cual es el nombre con el que nos
referimos coloquialmente a esta entidad, en dos versiones, para singular
"equipo" y el plural "equipos".

Añadimos esta definición al fichero `metahumans/models.py`. Al añadir
esta nueva clase, nuestra base de datos ya no está en sintonía con
nuestro modelos, asi que habrá que crear y aplicar una migración para
crear esta tabla.

Vamos a incluir este nuevo modelo en el *admin*, edita el fichero
`metahumans/admin.py` y añade las siguientes líneas:

```python
class EquipoAdmin(admin.ModelAdmin):
    list_display = (‘nombre’, ‘cuartel’)

admin.site.register(models.Equipo, EquipoAdmin)
```


Ahora que ya tenemos el modelo `Equipo` y `Poder`, podemos 
crear la clase `Metahumano`, incluyendo una referencia N:1 a
la clase `Equipo` y otra N:N para los poderes

Modifiquemos `models.py` para añadir la siguiente clase:

```python
class Metahumano(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    identidad = models.CharField(max_length=100)
    nivel = models.PositiveIntegerField(default=1)
    equipo = models.ForeignKey(
        Equipo,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    poderes = models.ManyToManyField(Poder)

    def __str__(self):
        return self.nombre
```

En el campo `equipo` hemos creado una referencia al modelo `Equipo` usando
un campo de tipo `ForeignKey`. Las opciones `blank`, `null` y `default`
nos permiten incluir la posibilidad de que el metahumano pertenezca a un
grupo o no. La opción `on_delete`, que es obligatoria, esta ajustada en
este caso a `PROTECT`. Veremos más adelante otras posibilidades para
este parámetro.

Por ahora, lo que nos interesa saber sobre el valor de `on_delete` es
que nos permite definir el comportamiento del sistema si se borra una
entidad de la clase referenciada; en nuestro caso, que hacemos con los
metahumanos que pertenencen a un grupo si dicho grupo se borra.

El valor `PROTECT` significa: Si el grupo que quieres borrar tiene algún
metahumano asignado, impide el borrado. Es decir, solo se permite el
borrado si ningun metahumano esta asignado a este grupo.

Se crea un índice de forma automática para cada clave foranea o
`ForeignKey`. Podemos desabilitar esto usando el parámetro `db_index` a
`False`.

¿Qué está pasando a nivel de base de datos? django añade un campo con el
nombre que hemos indicado (en nuestro caso, `equipo`) pero añadiendole
`_id`, de forma que a nivel de base de datos, en la tabla se crea un
nuevo campo `equipo_id`. En ese campo se guardará el valor de la clave
primaría del equipo, cuando se asigne este superheroe al mismo.

Pero normalmente, no tenemos que preocuparnos de este campo, a no ser
que estemos trabajando directamente al nivel de base de datos. Si usamos
el ORM, siempre trabajaremos directamente con el atribute `equipo`.

Vamos a asignar uno de nuestros superheroes a nuestro recien creado
grupo de Los Vengadores, pero no lo vamos a hacer con el admin, vamos a
hacerlo directamente desde Python.

Vamos a ejecutar un nuevo comando de `manage.py`, `shell`:

```shell
python manage.py shell
```

Esto nos abrira un shell de Python, como el normal que tenemos
instalado, pero con la diferencia de que Django se ha inicializado
previamente, de forma que podemos acceder a los modelos. Lo primero que
vamos a hacer es importar `Equipo` y `Metahumano`:

```shell
>>> from metahumans.models import Equipo, Metahumano
```

Una vez obtenido acceso a los modelos, vamos a pedirle al modelo `Equipo`
que nos devuelve un objeto de este tipo. En principio el primero que
encuentre, pero como solo hemos creado uno, debería devolvernos el de
Los vengadores:

```python
>>> avengers = Equipo.objects.first()
>>> print(avengers)
Vengadores
```

Dentro de cada modelo hay un gestor, que por defecto tiene el nombre de
`objects` que nos permite realizar operaciones con el modelo como hacer
búsquedas o filtros por determinados valores (una consulta o *query* en
la jerga de base de datos).

En este caso concreto, le hemos pedido que nos devuelve el primero, asi
que el resultado es una instancia concreta de `Equipo`. Lo mås normal con
los métodos de `objects`, sin embargo, es que no devuelvan objetos, sino
un tipo especial de datos llamado `queryset`, que representa un conjunto
de instancias y que, entre otras cosas, podemos *iterar* (es decir, usar
en en for).

Vamos ahora a obtener un heroe cualquiera. Si no has creado ninguno todavía,
crea uno ahora usando el admin. Vamos a conseguir este heroe de la misma manera
que conseguimos el equipo: pidiendole al gestor `objects` que nos de el primero
que encuentre:

```python
>>> hero = Metahumano.objects.first()
>>> print(hero) Spiderman
```

Ya tenemos un heroe (en la variable `hero`) y un equipo en la variable
`avengers`). Para asignar a este heroe a este equipo, solo hay que usar
el nuevo atributo `team` que definimos en la clase `Metahumano`:

```python
>>> hero.team = avengers
>>> hero.save()
```

Es importante la llamada al metodo `save`. Los cambios que se hagan en
los modelos en nuestro programa solo existen en la memoria RAM del
ordenador. No se almacenan en la base de datos hasta que no se llame al
método `save`.

Podemos usar ahora el admin para buscar al heroe en cuestion y verificar
que esta, efectivamente, asignado al equipo de Los Vengadores.

### El argumento `on_delete`

Cuando se borra un objeto que esta referenciado por una `ForeignKey`,
django sigue un comportamiento que está copiado del comportamiento
equivalente en las bases de datos relacionales. Estas son las opciones
disponibles:

- `CASCADE`: Viene de la expresion *Borrado en cascada*. Significa que, si el
  modelo referencia se borra, se deben borrar tambián las entidades que estan
  asociadas.

  En nuestro caso no tiene mucho sentido, porque el equipo puede desaparecer y
  los heroes, obviamente, seguir existiendo.

  Pero, por ejemplo, si tenemos el típico modelo Factura / Línea de factura,
  donde una (1) factura esta compuesta por (N) varias lineas, una por cada
  producto, si que podria tener sentido. Al borrar una factura, que se borren
  también todas las líneas de la misma, porque no tiene sentido la existencia
  de una línea de factura existiendo de forma independiente a una factura.

- `PROTECT`: El que hemos usado. En nuestro caso, para poder borrar un equipo,
  debemos desasignar todos los miembros que tenga. Solo cuando no haya ninguna
  referencia al equipo podrá borrarse.

- `SET_NULL`: Poner el campo de referencia a `NULL`. Tambien podría tener
  sentido en nuestro caso, vendria a decir que si el equipo se borra, entonces
  todos sus componentes pasan a a ser *lobos solitarios*. Obviamente, para
  poder usar esta opción, el campo debe admitir la posibilidad de ser nulo.

- `SET_DEFAULT`: Similar al anterior, pero en vez de asignar `NULL`, se asigna
  a una especie de grupo pr defecto. Para poder usar esto hay que especificar
  el parámetro `default`.

- `SET`: Se asigna al valor de `Foreignkey` en el modelo el valor que se le
  pase como parámetro a `SET`. Se puede pasar un valor o bien un *callable*,
  cuyo valor devuelto se usara como clave foranea.

  Por ejemplo, se podria buscar que grupo tiene el mínimo numero de componentes
  y asigar los heroes del equipo borrado a este. O elegir un equipo al azar, o
  elegir un equipo dependiendo del día de la semana, o cualquier otra
  posibilidad que se nos ocurra.

- `DO_NOTHING`: Como su nombre indica, no hace nada. Se usa cuando queremos
  dejar que la propia base de datos resuelvas el problema con sus propios
  mecanismos.

Un parámetro interesante es la opcion `limit_choices_to`. En nuestro caso, por
ejemplo, si queremos asignar heroes a un grupo seria deseable que solo me
dejara seleccionar heroes que actualmente no están asociados a ninguno. Se
puede usar un diccionario, un modelo `Q` (Que veremos más adelante) o
directamente un *callable* que devuelva un diccionario o un objeto `Q`.

Una cosa que hay que destacar, especialmente porque tiene asociado una cierta
_magia_, es que al incluir el campo en el modelo `Metahumano`, haciendo
referencia al modelo `Equipo`, es que hemos modificado, en realidad, ambos
modelos.

Por un lado, obviamente, el modelo `Metahumano` tiene ahora un nuevo atributo
`team`, que sera `None` si el personaje no esta asociado a ningun equipo, o una
instancia del equipo al que está asignado.

Por otro lado, el modelo `Equipo` tiene ahora un atributo, que nosotros no hemos
declarado explicitamente, que le permite realizar la relacion inversa, es
decir, le permite obtener los personajes que estan asociados al equipo.

El nombre de este atributo _mágico_ se forma con el nombre del modelo que
realizó el enlace, sequido de `_set` todo en minúsculas. En nuestro caso,
`Equipo` tiene un atributo ahora llamado `metahuman_set`. Este atributo es un
objeto tipo `query_set`, es decir, una representación de los modelos que
referencian a team.

Vamos a asignar en el admin dos o tres superheroes más al grupo de los
vengadores, y luego vamos a ejecutar el shell para comprobar el contenido de
este atributo, haremos:

```shell
python manage.py shell
```

Y una vez dentro de Python:

```python
>>> from metahumans.models import Equipo, Metahumano
>>> avengers = Equipo.objects.first()
>>> for hero in avengers.metahumano_set.all():
...     print(hero)
Spiderman
Iron Man
```

Dentro del bucle `for`, la variable `hero` no es simplemente en nombre del
superheroe, es un objeto de tipo `Metahumano` completo.

### Definir tu propio tipo de campo de datos

Si estos tipos de campos no son suficientes, podemos definir nuestros propios
tipos. Los detalles son un poco más complicados, pero en esencia lo único
realmente importante es decirle a django dos cosas: Como se almacena nuestro
tipo de dato en la base de datos (normalmente en un `VARCHAR`), y a la inversa,
como recuperar, a partir de lo almacenado, el dato original.

### Usar los modelos para hacer consultas y trabajar con la base de datos

El acceso a los modelos almacenados en la base de datos se realiza mediante un
objeto de tipo `Manager` o controlador. Un *manager* es la interfaz a traves de
la cual se comunica el modelo con la base de datos.  Internamente usa comandos
SQL, aunque la mayoría de las veces no nos hace falta llegar a ese nivel,
porque los modelos nos proporcionan métodos que son más fáciles de usar. Existe
siempre **al menos un manager** para cada modelo que definamos.

Por defecto, al crear un modelo se crea un manager asociado a la tabla
correspondiente y se le pone como nombre `objects`:

```python
python manage.py shell

>>> from metahumans import models 
>>> print(models.Equipo.objects)
<django.db.models.manager.Manager object at 0x7f8b4710dc50\> 
...
```

### Guardar en la base de datos

Podemos salvar un objeto instanciado de un modelo en la base de datos,
simplemente llamando al método `save`. Django es lo suficientemente listo como
para distinguir si debe hacer un `INSERT` (Crear un registro nuevo) o un
`UPDATE` (modificar un registro ya existente) en la base de datos:

```python
from metahumans import models

4f = models.Equipo(name='Los Cuatro Fantásticos')
4f.save()
```

Para reflejar un cambio del modelo en la base de datos, también usamos
`save`:

```python
4f.nombre = 'Cuatro Fantásticos'
4f.save()
```

### Recuperar de la base de datos

Para recuperar objetos desde la base de datos, el *manager* puede devolvernos
en algunos casos el propio objeto (por ejemplo, véase el método `get`), paro
por lo normal nos devuelve un objeto de tipo `QuerySet`, es decir un conjunto
de resultados.

La consulta más simple que podemos hacer es pedir todos los objetos:

```python
equipos = model.Equipo.objects.all()
```

En el código anterior, `equipos` es un `QuerySet`, que no será ejecutado
hasta que no se le pidan datos. Una forma habitual de pedir datos es
usarlo como iterador en un bucle `for`:

    equipos = model.Equipo.objects.all()  # No hay consulta todavía a la BD
    for t in equipos:                     # Aqui se realiza la consulta
        print(t.nombre)

Podemos modificar el `QuerySet` de forma que, cuando se ejecute la
consulta, obtengamos justo los objetos que estamos buscando. Una forma
de modificarlo es con su método `filter`, que viene a ser equivalente a
la clausula `WHERE` en una consulta SQL: definimos las condiciones que
tienen que cumplir los objetos para que se incluyan en el resultado. En
el siguiente código, solo obtendremos los metahumanos que estén activos:

```python
activos = Metahumano.objects.filter(activo=True)
```

También podemos usar el método `exclude`, que es la inversa de `filter`;
los objetos que cumplan la condicion indicada son excluidos del
resultado. El siguiente código obtiene el mismo resultado que el
anterior, pero usando `exclude` en vez de `filter`:

```python
Metahumano.objects.exclude(activo=False)
```

Normalmente los métodos ejecutados sobre un `QuerySet` devuelven un
`QuerySet` transformado, de forma que podemos encadenar métodos. Por
ejemplo, la siguiente consulta devuelve metahumanos en activo y con un
nivel mayor de 90:

    activos = Metahumano.objects.filter(activo=True)
    peligrosos = activos.filter(nivel__gte=90)

Un método de `objects` que no devuelve un `QuerySet` es el método `get`,
que siempre devuelve un (y solo uno) objeto.

La expresión que usemos dentro del `get` puede ser cualquiera de las que
puedas usar en un `filter`, pero es responsabilidad tuya que la consulta
devuelva **una única fila de la tabla**.

Si no devuelve ninguna, `get` elevará una excepción de tipo
`DoesNotExist`; si devuelve más de una, elevará una excepción del tipo
`MultipleObjectsReturned`. Ambas excepciones están definidas en el
propio modelo:

```python
>>> try:
...    sh = Metahumano.objects.get(active=True)
... except models.SuperHero.MultipleObjectsReturned as err:
...     print(err)
... 
get() returned more than one SuperHero -- it returned 17!
>>>
```

Normalmente el `get` se usa con la clave primaria para obtener el objeto
que queremos, para eso podemos especificar el nombre de la clave
primaria o, incluso más fácil, usar el parámetro `pk`, que siempre es un
ál\ias de la clave primaria del modelo:

```python
>>> capi = models.Metahumano.objects.get(pk=3)
```

### Consultas avanzadas

Podemos hacer consultas más potentes, usando una notación especial para
los parámetros: separando con un **doble caracter subrayado** el campo y
el operador. Se ve más claro con un ejemplo, el siguiente código
devuelve todos los superheroes con nivel mayor que cinco:

    amenazas = models.Metahumano.objects.filter(nivel__gt=4)

El nombre del parámetero es `nivel__gt`, al incluir el doble subrayado,
indicamos que el campo es `nivel`, y que el operador a usar es `gt` (Más
grande que: *Greater Than*). Otras formas de expresar esta misma
consulta podrían ser:

    amenazas = models.Metahumano.objects.filter(nivel__gte=5)
    amenazas = models.Metahumano.objects.exclude(nivel__lt=5)
    amenazas = models.Metahumano.objects.exclude(nivel__lte=4)

Existen muchos operadores, que están ampliamente descritos en la
documentación de Django, pero resultan especialmente interesantes
`__contains` e `__icontains` para búsquedas en texto (la *i* de
`__icontains` sirve para indicar que la búsqueda no debe considerar como
letras diferentes las mayúsculas de las minúsculas):

    spideramenazas =  models.Metahumano.objects.filter(
        nombre__icontains = 'spider'
        )

Podemos usar `__in` para buscar que el valor este dentro de los
indicados en una lista:

    nenazas = models.Metahumano.objects.filter(
        level__in = [1,2,3]
        )

Y podemos usar `__year`, `__month`, `__day`, `__week_day`, `__hour`,
`__minute` y `__second` para hacer consultas usando campos de fecha o
*timestamp*:

    Poder.objects.filter(fecha_creacion__year=2021)

Un error común es olvidarse de usar los dos caracteres subrayados y
poner solo uno:

    >>> piltrafillas = Metahumano.objects.filter(
    ...     nivel_in = [1,2,3]
    ...     )
    Traceback (most recent call last):
    ... Blah, blah, blah ...
    FieldError: Cannot resolve keyword 'nivel_in' into field.

También podemos usar el doble caracter subrayado para hacer una consulta
a un modelo relacionado con el modelo que estamos usaudo. Para ello
usamos la forma:

    <nombre de campo relacionado>__<campo en tabla_relacionad>

Por ejemplo:

```python
Metahumano.objects.filter(equipo__name='Los Vengadores')
```

### Consultas con SQL Crudo

En algunos casos las consultas que podemos hacer con los modelos pueden
ser más complicadas que su equivalente en SQL. Existen unos objetos,
`django.db.models.Q`, que nos permiten hacer consultas muy complicadas.
Aun asi, si no vemos mejor opción, podemos hacer directamente la
consulta en SQL usando el método `raw`, que acepta como parámetro una
sentencia SQL y nos devuelve, como es habitual, un `QuerySet`.

Por ejemplo, obtengamos usando `raw` los equipos, con un atributo
añadido indicando cuantos miembros tiene asignados:

    equipos = Equipo.objects.raw('''
        SELECT E.id, E.nombre, count(*) AS n_miembros
          FROM metahumans_equipo E
          LEFT JOIN metahumans_metahumano M ON E.id = M.equipo_id
         GROUP BY T.id, T.nombre
        ''')
    for t in equipos:
        print t.nombre, t.num_members

Este **no es el método recomendado** para hacer esta consulta. Es mejor
limitar las consultas hechas con SQL puro, ya que suelen depender mucho
del gestor de base de datos que estemos usando. Esto crea unas
dependencias que después pueden ser muy complicadas de deshacer. No
obstante, es una posibilidad que existe y en algunos casos -muy pocos,
en realidad- no tendremos más remedio que usarla.

Si la consulta es tan complicada que ni con el método `raw` podemos
obtener lo que queremos, podemos ignorar totalmente los modelos y hacer
una consulta SQL directamente a la base de datos, usando la variable
`django.db.connection`, que el el *handler* de la base de datos definida
por defecto:

```python
# reactivamos todos los superheroes ¡Es la guerra civil!
from django.db import connection

cursor = connection.cursor()
cursor.execute("UPDATE metahumans_metahumano SET activo = 1")
```

### Limitar el tamaño del resultado

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
