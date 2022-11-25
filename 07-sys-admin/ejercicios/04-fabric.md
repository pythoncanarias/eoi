# Fabric

En este ejercicio vamos a automatizar el despliegue de la aplicación `django_polls` en nuestro propio ordenador, usando fabric y su paquete `local`

El repositorio de django_polls lo podéis encontrar aquí: https://github.com/aliciapj/django_polls

Es muy importante que hagáis un fork del repositorio en vuestra propia cuenta de Github y hagáis el resto del ejercicio utilizando vuestra propia URL del proyecto.

En el readme del repositorio tenemos los pasos que hay que seguir para instalar el repositorio. A continuación vamos a reproducir esos mismos pasos utilizando al librería de Fabric.

0. Pasos previos a la instalación que indica en el repositorio:
    - Activa el virtual environment e instala fabric:
    ```
    pip install fabric3
    ```

    - Crea un fichero `fabfile.py` y añade los primeros imports y constantes de nuestro script. Sustituye las rutas del proyecto y la url del repositorio por las de tu repositorio y tu máquina local

    ```python
    from fabric.api import local

    PROJECT_NAME = "django_polls"
    PROJECT_PATH = f"/home/<pon_tu_usuario_aqui>/{PROJECT_NAME}"
    REPO_URL = "https://github.com/aliciapj/django_polls.git"
    VENV_PYTHON = f'{PROJECT_PATH}/.venv/bin/python'
    VENV_PIP = f'{PROJECT_PATH}/.venv/bin/pip'


    def deploy():
    local('echo "hello world"')
    ```

    - Comprueba que todo funciona correctamente ejecutando `fab deploy`. Deberías obtener algo como esto:
    ```
    [localhost] local: echo "hello world"
    hello world

    Done.
    ```

--------------
> 1. Descarga el código con el siguiente comando: \
    `git clone https://github.com/aliciapj/django_polls.git`


```python
import os

def clone(): 
    print(f"clone repo {REPO_URL}...")   

    if os.path.exists(PROJECT_PATH):
        print("project already exists")
    else:
        local(f"git clone {REPO_URL} {PROJECT_PATH}")
```

    Y ahora añadimos la tarea al proceso de deploy:

```python
def deploy():
    clone()
```

> Prueba la tarea con `fab deploy`, comprueba que el resultado es algo como lo siguiente y comprueba que la operación se ha ejecutado correctamente en el servidor
```
clone repo https://github.com/aliciapj/django_polls.git...
[localhost] local: git clone https://github.com/aliciapj/django_polls.git /tmp/django_polls
Cloning into '/tmp/django_polls'...
remote: Enumerating objects: 143, done.
remote: Counting objects: 100% (143/143), done.
remote: Compressing objects: 100% (99/99), done.
remote: Total 143 (delta 59), reused 116 (delta 33), pack-reused 0
Receiving objects: 100% (143/143), 718.35 KiB | 3.31 MiB/s, done.
Resolving deltas: 100% (59/59), done.

Done.
```

> 2. Entramos en la carpeta descargada django_polls y creamos el entorno virtual con el comando: \
    `python3 -m venv .venv`

Para trabajar en la carpeta que hemos creado en el paso anterior, tenemos que importar `lcd`

```python
from fabric.context_managers import lcd

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
    create_venv()
```

> Prueba la tarea con `fab deploy`

```
clone repo https://github.com/aliciapj/django_polls.git...
project already exists
creating venv....
[localhost] local: python3 -m venv .venv

Done.
```

> 3. Activamos el entorno virtual \
    `source .venv/bin/activate`

Este paso no se puede hacer porque en Fabric no trabajamos con la consola. En su lugar, en vez de usar el comando `python` y `pip` vamos a usar el python y pip que está en el entorno virtual que acabamos de crear, y cuya ruta tenemos guardada en el parámetro `VENV_PYTHON` y `VENV_PIP`

> 4. Instalamos las librerías necesarias que se encuentran en el fichero requirements.txt \
    `pip install -r requirements.txt`

```python
def install_requirements():

    print("installing requirements.txt....")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PIP} install -r requirements.txt ")


def deploy():
    clone()
    create_venv()
    install_requirements()
```

Debería salir algo como esto:
```
clone repo https://github.com/aliciapj/django_polls.git...
project already exists
creating venv....
[localhost] local: python3 -m venv .venv
installing requirements.txt....
[localhost] local: /tmp/django_polls/.venv/bin/pip install -r requirements.txt
Collecting asgiref==3.3.4
  Downloading asgiref-3.3.4-py3-none-any.whl (22 kB)
Collecting Django==3.2.3
  Downloading Django-3.2.3-py3-none-any.whl (7.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.9/7.9 MB 48.7 MB/s eta 0:00:00
Collecting pytz==2021.1
  Downloading pytz-2021.1-py2.py3-none-any.whl (510 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 510.8/510.8 KB 103.1 MB/s eta 0:00:00
Collecting sqlparse==0.4.1
  Downloading sqlparse-0.4.1-py3-none-any.whl (42 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.2/42.2 KB 12.6 MB/s eta 0:00:00
Installing collected packages: pytz, sqlparse, asgiref, Django
Successfully installed Django-3.2.3 asgiref-3.3.4 pytz-2021.1 sqlparse-0.4.1
```

> 5. Ejecutamos las migraciones \
    `python manage.py migrate`

```python
def django_migrate():

    print("executing django migrations....")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PYTHON} manage.py migrate ")


def deploy():
    clone()
    create_venv()
    install_requirements()
    django_migrate()
```

Debería salir algo como esto:

```
clone repo https://github.com/aliciapj/django_polls.git...
project already exists
creating venv....
[localhost] local: python3 -m venv .venv
installing requirements.txt....
[localhost] local: /tmp/django_polls/.venv/bin/pip install -r requirements.txt
Requirement already satisfied: asgiref==3.3.4 in ./.venv/lib/python3.9/site-packages (from -r requirements.txt (line 1)) (3.3.4)
Requirement already satisfied: Django==3.2.3 in ./.venv/lib/python3.9/site-packages (from -r requirements.txt (line 2)) (3.2.3)
Requirement already satisfied: pytz==2021.1 in ./.venv/lib/python3.9/site-packages (from -r requirements.txt (line 3)) (2021.1)
Requirement already satisfied: sqlparse==0.4.1 in ./.venv/lib/python3.9/site-packages (from -r requirements.txt (line 4)) (0.4.1)
WARNING: You are using pip version 22.0.4; however, version 22.3.1 is available.
You should consider upgrading via the '/tmp/django_polls/.venv/bin/python3 -m pip install --upgrade pip' command.
executing django migrations....
[localhost] local: /tmp/django_polls/.venv/bin/python manage.py migrate
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

> 6. Cargamos los datos iniciales: \
    `python manage.py loaddata fixtures/polls_data.json`

```python
def django_loaddata():

    print("loading initial data...")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PYTHON} manage.py loaddata fixtures/polls_data.json ")


def deploy():
    clone()
    create_venv()
    install_requirements()
    django_migrate()
    django_loaddata()
```

Debería salir algo como esto:

```
clone repo https://github.com/aliciapj/django_polls.git...
project already exists
creating venv....
[localhost] local: python3 -m venv .venv
installing requirements.txt...
[localhost] local: /tmp/django_polls/.venv/bin/pip install -r requirements.txt
Requirement already satisfied: asgiref==3.3.4 in ./.venv/lib/python3.9/site-packages (from -r requirements.txt (line 1)) (3.3.4)
Requirement already satisfied: Django==3.2.3 in ./.venv/lib/python3.9/site-packages (from -r requirements.txt (line 2)) (3.2.3)
Requirement already satisfied: pytz==2021.1 in ./.venv/lib/python3.9/site-packages (from -r requirements.txt (line 3)) (2021.1)
Requirement already satisfied: sqlparse==0.4.1 in ./.venv/lib/python3.9/site-packages (from -r requirements.txt (line 4)) (0.4.1)
WARNING: You are using pip version 22.0.4; however, version 22.3.1 is available.
You should consider upgrading via the '/tmp/django_polls/.venv/bin/python3 -m pip install --upgrade pip' command.
executing django migrations...
[localhost] local: /tmp/django_polls/.venv/bin/python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  No migrations to apply.
loading initial data...
[localhost] local: /tmp/django_polls/.venv/bin/python manage.py loaddata fixtures/polls_data.json
Installed 51 object(s) from 1 fixture(s)

Done.
```

> 7. Arrancamos el servidor \
    `python manage.py runserver`

```python
def django_runserver():

    print("runing server...")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PYTHON} manage.py runserver")


def deploy():
    clone()
    create_venv()
    install_requirements()
    django_migrate()
    django_loaddata()
    django_runserver()
```

Y debería salirte algo como esto y en la consola se te quedará arrancado el servidor de django:

```
clone repo https://github.com/aliciapj/django_polls.git...
project already exists
creating venv....
[localhost] local: python3 -m venv .venv
installing requirements.txt...
[localhost] local: /tmp/django_polls/.venv/bin/pip install -r requirements.txt
Requirement already satisfied: asgiref==3.3.4 in ./.venv/lib/python3.9/site-packages (from -r requirements.txt (line 1)) (3.3.4)
Requirement already satisfied: Django==3.2.3 in ./.venv/lib/python3.9/site-packages (from -r requirements.txt (line 2)) (3.2.3)
Requirement already satisfied: pytz==2021.1 in ./.venv/lib/python3.9/site-packages (from -r requirements.txt (line 3)) (2021.1)
Requirement already satisfied: sqlparse==0.4.1 in ./.venv/lib/python3.9/site-packages (from -r requirements.txt (line 4)) (0.4.1)
WARNING: You are using pip version 22.0.4; however, version 22.3.1 is available.
You should consider upgrading via the '/tmp/django_polls/.venv/bin/python3 -m pip install --upgrade pip' command.
executing django migrations...
[localhost] local: /tmp/django_polls/.venv/bin/python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  No migrations to apply.
loading initial data...
[localhost] local: /tmp/django_polls/.venv/bin/python manage.py loaddata fixtures/polls_data.json
Installed 51 object(s) from 1 fixture(s)
runing server...
[localhost] local: /tmp/django_polls/.venv/bin/python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 25, 2022 - 14:02:06
Django version 3.2.3, using settings 'django_polls.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

------

El resultado final del fichero sería el siguiente:

```python
import os

from fabric.api import local
from fabric.context_managers import lcd

PROJECT_NAME = "django_polls"
PROJECT_PATH = f"/tmp/{PROJECT_NAME}"
REPO_URL = "https://github.com/aliciapj/django_polls.git"
VENV_PYTHON = f'{PROJECT_PATH}/.venv/bin/python'
VENV_PIP = f'{PROJECT_PATH}/.venv/bin/pip'


def clone():
    print(f"clone repo {REPO_URL}...")

    if os.path.exists(PROJECT_PATH):
        print("project already exists")
    else:
        local(f"git clone {REPO_URL} {PROJECT_PATH}")


def create_venv():

    print("creating venv....")

    with lcd(PROJECT_PATH):
        local("python3 -m venv .venv")


def install_requirements():

    print("installing requirements.txt...")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PIP} install -r requirements.txt ")


def django_migrate():

    print("executing django migrations...")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PYTHON} manage.py migrate ")


def django_loaddata():

    print("loading initial data...")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PYTHON} manage.py loaddata fixtures/polls_data.json ")


def django_runserver():

    print("runing server...")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PYTHON} manage.py runserver")


def deploy():
    clone()
    create_venv()
    install_requirements()
    django_migrate()
    django_loaddata()
    django_runserver()
```

## Desplegar en el servidor remoto

1. Cambia las llamadas

```python
from fabric.api import local

local(do-something)
```

por
```python
from fabric.api import run

run(do-something)
```

2. Cambia los
```python
from fabric.context_managers import lcd

with lcd(PROJECT_PATH):
```

por

```python
from fabric.api import cd


with cd(PROJECT_PATH):
```

3. Define los hosts de destino con

```python
from fabric.api import env

env.hosts = ['3.15.38.15']
```

4. Para comprobar si un fichero existe en el servidor, usa

```python
from fabric.contrib.files import exists
```