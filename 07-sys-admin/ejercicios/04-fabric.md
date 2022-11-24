# Fabric

```
pip install fabric3
```


1. Crea un fichero llamado `fabfile.py` con el siguiente contenido

```python
from fabric.api import local

def deploy():
    local("uname")
    local("ls /")
```

2. Activa el entorno virtual y ejecuta el siguiente comando de Fabric en la consola:

```
source .venv/bin/activate
fab deploy
```  

Output:
```
[localhost] local: uname
Linux
[localhost] local: ls /
bin  boot  dev  etc  home  init  lib  lib32  lib64  libx32  lost+found  media  mnt  opt  proc  root  run  sbin  snap  srv  sys  tmp  usr  var
```


# Despliegue de una aplicación Django con Fabric

A continuacion vamos a desplegar una aplicación Django con Fabric en el servidor de vagrant

---------------
1. Vamos a añadir algunos import más que nos serán útiles a la hora de definir las siguientes tareas:

```
import os
import sys

from fabric.api import local
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
import os
import sys

from fabric.api import local

PROJECT_NAME = "django_polls"
PROJECT_PATH = f"/home/<pon_tu_usuario_aqui>/{PROJECT_NAME}"
REPO_URL = "https://github.com/aliciapj/django_polls.git"
VENV_PYTHON = f'{PROJECT_PATH}/.venv/bin/python'
VENV_PIP = f'{PROJECT_PATH}/.venv/bin/pip'


def deploy():
    local("uname")
    local("ls /")
```

--------------
4. Cambiamos el método de deploy para hacer un git clone del repositorio de nuestro proyecto django
A partir de ahora vamos a añadir tareas a nuestro proceso de deploy, definiendo una nueva función para cada paso y añadiéndola al método de deploy. Empezaremos por la de hacer un `git clone` del repo que hemos definido en la constante `REPO_URL`.  
En todas las tareas empezaremos obteniendo la conexión por parámetro y a continuación, ejecutando los comandos correspondientes.

```python
@task
def clone(): 
    print(f"clone repo {REPO_URL}...")   

    # si el nombre del proyecto ya está en la lista de carpetas
    # no es necesario hacer el clone 
    if os.path.exists(PROJECT_PATH):
        print("project already exists")
    else:
        local(f"git clone {REPO_URL} {PROJECT_PATH}")
```

    Y ahora añadimos la tarea al proceso de deploy:
    
```python
@task
def deploy():
    clone()
```

> Prueba la tarea con `fab development deploy`, comprueba que el resultado es algo como lo siguiente y comprueba que la operación se ha ejecutado correctamente en el servidor  
```
clone repo https://github.com/aliciapj/django_polls.git...
Cloning into 'django_polls'...
```

-----------------------------
1. Vamos a hacer un checkout de la rama `main` del repositorio:

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
project already exists
checkout to branch main...
[localhost] local: ls 
README.md  __pycache__  django_polls  fabfile.py  fixtures  manage.py  polls  requirements.txt
[localhost] local: git checkout main
Already on 'main'
Your branch is up to date with 'origin/main'.

Done.
```

------------------
8. Crea una tarea para crear un virtual environment con Python 3 (recuerda que el comando en linux para un entorno llamado `.venv` es `python3 -m venv .venv`.  
Además, instala a través del pip del virtualenv creado la librería de django

```python
def create_venv():
    
    print("creating venv....")
    
    with lcd(PROJECT_PATH):
        local("python3 -m venv .venv")
        local(f"{VENV_PIP} install django")
```

Y añade la nueva tarea a la función de deploy

```python
def deploy():
    clone()
    checkout('main')
    create_venv()
```

> Prueba la tarea con `fab development deploy`, comprueba que el resultado es algo como lo siguiente y comprueba que la operación se ha ejecutado correctamente en el servidor  

```
clone repo https://github.com/aliciapj/django_polls.git...
project already exists
checkout to branch main...
[localhost] local: git checkout main
Already on 'main'
Your branch is up to date with 'origin/main'.
creating venv....
[localhost] local: python3 -m venv .venv
[localhost] local: /home/alicia/django_polls//.venv/bin/pip install django
Collecting django
  Downloading Django-4.1.3-py3-none-any.whl (8.1 MB)
     |████████████████████████████████| 8.1 MB 6.3 MB/s 
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.3-py3-none-any.whl (42 kB)
     |████████████████████████████████| 42 kB 2.7 MB/s 
Collecting asgiref<4,>=3.5.2
  Downloading asgiref-3.5.2-py3-none-any.whl (22 kB)
Collecting backports.zoneinfo; python_version < "3.9"
  Downloading backports.zoneinfo-0.2.1-cp38-cp38-manylinux1_x86_64.whl (74 kB)
     |████████████████████████████████| 74 kB 7.5 MB/s 
Installing collected packages: sqlparse, asgiref, backports.zoneinfo, django
Successfully installed asgiref-3.5.2 backports.zoneinfo-0.2.1 django-4.1.3 sqlparse-0.4.3

Done.
```

--------------
9. Crea una tarea para ejecutar las migraciones de django

```python
def create_venv():
    
    print("creating venv....")
    
    with lcd(PROJECT_PATH):
        local("python3 -m venv .venv")
        local(f"{VENV_PIP} install django")
```

Y añade la nueva tarea a la función de deploy

```python
def deploy():
    clone()
    checkout('main')
    create_venv()
    migrate()
```

> Prueba la tarea con `fab development deploy`, comprueba que el resultado es algo como lo siguiente y comprueba que la operación se ha ejecutado correctamente en el servidor  

```
clone repo https://github.com/aliciapj/django_polls.git...
project already exists
checkout to branch main...
[localhost] local: git checkout main
Already on 'main'
Your branch is up to date with 'origin/main'.
creating venv....
[localhost] local: python3 -m venv .venv
[localhost] local: /home/alicia/django_polls//.venv/bin/pip install django
Requirement already satisfied: django in ./.venv/lib/python3.8/site-packages (4.1.3)
Requirement already satisfied: sqlparse>=0.2.2 in ./.venv/lib/python3.8/site-packages (from django) (0.4.3)
Requirement already satisfied: asgiref<4,>=3.5.2 in ./.venv/lib/python3.8/site-packages (from django) (3.5.2)
Requirement already satisfied: backports.zoneinfo; python_version < "3.9" in ./.venv/lib/python3.8/site-packages (from django) (0.2.1)
checking for django db migrations...
[localhost] local: /home/alicia/django_polls//.venv/bin/python manage.py migrate
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

Done.
```

### Con esto nuestra aplicación Django ya estaría lista para arrancar
--------------
