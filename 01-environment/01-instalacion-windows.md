


# Instalación de componentes en Windows

## Instalación de WSL (Windows Subsistem for Linux)

> https://learn.microsoft.com/es-es/windows/wsl/install

0. **Prerrequisitos**

   Debe ejecutar Windows 10 versión 2004 y posteriores (compilación 19041 y posteriores) o Windows 11.

   Si está ejecutando una compilación anterior o simplemente prefiere no usar el comando install y desea instrucciones paso a paso, consulte [Pasos de instalación manual de WSL para versiones anteriores](https://learn.microsoft.com/es-es/windows/wsl/install-manual).

1. **Lanzamos Powershell con permisos de administrador:**

![Lanzar Powershell con permisos de administrador](https://storage.googleapis.com/curso-eoi/launch-powershell.png)

2. **Comando de instalación de WSL**

    Ahora puede instalar todo lo que necesita para ejecutar el Subsistema de Windows para Linux (WSL) si escribe este comando en PowerShell o el símbolo del sistema de Windows del administrador y, a continuación, reinicia la máquina.

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

## Instalación de Visual Studio Code

> https://learn.microsoft.com/es-es/windows/wsl/tutorials/wsl-vscode#install-vs-code-and-the-remote-wsl-extension

1. Visite la [página VS Code instalación](https://code.visualstudio.com/download) y seleccione el instalador de 32 o 64 bits. Instale Visual Studio Code en Windows (no en el sistema de archivos WSL).

2. Cuando se le pida que seleccione Tareas adicionales durante la instalación, asegúrese de activar la opción Agregar a PATH para que pueda abrir fácilmente una carpeta en WSL mediante el comando de código.

3. Instale el [paquete de extensión desarrollo remoto](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). Este paquete de extensión incluye la extensión Remote - WSL, además de las extensiones Remote - SSH y Remote - Containers, lo que permite abrir cualquier carpeta en un contenedor, en un equipo remoto o en WSL.

## Instalación de Python

> https://learn.microsoft.com/es-es/windows/python/web-frameworks#install-python-pip-and-venv

1. Confirma que Python3 ya está instalado. Para ello, abre el terminal de Ubuntu y escribe python3 --version. Se te debería devolver el número de versión de Python. Si necesitas actualizar la versión de Python, primero actualiza la versión de Ubuntu. 

Para ello, escribe `sudo apt update && sudo apt upgrade` y, luego, actualiza Python con `sudo apt upgrade python3`.

1. Para instalar PIP, escribe `sudo apt install python3-pip`. PIP te permite instalar y administrar paquetes adicionales que no forman parte de la biblioteca estándar de Python.

2. Para instalar venv, escribe `sudo apt install python3-venv`.

3. Comprobamos la instalación creando un proyecto python
    
    1. En la línea de comandos de Ubuntu, navega a la ubicación en la que quieras colocar el proyecto y crea un directorio para este (`mkdir HelloWorld`). A continuación, entra en la carpeta (`cd HelloWorld`)
    
    2. Use el siguiente comando para crear un entorno virtual denominado .venv: 
    ```
    python3 -m venv .venv
    ```

    Si visualizas los ficheros de la carpeta, verás que se ha creado una nueva carpeta con el nombre del virtual env, en este caso `.venv`

    ```bash
    alicia@DESKTOP-7BGOCSQ:~/workspace/HelloWorld$ ll                                                                       total 12                                                                                                                drwxr-xr-x 3 alicia alicia 4096 Sep 18 22:06 ./                                                                         drwxr-xr-x 3 alicia alicia 4096 Sep 18 22:06 ../                                                                        drwxr-xr-x 6 alicia alicia 4096 Sep 18 22:06 .venv/
    ```

    1. Activa el entorno virtual con el siguiente comando:
    
    ```
    source .venv/bin/activate
    ```
    
    Si todo va bien, verás que al principio de la línea de la consola aparece el nombre del virtual env entre paréntesis:

    ```
    alicia@DESKTOP-7BGOCSQ:~/workspace/HelloWorld$ source .venv/bin/activate                                                (.venv) alicia@DESKTOP-7BGOCSQ:~/workspace/HelloWorld$ python            
    ```

    1. Arranca la consola de python escribiendo `python`

    ```bash
    (.venv) alicia@DESKTOP-7BGOCSQ:~/workspace/HelloWorld$ python                                                           Python 3.8.10 (default, Jun 22 2022, 20:18:18)                                                                          [GCC 9.4.0] on linux                                                                                                    Type "help", "copyright", "credits" or "license" for more information.                                                  >>>            
    ```

## Instalación de la extensión de Microsoft Python
> https://learn.microsoft.com/es-es/windows/python/web-frameworks#install-the-microsoft-python-extension

Tendrás que instalar las extensiones de VS Code para tu extensión de Remote-WSL. Las extensiones que ya estén instaladas localmente en VS Code no estarán disponibles automáticamente. Más información.

1. Para abrir la ventana Extensiones de VS Code, escribe Control + Mayús + X (o usa el menú para desplazarte a Ver>Extensiones).
2. En el cuadro Search Extensions in Marketplace (Buscar extensiones en Marketplace) de la parte superior, escriba: Python.
3. Busca la extensión Python (ms-python.python) de Microsoft y selecciona el botón Instalar de color verde.
4. Una vez finalizada la instalación de la extensión, deberás seleccionar el botón Reload required (Recarga necesaria) de color azul. Se volverá a cargar VS Code y se mostrara la sección WSL: UBUNTU-18.04 - Installed (WSL: UBUNTU-18.04 [instalado]) en la ventana VS Code Extensions (Extensiones de VS Code), que mostrará que ha instalado la extensión de Python.
