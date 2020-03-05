El módulo ``sqlite3``: Base de datos relacional embebida
----------------------------------------------------------

.. index:: sqlite3

Con este modulo podemos disponer de nuestra propia base de datos relacional , basada en **SQLite3**,
usando la misma interfaz (DB-API 2.0) que se usa en Python para acceder a cualquier otra base de
datos relacional, como MySQl, PostgreSQL, Oracle...  SQLite es rápida (para un número razonable de
datos), ha sido muy testeada por la comunidad y es muy flexible, lo que la hace ideal para
implementar prototipos e incluso para ser usada como base de datos final de una aplicación.

Crear una base de datos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Una base de datos SQLite se almacena en un único fichero. La librería gestiona el acceso a los
contenidos del fichero, permitiendo el acceso desde varios clientes a la vez, gestionando los
bloqueos y previniendo la currupción de la base de datos.

La base de datos es creada simplemente la primera vez que se accede al fichero, pero sigue siendo
responsabilidad nuestra el crear el **esquema** de la misma: las tablas, indices, vistas y demás
elementos que necesitemos.

En el siguiente ejemplo el código verifica si el fichero de la base de datos exsite, antes
de conectarse. Si no existe, sabe que tiene que crear el esquema::

    import os
    import sqlite3

    db_filename = 'todo.db'
    db_is_new = not os.path.exists(db_filename)
    conn = sqlite3.connect(db_filename)
    if db_is_new:
        print('Need to create schema')
    else:
        print('Database exists, assume schema does, too.')
    conn.close()

Si ejecutamos el script, veremos que la primera vez intentara crear el esquema, y por consiguiente, 
creará el fichero en el sistema. La segunda, al encontrar el fichero, asume que el esquema
ya está creado.

Despues de crear el nuevo fichero, nuestro siguinte paso debe ser crear  el esquema que define
las tablas. El siguiente ejemplo muestra el codiego necesario para crear el esquema que vamos
a mostrar a continuacion. Se trata de crear una pequeña aplicacion de gestion de tareas, asi que
vamos a crear una tabla para almacenar la informacion de los proyectos y otra para almacenar las
tablas de cada proyecto.

La tabla de proyectos:

=============  =======  ===============================
project
-------------------------------------------------------
Columna        Tipo     Descripcion
=============  =======  ===============================
name           text     Nombre código del proyecto
description    text     Descripcion
deadline       date     Fecha tope del proyecto
=============  =======  ===============================

La tabla de tareas:

=============  =======  ===============================
task
-------------------------------------------------------
Columna        Tipo     Descripcion
=============  =======  ===============================
task_id        number   Identificador unico de la tarea
priority       integer  Prioridad (mas baho es mas importante)
details        text     Descripción de la tarea
status         text     Estado [new|pending|done|canceled]
deadline       date     Fecha top de la tarea
completed_on   date     Cuando se termino esta tarea
project        text     Nombre del proyecto al que pertenece esta tarea
=============  =======  ===============================


La sintaxis en SQL para definir estas tablas (Esta parte del SQL se llama en realida DDL)
seria la siguiente::

    -- Esquema para aplicacion de tareas

    -- Projects are high-level activities made up of tasks

    CREATE TABLE project (
        name        text primary key,
        description text,
        deadline    date
    );

    -- Tasks are steps that can be taken to complete a project

    CREATE TABLE task (
        task_id      integer primary key autoincrement not null,
        priority     integer default 1,
        details      text,
        status       text,
        deadline     date,
        completed_on date,
        project      text not null references project(name)
    );

.. index:: executescript (sqlite3)

El método ``executescript()`` puede ser usado para ejecutar estas sentencis DDL
y crear así el esquema. Salvemos el contenido de este ejemplo al fichero ``todo_schema.sql``::

    import os
    import sqlite3

    db_filename = 'todo.db'
    schema_filename = 'todo_schema.sql'

    db_is_new = not os.path.exists(db_filename)

    with sqlite3.connect(db_filename) as conn:
        if db_is_new:
            print('Creating schema')
            with open(schema_filename, 'rt') as f:
                schema = f.read()
            conn.executescript(schema)

            print('Inserting initial data')
            
            conn.executescript("""
            
            insert into project (name, description, deadline)
            values ('pymotw', 'Python Module of the Week',
                    '2016-11-01');

            insert into task (details, status, deadline, project)
            values ('write about select', 'done', '2016-04-25',
                    'pymotw');

            insert into task (details, status, deadline, project)
            values ('write about random', 'waiting', '2016-08-22',
                    'pymotw');

            insert into task (details, status, deadline, project)
            values ('write about sqlite3', 'active', '2017-07-31',
                    'pymotw');
            """)
        else:
            print('Database exists, assume schema does, too.')

[TODO]

- Annaadir algunas filas a las tablas
- Examinar la base de datos con sqlite3 command line

- Hacer un pequeno programa para listar las tareas (usando cursores)


- Query Metadata


By default, the values returned by the fetch methods as “rows” from the database are tuples. The caller is responsible for knowing the order of the columns in the query and extracting individual values from the tuple. When the number of values in a query grows, or the code working with the data is spread out in a library, it is usually easier to work with an object and access values using their column names. That way, the number and order of the tuple contents can change over time as the query is edited, and code depending on the query results is less likely to break.

Connection objects have a row_factory property that allows the calling code to control the type of object created to represent each row in the query result set. sqlite3 also includes a Row class intended to be used as a row factory. Column values can be accessed through Row instances by using the column index or name.

- Placeholders. SQL Injection, parametros por posicion o por nombre
- Carga masiva vom ``executemany``. recordar csv
- convertir a/desde fechas
- anadir tipos a la base de datos

- Transactions. commit, rollback

- Isolation Levels
- In-Memory Databases
- Exporting the Contents of a Database
- Using Python Functions in SQL
- Custom Aggregation
- Restricting Access to Data

Ver tambien: sqlalchemy, csv
