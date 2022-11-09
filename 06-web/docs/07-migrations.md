---
title: Migraciones en Django
tags:
  - web
  - database
---

## Migración

Las **migraciones** es el sistema que usa Django para mantener la
correspondencia entre los modelos definínidos en las _apps_ y las tablas en la
base de datos. De esta forma podemos cambiar un modelo y reflejar de forma
controlada esos mismos cambios en el esquema de la base de datos.

Cada migración es en realidad un programa en Python. Normalmente
contiene una lista de operaciones que modifican el esquema de la base de
datos para que los modelos se mantengan en sintonía con dicho esquema.

!!! note "Cuando usa Django las migraciones"

    Para que una *app* de django pueda hacer uso de las migraciones, se tiene
    que cumplir dos condiciones, la primera que la *app* esté listada dentro de
    la variable `INSTALLED_APPS` de la configuración.

    En segundo lugar, que exista un directorio dentro de la *app* llamado
    `migrations`, que contega además un fichero `__init__.py`. Tanto la carpeta
    como el archivo son creados automáticamente cuando usamos la orden
    `startapp`, pero hay que tener cuidado de no olvidarse de crearlos si
    creamos la *app* manualmente.

    Si no se cumple alguna de estas condiciones, las migraciones no estarán
    activas para la *app*.

Echemos un vistazo a uno de estos ficheros de migración:

```python
from django.db import models, migrations

class Migration(migrations.Migration):
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    primary_key=True,
                    auto_created=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('volume', models.PositiveIntegerField()),
                ('total_btc', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
```

Hay dos cosas a destacar en este _script_, porque son constantes en
todas las migraciones.

En primer lugar, hay una clase llamada `Migration`, derivada de
`django.db.migrations.Migration`. Cuando se aplique una migración, esta
es la clase que se buscará y ejecutará.

La clase contiene, entre otras cosas, dos listas:

- `dependencies`
- `operations`

La lista `dependencies`, de dependencias, como su nombre indica, sirve
para indicar que migración o migraciones deben ser ejecutadas
obligatoriamente antes que esta. Veremos esto con más detalle,pero ahora
vamos a centrarnos en la segunda lista, la de operaciones.

La lista `operations` especifica todas las operaciones que hay que
ejecutar para aplicar la migración. Todas las operaciones son subclases
de `django.db.migrations.operations.base.Operation`. En la siguiente
tabla veremos las operaciones ya definidas en Django:

Operaciones disponibles en las migraciones de Django
 
| Operación                 | Descripción |
|---------------------------|-------------------------------------------------|
| `CreateModel`             | Crea la tabla correspondiente a un modelo |
| `DeleteModel`             | Borra un modelo y la tabla asociada |
| `RenameModel`             | Cambia el nombre de un modelo y su tabla asociada |
| `AlterModelTable`         | Cambia el nombre de la tabla asociada |
| `AlterUniqueTogether`     | Modifica restricciones de tipo único |
| `AlterIndexTogether`      | Modifica el índice de un modelo |
| `AlterOrderWithRespectTo` | Crea o borra la columna `_orden` para un modelo |
| `AlterModelOptions`       | Modifica varias opciones del modelo sin afectar la BD |
| `AlterModelManagers`      | Cambia los gestores (*managers*) disponibles durante las migraciones |
| `AddField`                | Añade un campo al modelo |
| `RemoveField`             | Borra un campo del modelo |
| `AlterField`              | Modifica la definición de un campo |
| `RenameField`             | Borra un campo |
| `AddIndex`                | Crea un índice en la tabla de un modelo |
| `RemoveIndex`             | Borra un índice de la tabla de un modelo |


Los nombres de las operaciones se basan en el tipo de cambio que se
desea ejecutar en la definición de los modelos, no en los cambios que
hay que realizar en la base de datos. En otras palabras, usamos los
nombres de las clases para definir lo que queremos que se haga, no la
forma en la que hay que hacerlo. Esto se llama [Programación
declarativa](https://es.wikipedia.org/wiki/Programaci%C3%B3n_declarativa).

De esta forma, cuando se aplica la migración, cada clase es responsable
de generar las ordenes SQL necesarias para cada base de datos
específica. Por ejemplo, `CreateModel` generará una sentencia SQL de
tipo `CREATE TABLE ...`.

En principio, las migraciones están soportadas para todos los tipos de
bases de datos que soporta Django. Por lo tanto, si nos limitamos a usar
las operaciones definidas aquí, podríamos hacer casi cualquier cambio
que deseemos en los modelos, sin tener que preocuparnos por el código
SQL que ha de ocuparse de ello. Toda esa parte esta ya implementada.

No obstante, en ciertos casos Django puede fallar en detectar
correctamente los cambios que queremos hacer. Por ejemplo, si se cambia
el nombre de una tabla a la vez que se cambian varios de sus campos,
Django podría interpretar que lo que queremos es un nuevo modelo, no una
modificación de un modelo anterior.

En este caso, en vez de crear una secuencia de una operación
`RenameModel` seguida por varias operaciones `AlterField`, crearía una
lista con una operación `DeleteModel` y una operación `CreateModel`. En
vez de cambiar el nombre de la tabla asociada al modelo, borraría la
tabla y crearía una nueva con el nuevo nombre, ¡borrando así todos los
datos almacenados anteriormente!.

Es una buena práctica comprobar las migraciones usando una copia de la
base de datos antes de ejecutarlas en la base de datos real.

Django proporciona además tres tipos más de operaciones, para usos
especiales:

- `RunSQL` permite ejecutar sentencias SQL personalizadas en la base de datos.

- `RunPython` permite ejecutar cualquier código Python.

- `SeparateDatabaseAndState` es una operación aun más especializada, para usuarios avanzados.

Con todas estas operaciones a nuestra disposición, podemos hacer
básicamente cualquier tipo de cambio en nuestra base de datos. Sin
embargo, estas tres últimas operaciones nunca se usarán en las
migraciones creadas de forma automática por la orden `makemigrations`.
