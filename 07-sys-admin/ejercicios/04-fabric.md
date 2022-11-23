# Fabric

1. Crea un fichero llamado `fabfile.py` con el siguiente contenido

```python
from fabric import Connection, task

@task
def development(ctx):
    ctx.user = <pon-aqui-tu-usuario>
    ctx.host = 'eoi-sysadmin-ec2'
    ctx.connect_kwargs = {"password": <pon-aqui-tu-password>}

@task
def deploy(ctx):
    with Connection(ctx.host, ctx.user, connect_kwargs=ctx.connect_kwargs) as conn:
        conn.run("uname")
        conn.run("ls")
```

2. Activa el entorno virtual y ejecuta el siguiente comando de Fabric en la consola:

```
source .venv/bin/activate
fab development deploy
```  

Output:
```
Linux
```


# Despliegue de una aplicación Django con Fabric

A continuacion vamos a desplegar una aplicación Django con Fabric en el servidor de vagrant

---------------
1. Vamos a añadir algunos import más que nos serán útiles a la hora de definir las siguientes tareas:

```
import sys
import os

from fabric import Connection, task
```

-------------------
2. Vamos a definir una serie de variables que nos servirán como constantes en el despliegue de la aplicación:

```python
PROJECT_NAME = "django_polls"
PROJECT_PATH = f"~/{PROJECT_NAME}"
REPO_URL = "https://github.com/aliciapj/django_polls.git"
VENV_PYTHON = f'{PROJECT_PATH}/.venv/bin/python'
VENV_PIP = f'{PROJECT_PATH}/.venv/bin/pip'
```


------------------
3. Ahora deberíamos tener el fichero con algo como esto:
    
```python
import sys
import os
from fabric import Connection, task

PROJECT_NAME = "django_polls"
PROJECT_PATH = f"~/{PROJECT_NAME}"
REPO_URL = "https://github.com/aliciapj/django_polls.git"
VENV_PYTHON = f'{PROJECT_PATH}/.venv/bin/python'
VENV_PIP = f'{PROJECT_PATH}/.venv/bin/pip'

@task
def development(ctx):
    ctx.user = <pon-aqui-tu-usuario>
    ctx.host = 'eoi-sysadmin-ec2'
    ctx.connect_kwargs = {"password": <pon-aqui-tu-password>}


@task
def deploy(ctx):
    with Connection(ctx.host, ctx.user, connect_kwargs=ctx.connect_kwargs) as conn:
        conn.run("uname")
        conn.run("ls")
```

--------------
4. Cambiamos el método de deploy para hacer un git clone del repositorio de nuestro proyecto django en el servidor remoto. Vamos a extraer del deploy la funcionalidad de crear la conexión para poder reutilizarla en otras tareas. Como va a ser un método auxiliar, no hace falta ponerle el decorador de `@task`:

```python
import sys
import os
from fabric import Connection, task

PROJECT_NAME = "django_polls"
PROJECT_PATH = f"~/{PROJECT_NAME}"
REPO_URL = "https://github.com/aliciapj/django_polls.git"
VENV_PYTHON = f'{PROJECT_PATH}/.venv/bin/python'
VENV_PIP = f'{PROJECT_PATH}/.venv/bin/pip'

@task
def development(ctx):
    ctx.user = <pon-aqui-tu-usuario>
    ctx.host = 'eoi-sysadmin-ec2'
    ctx.connect_kwargs = {"password": <pon-aqui-tu-password>}

def get_connection(ctx):
    try:
        with Connection(ctx.host, ctx.user, connect_kwargs=ctx.connect_kwargs) as conn:
            return conn
    except Exception as e:
        return None

@task
def deploy(ctx):
    conn = get_connection(ctx)
    if conn is None:
        sys.exit("Failed to get connection")
```

> Prueba la tarea con `fab development deploy` y comprueba que no aparezcan errores

---------------------
5. A partir de ahora vamos a añadir tareas a nuestro proceso de deploy, definiendo una nueva `@task` y añadiéndola al método de deploy. Empezaremos por la de hacer un `git clone` del repo que hemos definido en la constante `REPO_URL`.  
En todas las tareas empezaremos obteniendo la conexión por parámetro y a continuación, ejecutando los comandos correspondientes.

```python
@task
def clone(ctx): 
    print(f"clone repo {REPO_URL}...")   
    
    if isinstance(ctx, Connection):
        conn = ctx
    else:
        conn = get_connection(ctx)

    # obtengo las carpetas del directorio
    ls_result = conn.run("ls").stdout

    # divido el resultado para tener cada carpeta en un objeto de una lista
    ls_result = ls_result.split("\n")

    # si el nombre del proyecto ya está en la lista de carpetas
    # no es necesario hacer el clone 
    if PROJECT_NAME in ls_result:
        print("project already exists")
    else:
        conn.run(f"git clone {REPO_URL} {PROJECT_NAME}")
```

    Y ahora añadimos la tarea al proceso de deploy:
    
```python
@task
def deploy(ctx):
    conn = get_connection(ctx)
    if conn is None:
        sys.exit("Failed to get connection")
    
    clone(conn)
```

> Prueba la tarea con `fab development deploy`, comprueba que el resultado es algo como lo siguiente y comprueba que la operación se ha ejecutado correctamente en el servidor  
```
clone repo https://github.com/aliciapj/django_polls.git...
Cloning into 'django_polls'...
```

-----------------------------
6. Vamos a hacer un checkout de la rama `main` del repositorio:

```python
@task
def checkout(ctx, branch=None):
    print(f"checkout to branch {branch}...")

    if branch is None:
        sys.exit("branch name is not specified")
    
    if isinstance(ctx, Connection):
        conn = ctx
    else:
        conn = get_connection(ctx)
    
    with conn.cd(PROJECT_PATH):
        conn.run(f"git checkout {branch}")
```

Y añade la nueva tarea a la función de deploy

```python
@task
def deploy(ctx):
    conn = get_connection(ctx)
    if conn is None:
        sys.exit("Failed to get connection")
    
    clone(conn)
    checkout(conn, branch="main")
```

> Prueba la tarea con `fab development deploy`, comprueba que el resultado es algo como lo siguiente y comprueba que la operación se ha ejecutado correctamente en el servidor  
```
clone repo https://github.com/aliciapj/django_polls.git...
django_polls
project already exists
checkout to branch main...
Already on 'main'
Your branch is up to date with 'origin/main'.
```

----------------
7. Crea una tarea para hacer un git pull de la rama:

```python
@task
def pull(ctx, branch="main"):

    print(f"pulling latest code from {branch} branch...")

    if branch is None:
        sys.exit("branch name is not specified")

    if isinstance(ctx, Connection):
        conn = ctx
    else:
        conn = get_connection(ctx)

    with conn.cd(PROJECT_PATH):
        conn.run(f"git pull origin {branch}")
```

Y añade la nueva tarea a la función de deploy

```python
@task
def deploy(ctx):
    conn = get_connection(ctx)
    if conn is None:
        sys.exit("Failed to get connection")

    clone(conn)
    checkout(conn, branch="main")
    pull(conn, branch="main")
```

> Prueba la tarea con `fab development deploy`, comprueba que el resultado es algo como lo siguiente y comprueba que la operación se ha ejecutado correctamente en el servidor  

```
clone repo https://github.com/aliciapj/django_polls.git...
django_polls
project already exists
checkout to branch main...
Already on 'main'
Your branch is up to date with 'origin/main'.
pulling latest code from main branch...
From https://github.com/aliciapj/django_polls
 * branch            main       -> FETCH_HEAD
Already up to date.
```

------------------
8. Crea una tarea para crear un virtual environment con Python 3 (recuerda que el comando en linux para un entorno llamado `.venv` es `python3 -m venv .venv`.  
Además, instala a través del pip del virtualenv creado la librería de django

```python

@task
def create_venv(ctx):
    
    print("creating venv....")
    
    if isinstance(ctx, Connection):
        conn = ctx
    else:
        conn = get_connection(ctx)
    with conn.cd(PROJECT_PATH):
        conn.run("python3 -m venv .venv")
        conn.run(f"{VENV_PIP} install django")
```

Y añade la nueva tarea a la función de deploy

```python
@task
def deploy(ctx):
    conn = get_connection(ctx)
    if conn is None:
        sys.exit("Failed to get connection")

    clone(conn)
    checkout(conn, branch="main")
    pull(conn, branch="main")
    create_venv(conn)
```

> Prueba la tarea con `fab development deploy`, comprueba que el resultado es algo como lo siguiente y comprueba que la operación se ha ejecutado correctamente en el servidor  

```
clone repo https://github.com/aliciapj/django_polls.git...
django_polls
project already exists
checkout to branch main...
Already on 'main'
Your branch is up to date with 'origin/main'.
pulling latest code from main branch...
From https://github.com/aliciapj/django_polls
 * branch            main       -> FETCH_HEAD
Already up to date.
creating venv....
Collecting django
  Downloading https://files.pythonhosted.org/packages/89/69/c556b5b3e7a6701724485fc07c8349791e585b784dc70c9c0683d98ef0db/Django-3.2.3-py3-none-any.whl (7.9MB)
Collecting asgiref<4,>=3.3.2 (from django)
  Downloading https://files.pythonhosted.org/packages/17/8b/05e225d11154b8f5358e6a6d277679c9741ec0339d1e451c9cef687a9170/asgiref-3.3.4-py3-none-any.whl
Collecting pytz (from django)
  Downloading https://files.pythonhosted.org/packages/70/94/784178ca5dd892a98f113cdd923372024dc04b8d40abe77ca76b5fb90ca6/pytz-2021.1-py2.py3-none-any.whl (510kB)
Collecting sqlparse>=0.2.2 (from django)
  Downloading https://files.pythonhosted.org/packages/14/05/6e8eb62ca685b10e34051a80d7ea94b7137369d8c0be5c3b9d9b6e3f5dae/sqlparse-0.4.1-py3-none-any.whl (42kB)
Collecting typing-extensions; python_version < "3.8" (from asgiref<4,>=3.3.2->django)
  Downloading https://files.pythonhosted.org/packages/2e/35/6c4fff5ab443b57116cb1aad46421fb719bed2825664e8fe77d66d99bcbc/typing_extensions-3.10.0.0-py3-none-any.whl
Installing collected packages: typing-extensions, asgiref, pytz, sqlparse, django
Successfully installed asgiref-3.3.4 django-3.2.3 pytz-2021.1 sqlparse-0.4.1 typing-extensions-3.10.0.0
```

--------------
9. Crea una tarea para ejecutar las migraciones de django

```python
@task
def migrate(ctx):
    print("checking for django db migrations...")

    if isinstance(ctx, Connection):
        conn = ctx
    else:
        conn = get_connection(ctx)
        
    with conn.cd(PROJECT_PATH):
        conn.run(f"{VENV_PYTHON} manage.py migrate")
```

Y añade la nueva tarea a la función de deploy

```python
@task
def deploy(ctx):
    conn = get_connection(ctx)
    if conn is None:
        sys.exit("Failed to get connection")

    clone(conn)
    checkout(conn, branch="main")
    pull(conn, branch="main")
    create_venv(conn)
    migrate(conn)
```

> Prueba la tarea con `fab development deploy`, comprueba que el resultado es algo como lo siguiente y comprueba que la operación se ha ejecutado correctamente en el servidor  

```
clone repo https://github.com/aliciapj/django_polls.git...
django_polls
project already exists
checkout to branch main...
Already on 'main'
Your branch is up to date with 'origin/main'.
pulling latest code from main branch...
From https://github.com/aliciapj/django_polls
 * branch            main       -> FETCH_HEAD
Already up to date.
creating venv....
Requirement already satisfied: django in ./.venv/lib/python3.6/site-packages
Requirement already satisfied: sqlparse>=0.2.2 in ./.venv/lib/python3.6/site-packages (from django)
Requirement already satisfied: pytz in ./.venv/lib/python3.6/site-packages (from django)
Requirement already satisfied: asgiref<4,>=3.3.2 in ./.venv/lib/python3.6/site-packages (from django)
Requirement already satisfied: typing-extensions; python_version < "3.8" in ./.venv/lib/python3.6/site-packages (from asgiref<4,>=3.3.2->django)
checking for django db migrations...
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying polls.0001_initial... OK
  Applying sessions.0001_initial... OK
```

### Con esto nuestra aplicación Django ya estaría lista para arrancar
--------------

# Despliegue en varios entornos

Si tuviera dos entornos de ejecución (por ejemplo, `development` y `production`), con los siguientes parámetros distintos:

```
development_settings = {
    username = 'dev_user',
    password = 'dev_pass',
    github_branch = 'development',
}

production_settings = {
    username = 'pro_user',
    password = 'pro_pass',
    github_branch = 'production',
}
```

¿Cómo tendría que adaptar mi `fabfile.py` para que pueda desplegar en un entorno o en el otro con los siguientes comandos?
```
fab development deploy
fab production deploy
```

### Pistas:
- Crea 2 task para establecer las variables de contexto (`ctx`) y el resto de variables, ponlas como globales al principio y establece su valor en estos métodos
- Puedes guardar variables adicionales a las de la conexión (por ejemplo, la rama de github) en variables de entorno del usuario a través de `ctx.config.run.env`
- Crea una task para comprobar si el usuario existe en el servidor, y si no existe, crearlo a través del usuario vagrant
- Conéctate a través del usuario del entorno para realizar el resto de tareas
