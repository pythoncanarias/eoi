# Vagrant

1. Descargar el instalable de Vagrant e instalarlo
```
$ wget https://releases.hashicorp.com/vagrant/2.2.14/vagrant_2.2.14_x86_64.deb
$ sudo dpkg -i vagrant_2.2.14_x86_64.deb
```

2. Instalar VirtualBox con las instrucciones de su web:  
https://www.virtualbox.org/wiki/Linux_Downloads

### SOLO PARA SISTEMAS WINDOWS CON WSL

- Añade al fichero ~/.bashrc la siguiente línea, al final del todo, para configurar la integración con windows:  
```
export VAGRANT_WSL_ENABLE_WINDOWS_ACCESS="1"
```  
Después, ejecuta en la consola el siguiente comando para que el cambio tenga efecto:
```
source ~/.bashrc
```

- Además, a la hora de elegir el directorio donde crearemos la máquina virtual, debemos elegir un directorio de windows, así que tendrás que hacer algo como esto antes de continuar:
```
cd /mnt/c/Users/alicia/workspace/eoi/eoi-administracion-sistemas/vagrant
```

3. Inicializar una máquina virtual con Ubuntu 20.04
```bash
$ vagrant init bento/ubuntu-20.04
```
   Salida:
```
A 'Vagrantfile' has been placed in this directory. You are now
ready to 'vagrant up' your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
'vagrantup.com' for more information on using Vagrant.
```

4. Arrancar la máquina virtual
```
$ vagrant up
```
   Salida:
```
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'hashicorp/bionic64'...
==> default: Matching MAC address for NAT networking...
==> default: Checking if box 'hashicorp/bionic64' version '1.0.282' is up to date...
==> default: Setting the name of the VM: vagrant_default_1617039567887_20758
==> default: Fixed port collision for 22 => 2222. Now on port 2203.
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 22 (guest) => 2203 (host) (adapter 1)
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2203
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: 
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default: 
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default: 
    default: Guest Additions Version: 6.0.10
    default: VirtualBox Version: 6.1
==> default: Mounting shared folders...
    default: /vagrant => /home/alicia/workspace/eoi/eoi-administracion-sistemas/automatizacion/vagrant
```

5. Acceder a la máquina virtual

```
$ vagrant ssh
```
   Salida:
```
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-58-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon Mar 29 17:42:00 UTC 2021

  System load:  0.09              Processes:           92
  Usage of /:   2.5% of 61.80GB   Users logged in:     0
  Memory usage: 11%               IP address for eth0: 10.0.2.15
  Swap usage:   0%

 * Introducing self-healing high availability clusters in MicroK8s.
   Simple, hardened, Kubernetes for production, from RaspberryPi to DC.

     https://microk8s.io/high-availability

0 packages can be updated.
0 updates are security updates.
```

6. Salir de la máquina virtual
```
$ logout 
```
   Salida:
```
Connection to 127.0.0.1 closed.
```

## Configurando la red de la máquina virtual
1. Para la máquina virtual:
```
$ vagrant halt
```
```
==> default: Attempting graceful shutdown of VM...
```

2. Edita el fichero `Vagrantfile`, descomenta (elimina el corchete `#` del inicio de la línea) en línea 35, donde dice lo siguiente:

```
config.vm.network "private_network", ip: "192.168.33.10"
```

También descomenta la línea 26 y añade otra más para el puerto 5000 (el de flask)

```
# Create a forwarded port mapping which allows access to a specific port
# within the machine from a port on the host machine. In the example below,
# accessing "localhost:8080" will access port 80 on the guest machine.
# NOTE: This will enable public access to the opened port                       
config.vm.network "forwarded_port", guest: 80, host: 8080                       
config.vm.network "forwarded_port", guest: 5000, host: 5000    
```

3. Arranca la máquina virtual
```
$ vagrant up
```
   Salida:
```
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'hashicorp/bionic64'...
==> default: Matching MAC address for NAT networking...
==> default: Checking if box 'hashicorp/bionic64' version '1.0.282' is up to date...
==> default: Setting the name of the VM: vagrant_default_1617039999444_97628
==> default: Fixed port collision for 22 => 2222. Now on port 2203.
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
    default: Adapter 2: hostonly
==> default: Forwarding ports...
    default: 22 (guest) => 2203 (host) (adapter 1)
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2203
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: 
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default: 
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default: 
    default: Guest Additions Version: 6.0.10
    default: VirtualBox Version: 6.1
==> default: Configuring and enabling network interfaces...
==> default: Mounting shared folders...
    default: /vagrant => /home/alicia/workspace/eoi/eoi-administracion-sistemas/automatizacion/vagrant
```

4. Acceder a la máquina virtual via ssh (contraseña por defecto `vagrant`):
```
$ ssh vagrant@192.168.33.10
```

   Salida:
```
vagrant@192.168.33.10's password: 
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-58-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon Mar 29 17:50:31 UTC 2021

  System load:  0.0               Processes:           88
  Usage of /:   2.5% of 61.80GB   Users logged in:     0
  Memory usage: 11%               IP address for eth0: 10.0.2.15
  Swap usage:   0%                IP address for eth1: 192.168.33.10

 * Introducing self-healing high availability clusters in MicroK8s.
   Simple, hardened, Kubernetes for production, from RaspberryPi to DC.

     https://microk8s.io/high-availability
```
```
0 packages can be updated.
0 updates are security updates.
```
```
Last login: Mon Mar 29 16:55:09 2021 from 10.0.2.2
```
