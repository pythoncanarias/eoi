``sqlite3``: Base de datos relacional embebida
===============================================

Introducción
------------

.. index:: sqlite3

La base de detos **SQLite3** es una base de datos *server-less* que se puede
utilizar en casi todos los lenguajes de programación, incluido Python.
*Server-less* significa que no hay necesidad de instalar un servidor separado
para la gestión de la base de datos, lo que simplifica mucho su uso.

SQLite es rápida (para un número razonable de datos), ha sido muy testeada por
la comunidad y es muy flexible, lo que la hace ideal para implementar
prototipos e incluso para ser usada como base de datos final de una aplicación.

La librería estándar ``sqlite3`` de python nos permite conectarnos y usar este
sistema gestor de base de datos desde Python.  Con este modulo podemos disponer
de nuestra propia base de datos relacional, basada en SQLite3, usando la
misma interfaz (DB-API 2.0) que se usa en Python para acceder a cualquier otra
base de datos relacional, como MySQl, PostgreSQL, Oracle...  

Una base de datos SQLite se almacena en un único fichero. La librería gestiona
el acceso a los contenidos del fichero, permitiendo el acceso desde varios
clientes a la vez, gestionando los bloqueos y previniendo la currupción de la
base de datos.


Como conectar/crear una base de datos SQLite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El primer paso, como siempre, es importar el módulo ``sqlite3``.  Luego,
crearemos una conexión llamando a la función ``connect()`` de ``sqlite3``. Como
parámetro, tenemos que pasarle el nombre del fichero donde está (o estará, si
es la primera vez que nos conectamos) la base de datos::

    import sqlite3

    con = sqlite3.connect('database.db')

Si es la primera vez que nos conectamos, sqlite creará una base de datos nueva
y la almacena en el fichero indicado; en este ejemplo ``database.db``. Ya sea
porque se ha creado la base de datos o porque esta ya existia previamente, El
resultado de la función será una conexión con la base de datos. Todas las
interacciones con la base de datos las haremos directa o indirectamente a
través de esta variable.

.. Note:: Crear una base de datos en RAM

    Cuando creas una conexión con SQLite, un archivo de base de datos se crea
    automáticamente, si fuera necesario. Este archivo de base de datos se crea en el
    disco. Existe una opción para crear la base de datos en la memoria RAM usando el
    nombre especial ``:memory:`` como parametro de la función de conexión. Esta base
    de datos se llama base de datos en memoria. La ventaja de hacerlo asi es
    que es mucho más rapido crearla base de datos. La desventaja es que tan
    pornto como cerremos la conexión con la base de datos (Aunque esto último
    puede ser útil en determinados casos).

Ejercicio: Crear una base de datos llamada `ejemplo.db`

La base de datos en si ya está creada, pero sigue siendo responsabilidad
nuestra el crear el **esquema** de la misma: las tablas, indices, vistas y
demás elementos que necesitemos.

En el siguiente ejemplo el código verifica si el fichero de la base de datos
existe previemante. Si no fuera así, sabe que tiene que crear el esquema::

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

Si ejecutamos el script, veremos que la primera vez intentara crear el esquema,
y por consiguiente, creará el fichero en el sistema. La segunda, al encontrar
el fichero, asume que el esquema ya está creado.

Despues de crear el nuevo fichero, nuestro siguiente paso debe ser crear  el
esquema que define las tablas. El siguiente ejemplo muestra el código
necesario para crear el esquema que vamos a mostrar a continuacion. Se trata de
una base de datos para una pequeña aplicacion de gestion de tareas, asi que
vamos a crear una tabla para almacenar la informacion de los proyectos y otra
para almacenar las tablas de cada proyecto.

La tabla de proyectos:

============= ======= ===============================
project
-----------------------------------------------------
Columna       Tipo    Descripcion
============= ======= ========La Sentencia `SELECT=======================
name          text    Nombre código del proyecto
description   text    Descripcion
deadline      date    Fecha tope del proyecto
============= ======= ===============================

La tabla de tareas:

============= ======= ===============================
task
-----------------------------------------------------
Columna       Tipo    Descripcion
============= ======= ===============================
task_id       number  Identificador unico de la tarea
priority      integer Prioridad (mas alto es más importante)
details       text    Descripción de la tarea
status        text    Estado [new|pending|done|canceled]
deadline      date    Fecha top de la tarea
completed_on  date    Cuando se termino esta tarea
project       text    Nombre del proyecto al que pertenece esta tarea
============= ======= ===============================


La sintaxis en ``SQL`` para definir estas tablas (Esta parte del SQL se llama
en realida ``DDL``, *Data Definition Languague*) seria la siguiente::

    -- Esquema para aplicacion de tareas

    -- Projectos son actividades que se componen de diversas tareas

    CREATE TABLE project (
        name        text primary key,
        description text,
        deadline    date
    );

    -- Tareas son acciones individuales que deben ejecutarse para
    -- completar un proyecto.

    CREATE TABLE task (
        task_id      integer primary key autoincrement not null,
        title        text not null,
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

            insert into task(details, status, deadline, project)
            values ('write about select', 'done', '2016-04-25',
                    'pymotw'); (details, status, deadline, project)
            values ('write about sqlite3', 'active', '2017-07-31',
                    'pymotw');
            """)
        else:
            print('Database exists, assume schema does, too.')

**Ejercicio**: Examinar la base de datos con sqlite3 command line



Cursores
--------

Para ejecutar sentencias de SQLite en Python, necesita un objeto de tipo ``cursor``. Puedes
crearlo utilizando el método ``cursor()`` de la conexion.

Ahora podemos usar el método ``execute()`` del ``cursor`` para ejecutar cualquier
consulta SQL. Nótese que estamos usando un lenguaje dentro de otro, el lenguaje
SQL es un lenguaje informático, similiar en eso a Python, pero especializado en
realizar solo consultas y operaciones de modificación de la base de datos.

Para ejecutar sentencias de SQL, primero se establece una conexión y luego
se crea un objeto de tipo cursor utilizando la conexión, de la siguiente
manera::

    con = sqlite3.connect('ejemplo.db')
    cursor = con.cursor()



Crear una tabla
---------------

Para crear una tabla en SQLite3, puede usar la sentencia `CREATE TABLE` en el
método `execute()`.  Veamos el siguiente ejemplo::

    import sqlite3CREATE TABLE project (
        name        text primary key,
        description text,
        deadline    date
    );

        con = sqlite3.connect('ejemplo.db')
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE project (
              name        text primary key,
              description text,
              deadline    date
            )
            """)
        con.commit()

Para verificar si nuestra tabla está creada, puedes utilizar el navegador de la
base de datos de sqlite para ver tu tabla. Abre tu archivo `ejemplo.db` con
este programa y deberías ver tu tabla:


Insertar en una tabla
---------------------

Para insertar datos en una tabla, usamos la sentencia `INSERT INTO`::

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    cur.execute("""
        INSERT INTO project (name, description, deadline)
        VALUES ('DOC', 'Escribir documentación', NULL)
        """)
    con.commit()

Podemos verificar que se han insertado los datos con el navegador.

Pasar argumentos a la sentencia SQL
-----------------------------------

Podemos pasar valores / argumentos a las sentencias INSERT en el método `execute ()`. 
Se usa el signo de interrogación como un indicador por posicion de cada argumento. Luego
hay que añadir como segundo parámetro, después de la sentencia SQL, una tupla
con tantos valores como argumentos hayamos declarado en la sentencia.

Como siempre, se ve mejor con un ejemplo::
        VALUES ('DOC', 'Escribir documentación', NULL)
        """)
    con.commit()
    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    user_id = 2
    user_name = "Robert Mill"
    user_salary = 1400
    cur.execute("""
        INSERT INTO task (details, status, deadline, project)
            VALUES (?, done, '2021-04-25',
                    'DOC')
        VALUES (?, ?, ?, ?)
        """, ('Escribir sobre mkdocs', 'done', user_id, user_name, user_salary))
    con.commit()


Actualizar una tabla
--------------------

Para actualizar valores en una tabla se usa la
sentencia `UPDATE` dentro del método `execute()`.

Supongamos que queremos actualizar el nombre del empleado cuyo Id es igual a 2 y que
insertamos en el ejemplo amnteror. **Importante** Tenemos que usaren la sentencia
un `WHERE` como condición para seleccionar a este empleado, si no, se
modificarían todos los empleados de la tabla.

Veamos el ejemplo::

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    task_id = 2
    new_priority = 10
    cur.execute("""
        UPDATE task
           SET priority = ?
         WHERE task_id = ?
        """, (new
_preority, task_id))
    con.commit()

Hacer consultas SQL
-------------------

La sentencia `SELECT` se usa para seleccionar datos de una tabla en particular.
Si deseas seleccionar todas las columnas de los datos de una tabla, puede usar
el asterisco (*). La sintaxis para esto seria la siguiente::


    SELECT * FROM <table_name>


En SQLite3, ejecutamos la instrucción `SELECT` usando el método `execute` del 
cursor. Por eLa Sentencia `SELECTjemplo para obtener todas las columnas de la tabla de empleados,
ejecutariamos el siguiente código::

    SELECT * FROM task

Si deseas seleccionar algunas columnas de una tabla solamente, especifica las
columnas de la siguiente manera::

    SELECT <column1>[, <column2>] FROM <table_name>

Por ejemplo::

    SELECT task_id, title FROM task
    
    
**Ejercicio**: Hacer un pequeño programa para listar las tareas (usando cursores)


La sentencia ``SELECT`` realiza la búsqueda de los datos requeridos desde la 
base de datos y a continuación, para obtener los datos 
seleccionados, podemos utilizar el método `fetchall()` del cursor, que nos
devolvería todos los registros encontrados (En este caso, como no hay clausula
`WHERE`, todos). Veamos el siguiente ejemplo::

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM employee')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
Si deseas obtener datos específicos de la base de datos, puede utilizar la cláusula ``WHERE``. Por ejemplo, queremos obtener los ids y los nombres de aquellos empleados cuyo salario es superior a 800. Para esto, llenemos nuestra tabla con más filas y luego ejecutemos nuestra consulta.

Populate table

Puede usar la sentencia insert para rellenar los datos o puede ingresarlos manualmente en el programa del navegador DB.

Ahora, para obtener los ids y los nombres de las tareas que tienen una prioridad superior a 5::

    import sqlite3

    con = sqlite3.connect('tareas.db')

    cursor = con.cursor()
    cursor.execute('SELECT task_id, name FROM task WHERE priority > 5')
    for row in cursorObj.fetchall():
        print(row)

**Ejercicio**: Hacer un pequeño programa para listar las tareas (usando cursores)

En la sentencia ``SELECT`` anterior, en lugar de usar el asterisco (``*``), especificamos los atributos id y name. El resultado se muestra a continuación:

Select where clause
 


SQLite3 rowcount

El SQLite3 rowcount se utiliza para devolver el número de filas afectadas o seleccionadas por la última consulta SQL ejecutada.

Cuando utilizamos el conteo de de filas con la sentencia SELECT, devolverá -1, ya que se desconoce la cantidad de filas seleccionadas hasta que se recuperan todas. Considera el siguiente ejemplo::

    print(cursor.execute('SELECT * FROM employees').rowcount)
    
Por lo tanto, para obtener el conteo de filas, debes obtener todos los datos y luego obtener la longitud del resultado::

    cur = cursor.execute('SELECT * FROM employees')
    rows = cur.fetchall()
    print(cur.rowcount)

Borrar datos (``DELETE``)
-------------------------

Para borrar datos se usa la sentencia::

    DELETE FORM <table> [WHERE <cond>]
    
Cuando la instrucción DELETE se utiliza sin ninguna condición (una sentencia WHERE), todas las filas de la tabla se eliminarán. En algunas bases de datos a veces se
establece una regla de seguridad que impide ejecutar este comando si no se tiene un permiso
determinado, o algun sistema similar. En sqlite3, por desgracias, no hay nada similar, asi que hay que tener cuidado.


Listar tablas
-------------

Para enumerar todas las tablas en una base de datos SQLite3, debes realizar
una consulta a la tabla ``sqlite_master`` y luego usar ``fetchall()`` para obtener los resultados de la sentencia ``SELECT``. La tabla ``sqlite_master`` es la tabla maestra en SQLite3 que almno se permite
borrar la tabla siacena información de todas las demás tablas::

    import sqlite3

    con = sqlite3.connect('mydatabase.db')
    cursor = con.cursor()
    cursor.execute('SELECT name from sqlite_master where type= "table"')
    print(cursorObj.fetchall())



Como comprobar si una tabla existe o no
---------------------------------------

Al crear una tala, debemos asegurarnos de que la tabla aún no exista. Del mismo modo, al eliminar una tabla, la tabla debe existir.

Para verificar si la tabla no existe, usamos “if not exists” con la sentencia CREATE TABLE de la siguiente manera::

    create table if not exists table_name (column1, column2, …, columnN)
    
Por ejemplo::

    import sqlite3

    con = sqlite3.connect('tareas.db')
    cursor = con.cursor()
    cursorObj.execute('create table if not exists projects(id integer, name text)')
    con.commit()


De manera similar, para verificar si la tabla existe al eliminar, usamos “if exists” con la sentencia ``DROP TABLE`` de la siguiente manera:

    drop table if exists table_name
    
Por ejemplo::

    cursor.execute('drop table if exists projects')
    

También podríamos verificar si la tabla a la que queremos acceder existe o no ejecutando la siguiente consulta::

    SELECT name from sqlite_master
     WHERE type = "table" 
       AND name = "task"

Si existe la tabla de empleados, su nombre será devuelto, si no, tendremos un nulo
 

Eliminar una tabla
------------------

Puedes eliminar una tabla (junto con todo su contenido) utilizando la sentencia DROP. La sintaxis de la sentencia DROP es la siguiente::

    drop table table_name
    
Para eliminar una tabla, la tabla debe existir en la base de datos. Por lo tanto, se recomienda utilizar “if exists” con la sentencia drop de la siguiente manera:

    drop table if exists table_name

Excepciones SQLite3
-------------------

En SQLite3, tenemos definidas las siguientes excepciones:

- DatabaseError

Cualquier error relacionado con la base de datos genera el DatabaseError.

- IntegrityError

IntegrityError es una subclase de DatabaseError y se genera cuando hay un problema de integridad de los datos, por ejemplo, los datos foráneos no se actualizan en todas las tablas, lo que resulta en una inconsistencia de los datos.

- ProgrammingError

La excepción ProgrammingError se produce cuando hay errores de sintaxis o no se encuentra la tabla o se llama a la función con un número incorrecto de parámetros / argumentos.

- OperationalError

Esta excepción se produce cuando fallan las operaciones de la base de datos, por ejemplo, una desconexión inusual. Esto no es culpa de los programadores.

- NotSupportedError

Ocurre cuando utilizas algunos métodos que no están definidos o no son compatibles con la base de datos, se genera la excepción NotSupportedError.

 

Executemany (Inserción por lotes)
---------------------------------

Puedes utilizar la sentencia ``executemany`` para insertar varias filas a la vez.

Considera el siguiente código::

    import sqlite3

    con = sqlite3.connect('mydatabase.db')
    cursor = con.cursor()

    cursor.execute('create table if not exists project(project_id integer, name text)')
    data = [(1, "Ridesharing"), (2, "Water Purifying"), (3, "Forensics"), (4, "Botany")]
    cursor.executemany("INSERT INTO projects VALUES(?, ?)", data)
    con.commit()
    

Cerrar Conexión
---------------

Una vez que haya terminado de utilizar tu base de datos, es una buena práctica cerrar la conexión. La conexión se puede cerrar utilizando el método ``close``::

    con = sqlite3.connect('mydatabase.db')
    ...
    con.close()
 

Fechas y timestamp en SQLite3
-----------------------------

En la base de datos Python SQLite3, podemos almacenar fácilmente la fecha o la hora importando el módulo datatime. Los siguientes formatos son los formatos más utilizados para datetime::

    YYYY-MM-DD
    YYYY-MM-DD HH:MM
    YYYY-MM-DD HH:MM:SS
    YYYY-MM-DD HH:MM:SS.SSS
    HH:MM
    HH:MM:SS
    HH:MM:SS.SSS
    now

Observa el siguiente código:

import sqlite3

import datetime

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()


cursorObj.execute('create table if not exists assignments(id integer, name text, date date)')

data = [(1, "Ridesharing", datetime.date(2017, 1, 2)), (2, "Water Purifying", datetime.date(2018, 3, 4))]

cursorObj.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data)

con.commit()
En este código, el módulo de fecha y hora se importa primero y hemos creado una tabla denominada assignments con tres columnas.

El tipo de datos de la tercera columna es una fecha. Para insertar la fecha en la columna, hemos usado datetime.date. De manera similar, podemos usar datetime.time para manejar la hora.

El código anterior generará la siguiente salida:

SQLite3 datetime
La gran flexibilidad y movilidad de la base de datos SQLite3 la convierten en la primera opción para que cualquier desarrollador la use y la integre con cualquier producto con el que trabaje.

Las bases de datos SQLite3 se utilizan en proyectos de Windows, Linux, Mac OS, Android e iOS debido a su increíble portabilidad. Es un archivo integrado con tu proyecto y listo.


``sqlite3``: Base de datos relacional embebida
===============================================

Introducción
------------

.. index:: sqlite3

La base de detos **SQLite3** es una base de datos *server-less* que se puede
utilizar en casi todos los lenguajes de programación, incluido Python.
*Server-less* significa que no hay necesidad de instalar un servidor separado
para la gestión de la base de datos, lo que simplifica mucho su uso.

SQLite es rápida (para un número razonable de datos), ha sido muy testeada por
la comunidad y es muy flexible, lo que la hace ideal para implementar
prototipos e incluso para ser usada como base de datos final de una aplicación.

La librería estándar ``sqlite3`` de python nos permite conectarnos y usar este
sistema gestor de base de datos desde Python.  Con este modulo podemos disponer
de nuestra propia base de datos relacional, basada en SQLite3, usando la
misma interfaz (DB-API 2.0) que se usa en Python para acceder a cualquier otra
base de datos relacional, como MySQl, PostgreSQL, Oracle...  

Una base de datos SQLite se almacena en un único fichero. La librería gestiona
el acceso a los contenidos del fichero, permitiendo el acceso desde varios
clientes a la vez, gestionando los bloqueos y previniendo la currupción de la
base de datos.


Como conectar/crear una base de datos SQLite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El primer paso, como siempre, es importar el módulo ``sqlite3``.  Luego,
crearemos una conexión llamando a la función ``connect()`` de ``sqlite3``. Como
parámetro, tenemos que pasarle el nombre del fichero donde está (o estará, si
es la primera vez que nos conectamos) la base de datos::

    import sqlite3

    con = sqlite3.connect('database.db')

Si es la primera vez que nos conectamos, sqlite creará una base de datos nueva
y la almacena en el fichero indicado; en este ejemplo ``database.db``. Ya sea
porque se ha creado la base de datos o porque esta ya existia previamente, El
resultado de la función será una conexión con la base de datos. Todas las
interacciones con la base de datos las haremos directa o indirectamente a
través de esta variable.

.. Note:: Crear una base de datos en RAM

    Cuando creas una conexión con SQLite, un archivo de base de datos se crea
    automáticamente, si fuera necesario. Este archivo de base de datos se crea en el
    disco. Existe una opción para crear la base de datos en la memoria RAM usando el
    nombre especial ``:memory:`` como parametro de la función de conexión. Esta base
    de datos se llama base de datos en memoria. La ventaja de hacerlo asi es
    que es mucho más rapido crearla base de datos. La desventaja es que tan
    pornto como cerremos la conexión con la base de datos (Aunque esto último
    puede ser útil en determinados casos).

Ejercicio: Crear una base de datos llamada `ejemplo.db`

La base de datos en si ya está creada, pero sigue siendo responsabilidad
nuestra el crear el **esquema** de la misma: las tablas, indices, vistas y
demás elementos que necesitemos.

En el siguiente ejemplo el código verifica si el fichero de la base de datos
existe previemante. Si no fuera así, sabe que tiene que crear el esquema::

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

Si ejecutamos el script, veremos que la primera vez intentara crear el esquema,
y por consiguiente, creará el fichero en el sistema. La segunda, al encontrar
el fichero, asume que el esquema ya está creado.

Despues de crear el nuevo fichero, nuestro siguiente paso debe ser crear  el
esquema que define las tablas. El siguiente ejemplo muestra el código
necesario para crear el esquema que vamos a mostrar a continuacion. Se trata de
una base de datos para una pequeña aplicacion de gestion de tareas, asi que
vamos a crear una tabla para almacenar la informacion de los proyectos y otra
para almacenar las tablas de cada proyecto.

La tabla de proyectos:

============= ======= ===============================
project
-----------------------------------------------------
Columna       Tipo    Descripcion
============= ======= ========La Sentencia `SELECT=======================
name          text    Nombre código del proyecto
description   text    Descripcion
deadline      date    Fecha tope del proyecto
============= ======= ===============================

La tabla de tareas:

============= ======= ===============================
task
-----------------------------------------------------
Columna       Tipo    Descripcion
============= ======= ===============================
task_id       number  Identificador unico de la tarea
priority      integer Prioridad (mas alto es más importante)
details       text    Descripción de la tarea
status        text    Estado [new|pending|done|canceled]
deadline      date    Fecha top de la tarea
completed_on  date    Cuando se termino esta tarea
project       text    Nombre del proyecto al que pertenece esta tarea
============= ======= ===============================


La sintaxis en ``SQL`` para definir estas tablas (Esta parte del SQL se llama
en realida ``DDL``, *Data Definition Languague*) seria la siguiente::

    -- Esquema para aplicacion de tareas

    -- Projectos son actividades que se componen de diversas tareas

    CREATE TABLE project (
        name        text primary key,
        description text,
        deadline    date
    );

    -- Tareas son acciones individuales que deben ejecutarse para
    -- completar un proyecto.

    CREATE TABLE task (
        task_id      integer primary key autoincrement not null,
        title        text not null,
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

            insert into task(details, status, deadline, project)
            values ('write about select', 'done', '2016-04-25',
                    'pymotw'); (details, status, deadline, project)
            values ('write about sqlite3', 'active', '2017-07-31',
                    'pymotw');
            """)
        else:
            print('Database exists, assume schema does, too.')

**Ejercicio**: Examinar la base de datos con sqlite3 command line



Cursores
--------

Para ejecutar sentencias de SQLite en Python, necesita un objeto de tipo ``cursor``. Puedes
crearlo utilizando el método ``cursor()`` de la conexion.

Ahora podemos usar el método ``execute()`` del ``cursor`` para ejecutar cualquier
consulta SQL. Nótese que estamos usando un lenguaje dentro de otro, el lenguaje
SQL es un lenguaje informático, similiar en eso a Python, pero especializado en
realizar solo consultas y operaciones de modificación de la base de datos.

Para ejecutar sentencias de SQL, primero se establece una conexión y luego
se crea un objeto de tipo cursor utilizando la conexión, de la siguiente
manera::

    con = sqlite3.connect('ejemplo.db')
    cursor = con.cursor()



Crear una tabla
---------------

Para crear una tabla en SQLite3, puede usar la sentencia `CREATE TABLE` en el
método `execute()`.  Veamos el siguiente ejemplo::

    import sqlite3CREATE TABLE project (
        name        text primary key,
        description text,
        deadline    date
    );

        con = sqlite3.connect('ejemplo.db')
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE project (
              name        text primary key,
              description text,
              deadline    date
            )
            """)
        con.commit()

Para verificar si nuestra tabla está creada, puedes utilizar el navegador de la
base de datos de sqlite para ver tu tabla. Abre tu archivo `ejemplo.db` con
este programa y deberías ver tu tabla:


Insertar en una tabla
---------------------

Para insertar datos en una tabla, usamos la sentencia `INSERT INTO`::

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    cur.execute("""
        INSERT INTO project (name, description, deadline)
        VALUES ('DOC', 'Escribir documentación', NULL)
        """)
    con.commit()

Podemos verificar que se han insertado los datos con el navegador.

Pasar argumentos a la sentencia SQL
-----------------------------------

Podemos pasar valores / argumentos a las sentencias INSERT en el método `execute ()`. 
Se usa el signo de interrogación como un indicador por posicion de cada argumento. Luego
hay que añadir como segundo parámetro, después de la sentencia SQL, una tupla
con tantos valores como argumentos hayamos declarado en la sentencia.

Como siempre, se ve mejor con un ejemplo::
        VALUES ('DOC', 'Escribir documentación', NULL)
        """)
    con.commit()
    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    user_id = 2
    user_name = "Robert Mill"
    user_salary = 1400
    cur.execute("""
        INSERT INTO task (details, status, deadline, project)
            VALUES (?, done, '2021-04-25',
                    'DOC')
        VALUES (?, ?, ?, ?)
        """, ('Escribir sobre mkdocs', 'done', user_id, user_name, user_salary))
    con.commit()


Actualizar una tabla
--------------------

Para actualizar valores en una tabla se usa la
sentencia `UPDATE` dentro del método `execute()`.

Supongamos que queremos actualizar el nombre del empleado cuyo Id es igual a 2 y que
insertamos en el ejemplo amnteror. **Importante** Tenemos que usaren la sentencia
un `WHERE` como condición para seleccionar a este empleado, si no, se
modificarían todos los empleados de la tabla.

Veamos el ejemplo::

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    task_id = 2
    new_priority = 10
    cur.execute("""
        UPDATE task
           SET priority = ?
         WHERE task_id = ?
        """, (new
_preority, task_id))
    con.commit()

Hacer consultas SQL
-------------------

La sentencia `SELECT` se usa para seleccionar datos de una tabla en particular.
Si deseas seleccionar todas las columnas de los datos de una tabla, puede usar
el asterisco (*). La sintaxis para esto seria la siguiente::


    SELECT * FROM <table_name>


En SQLite3, ejecutamos la instrucción `SELECT` usando el método `execute` del 
cursor. Por eLa Sentencia `SELECTjemplo para obtener todas las columnas de la tabla de empleados,
ejecutariamos el siguiente código::

    SELECT * FROM task

Si deseas seleccionar algunas columnas de una tabla solamente, especifica las
columnas de la siguiente manera::

    SELECT <column1>[, <column2>] FROM <table_name>

Por ejemplo::

    SELECT task_id, title FROM task
    
    
**Ejercicio**: Hacer un pequeño programa para listar las tareas (usando cursores)


La sentencia ``SELECT`` realiza la búsqueda de los datos requeridos desde la 
base de datos y a continuación, para obtener los datos 
seleccionados, podemos utilizar el método `fetchall()` del cursor, que nos
devolvería todos los registros encontrados (En este caso, como no hay clausula
`WHERE`, todos). Veamos el siguiente ejemplo::

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM employee')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
Si deseas obtener datos específicos de la base de datos, puede utilizar la cláusula ``WHERE``. Por ejemplo, queremos obtener los ids y los nombres de aquellos empleados cuyo salario es superior a 800. Para esto, llenemos nuestra tabla con más filas y luego ejecutemos nuestra consulta.

Populate table

Puede usar la sentencia insert para rellenar los datos o puede ingresarlos manualmente en el programa del navegador DB.

Ahora, para obtener los ids y los nombres de las tareas que tienen una prioridad superior a 5::

    import sqlite3

    con = sqlite3.connect('tareas.db')

    cursor = con.cursor()
    cursor.execute('SELECT task_id, name FROM task WHERE priority > 5')
    for row in cursorObj.fetchall():
        print(row)

**Ejercicio**: Hacer un pequeño programa para listar las tareas (usando cursores)

En la sentencia ``SELECT`` anterior, en lugar de usar el asterisco (``*``), especificamos los atributos id y name. El resultado se muestra a continuación:

Select where clause
 


SQLite3 rowcount

El SQLite3 rowcount se utiliza para devolver el número de filas afectadas o seleccionadas por la última consulta SQL ejecutada.

Cuando utilizamos el conteo de de filas con la sentencia SELECT, devolverá -1, ya que se desconoce la cantidad de filas seleccionadas hasta que se recuperan todas. Considera el siguiente ejemplo::

    print(cursor.execute('SELECT * FROM employees').rowcount)
    
Por lo tanto, para obtener el conteo de filas, debes obtener todos los datos y luego obtener la longitud del resultado::

    cur = cursor.execute('SELECT * FROM employees')
    rows = cur.fetchall()
    print(cur.rowcount)

Borrar datos (``DELETE``)
-------------------------

Para borrar datos se usa la sentencia::

    DELETE FORM <table> [WHERE <cond>]
    
Cuando la instrucción DELETE se utiliza sin ninguna condición (una sentencia WHERE), todas las filas de la tabla se eliminarán. En algunas bases de datos a veces se
establece una regla de seguridad que impide ejecutar este comando si no se tiene un permiso
determinado, o algun sistema similar. En sqlite3, por desgracias, no hay nada similar, asi que hay que tener cuidado.


Listar tablas
-------------

Para enumerar todas las tablas en una base de datos SQLite3, debes realizar
una consulta a la tabla ``sqlite_master`` y luego usar ``fetchall()`` para obtener los resultados de la sentencia ``SELECT``. La tabla ``sqlite_master`` es la tabla maestra en SQLite3 que almno se permite
borrar la tabla siacena información de todas las demás tablas::

    import sqlite3

    con = sqlite3.connect('mydatabase.db')
    cursor = con.cursor()
    cursor.execute('SELECT name from sqlite_master where type= "table"')
    print(cursorObj.fetchall())



Como comprobar si una tabla existe o no
---------------------------------------

Al crear una tala, debemos asegurarnos de que la tabla aún no exista. Del mismo modo, al eliminar una tabla, la tabla debe existir.

Para verificar si la tabla no existe, usamos “if not exists” con la sentencia CREATE TABLE de la siguiente manera::

    create table if not exists table_name (column1, column2, …, columnN)
    
Por ejemplo::

    import sqlite3

    con = sqlite3.connect('tareas.db')
    cursor = con.cursor()
    cursorObj.execute('create table if not exists projects(id integer, name text)')
    con.commit()


De manera similar, para verificar si la tabla existe al eliminar, usamos “if exists” con la sentencia ``DROP TABLE`` de la siguiente manera:

    drop table if exists table_name
    
Por ejemplo::

    cursor.execute('drop table if exists projects')
    

También podríamos verificar si la tabla a la que queremos acceder existe o no ejecutando la siguiente consulta::

    SELECT name from sqlite_master
     WHERE type = "table" 
       AND name = "task"

Si existe la tabla de empleados, su nombre será devuelto, si no, tendremos un nulo
 

Eliminar una tabla
------------------

Puedes eliminar una tabla (junto con todo su contenido) utilizando la sentencia DROP. La sintaxis de la sentencia DROP es la siguiente::

    drop table table_name
    
Para eliminar una tabla, la tabla debe existir en la base de datos. Por lo tanto, se recomienda utilizar “if exists” con la sentencia drop de la siguiente manera:

    drop table if exists table_name

Excepciones SQLite3
-------------------

En SQLite3, tenemos definidas las siguientes excepciones:

- DatabaseError

Cualquier error relacionado con la base de datos genera el DatabaseError.

- IntegrityError

IntegrityError es una subclase de DatabaseError y se genera cuando hay un problema de integridad de los datos, por ejemplo, los datos foráneos no se actualizan en todas las tablas, lo que resulta en una inconsistencia de los datos.

- ProgrammingError

La excepción ProgrammingError se produce cuando hay errores de sintaxis o no se encuentra la tabla o se llama a la función con un número incorrecto de parámetros / argumentos.

- OperationalError

Esta excepción se produce cuando fallan las operaciones de la base de datos, por ejemplo, una desconexión inusual. Esto no es culpa de los programadores.

- NotSupportedError

Ocurre cuando utilizas algunos métodos que no están definidos o no son compatibles con la base de datos, se genera la excepción NotSupportedError.

 

Executemany (Inserción por lotes)
---------------------------------

Puedes utilizar la sentencia ``executemany`` para insertar varias filas a la vez.

Considera el siguiente código::

    import sqlite3

    con = sqlite3.connect('mydatabase.db')
    cursor = con.cursor()

    cursor.execute('create table if not exists project(project_id integer, name text)')
    data = [(1, "Ridesharing"), (2, "Water Purifying"), (3, "Forensics"), (4, "Botany")]
    cursor.executemany("INSERT INTO projects VALUES(?, ?)", data)
    con.commit()
    

Cerrar Conexión
---------------

Una vez que haya terminado de utilizar tu base de datos, es una buena práctica cerrar la conexión. La conexión se puede cerrar utilizando el método ``close``::

    con = sqlite3.connect('mydatabase.db')
    ...
    con.close()
 

Fechas y timestamp en SQLite3
-----------------------------

En la base de datos Python SQLite3, podemos almacenar fácilmente la fecha o la hora importando el módulo datatime. Los siguientes formatos son los formatos más utilizados para datetime::

    YYYY-MM-DD
    YYYY-MM-DD HH:MM
    YYYY-MM-DD HH:MM:SS
    YYYY-MM-DD HH:MM:SS.SSS
    HH:MM
    HH:MM:SS
    HH:MM:SS.SSS
    now

Observa el siguiente código:

import sqlite3

import datetime

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()


cursorObj.execute('create table if not exists assignments(id integer, name text, date date)')

data = [(1, "Ridesharing", datetime.date(2017, 1, 2)), (2, "Water Purifying", datetime.date(2018, 3, 4))]

cursorObj.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data)

con.commit()
En este código, el módulo de fecha y hora se importa primero y hemos creado una tabla denominada assignments con tres columnas.

El tipo de datos de la tercera columna es una fecha. Para insertar la fecha en la columna, hemos usado datetime.date. De manera similar, podemos usar datetime.time para manejar la hora.

El código anterior generará la siguiente salida:

SQLite3 datetime
La gran flexibilidad y movilidad de la base de datos SQLite3 la convierten en la primera opción para que cualquier desarrollador la use y la integre con cualquier producto con el que trabaje.

Las bases de datos SQLite3 se utilizan en proyectos de Windows, Linux, Mac OS, Android e iOS debido a su increíble portabilidad. Es un archivo integrado con tu proyecto y listo.

Crear una base de datos en RAM
------------------------------

Cuando creas una conexión con SQLite, un archivo de base de datos se crea
automáticamente si no existe ya. Este archivo de base de datos se crea en el
disco, ademas, también podemos crear una base de datos en la RAM usando el
nombre especial `:memory:` como parametro de la función de conexión. Esta base
de datos se llama base de datos en memoria.

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









#### Crear una base de datos en RAM

Cuando creas una conexión con SQLite, un archivo de base de datos se crea
automáticamente si no existe ya. Este archivo de base de datos se crea en el
disco, ademas, también podemos crear una base de datos en la RAM usando el
nombre especial `:memory:` como parametro de la función de conexión. Esta base
de datos se llama base de datos en memoria.

### Crear una tabla

Para crear una tabla en SQLite3, puede usar la sentencia `CREATE TABLE` en el
método `execute()`. 
Veamos el siguiente ejemplo:

import sqlite3

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE employee (
            id integer PRIMARY KEY,
            name text,
            salary real
        """)
    con.commit()


Para verificar si nuestra tabla está creada, puedes utilizar el navegador de la
base de datos de sqlite para ver tu tabla. Abre tu archivo `ejemplo.db` con
este programa y deberías ver tu tabla:


### Insertar en una tabla

Para insertar datos en una tabla, usamos la sentencia `INSERT INTO`.

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    cur.execute("""
        INSERT INTO employee (id, name, salary)
        VALUES (1, 'John Smith', 1200)
        """)
    con.commit()

Podemos verificar que se han insertado los datos con el navegador.

### Pasar argumentos a la sentencia SQL

Podemos pasar valores / argumentos a las sentencias INSERT en el método `execute ()`. 
Se usa el signo de interrogación como un indicador por posicion de cada argumento. Luego
hay que añadir como segundo parametro, sdespues de la sentencia SQL, una tupla
con tantos valores como argumentos hayamos declarado en la sentencia.

Como siempre, se ve mejor con un ejemplo:

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    user_id = 2
    user_name = "Robert Mill"
    user_salary = 1400
    cur.execute("""
        INSERT INTO employee (id, name, salary)
        VALUES (?, ?, ?)
        """, (user_id, user_name, user_salary))
    con.commit()


### Actualizar una tabla

Para actualizar valores en una tabla se usa la
sentencia `UPDATE` dentro del método `execute()`.

Supongamos que queremos actualizar el nombre del empleado cuyo Id es igual a 2 y que
insertamos en el ejemplo amnteror. **Importante** Tenemos que usaren la sentencia
un `WHERE` como condición para seleccionar a este empleado, si no, se
modificarían todos los empleados de la tabla.

Veamos el ejemplo:

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    user_id = 2
    new_name = "Robert Millhouse"
    cur.execute("""
        UPDATE employee
           SET name = ?
         WHERE id = ?
        """, (new_name, user_id))
    con.commit()

### Hacer consultas

#### La Sentencia `SELECT`

La sentencia `SELECT` se usa para seleccionar datos de una tabla en particular.
Si deseas seleccionar todas las columnas de los datos de una tabla, puede usar
el asterisco (*). La sintaxis para esto seria la siguiente:


    SELECT * FROM <table_name>


En SQLite3, ejecutamos la instrucción `SELECT` usando el método `execute` del 
cursor. Por ejemplo para obtener todas las columnas de la tabla de empleados,
ejecutariamos el siguiente código:

    SELECT * FROM employee

Si deseas seleccionar algunas columnas de una tabla solamente, especifica las
columnas de la siguiente manera:

    SELECT <column1>[, <column2>] FROM <table_name>

Por ejemplo:

    SELECT id, name FROM employee


La sentencia select realiza la búsqueda de los datos requeridos desde la 
tabla de la base de datos y a continuación, para obtener los datos 
seleccionados, podemos utilizar el método `fetchall()` del cursor, que nos
devolvería todos los registros encontrador (En este caso, como no hay clausula
`WHERE`, todos). Veamos el siguiente eejmplo:

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM employee')
    rows = cur.fetchall()
    for row in rows:
        print(row)



Obtener todos los datos
También puede usar el fetchall () en una línea de la siguiente manera:

[print(row) for row in cursorObj.fetchall()]
Si deseas obtener datos específicos de la base de datos, puede utilizar la cláusula WHERE. Por ejemplo, queremos obtener los ids y los nombres de aquellos empleados cuyo salario es superior a 800. Para esto, llenemos nuestra tabla con más filas y luego ejecutemos nuestra consulta.

Populate table
Puede usar la sentencia insert para rellenar los datos o puede ingresarlos manualmente en el programa del navegador DB.

Ahora, para obtener los ids y los nombres de aquellos empleados que tienen un salario superior a 800:

import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT id, name FROM employees WHERE salary > 800.0')

    rows = cursorObj.fetchall()

    for row in rows:

        print(row)

sql_fetch(con)
En la sentencia SELECT anterior, en lugar de usar el asterisco (*), especificamos los atributos id y name. El resultado se muestra a continuación:

Select where clause
 


SQLite3 rowcount
El SQLite3 rowcount se utiliza para devolver el número de filas afectadas o seleccionadas por la última consulta SQL ejecutada.

Cuando utilizamos el conteo de de filas con la sentencia SELECT, devolverá -1, ya que se desconoce la cantidad de filas seleccionadas hasta que se recuperan todas. Considera el siguiente ejemplo:

print(cursorObj.execute('SELECT * FROM employees').rowcount)
SQLite3 rowcount
Por lo tanto, para obtener el conteo de filas, debes obtener todos los datos y luego obtener la longitud del resultado:

rows = cursorObj.fetchall()

print len (rows)
Cuando la instrucción DELETE se utiliza sin ninguna condición (una sentencia WHERE), todas las filas de la tabla se eliminarán y el número total de filas eliminadas se devolverá por conteo de filas.

print(cursorObj.execute('DELETE FROM employees').rowcount)
Row count
Si no se borra ninguna fila, se devolverá 0.

Los registros no han sido borrados
Listar tablas
Para enumerar todas las tablas en una base de datos SQLite3, debes consultar la tabla sqlite_master y luego usar fetchall() para obtener los resultados de la sentencia SELECT.

El sqlite_master es la tabla maestra en SQLite3 que almacena todas las tablas.

import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT name from sqlite_master where type= "table"')

    print(cursorObj.fetchall())

sql_fetch(con)
Con este código se listará todas las tablas de la siguiente manera:

List tables
 

Comprobar si una tabla existe o no
Al crear una tabla, debemos asegurarnos de que la tabla aún no exista. Del mismo modo, al remover / eliminar una tabla, la tabla debe existir.

Para verificar si la tabla no existe, usamos “if not exists” con la sentencia CREATE TABLE de la siguiente manera:

create table if not exists table_name (column1, column2, …, columnN)
Por ejemplo:

import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('create table if not exists projects(id integer, name text)')

    con.commit()

sql_fetch(con)
Comprobar si una tabla existe o no
De manera similar, para verificar si la tabla existe al eliminar, usamos “if exists” con la sentencia DROP TABLE de la siguiente manera:

drop table if exists table_name
Por ejemplo,

cursorObj.execute('drop table if exists projects')
Tabla eliminada
También podemos verificar si la tabla a la que queremos acceder existe o no ejecutando la siguiente consulta:

cursorObj.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "employees"')

print(cursorObj.fetchall())
Si existe la tabla de empleados, su nombre será devuelto como se muestra a continuación:

Tabla existe

Si el nombre de la tabla que especificamos no existe, se devolverá una arreglo vacío:

Tabla no existe
 


Eliminar una tabla
Puedes remover /eliminar una tabla utilizando la sentencia DROP. La sintaxis de la sentencia DROP es la siguiente:

drop table table_name
Para eliminar una tabla, la tabla debe existir en la base de datos. Por lo tanto, se recomienda utilizar “if exists” con la sentencia drop de la siguiente manera:

drop table if exists table_name
Por ejemplo,

import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('DROP table if exists employees')

    con.commit()

sql_fetch(con)
Eliminar una tabla
Excepciones SQLite3
Las excepciones son errores de tiempo de ejecución. en la programación en Python, todas las excepciones son instancias de la clase derivadas de la BaseException.

En SQLite3, tenemos las siguientes excepciones principales de Python:

DatabaseError
Cualquier error relacionado con la base de datos genera el DatabaseError.

IntegrityError
IntegrityError es una subclase de DatabaseError y se genera cuando hay un problema de integridad de los datos, por ejemplo, los datos foráneos no se actualizan en todas las tablas, lo que resulta en una inconsistencia de los datos.

ProgrammingError
La excepción ProgrammingError se produce cuando hay errores de sintaxis o no se encuentra la tabla o se llama a la función con un número incorrecto de parámetros / argumentos.

OperationalError
Esta excepción se produce cuando fallan las operaciones de la base de datos, por ejemplo, una desconexión inusual. Esto no es culpa de los programadores.

NotSupportedError
Ocurre cuando utilizas algunos métodos que no están definidos o no son compatibles con la base de datos, se genera la excepción NotSupportedError.

 

SQLite3 Executemany (Inserción por lotes)
Puedes utilizar la sentencia Executemany para insertar varias filas a la vez.

Considera el siguiente código:

import sqlite3

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()

cursorObj.execute('create table if not exists projects(id integer, name text)')

data = [(1, "Ridesharing"), (2, "Water Purifying"), (3, "Forensics"), (4, "Botany")]

cursorObj.executemany("INSERT INTO projects VALUES(?, ?)", data)

con.commit()
Creamos una tabla con dos columnas, luego “data” tiene cuatro valores para cada columna. Esta variable se pasa al método executemany () junto con la consulta.

Ten en cuenta que hemos utilizado el ? para pasar los valores.

El código anterior generará el siguiente resultado:

Bulk insert (executemany)
 

Cerrar Conexión

Una vez que haya terminado de utilizar tu base de datos, es una buena práctica cerrar la conexión. La conexión se puede cerrar utilizando el método close ().

Para cerrar una conexión, utiliza el objeto de conexión y llame al método close () de la siguiente manera:

con = sqlite3.connect('mydatabase.db')

#program statements

con.close()
 

SQLite3 datetime
En la base de datos Python SQLite3, podemos almacenar fácilmente la fecha o la hora importando el módulo datatime. Los siguientes formatos son los formatos más utilizados para datetime:

YYYY-MM-DD

YYYY-MM-DD HH:MM

YYYY-MM-DD HH:MM:SS

YYYY-MM-DD HH:MM:SS.SSS

HH:MM

HH:MM:SS

HH:MM:SS.SSS

now
Observa el siguiente código:

import sqlite3

import datetime

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()

cursorObj.execute('create table if not exists assignments(id integer, name text, date date)')

data = [(1, "Ridesharing", datetime.date(2017, 1, 2)), (2, "Water Purifying", datetime.date(2018, 3, 4))]

cursorObj.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data)

con.commit()
En este código, el módulo de fecha y hora se importa primero y hemos creado una tabla denominada assignments con tres columnas.

El tipo de datos
### Crear una tabla

Para crear una tabla en SQLite3, puede usar la sentencia `CREATE TABLE` en el
método `execute()`. 
Veamos el siguiente ejemplo:

import sqlite3

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE employee (
            id integer PRIMARY KEY,
            name text,
            salary real
        """)
    con.commit()


Para verificar si nuestra tabla está creada, puedes utilizar el navegador de la
base de datos de sqlite para ver tu tabla. Abre tu archivo `ejemplo.db` con
este programa y deberías ver tu tabla:


### Insertar en una tabla

Para insertar datos en una tabla, usamos la sentencia `INSERT INTO`.

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    cur.execute("""
        INSERT INTO employee (id, name, salary)
        VALUES (1, 'John Smith', 1200)
        """)
    con.commit()

Podemos verificar que se han insertado los datos con el navegador.

### Pasar argumentos a la sentencia SQL

Podemos pasar valores / argumentos a las sentencias INSERT en el método `execute ()`. 
Se usa el signo de interrogación como un indicador por posicion de cada argumento. Luego
hay que añadir como segundo parametro, sdespues de la sentencia SQL, una tupla
con tantos valores como argumentos hayamos declarado en la sentencia.

Como siempre, se ve mejor con un ejemplo:

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    user_id = 2
    user_name = "Robert Mill"
    user_salary = 1400
    cur.execute("""
        INSERT INTO employee (id, name, salary)
        VALUES (?, ?, ?)
        """, (user_id, user_name, user_salary))
    con.commit()


### Actualizar una tabla

Para actualizar valores en una tabla se usa la
sentencia `UPDATE` dentro del método `execute()`.

Supongamos que queremos actualizar el nombre del empleado cuyo Id es igual a 2 y que
insertamos en el ejemplo amnteror. **Importante** Tenemos que usaren la sentencia
un `WHERE` como condición para seleccionar a este empleado, si no, se
modificarían todos los empleados de la tabla.

Veamos el ejemplo:

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    user_id = 2
    new_name = "Robert Millhouse"
    cur.execute("""
        UPDATE employee
           SET name = ?
         WHERE id = ?
        """, (new_name, user_id))
    con.commit()

### Hacer consultas

#### La Sentencia `SELECT`

La sentencia `SELECT` se usa para seleccionar datos de una tabla en particular.
Si deseas seleccionar todas las columnas de los datos de una tabla, puede usar
el asterisco (*). La sintaxis para esto seria la siguiente:


    SELECT * FROM <table_name>


En SQLite3, ejecutamos la instrucción `SELECT` usando el método `execute` del 
cursor. Por ejemplo para obtener todas las columnas de la tabla de empleados,
ejecutariamos el siguiente código:

    SELECT * FROM employee

Si deseas seleccionar algunas columnas de una tabla solamente, especifica las
columnas de la siguiente manera:

    SELECT <column1>[, <column2>] FROM <table_name>

Por ejemplo:

    SELECT id, name FROM employee


La sentencia select realiza la búsqueda de los datos requeridos desde la 
tabla de la base de datos y a continuación, para obtener los datos 
seleccionados, podemos utilizar el método `fetchall()` del cursor, que nos
devolvería todos los registros encontrador (En este caso, como no hay clausula
`WHERE`, todos). Veamos el siguiente eejmplo:

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM employee')
    rows = cur.fetchall()
    for row in rows:
        print(row)



Obtener todos los datos
También puede usar el fetchall () en una línea de la siguiente manera:

[print(row) for row in cursorObj.fetchall()]
Si deseas obtener datos específicos de la base de datos, puede utilizar la cláusula WHERE. Por ejemplo, queremos obtener los ids y los nombres de aquellos empleados cuyo salario es superior a 800. Para esto, llenemos nuestra tabla con más filas y luego ejecutemos nuestra consulta.

Populate table
Puede usar la sentencia insert para rellenar los datos o puede ingresarlos manualmente en el programa del navegador DB.

Ahora, para obtener los ids y los nombres de aquellos empleados que tienen un salario superior a 800:

import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT id, name FROM employees WHERE salary > 800.0')

    rows = cursorObj.fetchall()

    for row in rows:

        print(row)

sql_fetch(con)
En la sentencia SELECT anterior, en lugar de usar el asterisco (*), especificamos los atributos id y name. El resultado se muestra a continuación:

Select where clause
 


SQLite3 rowcount
El SQLite3 rowcount se utiliza para devolver el número de filas afectadas o seleccionadas por la última consulta SQL ejecutada.

Cuando utilizamos el conteo de de filas con la sentencia SELECT, devolverá -1, ya que se desconoce la cantidad de filas seleccionadas hasta que se recuperan todas. Considera el siguiente ejemplo:

print(cursorObj.execute('SELECT * FROM employees').rowcount)
SQLite3 rowcount
Por lo tanto, para obtener el conteo de filas, debes obtener todos los datos y luego obtener la longitud del resultado:

rows = cursorObj.fetchall()

print len (rows)
Cuando la instrucción DELETE se utiliza sin ninguna condición (una sentencia WHERE), todas las filas de la tabla se eliminarán y el número total de filas eliminadas se devolverá por conteo de filas.

print(cursorObj.execute('DELETE FROM employees').rowcount)
Row count
Si no se borra ninguna fila, se devolverá 0.

Los registros no han sido borrados
Listar tablas
Para enumerar todas las tablas en una base de datos SQLite3, debes consultar la tabla sqlite_master y luego usar fetchall() para obtener los resultados de la sentencia SELECT.

El sqlite_master es la tabla maestra en SQLite3 que almacena todas las tablas.

import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT name from sqlite_master where type= "table"')

    print(cursorObj.fetchall())

sql_fetch(con)
Con este código se listará todas las tablas de la siguiente manera:

List tables
 

Comprobar si una tabla existe o no
Al crear una tabla, debemos asegurarnos de que la tabla aún no exista. Del mismo modo, al remover / eliminar una tabla, la tabla debe existir.

Para verificar si la tabla no existe, usamos “if not exists” con la sentencia CREATE TABLE de la siguiente manera:

create table if not exists table_name (column1, column2, …, columnN)
Por ejemplo:

import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('create table if not exists projects(id integer, name text)')

    con.commit()

sql_fetch(con)
Comprobar si una tabla existe o no
De manera similar, para verificar si la tabla existe al eliminar, usamos “if exists” con la sentencia DROP TABLE de la siguiente manera:

drop table if exists table_name
Por ejemplo,

cursorObj.execute('drop table if exists projects')
Tabla eliminada
También podemos verificar si la tabla a la que queremos acceder existe o no ejecutando la siguiente consulta:

cursorObj.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "employees"')

print(cursorObj.fetchall())
Si existe la tabla de empleados, su nombre será devuelto como se muestra a continuación:

Tabla existe

Si el nombre de la tabla que especificamos no existe, se devolverá una arreglo vacío:

Tabla no existe
 


Eliminar una tabla
Puedes remover /eliminar una tabla utilizando la sentencia DROP. La sintaxis de la sentencia DROP es la siguiente:

drop table table_name
Para eliminar una tabla, la tabla debe existir en la base de datos. Por lo tanto, se recomienda utilizar “if exists” con la sentencia drop de la siguiente manera:

drop table if exists table_name
Por ejemplo,

import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('DROP table if exists employees')

    con.commit()

sql_fetch(con)
Eliminar una tabla
Excepciones SQLite3
Las excepciones son errores de tiempo de ejecución. en la programación en Python, todas las excepciones son instancias de la clase derivadas de la BaseException.

En SQLite3, tenemos las siguientes excepciones principales de Python:

DatabaseError
Cualquier error relacionado con la base de datos genera el DatabaseError.

IntegrityError
IntegrityError es una subclase de DatabaseError y se genera cuando hay un problema de integridad de los datos, por ejemplo, los datos foráneos no se actualizan en todas las tablas, lo que resulta en una inconsistencia de los datos.

ProgrammingError
La excepción ProgrammingError se produce cuando hay errores de sintaxis o no se encuentra la tabla o se llama a la función con un número incorrecto de parámetros / argumentos.

OperationalError
Esta excepción se produce cuando fallan las operaciones de la base de datos, por ejemplo, una desconexión inusual. Esto no es culpa de los programadores.

NotSupportedError
Ocurre cuando utilizas algunos métodos que no están definidos o no son compatibles con la base de datos, se genera la excepción NotSupportedError.

 

SQLite3 Executemany (Inserción por lotes)
Puedes utilizar la sentencia Executemany para insertar varias filas a la vez.

Considera el siguiente código:

import sqlite3

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()

cursorObj.execute('create table if not exists projects(id integer, name text)')

data = [(1, "Ridesharing"), (2, "Water Purifying"), (3, "Forensics"), (4, "Botany")]

cursorObj.executemany("INSERT INTO projects VALUES(?, ?)", data)

con.commit()
Creamos una tabla con dos columnas, luego “data” tiene cuatro valores para cada columna. Esta variable se pasa al método executemany () junto con la consulta.

Ten en cuenta que hemos utilizado el ? para pasar los valores.

El código anterior generará el siguiente resultado:

Bulk insert (executemany)
 

Cerrar Conexión

Una vez que haya terminado de utilizar tu base de datos, es una buena práctica cerrar la conexión. La conexión se puede cerrar utilizando el método close ().

Para cerrar una conexión, utiliza el objeto de conexión y llame al método close () de la siguiente manera:

con = sqlite3.connect('mydatabase.db')

#program statements

con.close()
 

SQLite3 datetime
En la base de datos Python SQLite3, podemos almacenar fácilmente la fecha o la hora importando el módulo datatime. Los siguientes formatos son los formatos más utilizados para datetime:

YYYY-MM-DD

YYYY-MM-DD HH:MM

YYYY-MM-DD HH:MM:SS

YYYY-MM-DD HH:MM:SS.SSS

HH:MM

HH:MM:SS

HH:MM:SS.SSS

now
Observa el siguiente código:

import sqlite3

import datetime

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()

cursorObj.execute('create table if not exists assignments(id integer, name text, date date)')

data = [(1, "Ridesharing", datetime.date(2017, 1, 2)), (2, "Water Purifying", datetime.date(2018, 3, 4))]

cursorObj.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data)

con.commit()
En este código, el módulo de fecha y hora se importa primero y hemos creado una tabla denominada assignments con tres columnas.

El tipo de datos de la tercera columna es una fecha. Para insertar la fecha en la columna, hemos usado datetime.date. De manera similar, podemos usar datetime.time para manejar la hora.

El código anterior generará la siguiente salida:

SQLite3 datetime
La gran flexibilidad y movilidad de la base de datos SQLite3 la convierten en la primera opción para que cualquier desarrollador la use y la integre con cualquier producto con el que trabaje.

Las bases de datos SQLite3 se utilizan en proyectos de Windows, Linux, Mac OS, Android e iOS debido a su increíble portabilidad. Es un archivo integrado con tu proyecto y listo.






 de la tercera columna es una fecha. Para insertar la fecha en la columna, hemos usado datetime.date. De manera similar, podemos usar datetime.time para manejar la hora.

El código anterior generará la siguiente salida:

SQLite3 datetime
La gran flexibilidad y movilidad de la base de datos SQLite3 la convierten en la primera opción para que cualquier desarrollador la use y la integre con cualquier producto con el que trabaje.

Las bases de datos SQLite3 se utilizan en proyectos de Windows, Linux, Mac OS, Android e iOS debido a su increíble portabilidad. Es un archivo integrado con tu proyecto y listo.







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
