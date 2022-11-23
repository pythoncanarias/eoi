# psutil — Process and system utilities

- Biblioteca multiplataforma para recuperar información sobre procesos en ejecución y utilización del sistema (CPU, memoria, discos, red, sensores) en Python
- Implementa muchas funcionalidades que ofrecen las herramientas clásicas de línea de comandos de UNIX como `ps`, `top`, `iotop`, `lsof`, `netstat`, `ifconfig`, `free` y otras

<small><a href="https://psutil.readthedocs.io/en/latest/">Documentación oficial</a></small>

#### Instalación


```python
! pip install psutil
```

    Requirement already satisfied: psutil in /mnt/c/Users/alicia/workspace/eoi/eoi-administracion-sistemas/.venv/lib/python3.8/site-packages (5.8.0)
    [33mWARNING: You are using pip version 21.1.1; however, version 21.1.2 is available.
    You should consider upgrading via the '/mnt/c/Users/alicia/workspace/eoi/eoi-administracion-sistemas/.venv/bin/python3 -m pip install --upgrade pip' command.[0m


## Memoria RAM
Crea un script que muestre el estado de la memoria RAM, tanto en la memoria como en el swap, en el mismo formato que el comando `free` de ubuntu:
```
              total        used        free      shared  buff/cache   available
Mem:       26047344     2024548    21625084        1532     2397712    23632008
Swap:       7340032           0     7340032
```

Consejos:
- En la librería de psutils consulta las funciones de memoria [virtual_memory](https://psutil.readthedocs.io/en/latest/#psutil.virtual_memory) y [swap_memory](https://psutil.readthedocs.io/en/latest/#psutil.swap_memory)
- Para imprimir los números alineados a la derecha o añadiendo espacios antes o después, busca 'string padding' en Python 
- (Para puntos extra) Para convertir bytes a "formato humano" (con la cifra en KB, MB o GB según corresponda) podéis implementar vuestra propia función... o podéis usar la librería [humanize](https://python-humanize.readthedocs.io/en/latest/filesize/)


## Discos
Crea un script que muestre todas las *particiones* montadas en tu sistema con el mismo formato que el comando `df -h` de ubuntu:
```
Device                 Total       Used       Free  Use %       Type Mount
/dev/sdb            269.5 GB     5.7 GB   250.0 GB     2%       ext4 /
/dev/sdd            269.5 GB     3.9 GB   251.8 GB     1%       ext4 /mnt/wsl/docker-desktop-data/isocache
/dev/sdc            269.5 GB   126.7 MB   255.6 GB     0%       ext4 /mnt/wsl/docker-desktop/docker-desktop-user-distro
/dev/loop0          374.9 MB   374.9 MB    0 Bytes   100%    iso9660 /mnt/wsl/docker-desktop/cli-tools
/dev/sdb            269.5 GB     5.7 GB   250.0 GB     2%       ext4 /mnt/wsl/docker-desktop-bind-mounts/Ubuntu/9d29
```

Consejos:
- En la librería de psutils consulta las funciones de memoria [disk_partitions](https://psutil.readthedocs.io/en/latest/#psutil.disk_partitions) y [disk_usage](https://psutil.readthedocs.io/en/latest/#psutil.disk_usage)
- Para convertir bytes a "formato humano" (con la cifra en KB, MB o GB según corresponda) podéis implementar vuestra propia función... o podéis usar la librería [humanize](https://python-humanize.readthedocs.io/en/latest/filesize/)
- Para imprimir los números alineados a la derecha o añadiendo espacios antes o después, busca 'string padding' en Python 

## Procesos
Crea un script que muestre la información del proceso llamado 'python' en tu sistema con el siguiente formato:
```
Proceso: python
ID: 7713
Proceso padre: 604 - bash
Ruta del proceso: /usr/bin/python3.8
Llamado como: ['python', '07-sys-admin/ejercicios/psutils/process_detail.py']
Llamado por el usuario: alicia
Estado: running
Creado el 2022-11-01 a las 14:23:37
```

Consejos:
- Para encontrar el proceso `'python'` entre la lista de procesos, puedes iterar con [process_iter](https://psutil.readthedocs.io/en/latest/#psutil.process_iter) y comprobar cuál de ellos se llama `'python'`. Puedes hacer una función que dado el nombre del proceso te devuelva el objeto proceso
- Las propiedades del objeto proceso las tienes en la [documentación](https://psutil.readthedocs.io/en/latest/#psutil.Process)
