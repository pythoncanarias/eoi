## Mini proyecto desarrollo web

Partiendo de la web de tareas que hemos estado realizando con Python, realizar
alguna de los siguientes mejoras. Recordar que **no es necesario hacerlas
todas**, solo una de ellas.

## Barra de progreso en proyectos

Añadir un **método** `progress` a la clase `Project`, cuya función debe ser
indicar el porcentaje de progreso del proyecto, basándonos en las fechas de
inicio (`start_date`) y final del proyecto (`end_date`) y la fecha actual.

Según la fecha actual, se pueden dar tres casos:

- Si la fecha actual es anterior o igual a la fecha de inicio del proyecto, el
  método debe devolver $0.0$

- Si la fecha actual es igual o posterior a la fecha final, el método debe
  devolver $100.0$

- Si la fecha actual está comprendida entre la fecha de inicio y la fecha final
  del proyecto, calcular el porcentaje a partir del número de días entre las
  fechas de inicio y final y los días transcurridos desde la fecha de inicio a
  la fecha actual.

Por ejemplo, supongamos que el inicio del proyecto es el día 17 de enero de
2023, y la fecha final es el 24 de abril de 2023. En ese caso el total de días
asignados al proyecto es $97$:

```python
>>> import datetime
>>> delta = datetime.date(2023, 4, 24) - datetime.date(2023, 1, 17)
>>> print(delta.days)
97
```

Si la fecha actual fuera el 7 de febrero de 2023, los días trascurridos desde
el inicio del proyecto serían $21$. El porcentaje de progreso sería, por tanto:

$$ \frac{21 \times 100.0}{97} = 21.649484536082475 $$

El resultado debe redondearse con un dígito de precisión (Puedes usar la
función [`round`](https://docs.python.org/es/3/library/functions.html#round), así que el método debería devolver $21.6$.

Modifica ahora la plantilla usada en la vista de los proyecto para incluir una
columna en la tabla de proyectos con una barra de progreso en HTML.

```html
<progress class="progress" value="21.6" max="100">21.6 %</progress>
```

## Botón de marcar la tarea como terminada

Hacer un formulario para marcar la tarea como terminada. Solo necesita el campo del id de la tarea.

- Hacer una plantilla tipo `include` para pintar on boton, que sea un formulario autocontenido para marcar la tarea como terminada (Puedes usar el campo `HIDDEN`).  Usa la clase de Bulma `is-danger` para que el botón se vea rojo.  
- Incluye este botón en la tabla que lista las tareas,pero solo en las que no estén terminadas.
- Una vez marcada la tarea como terminada, volver a la página de inicio.

## Entrada de múltiples tareas

Haz un formulario que permita dar de alta varias tareas a partir de una texto.
Cada línea de texto debe corresponderse con un nueva  tarea. El formulario
debería constar solo de un `textarea` donde el usuario pondría los títulos de
las tareas, sabiendo que cada línea se corresponderá con una nueva Tarea. 

No podrás usar un `ModelForm` porque este formulario no se corresponde con una
única tarea. Usa un `Form` normal. Crea todas las tareas con los parámetros que
tienen las tareas por defecto, excepto, claro está, el nombre (`name`).

En la vista, cuando estés procesando la petición del `POST`, divide el texto de
entrada usando `split("\n")`. Esto te devolverá una lista de líneas de textos.
Para cada una de esas líneas, crea una nueva tarea y salvala en la base de
datos con el método `save()`.

## Nuevo modelo `Place`

Añadir un nuevo modelo `Place`,  que servirá simplemente para describir sitios
en los que se puede realizar una tarea.  El modelo podría ser, por ejemplo.

```
class Place(models.Model):
	description = models.CharField(max_length=32)
```

La idea es poder asociar tareas con posibles ubicaciones, de forma que, cuando
estemos en ese sitio podemos consultar que tareas podemos realizar ahí. La
siguiente tabla muestra posibles valores para estos lugares:

| `id` | `description`                     |
|------|-----------------------------------|
| 0    | En cualquier lugar                |
| 1    | En la calle                       |
| 2    | En casa                           |
| 3    | En la oficina                     |

Para incluir este nuevo modelo, debemos hacer tres migraciones:

1) Crear el modelo `Place` y crear la migración que simplemente crea el modelo
en la base de datos.


2) Creamos una migración vacia (_--empty_):

```shell
./manage.py makemigrations --empty --name <nombre_que_quieras_para_la_migracion> <app>
```

Esto creará un fichero de migración vacío, con un contenido similar a este:

```python
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ...
    ]

    operations = [
    ]
```

Como vemos, solo se define el campo de dependencias, las operaciones a realizar
en esta migración están vacías. Vamos a incluir código SQL para añadir los
datos a la tabla:

```sql
INSERT INTO tasks_place (id, description) VALUES (0, 'En cualquier lugar');
INSERT INTO tasks_place (id, description) VALUES (1, 'En la calle');
INSERT INTO tasks_place (id, description) VALUES (2, 'En casa');
INSERT INTO tasks_place (id, description) VALUES (3, 'En la oficina');
```

Para ello haremos uso de la clase
[migration.RunSQL](https://docs.djangoproject.com/en/1.10/ref/migration-operations/#runsql),
que nos permite definir la migración tanto en una dirección como en otra, es
decir, crearemos este objeto con dos sentencias SQL, una para definir como
aplicar la migración, y otra para deshacerla. En nuestro caso, quedaría así:

```python
from django.db import migrations

ADD_VALUES = '''
  INSERT INTO tasks_place (id, description) VALUES (0, 'En cualquier lugar');
  INSERT INTO tasks_place (id, description) VALUES (1, 'En la calle');
  INSERT INTO tasks_place (id, description) VALUES (2, 'En casa');
  INSERT INTO tasks_place (id, description) VALUES (3, 'En la oficina');'''
'''

REMOVE_VALUES = '''
  DELETE FROM tasks_place WHERE id IN (0, 1, 2, 3);
'''


class Migration(migrations.Migration):

    dependencies = [
        ...  # deja aqui las migraciones que hubiera antes
    ]

    operations = [
        migrations.RunSQL(ADD_VALUES, REMOVE_VALUES),
    ]
```

Una vez creada esta nueva **migración de datos**, podemos aplicarla. Los datos
deberían aparecer en la tabla. Puede añadir el modelo Place al `admin` para
añadir más lugares, si quieres.

3) Ahora haríamos la tercera migración, para vincular la tabla de tareas `Task`
con la de lugares `Place`. Para ello usaremos un `ForeignKey` desde la tarea
hasta el lugar, y pondremos como valor por defecto `0`. Este valor por defecto
hará que la migración asigne a todas las tareas ya existentes en la base de
datos a `"En cualquier lugar"`.

Por último, crear una vista con la url `/lugares/' que muestro los distintos
lugares posibles, y que cada lugar sea una enlace a '/lugares/<pk>/', que es
otra vista que hay que hacer, para mostrar las tareas que esten asociadas con
ese lugar.

Date cuenta que si accedo a `/lugares/3/`, tiene que mostrarme todas las tareas
que puedo hacer en la oficina, (`id` de place iqual a $3$), pero también todas
las tareas con `id` de place a $0$, porque estas tareas se pueden hacer en
cualquier lugar, y eso incluye a la oficina.


