- [0. Instalación de WSL (Windows Subsistem for Linux)](#0-instalación-de-wsl-windows-subsistem-for-linux)
- [1. Instalación de Python](#1-instalación-de-python)
- [2. Administración de librerías](#2-administración-de-librerías)
  - [pip](#pip)
  - [pipenv](#pipenv)
- [3. Entornos virtuales](#3-entornos-virtuales)
- [4. Editores / IDEs / REPLs](#4-editores--ides--repls)
  - [IPython](#ipython)
  - [Atom](#atom)
  - [Sublime](#sublime)
  - [Visual Studio Code](#visual-studio-code)
- [5. Linters](#5-linters)
  - [Flake8](#flake8)
- [6. Debugging](#6-debugging)
  - [pdb](#pdb)
  - [Debuggers integrados en IDE](#debuggers-integrados-en-ide)


# 0. Instalación de WSL (Windows Subsistem for Linux)

> https://learn.microsoft.com/es-es/windows/wsl/install

**Prerrequisitos**

Debe ejecutar Windows 10 versión 2004 y posteriores (compilación 19041 y posteriores) o Windows 11.

Si está ejecutando una compilación anterior o simplemente prefiere no usar el comando install y desea instrucciones paso a paso, consulte [Pasos de instalación manual de WSL para versiones anteriores](https://learn.microsoft.com/es-es/windows/wsl/install-manual).

1. **Lanzamos Powershell con permisos de administrador:**

![Lanzar Powershell con permisos de administrador](https://storage.googleapis.com/curso-eoi/launch-powershell.png)

2. **Comando de instalación de WSL**

    Escribe este comando en PowerShell o el símbolo del sistema de Windows del administrador y, a continuación, reinicia la máquina.

    ```bash
    wsl --install
    ```

    La salida por consola debería ser algo parecido a esto:

    ```bash
    C:\Windows\system32> wsl --install
        Installing: Virtual Machine Platform
        Virtual Machine Platform has been installed.
        Installing: Windows Subsystem for Linux
        Windows Subsystem for Linux has been installed.
        Downloading: WSL Kernel
        Installing: WSL Kernel
        WSL Kernel has been installed.
        Downloading: Ubuntu
        The requested operation is successful. Changes will not be effective until the system is rebooted.

    C:\Windows\system32>
    ```

3. **Iniciar la consola de WSL**

    En este punto, WSL debería estar instalado correctamente, y debería también aparecer en el menú Inicio. Busquémoslo ahí:

    ![Ubuntu 18.04 en menu Inicio](https://storage.googleapis.com/curso-eoi/ubuntu-menu-entry.png)

    La primera vez que inicie una distribución de Linux recién instalada, se abrirá una ventana de la consola y se le pedirá que espere a que los archivos se descompriman y se almacenen en el equipo. Todos los inicios posteriores deberían tardar menos de un segundo en completarse.

4. **Configuración del nombre de usuario y la contraseña de Linux**

> https://learn.microsoft.com/es-es/windows/wsl/setup/environment#set-up-your-linux-username-and-password

Una vez completado el proceso de instalación de la distribución de Linux con WSL, abra la distribución (Ubuntu de forma predeterminada) mediante el menú Inicio. Se le pedirá que cree un nombre de usuario y una contraseña para la distribución de Linux.

![](https://learn.microsoft.com/es-es/windows/wsl/media/ubuntuinstall.png)

```
Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
Enter new UNIX username: alicia
New password:
Retype new password:
passwd: password updated successfully
Installation successful!
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

Welcome to Ubuntu 20.04 LTS (GNU/Linux 5.10.16.3-microsoft-standard-WSL2 x86_64)

* Documentation:  https://help.ubuntu.com
* Management:     https://landscape.canonical.com
* Support:        https://ubuntu.com/advantage

System information as of Sun Sep 18 20:57:04 CEST 2022

System load:  0.0                Processes:             11
Usage of /:   0.4% of 250.98GB   Users logged in:       0
Memory usage: 0%                 IPv4 address for eth0: 172.30.52.132
Swap usage:   0%


0 updates can be installed immediately.
0 of these updates are security updates.


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
New release '22.04.1 LTS' available.
Run 'do-release-upgrade' to upgrade to it.



This message is shown once once a day. To disable it please create the
/home/alicia/.hushlogin file.
```

# 1. Instalación de Python

> https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/#installing-python-38-on-ubuntu-with-apt


> NOTA: Primero comprueba que Python 3.8 no está instalado en tu máquina, ejecutando `python3.8 --version`


1. Ejecuta el siguiente comando en la consola de linux:

```bash
sudo apt update
sudo apt install software-properties-common
```

2. Añade el PPA de deadsnakes a la lista de fuentes del sistema:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
```

Aparecerá un mensaje indicando que presiones "Enter":

```bash
Press [ENTER] to continue or Ctrl-c to cancel adding it.
```

3. Una vez que el repositorio está habilitado, instala Python 3.8:

```bash
sudo apt install python3.8
```

4. Verifica que la instalación se ha realizado correctamente con el siguiente comando:

```bash
python3.8 --version
```

# 2. Administración de librerías

## pip

> https://pip.pypa.io/en/stable/getting-started/

Python viene con varios módulos integrados, pero existeng muchas más librerías desarrolladas por la comunidad de Pythonque añaden mucha más funcionalidad al core de Python. 

La forma más sencilla de instalar estos módulos para que podamos usarlos en nuestros programas es utilizar `pip`.

Para instalar módulos localmente, necesitas crear y activar lo que se llama un entorno virtual (lo haremos en el siguiente apartado), por lo que `pip install` se instalá en la carpeta donde se encuentra ese entorno virtual, en lugar de globalmente (que puede requerir privilegios de administrador).

Antes de usar pip, deberás instalarlo:

```
sudo apt install python3-pip
```

El repositorio de librerías que usa pip por defecto es [PyPI](https://pypi.org/)

## pipenv

> https://pipenv-es.readthedocs.io/es/latest/

Pipenv es una herramienta que apunta a traer todo lo mejor del mundo de empaquetado (bundler, composer, npm, cargo, yarn, etc.) al mundo de Python.

Automáticamente crea y maneja un entorno virtual para tus proyectos, también como agregar/remover paquetes desde tu Pipfile como instalar/desisntalar paquetes. También genera el más importante Pipfile.lock, que es usado para producir determinado build.

Para instalarlo:
```bash
pip install pipenv
```

# 3. Entornos virtuales

> https://docs.python.org/es/3/library/venv.html

El módulo venv proporciona soporte para crear «entornos virtuales» ligeros con sus propios directorios de ubicación, aislados opcionalmente de los directorios de ubicación del sistema. 

Cada entorno virtual tiene su propio binario Python (que coincide con la versión del binario que se utilizó para crear este entorno) y puede tener su propio conjunto independiente de paquetes Python instalados en sus directorios de ubicación.

1. Para instalar venv, escribe:
```bash
sudo apt install python3-venv
```

2. Para crear un entorno virtual:

```bash
python3.8 -m venv /path/to/new/virtual/environment
```

> Es muy común llamar al virtualenv `.venv` y situarlo en la misma carpeta donde crearemos el proyecto, por lo que es muy común ejecutar el comando de creación de entornos virtuales de la siguiente forma:

  ```bash
  python3.8 -m venv .venv
  ```

3. Para activar el entorno virtual, debemos escribir (en el caso de haber llamado el entorno virtual `.venv`):

```bash
source .venv/bin/activate
```

> Después de este comando, el nombre de nuestro entorno virtual aparecerá en la consola al principio de la línea y entre paréntesis:

```bash
(.venv) usuario@host:~
```

# 4. Editores / IDEs / REPLs

## IPython

> https://ipython.readthedocs.io/en/stable/

IPython es un shell interactivo que añade funcionalidades extra al modo interactivo incluido con Python, como resaltado de líneas y errores mediante colores, una sintaxis adicional para el shell, autocompletado mediante tabulador de variables, módulos y atributos; entre otras funcionalidades.

![screenshot de la consola de ipython](https://ipython.readthedocs.io/en/stable/_images/ipython-6-screenshot.png)

Para instalarlo (idealmente, en un entorno virtual):
```bash
pip install ipython
```

## Atom

> https://atom.io/

Atom es un editor de código fuente de código abierto para macOS, Linux, y Windows​ con soporte para múltiples plug-in escritos en Node.js y control de versiones Git integrado, desarrollado por GitHub.

![screenshot of atom](https://upload.wikimedia.org/wikipedia/commons/6/64/Atom-editor.png)

Para instalarlo:
```bash
sudo apt install atom
```

## Sublime

> https://www.sublimetext.com/

Sublime Text es un editor de texto y editor de código fuente. Está escrito en C++ y Python para los plugins.​ Desarrollado originalmente como una extensión de Vim, con el tiempo fue creando una identidad propia.

![screenshot de sublime-text](https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_819,h_478/https://dashboard.snapcraft.io/site_media/appmedia/2018/03/linux.png)

Para instalarlo:
```bash
sudo snap install sublime-text --classic
```

## Visual Studio Code

> https://code.visualstudio.com/

Visual Studio Code es un editor de código fuente desarrollado por Microsoft para Windows, Linux, macOS y Web.

Incluye soporte para la depuración, control integrado de Git, resaltado de sintaxis, finalización inteligente de código, fragmentos y refactorización de código.

![screenshot de vscode](https://code.visualstudio.com/assets/home/home-screenshot-linux-lg.png)

Para instalarlo:
```bash
sudo snap install --classic code
```


> Para WSL existe un tutorial desarrollado por microsoft para instalar e integrar correctamente Visual Studio Code: \
https://learn.microsoft.com/es-es/windows/wsl/tutorials/wsl-vscode#install-vs-code-and-the-remote-wsl-extension


# 5. Linters

Los linters son programas que realizan análisis estático de código. Se diferencian de los tests unitarios, de integración o manuales que analizan el código de manera dinámica y en ejecución.

Los linters suelen buscar:

- Uso de variables antes de ser inicializadas o creadas.
- Condiciones que no varían bajo ninguna circunstancia (siempre verdaderas o falsas).
- Cálculos cuyos resultados probablemente caigan fuera del rango permitido por la variable.

## Flake8

> https://flake8.pycqa.org/en/latest/

Es un gran conjunto de herramientas para verificar su código fuente contra el PEP8, errores de programación (como “library imported but unused” y “Undefined name”) y para verificar la complejidad ciclomática (es una métrica de software para medir el número de rutas independientes a través del código fuente - a mayor número de ifs dentro de una función, mayor número de caminos tendrá).

**Instalación de Flake8**

```bash
pip install flake8
```

# 6. Debugging

## pdb

> https://docs.python.org/es/3/library/pdb.html

El módulo pdb define un depurador de código fuente interactivo para programas Python.

Soporta el establecimiento de puntos de ruptura (condicionales) y pasos sencillos a nivel de línea de código fuente, inspección de marcos de pila, listado de código fuente, y evaluación de código Python arbitrario en el contexto de cualquier marco de pila.

También soporta depuración post-mortem y puede ser llamado bajo control del programa.

> https://docs.python.org/es/3/library/pdb.html#debugger-commands

## Debuggers integrados en IDE

