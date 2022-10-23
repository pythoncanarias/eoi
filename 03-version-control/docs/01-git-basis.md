---
title: Introducción a Git
---
### Historia

Linux Torvlads  -> Linux Kernel

- Inicialmente Parches
- 2002 Empieza a usar Bitkeeper
- 2005 Fricciones con Bitkeeper
- A raiz de estos problemas, decide empezar un propio SCVD, que acabaría siendo
  Git (Casualmente, estos mismos problemas también fueron la causa de la
  creación de otro SCVD, mercurial

Carácterísticas que debería tener el nuevo sistema

- Rápido (En algunos sistemas, aplicar un parche podía llevar hasta 30
  segundos)

- Diseño sencillo

- Debe permitir el desarrollo de múltiples ramas en paralelo, incluso hasta
  miles de ramas

- Totalmente distribuido

- Seguro frente a problemas de corrupción, ya sea accidental o maliciosa

Ninguno de los sistemas que existían en ese momento cumplía todas las
expectativas, y así se decidió crear uno nuevo.

Frase famosa: Mirar a _Concurrent Versions System_ (CVS) como ejemplo a **no**
seguir. En caso de duda, estudiar la decisión tomada por CVS y hacer exactamente
lo contrario.

La primera Versión alfa, con funcionalidad mínima, se hizo en unos 10 días. El
desarrollo empezó el 3 de abril de 2005; a partir del 16 de junio Git ya podía
mantener el código fuente del Linux Kernel 2.6.12.  La versión 1.0 fue liberada
el 21 de diciembre de 2005.

Evolución del tamaño en líneas de código del núcleo Linux:

| Año      | Version Linux | Líneas de código     |
|----------|--------------:|---------------------:|
| 1999     | 2.2.0         | 1.800.847            |
| 2003     | 2.6.0         | 5.929.913            |
| 2010     | 2.6.36        | 13.499.457           |
| 2022     | 5.10          | 23.359.556           |


### Qué significa Git

Según a quien le preguntes.

Según Linus Torvalds, Git -> Capullo. Según el, siempre le pone nombre a sus proyectos
basados en su persona, Linux y Git.


Si queremos ser más formales: _Global Information Tracker_


### Instalación de Git

Lo primero es descubrir si lo tenemos instalado ya o no:

[ ] Ejercicio: Abrir una terminal, y ejecutar:

```
git --version
```

Mandad por el canal de Discord `#control-versiones` la versión que os sale,
debería ser similar a esto:

```
git version 2.34.1
```

En caso de que no lo tengáis instalado, hay que instalarlo `¯\_(ツ)_/¯`


Si la máquina en Linux o Mac, lo más probable es que ya lo tengan. En caso contrario:

Para Debian/Ubuntu/Mint Linux:

```
sudo apt install git-all
```

Para Fedora/RHEL/CentOS:

```
sudo dnf install git-all
```

Para Mac:

Muy posiblemente, si el `git --version` ha dado error, el mismo Sistema
Operativo te da la opción de instalarlo. Si no, se puede descargar un
instalador en la dirección
[https://git-scm.com/download/mac](https://git-scm.com/download/mac)

Si tenéis instalado [homebrew](https://brew.sh/):

```
brew install git
```

Si tenéis instalado [MacPorts](https://www.macports.org/)

```
sudo port install git
```


- Si estáis en Windows, pero habéis instalado el WSL (_Windows Subsystem for
  Linux_), seguramente esté instalado, y si no lo instaláis con

```
apt install git
```

Si queréis instalarlo en Windows directamente, lo mejor es instalar antes
[chocolatey](https://chocolatey.org/) y luego, en una terminal con privilegios
de administración:

```
choco install git
```



[ ] Ejercicio: 

- Instalar Git



### Configuración de Git

El comando `git config` nos permite configurar la forma de funcionamiento de
Git. El primer paso que hay que dar es identificarse con Git, ya que este
registra esta información en casi todas las operaciones que hagamos. Para
identificarnos, Git nos pide un nombre y un email. 

Cuando usamos `git config`, tenemos tres posibilidades:

- `git config --system`: Configuración a nivel de sistema. Todos los
   usuarios y todos sus repositorios heredan estos valor, a no ser que se
   redefinan a nivel global o de proyecto.

- `git config --global`: Configuración a nivel de usuario. Todos los
  repositorios del usuario usarán este valor, a no ser que se redefinan a nivel
  de proyecto.

- `git config --local` o `git config`, ya que `--local` es la opción por
  defecto; definen valores a nivel de repositorio

Para identificarnos, ejecutaremos los siguientes comandos:

```
git config --global user.name "<Nuestro nombre>"
git config --global user.email "<nuestra dirección de correo>"
```

[ ] Ejercicio:

- Identificar ante git (Configurar nombre y email) (config)
- Usar `git config user.name` y `git config user.email` para verificar que
  nuestros datos están correctos



### Principales conceptos de Git

El principal concepto para entender como funciona internamente Git es el de
**snapshot** o instantánea. 


### Crear / Obtener un repositorio Git

[ ] Ejercicio

- Crear un repo local (`init`)
- Clonar un repo (Curso EOI)


### Registrar cambios en el repositorio



[ ] Ejercicio
- Añadir un fichero. (`add`)
- Modificar el fichero.
- Ver que Git se ha dado cuenta de que el fichero ha cambiado (`status`)
- Volver a añadirlo. (`add`)

### Revisar los cambios realizados

[ ] Ejercicio

- Ver el historico de cambios (`status`, `log`)

### Etiquetas

### Alias


