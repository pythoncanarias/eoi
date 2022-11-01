- [Comandos básicos de Linux](#comandos-básicos-de-linux)
  - [Cómo ubicarnos](#cómo-ubicarnos)
  - [Crear archivos usando la redirección](#crear-archivos-usando-la-redirección)
  - [Moviendo y manipulando ficheros](#moviendo-y-manipulando-ficheros)
  - [Eliminar archivos y carpetas](#eliminar-archivos-y-carpetas)
  - [Uso de tuberías (pipes)](#uso-de-tuberías-pipes)
  - [Ficheros ocultos](#ficheros-ocultos)
  - [Superusuarios :superhero:](#superusuarios-superhero)
    - [Instalación de software nuevo](#instalación-de-software-nuevo)
  - [Limpieza final](#limpieza-final)


# Comandos básicos de Linux

Basados en el tutorial oficial de Ubuntu
> https://ubuntu.com/tutorials/command-line-for-beginners

## Cómo ubicarnos

- `pwd`: ‘print working directory’ - muestra el directorio actual
- `cd`: ‘change directory’ - cambia el cursor a otro directorio. 

1. Con el siguiente comando irás al directorio raíz. El directorio "/", es la base de ese sistema de archivos unificado. A partir de ahí, todo lo demás se ramifica para formar un árbol de directorios y subdirectorios.
    ```bash
    cd /
    pwd
    ```

2. Desde el directorio raíz, el siguiente comando lo llevará al directorio "home" (que es un subdirectorio inmediato de "/"):
    ```bash
    cd home
    pwd
    ```

3. Para subir al directorio principal, en este caso volver a “/”, puedes usar los dos puntos (..) para cambiar de directorio:
    ```bash
    cd ..
    pwd
    ```
4. Escribir `cd` por sí solo es un atajo rápido para volver a su directorio de `home`:
    ```bash
    cd
    pwd
    ```
5. También puedes usar `..` más de una vez si tiene que subir a través de varios niveles de directorios principales:
    ```bash
    cd ../..
    pwd
    ```
6. Si quisiéramos ir directamente desde nuestro directorio de inicio al directorio "etc" (que está directamente dentro de la raíz del sistema de archivos), podríamos usar este enfoque:
    ```bash
    cd
    pwd

    cd ../../etc
    pwd
    ```
7. En el siguiente comando, reemplaza USERNAME con tu propio nombre de usuario; el comando whoami te recordará tu nombre de usuario:

   ```bash
    whoami
    cd /home/USERNAME/Desktop
    pwd
    ```
8. Usar el carácter de tilde (`~`) al comienzo de su ruta significa de manera similar "comenzar desde mi directorio de home".
   ```bash
    cd ~
    pwd

    cd ~/Desktop
    pwd
    ```


## Creando ficheros y directorios


En esta sección vamos a crear algunos archivos reales para trabajar. Para evitar pisotear accidentalmente cualquiera de nuestros archivos reales, vamos a comenzar creando un nuevo directorio, lejos de nuestra carpeta de inicio, que servirá como un entorno más seguro para experimentar:
```bash
mkdir /tmp/tutorial
cd /tmp/tutorial
```

En caso de que no lo hayas adivinado, mkdir es la abreviatura de "hacer directorio". Ahora que estamos seguros dentro de nuestra área de prueba (verifique dos veces con pwd si no está seguro), creemos algunos subdirectorios:
```bash
mkdir dir1 dir2 dir3
```

El comando anterior habrá creado tres nuevos subdirectorios dentro de nuestra carpeta. Echemos un vistazo a ellos con el comando ls (lista):
```bash
ls
```

Si ha seguido los últimos comandos, su terminal debería verse así:
```bash
alicia@cocombra2:/tmp/tutorial$ ls
dir1  dir2  dir3
```

En este caso `mkdir` creó todas las carpetas en un directorio. No creó dir3 dentro de dir2 dentro de dir1, ni ninguna otra estructura anidada. Pero a veces es útil poder hacer exactamente eso, y mkdir tiene una manera:
```bash
alicia@cocombra2:/tmp/tutorial$ mkdir -p dir4/dir5/dir6
alicia@cocombra2:/tmp/tutorial$ ls
dir1  dir2  dir3  dir4
alicia@cocombra2:/tmp/tutorial$ ls dir4/
dir5
alicia@cocombra2:/tmp/tutorial$ ls dir4/dir5/
dir6
```

## Crear archivos usando la redirección

Nuestra carpeta de demostración comienza a verse bastante llena de directorios, pero le faltan algunos archivos. Solucionemos eso redirigiendo la salida de un comando para que, en lugar de imprimirse en la pantalla, termine en un archivo nuevo. Primero, recuerde lo que muestra actualmente el comando ls:
```bash
ls
```

Supongamos que quisiéramos capturar la salida de ese comando como un archivo de texto que podemos mirar o manipular más. Todo lo que tenemos que hacer es agregar el carácter mayor que (”>”) al final de nuestra línea de comando, seguido del nombre del archivo para escribir:
```bash
ls > output.txt
```

Esta vez no hay nada impreso en la pantalla, porque la salida se redirige a nuestro archivo. Si solo ejecuta ls solo, debería ver que se ha creado el archivo output.txt. Podemos usar el comando `cat` para ver su contenido:
```bash
alicia@cocombra2:/tmp/tutorial$ cat output.txt
dir1
dir2
dir3
dir4
output.txt
```

No es exactamente lo que se mostraba en la pantalla anteriormente, pero contiene todos los mismos datos y está en un formato más útil para su posterior procesamiento. Veamos otro comando, `echo`:
```bash
alicia@cocombra2:/tmp/tutorial$ echo "Esto es una prueba"
Esto es una prueba
```

Pero combínelo con una redirección y tendrá una manera de crear fácilmente pequeños archivos de prueba:
```bash
alicia@cocombra2:/tmp/tutorial$     echo "Esto es una prueba" > test_1.txt
alicia@cocombra2:/tmp/tutorial$     echo "Esta es una segunda prueba" > test_2.txt
alicia@cocombra2:/tmp/tutorial$     echo "Esta es una tercera prueba" > test_3.txt
alicia@cocombra2:/tmp/tutorial$     ls
dir1  dir2  dir3  dir4  output.txt  test_1.txt  test_2.txt  test_3.txt
```

Pero `cat` es más que un visor de archivos: su nombre proviene de "concatenar", que significa "enlazar". Si pasas más de un nombre de archivo a `cat`, generará cada uno de ellos, uno tras otro, como un solo bloque de texto:
```bash
alicia@cocombra2:/tmp/tutorial$ cat  test_1.txt test_2.txt test_3.txt 
Esto es una prueba
Esta es una segunda prueba
Esta es una tercera prueba
```

Cuando deseas pasar varios nombres de archivo a un solo comando, existen algunos atajos útiles que pueden ahorrarle mucho tipeo si los archivos tienen nombres similares. 

Se puede utilizar un signo de interrogación ("?") para indicar "cualquier carácter único" dentro del nombre del archivo. Se puede utilizar un asterisco ("*") para indicar "cero o más caracteres". Estos a veces se denominan caracteres "comodines". Un par de ejemplos pueden ayudar, los siguientes comandos hacen lo mismo:
```bash
cat test_1.txt test_2.txt test_3.txt
cat test_?.txt
cat test_*
```

Usemos esta funcionalidad también para unir todos nuestros archivos en un solo archivo nuevo, y luego verlo:
```bash
alicia@cocombra2:/tmp/tutorial$ cat t* > combined.txt
alicia@cocombra2:/tmp/tutorial$ cat combined.txt
Esto es una prueba
Esta es una segunda prueba
Esta es una tercera prueba
```

Si ejecutamos estos comandos otra vez, veremos que no obtenemos ningún error, sino que se reemplaza el contenido. Si deseamos agregar, en lugar de reemplazar el contenido de los archivos, duplicaremos el carácter "mayor que":
```bash
cat t* >> combined.txt
echo "¡He agregado una línea!" >> combined.txt
cat combined.txt
```

Ejecuta estas líneas hasta que el fichero sea demasiado grande como para caber en la pantalla. Con `cat` resulta muy incómodo de visualizar. Prueba con `less` en su lugar.
```bash
less combined.txt
```

## Moviendo y manipulando ficheros

En la práctica, lo más probable es que siga utilizando un programa gráfico cuando queramos mover, renombrar o eliminar uno o dos archivos, pero saber cómo hacerlo mediante la línea de comandos puede ser útil para cambios masivos o cuando los archivos se distribuyen entre diferentes carpetas. Además, aprenderemos algunas cosas más sobre la línea de comandos en el camino.

Comencemos colocando nuestro archivo combine.txt en nuestro directorio dir1, usando el comando `mv` (mover):
```bash
mv combined.txt dir1
```

Podemos pasar una ruta directamente al comando `ls` para llegar confirmar que el trabajo se ha realizado:

```bash
alicia@cocombra2:/tmp/tutorial$ ls dir1
combined.txt
```

Ahora suponga que resulta que el archivo no debería estar en dir1 después de todo. Volvamos a moverlo al directorio de trabajo. 

```bash
mv dir1/* .
```

El comando `mv` también nos permite mover más de un archivo a la vez. Si pasas más de dos argumentos, el último se toma como el directorio de destino y los demás se consideran archivos (o directorios) para mover. Usemos un solo comando para mover `combined.txt`, todos nuestros archivos test_n.txt y dir3 a `dir2`.

```bash
mv combined.txt test_* dir3 dir2
ls
ls dir2
```

Con `combined.txt` ahora movido a `dir2`, ¿qué sucede si decidimos que está en el lugar equivocado nuevamente? En lugar de `dir2` se debería haber puesto en `dir6`, que es el que está dentro de `dir5`, que está en `dir4`. Con lo que ahora sabemos sobre las rutas, tampoco hay problema:

```bash
mv dir2/combined.txt dir4/dir5/dir6
ls dir2
ls dir4/dir5/dir6
```

Como parece que estamos usando (y moviendo) mucho ese archivo, tal vez deberíamos guardar una copia en nuestro directorio de trabajo. Así como el comando `mv` mueve archivos, el comando `cp` los copia (nuevamente, tenga en cuenta el espacio antes del punto):

```bash
cp dir4/dir5/dir6/combined.txt .
ls dir4/dir5/dir6
ls
```

Ahora vamos a crear otra copia del archivo, en nuestro directorio de trabajo pero con un nombre diferente. Podemos usar el comando `cp` nuevamente, pero en lugar de darle una ruta de directorio como último argumento, le daremos un nuevo nombre de archivo:

```bash
cp combined.txt backup_combined.txt
ls
```

Quizás la elección del nombre de la copia de seguridad podría ser mejor. ¿Por qué no cambiarle el nombre para que siempre aparezca junto al archivo original en una lista ordenada? Vamos a renombrarlo a `combined_backup.txt`

```bash
mv backup_combined.txt combined_backup.txt
ls
```

## Eliminar archivos y carpetas

> IMPORTANTE: \
>  En esta sección comenzaremos a eliminar archivos y carpetas. Para estar absolutamente seguro de que no eliminas accidentalmente nada en tu carpeta de inicio, use el comando `pwd` para verificar que todavía se encuentra en el directorio `/tmp/tutorial` antes de continuar.

Dado que estos son solo archivos de prueba, tal vez no necesitemos tres copias diferentes de combined.txt después de todo. Ordenemos un poco, usando el comando `rm` (eliminar):

```bash
rm dir4/dir5/dir6/combined.txt combined_backup.txt
```

Quizás también deberíamos eliminar algunas de las carpetas de prueba. Empecemos por `dir4`:

```bash
alicia@cocombra2:/tmp/tutorial$ rm dir4
rm: cannot remove 'dir4': Is a directory
```

Resulta que `rm` tiene una pequeña red de seguridad. Afortunadamente, hay un comando `rmdir` (eliminar directorio) que hará el trabajo por nosotros:

```bash
alicia@cocombra2:/tmp/tutorial$ rmdir dir4
rmdir: failed to remove 'dir4': Directory not empty
```

Nuevamente, es una pequeña red de seguridad para evitar que borremos accidentalmente una carpeta llena de archivos cuando no fue su intención.
Cuando estamos muy, muy, muy seguros de que deseamos eliminar un directorio completo y cualquier cosa dentro de él, es decirle a `rm` que trabaje recursivamente usando el modificador -r, en cuyo caso eliminará las carpetas como así como archivos. 

```bash
rm -r folder_6
ls
```

## Uso de tuberías (pipes)

Cuántas líneas hay en su archivo `combined.txt`? El comando wc (conteo de palabras) puede decirnos que, usando el interruptor -l para decirle que solo queremos el conteo de líneas (también puede hacer conteos de caracteres y, como sugiere el nombre, conteos de palabras):

```bash
alicia@cocombra2:/tmp/tutorial$ wc -l combined.txt
23 combined.txt
```

Del mismo modo, si quisieras saber cuántos archivos y carpetas hay en su directorio `home` sin crear archivos basura, podríamos hacer:

```bash
ls ~ > file_list.txt
wc -l file_list.txt
rm file_list.txt
```

Ese método funciona, pero crear un archivo temporal para contener la salida de ls solo para eliminarlo dos líneas después parece un poco excesivo. 

Afortunadamente, la línea de comandos de Unix proporciona un atajo que evita tener que crear un archivo temporal, tomando la salida de un comando (referido como salida estándar o `STDOUT`) e introduciéndola directamente como entrada a otro comando (entrada estándar o `STDIN`).

Es como si hubiera conectado una `tubería` entre la salida de un comando y la entrada del siguiente, tanto que este proceso en realidad se conoce como canalización de datos de un comando a otro. Así es como canalizar la salida de nuestro comando `ls` en `wc`:

```bash
alicia@cocombra2:/tmp/tutorial$ ls ~ | wc -l
14
```

Esta vez vamos a consultar cuántos elementos hay en el directorio `/etc`:

```bash
alicia@cocombra2:/tmp/tutorial$ ls /etc | wc -l
252
```

Son bastantes archivos. Si quisiéramos mostrar los nombres de todos con `ls`, claramente llenaría más de una pantalla. Como descubrimos anteriormente, cuando un comando produce una gran cantidad de resultados, es mejor usar `less` para verlos, y ese consejo aún se aplica cuando se usa una tubería (recuerda presionar `q` para salir):
```bash
ls /etc | less
```

Volviendo a nuestros propios archivos, sabemos cómo obtener la cantidad de líneas en `combined.txt`, pero dado que se creó concatenando los mismos archivos varias veces, ahora queremos saber cuántas líneas únicas hay. Unix tiene un comando, `uniq`, que solo generará líneas únicas en el archivo. Por lo tanto, debemos extraer el archivo y canalizarlo a través de `uniq`. Pero todo lo que queremos es un conteo de líneas, así que también necesitamos usar `wc`. Afortunadamente, la línea de comandos no lo limita a una sola tubería a la vez, por lo que podemos continuar encadenando tantos comandos como necesitemos:

```bash
cat combined.txt | uniq | less
```

Parece ninguna de nuestras líneas duplicadas se han eliminado. 

Para entender por qué, debemos consultar la documentación del comando `uniq`. La mayoría de las herramientas de línea de comandos vienen con un manual de instrucciones breve (ya veces no tan breve), al que se accede a través del comando `man` (manual). 

```bash
man uniq
```

![](https://ubuntucommunity.s3.dualstack.us-east-2.amazonaws.com/optimized/2X/6/60d1b71b8e3736d7f49b0550ad39c53253de7d17_2_690x412.png)

La primera línea de la sección DESCRIPCIÓN para man uniq responde a la pregunta de por qué no se han eliminado las líneas duplicadas: *solo funciona en líneas coincidentes adyacentes*.

La pregunta, entonces, es cómo reorganizar las líneas en nuestro archivo para que las entradas duplicadas estén en líneas adyacentes. Si tuviéramos que ordenar el contenido del archivo alfabéticamente, eso sería suficiente. Unix ofrece un comando `sort` para hacer exactamente eso. Una revisión rápida de `man sort` muestra que podemos pasar un nombre de archivo directamente al comando, así que veamos qué le hace a nuestro archivo:

```bash
sort combined.txt | less
```

Deberías poder ver que las líneas se han reordenado y ahora es cuando podemos canalizar directamente en `uniq`. Finalmente podemos completar nuestra tarea de contar las líneas únicas en el archivo:

```bash
alicia@cocombra2:/tmp/tutorial$ sort combined.txt | uniq | wc -l
4
```

## Ficheros ocultos

Se usan comúnmente en los sistemas Linux para almacenar configuraciones y datos de configuración, y generalmente se ocultan para que no abarroten la vista de sus propios archivos.

No hay nada especial en un archivo o carpeta oculto, aparte de su nombre: simplemente comenzar un nombre con un punto (”.”) es suficiente para que desaparezca.

```bash
cd /tmp/tutorial
ls
mv combined.txt .combined.txt
ls
```

Puedes trabajar igualmente con los archivos ocultos asegurándote de incluir el punto cuando especificas su nombres de archivo:

```bash
cat .combined.txt
mkdir .hidden
mv .combined.txt .hidden
less .hidden/.combined.txt
```

Si ejecuta `ls`, verá que el directorio `.hidden` está, como era de esperar, oculto. Todavía puede enumerar su contenido usando `ls .hidden`, pero como solo contiene un único archivo que, en sí mismo, está oculto, no obtendrá mucho resultado. Pero puede usar la opción `-a` (mostrar todo) en `ls` para que muestre todo en un directorio, incluidos los archivos y carpetas ocultos:

```bash
ls
ls -a
ls .hidden
ls -a .hidden
```

## Superusuarios :superhero:

El superusuario es, como su nombre indica, un usuario con superpoderes. En los sistemas más antiguos, era un usuario real, con un nombre de usuario real (casi siempre `root`) que podía iniciar sesión como si tuviera la contraseña. En cuanto a esos superpoderes: `root` puede modificar o eliminar cualquier archivo en cualquier directorio del sistema, independientemente de quién sea el propietario; `root` puede reescribir las reglas del firewall o iniciar servicios de red que potencialmente podrían exponer la máquina a un ataque; `root` puede apagar la máquina incluso si otras personas todavía la están usando. En resumen, `root` puede hacer casi cualquier cosa, saltándose fácilmente las medidas de seguridad que generalmente se implementan para evitar que los usuarios se excedan en sus límites.

Por supuesto, una persona que inició sesión como `root` es tan capaz de cometer errores como cualquier otra persona, luego existe la posibilidad de un ataque malicioso si, por ejemplo, un usuario inicia sesión como `root` y abandona su escritorio y un colega descontento tiene acceso a su máquina.

En un esfuerzo por reducir estos problemas, muchas distribuciones de Linux comenzaron a fomentar el uso del comando `su`. Esto se describe de diversas formas como la abreviatura de `superuser` o `switch user`, y permite cambiar a otro usuario en la máquina sin tener que cerrar sesión y volver a iniciar sesión. Cuando se usa sin argumentos, asume que desea cambiar al usuario `root` (de ahí la primera interpretación del nombre), pero puedes pasarle un nombre de usuario para cambiar a una cuenta de usuario específica (la segunda interpretación). 

Al alentar el uso de `su`, el objetivo era persuadir a los administradores para que pasaran la mayor parte de su tiempo usando una cuenta normal, solo cambiaran a la cuenta de superusuario cuando lo necesitaran y luego usaran el comando de cierre de sesión (o el atajo Ctrl-D) tan pronto como fuera posible. para volver a su cuenta de nivel de usuario.

Es mejor deshabilitar la cuenta raíz por completo y luego, en lugar de permitir sesiones de terminal de larga duración con poderes peligrosos, solicitar al usuario que solicite específicamente derechos de superusuario por comando. La clave de este enfoque es un comando llamado `sudo` (como en "cambiar de usuario y ejecutar este comando").

`sudo` se usa para prefijar un comando que debe ejecutarse con privilegios de superusuario. Se usa un archivo de configuración para definir qué usuarios pueden usar sudo y qué comandos pueden ejecutar. Cuando se ejecuta un comando como este, se le solicita al usuario su propia contraseña, que luego se almacena en caché durante un período de tiempo (de forma predeterminada en 15 minutos), por lo que si necesita ejecutar varios comandos de nivel de superusuario, no seguirá obteniendo continuamente pidió que lo escribiera.

Suponiendo que está en un sistema Linux que usa `sudo` y su cuenta está configurada como administrador, intente lo siguiente para ver qué sucede cuando intenta acceder a un archivo que se considera confidencial (contiene contraseñas cifradas):

![](https://ubuntucommunity.s3.dualstack.us-east-2.amazonaws.com/original/2X/1/13ea055ef5e5d362ece7144dbc477d9c8fd9b6f2.png)

Si ingresa su contraseña cuando se le solicite, debería ver el contenido del archivo `/etc/shadow`. Ahora cierra la terminal, vuelve a abrirla y ejecuta `sudo cat /etc/shadow` nuevamente. Esta vez, el archivo se mostrará sin pedirle una contraseña, ya que todavía está en la caché.

### Instalación de software nuevo

Hay muchas formas diferentes de instalar software en sistemas Linux. Instalar directamente desde los repositorios de software oficiales de su distribución es la opción más segura, pero a veces la aplicación o la versión que desea simplemente no está disponible de esa manera. Al instalar a través de cualquier otro mecanismo, asegúrese de obtener los archivos de una fuente oficial para el proyecto en cuestión.

Instalemos un nuevo programa de línea de comandos desde los repositorios estándar de Ubuntu para ilustrar este uso de sudo:

```bash
sudo apt install tree
```

Una vez que haya proporcionado su contraseña, el programa `apt` imprimirá unas cuantas líneas de texto para decirle lo que está haciendo. El programa de `tree` es pequeño, por lo que no debería llevar más de uno o dos minutos descargarlo e instalarlo para la mayoría de los usuarios. Una vez que regrese a la línea de comandos normal, el programa está instalado y listo para usar. Vamos a ejecutarlo para obtener una mejor visión general de cómo se ve nuestra colección de archivos y carpetas:

```bash
alicia@cocombra2:/tmp/tutorial$ tree
.
├── dir1
│   └── combined.txt
├── dir2
├── dir3
├── dir4
│   └── dir5
│       └── dir6
├── output.txt
├── test_1.txt
├── test_2.txt
└── test_3.txt

6 directories, 5 files
```

![](https://ubuntucommunity.s3.dualstack.us-east-2.amazonaws.com/optimized/2X/5/5249bad7f0bb536adceb8a9381c7366054546763_2_690x404.png)

## Limpieza final

Hemos llegado al final de este tutorial, así que vamos a dejar las carpetas en el mismo estado en que las encontramos, así que, como paso final, eliminemos el área experimental que estábamos usando antes, y luego verifiquemos que ya no esté:

```bash
cd
rm -r /tmp/tutorial
ls /tmp
```