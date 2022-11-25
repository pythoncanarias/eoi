# 1 - Ansible: Primeros pasos

En este ejercicio .......

1. Mostrar el inventario actual (estará vacío)  
```
$ ansible --list-hosts all
```
   Salida:
```
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'
  hosts (0):
```

2. Crear un fichero que se llame `inventario.txt` con el siguiente contenido:  
```
eoi-server1 ansible_host=3.15.38.15 ansible_user=alicia
eoi-server2 ansible_host=18.217.241.86 ansible_user=alicia
```

3. Mostrar el inventario según el fichero que acabamos de crear:
```bash
$ ansible -i inventario.txt --list-hosts all
```
   Salida:
```
  hosts (1):
    eoi-server
```

4. Como no queremos tener que especificar el fichero de inventario cada vez que queramos operar con Ansible, crea un fichero en el mismo directorio que se llame `ansible.cfg` con el siguiente contenido:
```bash
[defaults]
inventory = ./inventario.txt
```

5. Mostrar el inventario sin especificar ningún fichero:  
```
$ ansible --list-hosts all
```
   Salida:
```
  hosts (1):
    eoi-server
```  

6. Lanzar una tarea a todos los servidores del inventario:
```
$ ansible -m ping all
```
   Salida:
```
eoi-server | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

7. Lanzar una tarea a todos los servidores del inventario pasando por parámetro que nos pida la contraseña ssh:
```bash
$ ansible -m ping all
```
   Salida:
```
SSH password: 
eoi-server | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

# 2 - Ansible: Playbooks

1. Crea una carpeta que se llama `playbooks`
```
$ mkdir playbooks
$ cd playbooks
```

2. Crear un fichero que se llame `basics.yml` con el siguiente contenido:

```yaml
---
- hosts: all
  tasks:
    - name: hacer un ping
      ping:
        
    - name: mostrar el nombre de la máquina
      debug:
        msg: "Nombre de la máquina {{ ansible_hostname }}"
```

3. Ejecutar el playbook con el siguiente comando:
```
$ ansible-playbook playbooks/basics.yml 
```
   Salida:
```
SSH password:

PLAY [all] *****************************************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************************
ok: [eoi-server]

TASK [hacer un ping] *******************************************************************************************************************************************************************
ok: [eoi-server]

TASK [mostrar el nombre de la máquina] *************************************************************************************************************************************************
ok: [eoi-server] => {
    "msg": "Nombre de la máquina ip-172-31-29-30"
}

PLAY RECAP *****************************************************************************************************************************************************************************
eoi-server                 : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Despliegue de django-polls


En este ejercicio vamos a automatizar el despliegue de la aplicación `django_polls` en nuestro propio ordenador, usando ansible

El repositorio de django_polls lo podéis encontrar aquí: https://github.com/aliciapj/django_polls

Es muy importante que hagáis un fork del repositorio en vuestra propia cuenta de Github y hagáis el resto del ejercicio utilizando vuestra propia URL del proyecto.

En el readme del repositorio tenemos los pasos que hay que seguir para instalar el repositorio. A continuación vamos a reproducir esos mismos pasos utilizando ansible.


0. Pasos previos a la instalación que indica en el repositorio:
    - Crea un fichero llamado `deploy.yml` con el siguiente contenido:
    ```yaml
    - hosts: all

      tasks:
      - name: hacer un ping
        ping:
    ```

    - Ejecuta la receta para ver que todo funciona:
    ```bash
    ansible-playbook deploy.yml
    ```

    - Deshabilita los gather_facts para que vaya un poco más rápido:
    ```yaml
    - hosts: all
      gather_facts: false

      tasks:
      - name: hacer un ping
        ping:
    ```

--------------
A partir de aquí, añade las siguientes tareas a tu receta:

> 1. Descarga el código con el siguiente comando: \
    `git clone https://github.com/aliciapj/django_polls.git`

Recuerda poner tu repositorio de github y tu ruta de `home`!!

```yaml
  tasks:
    # https://docs.ansible.com/ansible/latest/collections/ansible/builtin/git_module.html
    - name: Clone/pull project repo
      git:
        repo: https://github.com/aliciapj/django_polls.git
        dest: /home/alicia/django-polls
```

> 2. Entramos en la carpeta descargada django_polls y creamos el entorno virtual con el comando: \
    `python3 -m venv .venv`

Prueba con el módulo: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/pip_module.html


> 3. Activamos el entorno virtual \
    `source .venv/bin/activate`

Este paso no es necesario - en las siguientes tareas, tendremos que poner como parámetro la ruta de nuestro `virtualenv`

> 4. Instalamos las librerías necesarias que se encuentran en el fichero requirements.txt \
    `pip install -r requirements.txt`

Este paso no es necesario - en el paso 2 nos aseguramos de crear el virtualenv y de que tenga las librerías del requirements.txt

> 5. Ejecutamos las migraciones \
    `python manage.py migrate`

Prueba con el módulo: https://docs.ansible.com/ansible/latest/collections/community/general/django_manage_module.html

Si te da error de permisos, igual antes de ejecutar este módulo tienes que darle permisos de ejecución (0777) al fichero manage.py con este módulo: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/file_module.html

> 6. Cargamos los datos iniciales: \
    `python manage.py loaddata fixtures/polls_data.json`

Prueba con el módulo: https://docs.ansible.com/ansible/latest/collections/community/general/django_manage_module.html

---
Puntos extra!!

- Utiliza un fichero de variables para poner las rutas y cadenas de configuración.
  - Crea un fichero `vars.yml` con los parámetros usando esta sintaxis:
    ```yaml
    # the base path to install to. You should not need to change this.
    project_path: /home/alicia/django-polls

    ...
    ```

  - Importa las variables añadiendo esto a la cabecera del `deploy.yml`
  ```yaml
  - hosts: all
    vars_files:
      - vars.yml
    gather_facts: false

    tasks:
  ```

  - Sustituye las cadenas de string por el valor de la variable así:
  ```yaml
    tasks:
    # https://docs.ansible.com/ansible/latest/collections/ansible/builtin/git_module.html
    - name: Clone/pull project repo
      git:
        repo: "{{project_repo}}"
        dest: "{{project_path}}"
        force: true
  ```
