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
myserver ansible_user=192.168.33.10 ansible_connection=local
```

3. Mostrar el inventario según el fichero que acabamos de crear:
```bash
$ ansible -i inventario.txt --list-hosts all
```
   Salida:
```
  hosts (1):
    myserver
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
    myserver
```  

6. Lanzar una tarea a todos los servidores del inventario:
```
$ ansible -m ping all
```
   Salida:
```
vhost-default | UNREACHABLE! => {
    "changed": false,
    "msg": "Failed to connect to the host via ssh: vagrant@192.168.33.10: Permission denied (publickey,password).",
    "unreachable": true
}
```

7. Lanzar una tarea a todos los servidores del inventario pasando por parámetro que nos pida la contraseña ssh:
```bash
$ ansible -m ping all --ask-pass
```
   Salida:
```
SSH password: 
[DEPRECATION WARNING]: Distribution Ubuntu 18.04 on host vhost-default should use /usr/bin/python3, but is using /usr/bin/python for backward compatibility with prior Ansible releases. A future Ansible release 
will default to using the discovered platform python for this host. See https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information. This feature will be removed in
 version 2.12. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
vhost-default | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
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
$ ansible-playbook playbooks/basics.yml --ask-pass
```
   Salida:
   
```
SSH password: 
```
```
PLAY [all] ******************************************************************************************************************************************************************************************
```
```
TASK [Gathering Facts] ******************************************************************************************************************************************************************************
[DEPRECATION WARNING]: Distribution Ubuntu 18.04 on host 192.168.33.10 should use /usr/bin/python3, but is using /usr/bin/python for backward compatibility with prior Ansible releases. A future 
Ansible release will default to using the discovered platform python for this host. See https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information. 
This feature will be removed in version 2.12. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
ok: [192.168.33.10]
```
```
TASK [hacer un ping] ********************************************************************************************************************************************************************************
ok: [192.168.33.10]
```
```
TASK [mostrar el nombre de la máquina] **************************************************************************************************************************************************************
ok: [192.168.33.10] => {
    "msg": "Nombre de la máquina vagrant"
}
PLAY RECAP ******************************************************************************************************************************************************************************************
192.168.33.10              : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```
