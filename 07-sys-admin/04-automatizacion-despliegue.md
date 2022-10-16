# Configuration Management & IaC
![robot](https://images.unsplash.com/photo-1563968743333-044cef800494?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80)

# Configuration Management & IaC
- Fabric
- Ansible

## Configuration Management

- Cambiar y mantener el estado de algunas piezas de la infraestructura de manera consistente, sostenible y estable
- Automatizar operaciones que surgen del día a día, como la creación de usuarios, actualización de software, etc

**Beneficios**
- Ahorro de tiempo - se tarda menos en hacer cambios en la configuración
- Mejor monitorización sobre los recursos
- Mejora la mantenibilidad del sistema
- Mantiene la configuración estandarizada en todos los servidores

## Infrastructure as Code - IaC
Administrar y aprovisionar infraestructura usando código.
En lugar de hacer cosas manualmente para administrar y aprovisionar estructura (servidores, máquinas virtuales, etc) usaremos scripts y código para crear y cambiar cosas como servidores, instancias, entornos, contenedores o clústers

**Beneficios**
- Consistencia en la creación y gestión de recursos
- Reusabilidad - el mismo script se utiliza para múltiples máquinas
- Facilita la escalabilidad - es fácil crear más máquinas o aumentar la infraestructura
- Es auto-documentada

# Fabric
![Fabric logo](http://www.fabfile.org/_static/logo.png)

Fabric es una librería de alto nivel de Python diseñada para ejecutar comandos de shell de forma remota a través de SSH.

Fabric se basa en otras librerías Python extendiendo sus API para complementarse entre sí y proporcionar funcionalidad adicional:

- [Invoke](http://www.pyinvoke.org/) implementa el análisis en cliente, la organización de tareas y la ejecución de comandos de shell (un marco genérico más una implementación específica para comandos locales).

    - Toda la funcionalidad que no sea específica de los sistemas remotos tiende a residir en Invoke y, a menudo, los programadores que no necesitan ninguna funcionalidad remota lo utilizan de forma independiente (sin usar Fabric).
    - Los usuarios de Fabric importarán con frecuencia objetos de Invoke, en los casos en que Fabric en sí no tenga necesidad de crear una subclase o modificar alguno de los métodos que proporciona Invoke.

- [Paramiko](http://www.paramiko.org/) implementa la funcionalidad SSH de nivel bajo / medio: sesiones SSH y SFTP, administración de claves, etc.
    - Fabric utiliza Paramiko "por dentro"; los usuarios rara vez lo usarán directamente desde Paramiko.

- run - Ejecuta comandos en una shell del host remoto
- sudo - Ejecuta comandos en una shell del host remoto con privilegios de sudo
- get - Descarga uno o más ficheros del host remoto
- put - Copia al host remoto uno o más ficheros del host local

### Instalación


```python
! pip install fabric
```

    Collecting fabric
      Using cached fabric-2.6.0-py2.py3-none-any.whl (53 kB)
    Collecting paramiko>=2.4
      Using cached paramiko-2.7.2-py2.py3-none-any.whl (206 kB)
    Collecting invoke<2.0,>=1.3
      Using cached invoke-1.5.0-py3-none-any.whl (211 kB)
    Collecting pathlib2
      Using cached pathlib2-2.3.5-py2.py3-none-any.whl (18 kB)
    Collecting cryptography>=2.5
      Using cached cryptography-3.4.7-cp36-abi3-manylinux2014_x86_64.whl (3.2 MB)
    Collecting pynacl>=1.0.1
      Using cached PyNaCl-1.4.0-cp35-abi3-manylinux1_x86_64.whl (961 kB)
    Collecting bcrypt>=3.1.3
      Using cached bcrypt-3.2.0-cp36-abi3-manylinux2010_x86_64.whl (63 kB)
    Requirement already satisfied: six in ./.venv/lib/python3.8/site-packages (from pathlib2->fabric) (1.16.0)
    Requirement already satisfied: cffi>=1.12 in ./.venv/lib/python3.8/site-packages (from cryptography>=2.5->paramiko>=2.4->fabric) (1.14.5)
    Requirement already satisfied: pycparser in ./.venv/lib/python3.8/site-packages (from cffi>=1.12->cryptography>=2.5->paramiko>=2.4->fabric) (2.20)
    Installing collected packages: cryptography, pynacl, bcrypt, paramiko, invoke, pathlib2, fabric
    Successfully installed bcrypt-3.2.0 cryptography-3.4.7 fabric-2.6.0 invoke-1.5.0 paramiko-2.7.2 pathlib2-2.3.5 pynacl-1.4.0


### Ejemplos de código
(Arranca la máquina virtual con Vagrant)


```python
from fabric.connection import Connection

vhost_conn = Connection('vagrant@192.168.33.10', connect_kwargs={"password": "vagrant"})
result = vhost_conn.run('hostname')
print(result)
```

    vagrant
    Command exited with status 0.
    === stdout ===
    vagrant
    
    (no stderr)



```python
vhost_conn.sudo('whoami', hide='stderr')
```

    root





    <Result cmd="sudo -S -p '[sudo] password: ' whoami" exited=0>




```python
# Mostrar el espacio en disco libre 
def disk_free(c):
    uname = c.run('uname -s', hide=True)
    if 'Linux' in uname.stdout:
        command = "df -h / | tail -n1 | awk '{print $5}'"
        return c.run(command, hide=True).stdout.strip()
    err = f"No idea how to get disk space on {uname}!"
    raise Exit(err)

print(disk_free(vhost_conn))
```

    3%



```python
# Transfer files
result = vhost_conn.put('/mnt/c/Users/alicia/workspace/eoi/eoi-administracion-sistemas/README.md', remote='/home/vagrant/')
print("Uploaded {0.local} to {0.remote}".format(result))
```

    Uploaded /mnt/c/Users/alicia/workspace/eoi/eoi-administracion-sistemas/README.md to /home/vagrant/README.md


### Ejercicio de Fabric!
Ve a [ejercicios/fabric.ipynb](ejercicios/fabric.ipynb)

![Ansible logo](https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Ansible_logo.svg/245px-Ansible_logo.svg.png)

Ansible es una plataforma de software libre para configurar y administrar ordenadores. 


Combina instalación multi-nodo (es decir: permite desplegar configuraciones de servidores y servicios por lotes), ejecuciones de tareas ad hoc y administración de configuraciones. 

Adicionalmente, Ansible es categorizado como una herramienta de orquestación.

Gestiona nodos a través de SSH y no requiere ningún software remoto adicional (excepto Python 2.4 o posterior) para instalarlo. 

Dispone de módulos que trabajan sobre JSON y la salida estándar puede ser escrita en cualquier lenguaje. Nativamente utiliza YAML para describir configuraciones reusables de los sistemas

### Principales características

- Aprovisionamiento
- Gestión de la configuración
- Despliegue de aplicaciones
- Seguridad y Cumplimiento
- Orquestación

### Propósitos

- Mínimo por naturaleza. Los sistemas de administración no deben imponer dependencias adicionales.
- Consistente.
- Seguro. Ansible no instala agentes vulnerables en los nodos. Solamente se requiere OpenSSH que es considerado crítico y altamente comprobado.
- Alta confiabilidad. El modelo de idempotencia es aplicado para las instalaciones y configuraciones, para prevenir efectos secundarios en la ejecución repetitiva de guiones (scripts)
- Suave curva de aprendizaje. Los playbooks o libretos usan un lenguaje descriptivo simple, basado en YAML.

### Conceptos

- **Controladora (servidores)**  
Cualquier máquina con Ansible instalado.

- **Nodos (clientes)**  
Máquinas que serán controladas con Ansible (también llamados _hosts_). Ansible no se instalará en esas máquinas

- **Inventario**  
Descripción de los nodos que pueden ser accedidos por Ansible. Por defecto se ubica en `/etc/ansible/hosts`. Además, los nodos pueden ser asignados a grupos.  

- **Módulos**  
Las unidades de trabajo en Ansible. Cada módulo es autosuficiente e idempotente

- **Tareas**
Son las unidades de acción de Ansible, y cada tarea es una llamada a un módulo de Ansible. Las tareas son ejecutadas en orden, de una en una, contra cada máquina que encaja con el patrón del host, para luego seguir con la próxima tarea

- **Manual de tácticas o Playbooks**
Son listas ordenadas de tareas guardadas en un fichero para poder ejecutarlas múltiples veces. Los libros de jugadas pueden incluir tanto variables como tareas. Están escritos en YAML y deben ser fáciles de leer, escribir, compartir y comprender.

### Instalación

En la terminal de Ubuntu: 

```
sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
```

Para comprobar que se ha instalado correctamente:
```
ansible localhost -m ping --ask-pass
```

### Ejercicio de Ansible!
Ve a [ejercicios/ansible.ipynb](ejercicios/ansible.ipynb)

# Siguientes pasos en Administración de Sistemas
![camino](https://images.unsplash.com/photo-1439396874305-9a6ba25de6c6?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80)

- Contenedores & Orquestación
    * Docker & Kubernetes
- Miniproyecto!
