---
title: Introducción a Git
---

## Historia

Linux Torvlads  -> Linux Kernel

- Inicialmente Parches
- 2002 Empieza a usar Bitkeeper
- 2005 Fricciones con Bitkeeper
- A raiz de estos problemas, decide empezar un propio SCVD, que acabaría siendo
  Git (Casualmente, estos problemas fueron también la causa de la
  creación de otro SCVD, [Mercurial](https://www.mercurial-scm.org/))

## Carácterísticas que debería tener el nuevo sistema

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


## Qué significa Git

Según a quien le preguntes. Según Linus Torvalds, Git -> Capullo. Según el,
siempre le pone nombre a sus proyectos basados en su persona, Linux y Git.  Si
queremos ser más formales: _Global Information Tracker_.


## Instalación de Git

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



## Configuración de Git

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



## Principales conceptos de Git

El principal concepto para entender como funciona internamente Git es el de
**snapshot** o instantánea, y es interesante verlo porque es una característica
propia de Git que lo diferencia de casi todos los demás SCVD.

La mayoría de los otros sistemas (CVS, Subversion, Perforce, Bazaar, por
ejemplo) almacenan la información relativa a un fichero como **una lista de cambios
o parches a aplicar sucesivamente**, de forma que para obtener el fichero en su
estado actual, partimos del fichero inicial y vamos aplicando sucesivamente los
parches hasta obtener el resultado actual. Este modelo se conoce habitualmente
como control de versiones basado en diferencias o _delta-based_.

![Delta-Based version control](delta-based.svg)

Git, sin embargo, usa otro sistema. Github almacena sus datos como una secuencia
de **snapshots** o instantaneas de un sistema de ficheros en miniatura. Cuando
añadimos información a Git, normalmente salvando el estado del proyecto, se toma
una foto o instantanea del sistema de ficheros en ese momento y se almacena una
referencia al mismo. Para no desperdiciar espacio, si un fichero no ha sufrdo
cambios Git no lo almacena de nuevo, solo guarda un enlace al fichero anterior
que haya sido guardado. Git por tanto guarda sus datos como una secuencia de
_snapshots_ o instantaneas.


![Snapshot-Based version control](snapshot-based.svg)

Este cambio radical en el enfoque es lo que especial a Git, porque esta
arquitectura le permite ofrecer muchas ventajas:

En primer lugar, casi todas las operaciones son locales. Generalmente no se
necesita información de otros ordenadores o acceso a red. Al ser locales, las
operaciones son muy, muy rápidas, especialmente comparados con sistemas
centralizados como CVS o Subversión.

Esto también se traduce en que podemos hacer casi cualquier cosa aunque estemos
trabajando en uin avión o en un tren, por ejemplo.

### Crear / Obtener un repositorio Git

[ ] Ejercicio

- Crear un repo local (`init`)
- Clonar un repo (Curso EOI)


### Registrar cambios en el repositorio

Git usa on código de _checksum_ para todas sus operaciones. Esto le permite
ofrecer un cierto grado de integridad delos ficheros, y también la permite saber
el estado de un fichero, especialmente si el fichero está _sincronizado_, es
decir, si la version local que tenemos se corresponde con la que está almacenada
en el repositorio.

El mecanismo de verificación que usa Git es el conocico como
[SHA-1](https://es.wikipedia.org/wiki/Secure_Hash_Algorithm#SHA-1). No nos
interesan demasiado los detalles a este nivel, pero si saber que este codigo,
son 40 caracteres hexadecimales (Las letras desde el 0 al 9, y las letras
`A` hasta la `F`, en total 16 símbolos) y que,
como todos los códigos _Hash_, cambia si el contenido del fichero es modificado.

En linux podemos usar el comando `sha1sum` para generar o  verificar en código
de verificación o _checksum_. Por ejemplo, si tengo un fichero con el contenido
"hola, mundo":

```
echo "hola, mundo" > ejemplo-para-hash.txt
```

Puedo usar `sha1sum` para mostrar su _checksum_:

```
$ sha1sum  ejemplo-para-hash.txt
2349981c5586135aecb28e3c6d8784208eef7b09  ejemplo-para-hash.txt
```

Lo importante aquí no son los detalles matemáticos del funcionamiento de
`SHA-1` (Aunque son muy interesantes), sino darse cuenta de dos cosas muy
importantes:

1) Si han seguido el ejemplo anterior, usando exactamente el mismo contenido del
fichero (El famoso "hola, mundo"), el código SHA-1 que genere debe ser el mismo
para todos ustedes. Es decir, que para el mismo contenido, SHA-1 siempre genera
el mismo código.

2) Cualquier modificación del contenido, aunque sea mínima, produce un código
SHA-1 sustancialmente diferente, como podemos comprobar en el siguiente ejemplo:

```
$ echo "hola, mundo" > ejemplo-para-hash.txt
$ sha1sum  ejemplo-para-hash.txt
2349981c5586135aecb28e3c6d8784208eef7b09  ejemplo-para-hash.txt
$ echo "Hola, mundo" > ejemplo-para-hash.txt
b259c960361493db459181358676e16d79cf1558  ejemplo-para-hash.txt
```

Así se consigue tanto una mayor seguridad en el almacenamiento de los datos,
como un sistema para determinar el estado de un fichero.


### Primeros pasos con Git

En primer lugar, hay que decir que Git solo atiende o se ocupa de los ficheros
que nosotros le indicamos. Por tanto, cuando creamos nuestro repositorio un par
de pasos antes, con el comando `git init`, podemos ver que el repositorio está
vació; no le hemos dicho a Git de que ficheros debe ocuparse. Los ficheros de
los que Git no sepa, para el prácticamente no existen. No se va a ocupar de
ellos.

Para añadir un fichero a git, usamos el subcomando `add`.

[ ] Ejercicio
- Ejecutar `git status`
- Crear y añadir un fichero. (`add`)

Creemos un fichero con un editor de texto cualquiera, por ejempo `README.md`

```
$ vim README.md
```

si usamos el comando `git status`, una vez creado el fichero, veremos que Git
reconoce su existencia, pero como un fichero externo, _sin seguimiento_:

```
$ git status
En la rama main
Archivos sin seguimiento:
  (usa "git add <archivo>..." para incluirlo a lo que se será confirmado)
	README.md

no hay nada agregado al commit pero hay archivos sin seguimiento presentes (usa "git add" para hacerles seguimiento)
```

Lo bueno es que el propio mensaje de Git nos indica como tenemos que hacer para
añadir el fichero al repo, es decir, para decirle a Git: "Este fichero importa,
y quiero que a partir de ahora este bajo tu control". Es la orden `git add`:

```
$ git add README.md
```

Vemos que esta orden se ejecuta y que no nos dice nada; esto es porque esta
herramienta sigue la filosofía de Linux de mantener un respetuoso silencio en
las operaciones realizadas con éxito, y solo emitir mensajes de error en casos
de fallo.

El silencio en este caso es, por lo tanto, una buena se¶ál. Git ya sabe que
`README.md` es un fichero interesante.

Pero antes de seguir, tenemos que ver un apartado sobre los estados en los que
puede estar un fichero para Git. Hemos visto que no se lo decimos
explícitamente, Git ni se preocupa de lo que le pase aun fichero que no esté
bajo su control, pero desde el momento en que hacemos el `add`, ya la cosa
cambia, y el fichero -desde el punto de vista de git- estará en uno de los
**tres estados** posibles.

### Estados de un fichero

Esta parte es importante, porque también es especifica de Git. La mayoría de los
sistemas de control de versiones solo tienen 2 estados para los ficheros, pero
Git usa tres. No hay ninguna razón especial para ello, simplemente a los
creadores de Git les pareció mejor este sistema.

Para Git, un fichero del repositorio puede estar en alguno de estos tres
estados:

- _Modified_ o Modificado

- _Commited_ o Confirmado

- _Staged_ o preparado

Veamos antes los dos primeros, que son más sencillos, y dejemos para más
adelante el tercer estado `staged`.

- Un fichero está modificado o _Modified_ si hay cambios entre la versión del
  fichero que tenemos en nuestro sistema de archivos y lo que hay en el
  repositorio. Es decir, si hemos editado y modificado el fichero, los cambios
  hechos están en nuestro sistema de ficheros, pero en el repo sigue estando la
  versión anterior.

- Un fichero esta confirmado o _Commited_ si no existen cambios entre la versión
  en el sistema de ficheros y la última versión del mismo fichero en el
  repositorio.  Este es el estado ideal, donde toda la información está
  perfectamente almacenada en el repositior. La mayoría de nuestros ficheros
  estarán en ese estado, ya que solo tendremos un pequeño conjunto de ficheros
  modificados, normalmente.

- Un fichero `Staged` es un fichero que está modificado, pero que nosotros hemos
  puesto en un area, llamada _Stage_, que sirve solo para indicar que estos
  ficheros están listos para ser confirmados. Es como un paso obligado para
  pasar de modificado a confirmado. Esto sirve, por ejemplo, para casos en que
  hayamos modificado varios ficheros, pero solo queramos confirmar unos pocos;
  lo hariamos pasando estos pocos al area _stage_, y de hay los confirmariamos.

Parece mucho más complicado de lo que es en realidad, así que la mejor forma de
entenderlo es con un ejemplo:

En el ejercicio anterior le indicamos a Git que el fichero `README.md` debe estar
contemplado en el sistema. Podemos ver con un nuevo `git status` que el fichero
ya es "interesante" para Git:

```
$ git status
En la rama main
Cambios a ser confirmados:
  (usa "git restore --staged <archivo>..." para sacar del área de stage)
	nuevos archivos: README.md
```

Pero cuidado, el fichero aun no está almacenado en el repositorio. Esta en lo
que Git llama estado "staged", que vendría a ser como "preparado para
confirmar". La confirmación en si se realiza con el comando `git commit`. Si la
ejecutamos sin más, veremos que abrirá (o intentará abrir) un editor para que
introduzcamos un breve mensaje de texto, normalmente un resumen de los cambios
realizados en el fichero. Si no queremos que nos abra el editor, podemos usar el
flag `-m` para indicar este mensaje. El mensaje es obigatorio, y es una buena
idea poner un mensaje corto pero claro de los cambios, porque nos ayudará mucho
cuando revisemos el historial de los ficheros.

[ ] Ejercicio: Confirmar el fichero (`commit`)

Como el cambio que hemos hecho es, directamente, crear un fichero nuevo, hagamos
un `commit` con el mensaje "Carga inicial de código":

```
git commit -m "Carga inicial de código"
```

En este caso, el `commit` no guarda silencio, aun habiendo realizado la
operación con éxito. Deberiamos trener algo parecido a esto en la consola:

```
$ git commit -m "Carga inicial de código"
[main 0b8d083] Carga inicial de código
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
```

Podemos ver que nos informa de en que rama estamos realizando el `commit` (`main`),
parte del código _hash_ SHA-1 que identifica el commit (`0b8d083`), el mensaje que
le hemos pasado y un resumen de lo que ha hecho: Un fichero cambiado, ninguna
línea nueva, ninguna línea borrada, etc.




- Modificar el fichero.
- Ver que Git se ha dado cuenta de que el fichero ha cambiado (`status`)
- Volver a añadirlo. (`add`)


## Ignorar archivos

Podemos decirle a git que determinados archivos o tipos de archivos deben
permanecer fuera del control de versiones, con lo cual git los va a ignorar
como si no existieran.

Esto es muy normal, por ejemplo, para que git no se ocupe de ficheros
compilados, temporales, ejecutables, etc. En el caso de Python, el compilador
genera una serie de directorios y ficheros, como por ejemplo los que usan
la extensión `.pyc` (Python compilado). Estos ficheros se generan
automáticamente a partir del fichero `.py` correxpondiente, por lo que **nunca
deben almacenarse en el repositorio** (como cualquier otro producto derivado,
por lo general).

La forma de excluir los ficheros `*.pyc`, por ejemplo, es sencillamente 
con un fichero que se llama `.gitignore` (El punto al principio del nombre
lo hace invisible, en los sistemas Unix/Linux, para el comando `ls`, así que
tendremos que llamar a `ls` con el _flag_ `-a` o `--all`. En ese fichero, cada
línea describe un patrón de ficheros que git ignorará:

En nuestro caso, para que ignore los ficheros con la extension `.pyc`, el
contenido del archivo `.gitignore` podría ser:

```
# Ignorar los ficheros compilados de python
*.pyc
```

Es recomendable que el fichero `.gitignore` este incluido en el propio
repositorio.

El formato del fichero es muy sencillo:

- Una línea en blanco no tiene efecto, sirve solo para aumentar la legibilidad.

- Podemos usar comentario empezándolos con el carácter `#`

- El prefijo `!` niega el significado de un patrón. Esto nos permite, por
  ejemplo, excluir todos los ficheros de tipo `.pdf`, (Con `*.pdf`) excepto el
  que se llama `handbook.pdf` (Con `!handbook.pdf`).

- El carácter especial `*` sirve para reemplazar a uno o más caracteres
  cualesquiera.

- El caráter especial `?` sirva para reemplazar un carácter cualquiera.

- Se pueden usar expresiones regulares, como por ejemplo `[0-9]`, que
  representa un digito cualquiera entre el `0` y el `9`. Veremos más sobre
  expresiones regulares en temas posteriores.

[ ] Ejercicio: Crear un fichero `.gitignore` y decirle que ignore los archivos
de tipo `.pyc`. Añadir otra línea para excluir los ficheros `.txt`. Crear un
fichero con esta extensión para verificar que git no le hace ni caso. Borrar la
linea de los `.txt` y vrificar que ahora si que los considera como posibles
partes del proyecto.

### Revisar los cambios realizados

[ ] Ejercicio

- Ver el historico de cambios (`status`, `log`)

### Etiquetas

### Alias


