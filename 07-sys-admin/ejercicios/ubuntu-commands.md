# Introducción a Linux - Ubuntu

### La terminal

Al abrir la terminal o símbolo del sistema, por defecto veremos algo como esto:
```
sammy@webapp:~$
```

- `sammy`: El nombre de usuario del usuario actual
- `webapp`: El hostname del sistema
- `~`: El directorio actual. En bash, la terminal por defecto de Ubuntu, el símbolo ~ representa a la carpeta home del usuario actual, en este caso /home/sammy
- `$`: El simbolo de solicitud. Después de este símbolo, el usuario puede introducir los comandos

### Ejecucion de comandos

```
ls -la /home
```

- `ls` muestra el contenido de un directorio
- `-la` son 2 argumentos opcionales
    * `-a` muestra todos los ficheros del path espeficicado, incluso los ficheros ocultos (los que empiezan por `.`) 
    * `-l` usa el formato de "lista larga" para mostrar el resultado
- `\home` indica el directorio del que se mostrará el contenido 

Para ver las instrucciones y parámetros de un comando, usar `man` y a continuación el nombre del comando 

### Variables de entorno

Una variable de entorno es una variable dinámica que puede afectar al comportamiento de los procesos en ejecución en un ordenador. Son parte del entorno en el que se ejecuta un proceso.

Para visualizar las variables de entorno de una sesión de terminal:
```
env
```

Para visualizar una variable en concreta o utilizarla en un comando
```
echo $PATH
cd $HOME
```

Para crear una nueva variable de entorno o cambiar el valor de una de ellas:
```
VAR=value
export PATH=$PATH:/opt/app/bin
```

### Navegar por los ficheros del sistema
Para visualizar el path actual
```
pwd
```

Para explorar el contenido de un directorio (si no le pasamos la ruta a explorar, ejecutará el comando sobre el path actual
```
ls
ls -l
ls -a
```

### Navegar por los ficheros del sistema
Para cambiar el directorio activo
```
cd /usr/share
cd en/LC_MESSAGES
cd ..
cd
```

### Ver el contenido de un fichero
```
less /etc/services
cat /etc/services
tail -f /etc/services
```

### Crear un fichero

`touch` crea un fichero vacío
```
touch file1
```


```
touch /home/demo/file2 /home/demo/file3
ls
```


### Crear un directorio
```
cd
mkdir test
mkdir test/example
mkdir -p some/other/directories
```

### Mover o renombrar ficheros o directorios
```
mv file1 test
cd
mv test/file1 .
mv test testing
```

### Copiar ficheros o directorios
```
cp file3 file4
cp -r some again
cp file1 again
```

### Eliminar ficheros o directorios
```
rm file4
rmdir testing/example
rm -r again
```

### Editar ficheros
```
nano file1
```

```
vi file1
```
