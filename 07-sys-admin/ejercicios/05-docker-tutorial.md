- [Introducción a Docker](#introducción-a-docker)
  - [Crear una aplicación de ejemplo](#crear-una-aplicación-de-ejemplo)
    - [Probar la aplicación](#probar-la-aplicación)
    - [Estructura de ficheros](#estructura-de-ficheros)
    - [Construir la imagen](#construir-la-imagen)
    - [Ver las imágenes locales](#ver-las-imágenes-locales)
    - [Etiquetar imágenes](#etiquetar-imágenes)
    - [Ejecutar una imagen como contenedor](#ejecutar-una-imagen-como-contenedor)
    - [Ejecutar en segundo plano](#ejecutar-en-segundo-plano)
    - [Mostrar contenedores](#mostrar-contenedores)
    - [Detener, iniciar y nombrar contenedores](#detener-iniciar-y-nombrar-contenedores)
  - [Usar contenedores en nuestro entorno de desarrollo](#usar-contenedores-en-nuestro-entorno-de-desarrollo)
    - [Conectar la aplicación a la base de datos.](#conectar-la-aplicación-a-la-base-de-datos)
  - [Usa Compose para desarrollar en local](#usa-compose-para-desarrollar-en-local)
  - [Debug con docker](#debug-con-docker)

# Introducción a Docker

El contenido de este tutorial es una traducción y adaptación del tutorial oficial de docker
https://docs.docker.com/language/python/ 

## Crear una aplicación de ejemplo

Vamos a crear una aplicación de Python simple utilizando Flask. Crea un directorio en su máquina local llamado python-docker y siga los pasos a continuación para crear un servicio web simple.

```bash
#crear la carpeta del proyecto en nuestra carpeta home
cd 
mkdir docker-hello
cd docker-hello

# crear el entorno virtual y activarlo
python3 -m venv .venv
source .venv/bin/activate

# instalar flask
pip install Flask
pip3 freeze | grep Flask >> requirements.txt

# crear el fichero de la app de flask
touch app.py

# abrir visual studio code
code .
```

A continuación, añade el siguiente código al fichero `app.py`

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'
```

### Probar la aplicación

Vamos a asegurarnos de que la aplicación web funciona correctamente. Para ello, pon el siguiente comando en la terminal:

```bash
python -m flask run
```

A continuación abre un navegador web (Firefox, Chrome...) y navega hasta la url `http://localhost:5000`

Vuelve al terminal donde se ejecuta nuestro servidor y debería ver las siguientes requests en el servidor. 

```bash
127.0.0.1 - - [22/Sep/2020 11:07:41] "GET / HTTP/1.1" 200 -
```

Ahora que nuestra aplicación se ha ejecutado correctamente, vamos a crear el fichero Dockerfile.

El fichero Dockerfile es un documento de texto que contiene las instrucciones para ensamblar una imagen de Docker. Cuando le decimos a Docker que construya nuestra imagen ejecutando el comando de compilación de docker, Docker lee estas instrucciones, las ejecuta y crea una imagen d

El nombre de archivo predeterminado que se usa para un Dockerfile es Dockerfile (sin una extensión de archivo). El uso del nombre predeterminado le permite ejecutar el comando de compilación de docker sin tener que especificar indicadores de comando adicionales.

1. La primera línea de un Dockerfile es siempre la directiva de analizador de sintaxis `#`. Aunque es opcional, esta directiva le indica al compilador de Docker qué sintaxis usar al analizar el Dockerfile y permite que las versiones anteriores de Docker con BuildKit habilitado actualicen el analizador antes de comenzar la compilación.
    ```
    # syntax=docker/dockerfile:1
    ```

    Lo recomendado es usar `docker/dockerfile:1`, que siempre apunta a la versión más reciente de la sintaxis de la versión 1.

2. A continuación, debemos agregar una línea en nuestro Dockerfile que le diga a Docker qué imagen base nos gustaría usar para nuestra aplicación.
    ```
    # syntax=docker/dockerfile:1

    FROM python:3.8-slim-buster
    ```

    Las imágenes de Docker se pueden heredar de otras imágenes. Por lo tanto, en lugar de crear nuestra propia imagen base, usaremos la imagen oficial de Python que ya tiene todas las herramientas y paquetes que necesitamos para ejecutar una aplicación de Python.

3. Para facilitar la ejecución del resto de nuestros comandos, vamos a crear un directorio de trabajo. Esto le indica a Docker que use esta ruta como la ubicación predeterminada para todos los comandos posteriores. Al hacer esto, no tenemos que escribir rutas completas de archivos y podemos usar rutas relativas basadas en el directorio de trabajo.
    ```
    WORKDIR /app
    ```

4. Por lo general, lo primero que hace una vez que hemos descargado un proyecto en Python es instalar las dependencias con `pip`. 
    
    Antes de que podamos ejecutar `pip install`, necesitamos copiar nuestro archivo `requirements.txt` en nuestra imagen. Usaremos el comando `COPY` para hacer esto. 
    
    El comando `COPY` acepta dos parámetros:
    - El primer parámetro le dice a Docker qué archivo(s) le gustaría copiar en la imagen. 
    - El segundo parámetro le dice a Docker dónde desea que se copien los archivos. 
    
    Copiaremos el archivo requirements.txt en nuestro directorio de trabajo `/app`.

    ```
    COPY requirements.txt requirements.txt
    ```

5. Una vez que tengamos nuestro archivo requirements.txt dentro de la imagen, podemos usar el comando `RUN` para ejecutar el comando `pip install`. Esto funciona exactamente igual que si estuviéramos ejecutando `pip install` en nuestra máquina local, pero en este caso las librerías se instalan en la imagen.
    ```
    RUN pip3 install -r requirements.txt
    ```

6. En este punto, tenemos una imagen basada en la versión 3.8 de Python y hemos instalado nuestras dependencias. El siguiente paso es agregar nuestro código fuente a la imagen. Usaremos el comando `COPY` tal como lo hicimos con el `requirements.txt`.
    ```
    COPY . .
    ```
    
    Este comando `COPY` toma todos los archivos ubicados en el directorio actual y los copia en la imagen. 
    
7. Ahora, tenemos que decirle a Docker qué comando queremos ejecutar cuando nuestra imagen se ejecute dentro de un contenedor. Hacemos esto usando el comando `CMD`. 
    
    Ten en cuenta que debemos hacer que la aplicación sea visible externamente (es decir, desde fuera del contenedor) especificando `--host=0.0.0.0.`

    ```
    CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
    ```

8. Este sería el Dockerfile final con todos los comandos anteriores:
    ```python
    # syntax=docker/dockerfile:1

    FROM python:3.8-slim-buster

    WORKDIR /app

    COPY requirements.txt requirements.txt
    RUN pip3 install -r requirements.txt

    COPY . .

    CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
    ```

### Estructura de ficheros

Recapitulando, a estas alturas del proyecto deberíamos tener los siguientes tres ficheros:

```
python-docker
|____ app.py
|____ requirements.txt
|____ Dockerfile
```

### Construir la imagen

Ahora que hemos creado nuestro Dockerfile, vamos a construir nuestra imagen. Para hacer esto, usamos el comando `docker build`. El comando `docker build` crea imágenes Docker a partir de un Dockerfile y un "contexto". El contexto es el conjunto de archivos ubicados en el `PATH` o `URL` especificada. El proceso de compilación de Docker puede acceder a cualquiera de los archivos ubicados en este contexto.

El comando de compilación opcionalmente toma un indicador `--tag`. La etiqueta se utiliza para establecer el nombre de la imagen y una etiqueta opcional en el formato `nombre:etiqueta`. Dejaremos la etiqueta opcional por ahora para ayudar a simplificar las cosas. Si no pasa una etiqueta, Docker usa `"latest"` como su etiqueta predeterminada.

A continuación vamos a construir nuestra primera imagen de Docker:

```
docker build --tag python-docker .
```

Si te sale el siguiente error, puede que tengas que desactivar el DOCKER_BUILDKIT al ejecutar el comando:

```
DOCKER_BUILDKIT=0 docker build --tag python-docker .
```

### Ver las imágenes locales

Para ver una lista de imágenes que tenemos en nuestra máquina local, tenemos dos opciones:
- Una es usar el cliente de terminal:

```
$ docker images
REPOSITORY      TAG       IMAGE ID       CREATED          SIZE
python-docker   latest    33f8dd462e4a   12 minutes ago   139MB
```

- La otra es usar Docker Desktop

### Etiquetar imágenes

Para crear una nueva etiqueta para la imagen que hemos creado arriba, ejecute el siguiente comando.

```bash
docker tag python-docker:latest python-docker:v1.0.0
```

El comando `docker tag` crea una nueva etiqueta para una imagen. **No crea una nueva imagen.** La etiqueta apunta a la misma imagen y es solo otra forma de hacer referencia a la imagen.

Ahora, ejecute el comando de `docker images` para ver una lista de nuestras imágenes locales.

```bash
$ docker images
REPOSITORY      TAG       IMAGE ID       CREATED          SIZE
python-docker   latest    33f8dd462e4a   12 minutes ago   139MB
python-docker   v1.0.0    33f8dd462e4a   12 minutes ago   139MB
```

Puede ver que tenemos dos imágenes que comienzan con `python-docker`. Sabemos que son la misma imagen porque si observa la columna `IMAGE_ID`, puede ver que los valores son los mismos para las dos imágenes.

Eliminemos la etiqueta que acabamos de crear. Para hacer esto, usaremos el comando `rmi`. El comando `rmi` significa eliminar imagen.

```bash
$ docker rmi python-docker:v1.0.0
Untagged: python-docker:v1.0.0
```

Tenga en cuenta que la respuesta de Docker nos dice que la imagen no se ha eliminado, sino que solo se "desetiquetado". Puede verificar esto ejecutando el comando `docker images`.

```bash
$ docker images
REPOSITORY      TAG       IMAGE ID       CREATED          SIZE
python-docker   latest    33f8dd462e4a   15 minutes ago   139MB
```

Nuestra imagen que estaba etiquetada con `:v1.0.0` se eliminó, pero todavía tenemos la etiqueta `python-docker:latest` disponible en nuestra máquina.

### Ejecutar una imagen como contenedor

Para ejecutar una imagen dentro de un contenedor, usamos el comando `docker run`. El comando `docker run` requiere de un parámetro que es el nombre de la imagen. 

Arranquemos nuestra imagen y asegurémonos de que se está ejecutando correctamente. Ejecute el siguiente comando en su terminal:

```
docker run python-docker
```

Después de esto, normalmente se abre un navegador en la dirección `http://127.0.0.1:5000/` y, comprobaremos que en el navegador no abre correctamente la aplicación web.

Probamos a abrir una terminal nueva y poner:
```bash
$ curl localhost:5000
curl: (7) Failed to connect to localhost port 5000: Connection refused
```

Como puede ver, nuestro comando curl falló porque se rechazó la conexión a nuestro servidor. Esto significa que no pudimos conectarnos al host local en el puerto 5000. 

Detengamos el contenedor y reiniciemos con el puerto 5000 publicado en nuestra red local. Para detener el contenedor, presiona ctrl-c. Esto lo regresará al indicador de la terminal.

Para publicar un puerto para nuestro contenedor, usaremos el indicador `--publish` (-p para abreviar) en el comando de ejecución de docker. 

El formato del comando `--publish` es `[puerto de host]:[puerto de contenedor]`. Entonces, si quisiéramos abrir el puerto `5000` dentro del contenedor al puerto `3000` fuera del contenedor, pasaríamos `3000:5000` al --publish.

Como no especificamos un puerto cuando ejecutamos la aplicación flask en el contenedor el valor predeterminado es 5000. Si queremos que nuestra solicitud anterior vaya al puerto 5000 para que funcione, podemos asignar el puerto 8000 del host al puerto 5000 del contenedor:

```bash
docker run --publish 8000:5000 python-docker
```

A continuación abrimos en el navegador la url http://127.0.0.1:8000/ o hacemos un get desde una terminal nueva, y veremos que en esta ocasión la aplicación funciona correctamente:

```bash
$ curl localhost:8000
Hello, Docker!
```

Presiona ctrl-c para parar el contenedor

### Ejecutar en segundo plano

El ejercicio se ha ejecutado bien, pero nuestra aplicación debería estar desplegada en un servidor web y no tendríamos que estar conectados al contenedor. 

Docker puede ejecutar su contenedor en segundo plano. Para hacer esto, podemos usar `--detach` o `-d` para abreviar. Docker inicia su contenedor de la misma manera que antes, pero esta vez se "desacoplará" del contenedor y lo regresará al puntero de la terminal.

```bash
$ docker run -d -p 8000:5000 python-docker
71497a9808e81fa90f0dbc2aa2f75023367c4987ad831c5c6e3266ffa755cc27
```

Docker iniciará nuestro contenedor en segundo plano e imprimirá el id del contenedor en la terminal.

### Mostrar contenedores

Dado que podemos ejecutar nuestro contenedor en segundo plano, ¿cómo sabemos si nuestro contenedor se está ejecutando o qué otros contenedores se están ejecutando en nuestra máquina? Para ello podemos ejecutar el comando `docker ps`. 

```bash
$ docker ps
CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS          PORTS                    NAMES
71497a9808e8   python-docker   "python3 -m flask ru…"   19 seconds ago   Up 17 seconds   0.0.0.0:8000->5000/tcp   naughty_merkle
```

El comando docker ps proporciona mucha información sobre nuestros contenedores en ejecución. Podemos ver el ID del contenedor, la imagen que se ejecuta dentro del contenedor, el comando que se usó para iniciar el contenedor, cuándo se creó, el estado, los puertos expuestos y el nombre del contenedor.

Probablemente se esté preguntando de dónde viene el nombre de nuestro contenedor. Como no proporcionamos un nombre para el contenedor cuando lo iniciamos, Docker genera un nombre aleatorio. 

Para detener el contenedor, ejecute el comando `docker stop`. Debe pasar el nombre del contenedor o puede usar la ID del contenedor.

```
$ docker stop naughty_merkle
naughty_merkle
```

Ahora, vuelva a ejecutar el comando `docker ps` para ver una lista de contenedores en ejecución.

```bash
$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

### Detener, iniciar y nombrar contenedores

Puede iniciar, detener y reiniciar contenedores Docker. Cuando detenemos un contenedor, no se elimina, pero el estado cambia a detenido y el proceso dentro del contenedor se detiene. Cuando ejecutamos el comando `docker ps` en el módulo anterior, la salida predeterminada solo muestra contenedores en ejecución. Cuando pasamos `--all` o `-a` para abreviar, vemos todos los contenedores en nuestra máquina, independientemente de su estado de inicio o parada.

```bash
$ docker ps -a
CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS                       PORTS                    NAMES
71497a9808e8   python-docker   "python3 -m flask ru…"   4 minutes ago    Exited (137) 2 minutes ago                            naughty_merkle
68a9848a46cf   python-docker   "-d"                     4 minutes ago    Created                      0.0.0.0:8000->5000/tcp   vibrant_einstein
9ffaed22951c   python-docker   "python3 -m flask ru…"   10 minutes ago   Exited (0) 7 minutes ago                              strange_heisenberg
9674f7de63c4   python-docker   "python3 -m flask ru…"   15 minutes ago   Exited (0) 12 minutes ago                             magical_diffie
```

Ahora deberías ver varios contenedores en la lista. Estos son contenedores que iniciamos y detuvimos pero que no se han eliminado.

Reiniciemos el contenedor que acabamos de detener. Localice el nombre del contenedor que acabamos de detener y reemplace el nombre del contenedor a continuación en el comando de reinicio.

```bash
$ docker restart naughty_merkle
naughty_merkle
```

Ahora enumera todos los contenedores nuevamente usando el comando `docker ps`.
```bash
$ docker ps --all
CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS                      PORTS                    NAMES
71497a9808e8   python-docker   "python3 -m flask ru…"   5 minutes ago    Up 46 seconds               0.0.0.0:8000->5000/tcp   naughty_merkle
68a9848a46cf   python-docker   "-d"                     6 minutes ago    Created                     0.0.0.0:8000->5000/tcp   vibrant_einstein
9ffaed22951c   python-docker   "python3 -m flask ru…"   12 minutes ago   Exited (0) 9 minutes ago                             strange_heisenberg
9674f7de63c4   python-docker   "python3 -m flask ru…"   17 minutes ago   Exited (0) 14 minutes ago                            magical_diffie
```

Observa que el contenedor que acabamos de reiniciar se inició en modo separado y tiene el puerto 8000 expuesto. Además, observe que el estado del contenedor es "Up X segundos". Cuando reinicia un contenedor, comienza con los mismos parámetros o comandos con los que se inició originalmente.

Ahora, detengámonos y eliminemos todos nuestros contenedores y echemos un vistazo a solucionar el problema de los nombres aleatorios. Detén el contenedor que acabamos de arrancar. Busca el nombre de ese contenedor en ejecución y reemplaza el nombre en el siguiente comando con el nombre del contenedor en su sistema.
```bash
$ docker stop naughty_merkle
naughty_merkle
```

Ahora que todos nuestros contenedores están detenidos, eliminémoslos. Cuando elimina un contenedor, ya no se está ejecutando ni está detenido, pero el proceso dentro del contenedor detendrá y los metadatos del contenedor se eliminará.
```bash
i$ docker ps --all
CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS                        PORTS                    NAMES
71497a9808e8   python-docker   "python3 -m flask ru…"   8 minutes ago    Exited (137) 33 seconds ago                            naughty_merkle
68a9848a46cf   python-docker   "-d"                     8 minutes ago    Created                       0.0.0.0:8000->5000/tcp   vibrant_einstein
9ffaed22951c   python-docker   "python3 -m flask ru…"   14 minutes ago   Exited (0) 11 minutes ago                              strange_heisenberg
9674f7de63c4   python-docker   "python3 -m flask ru…"   20 minutes ago   Exited (0) 17 minutes ago                              magical_diffie
```

Para eliminar un contenedor, ejecute el comando `docker rm` con el nombre del contenedor. Puede pasar varios nombres de contenedores al comando con un solo comando. Nuevamente, reemplace los nombres de los contenedores en el siguiente comando con los nombres de los contenedores de su sistema.
```bash
$ docker rm naughty_merkle vibrant_einstein strange_heisenberg magical_diffie
naughty_merkle
vibrant_einstein
strange_heisenberg
magical_diffie
```

Ejecute el comando `docker ps --all` nuevamente para ver que se han eliminado todos los contenedores.

Ahora, abordemos el problema de los nombres aleatorios. La práctica estándar es nombrar sus contenedores por la sencilla razón de que es más fácil identificar qué se está ejecutando en el contenedor y con qué aplicación o servicio está asociado.

Para nombrar un contenedor, solo necesitamos pasar el indicador `--name` al comando de ejecución de la ventana acoplable.
```bash
$ docker run -d -p 8000:5000 --name rest-server python-docker
c3503a36bee509a7104ac09640fe862aa168b0034d2f27f4eba3672b1cb04592
```

```bash
$ docker ps
CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS          PORTS                    NAMES
c3503a36bee5   python-docker   "python3 -m flask ru…"   37 seconds ago   Up 36 seconds   0.0.0.0:8000->5000/tcp   rest-server
```

Ahora podemos identificar fácilmente nuestro contenedor según el nombre.

## Usar contenedores en nuestro entorno de desarrollo

Primero, veremos cómo ejecutar una base de datos en un contenedor y cómo usamos los volúmenes y las redes para conservar nuestros datos y permitir que nuestra aplicación se comunique con la base de datos. Luego, juntaremos todo en un archivo `compose` que nos permite configurar y ejecutar un entorno de desarrollo local con un solo comando.

En lugar de descargar MySQL, instalar, configurar y luego ejecutar la base de datos MySQL como un servicio, podemos usar la imagen oficial de Docker para MySQL y ejecutarla en un contenedor.

Antes de ejecutar MySQL en un contenedor, crearemos un par de volúmenes que Docker puede administrar para almacenar nuestra configuración y datos persistentes. Usemos la función de volúmenes administrados que proporciona Docker en lugar de usar montajes de enlace. Puedes leer todo sobre el uso de volúmenes [aquí](https://docs.docker.com/storage/volumes/).

Vamos a crear dos volúmenes: uno para los datos y otro para la configuración de MySQL.
```bash
$ docker volume create mysql
$ docker volume create mysql_config
```

Ahora crearemos una red que nuestra aplicación y base de datos usarán para comunicarse entre sí. La red se denomina "user-defined bridge network" y nos brinda un buen servicio de búsqueda de DNS que podemos usar al crear nuestra cadena de conexión.
```bash
$ docker network create mysqlnet
```

Ahora podemos ejecutar MySQL en un contenedor y adjuntarlo a los volúmenes y la red que creamos anteriormente. Docker extraerá la imagen de Hub y la ejecutará localmente. 

En el siguiente comando, la opción -v es para iniciar el contenedor con volúmenes
```bash
$ docker run --rm -d -v mysql:/var/lib/mysql \
  -v mysql_config:/etc/mysql -p 3306:3306 \
  --network mysqlnet \
  --name mysqldb \
  -e MYSQL_ROOT_PASSWORD=p@ssw0rd1 \
  mysql
```

Ahora, asegurémonos de que nuestra base de datos MySQL se esté ejecutando y que podamos conectarnos a ella. Conéctese a la base de datos MySQL en ejecución dentro del contenedor usando el siguiente comando e ingrese "p@ssw0rd1" cuando se le solicite la contraseña:
```bash
$ docker exec -ti mysqldb mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.31 MySQL Community Server - GPL

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```

### Conectar la aplicación a la base de datos.

En el comando anterior, iniciamos sesión en la base de datos MySQL pasando el comando 'mysql' al contenedor mysqldb. Presione CTRL-D para salir del terminal de MySQL.

Ahora que tenemos MySQL en ejecución, actualicemos el fichero `app.py` para usar MySQL como almacén de datos. Agregaremos también algunas rutas nuevas a nuestro servidor: una para obtener registros y otra para crear nuestra base de datos y tablas.

```python
import mysql.connector
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/widgets')
def get_widgets():
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="inventory"
    )
    cursor = mydb.cursor()


    cursor.execute("SELECT * FROM widgets")

    row_headers=[x[0] for x in cursor.description] #this will extract row headers

    results = cursor.fetchall()
    json_data=[]
    for result in results:
        json_data.append(dict(zip(row_headers,result)))

    cursor.close()

    return json.dumps(json_data)

@app.route('/initdb')
def db_init():
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1"
    )
    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS inventory")
    cursor.execute("CREATE DATABASE inventory")
    cursor.close()

    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="inventory"
    )
    cursor = mydb.cursor()

    cursor.execute("DROP TABLE IF EXISTS widgets")
    cursor.execute("CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")
    cursor.close()

    return 'init database'

if __name__ == "__main__":
    app.run(host ='0.0.0.0')
```

Hemos añadido la librería de mysql y hemos actualizado el código para conectarnos al servidor de la base de datos, crear una base de datos y una tabla. También crear una ruta para obtener widgets. Ahora necesitamos reconstruir nuestra imagen para que incluya nuestros cambios.

Primero, agreguemos la librería `mysql-connector-python` a nuestra aplicación usando `pip`.
```bash
$ pip install mysql-connector-python  # instala la librería
$ pip freeze | grep mysql-connector-python >> requirements.txt  # añade la dependencia al requirements.txt
```

Comprueba ahora que tu fichero `requirements.txt` contiene algo como esto:
```
Flask==2.2.2
mysql-connector-python==8.0.31
```

Ahora vamos a construir la imagen:
```bash
$ docker build --tag python-docker-dev .
```

Ahora, agregaremos el contenedor a la red de la base de datos y luego vamos a ejecutar nuestro contenedor. Esto nos permitirá acceder a la base de datos por su nombre de contenedor.
```bash
 docker run \
  --rm -d \
  --network mysqlnet \
  --name rest-server \
  -p 8000:5000 \
  python-docker-dev
```

Ahora comprobaremos que nuestra aplicación está conectada a la base de datos y puede agregar una nota:
```bash
$ curl http://localhost:8000/initdb
$ curl http://localhost:8000/widgets
```

Si todo va bien, deberías recibir el siguiente json por pantalla:
```bash
[]
```

Puedes comprobar que la base de datos se ha creado correctamente abriendo la consola de mysql y ejecutando los siguientes comandos:

```bash
$ docker exec -ti mysqldb mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 12
Server version: 8.0.31 MySQL Community Server - GPL

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```

- Mostrar las bases de datos que existen en mysql
  ```
  mysql> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | inventory          |
    | mysql              |
    | performance_schema |
    | sys                |
    +--------------------+
    5 rows in set (0.01 sec)
  ```

- Entrar en la de `inventory`
  ```
  mysql> use inventory;
    Reading table information for completion of table and column names
    You can turn off this feature to get a quicker startup with -A

    Database changed
  ```

- Mostrar las tablas de la bd
  ```
  mysql> show tables;
    +---------------------+
    | Tables_in_inventory |
    +---------------------+
    | widgets             |
    +---------------------+
    1 row in set (0.00 sec)
  ```

## Usa Compose para desarrollar en local

En esta sección, crearemos un archivo `Compose` para iniciar nuestro `python-docker` y la base de datos MySQL usando un solo comando.

Crea un nuevo archivo llamado `docker-compose.dev.yml`. A continuación copia y pega los siguientes comandos en el archivo.

```yml
version: '3.8'

services:
 web:
  build:
   context: .
  ports:
  - 8000:5000
  volumes:
  - ./:/app

 mysqldb:
  image: mysql
  ports:
  - 3306:3306
  environment:
  - MYSQL_ROOT_PASSWORD=p@ssw0rd1
  volumes:
  - mysql:/var/lib/mysql
  - mysql_config:/etc/mysql

volumes:
  mysql:
  mysql_config:
```

Este archivo Compose es muy conveniente ya que no tenemos que escribir todos los parámetros para pasar al comando de `docker run`. Podemos hacerlo directamente usando un archivo Compose.

Publicaremos la web en el puerto 8000 para que podamos llegar al servidor web de desarrollo dentro del contenedor. También mapeamos nuestro código fuente local en el contenedor en ejecución para realizar cambios en nuestro editor de texto y hacer que esos cambios se recojan en el contenedor.

Otra característica realmente interesante de usar un archivo Compose es que tenemos una resolución de servicio configurada para usar los nombres de servicios. Por lo tanto, ahora podemos usar "mysqldb" en nuestra cadena de conexión. La razón por la que usamos "mysqldb" es porque así es como llamamos a nuestro servicio MySQL en el archivo Compose.

Ten en cuenta que no especificamos una red para esos 2 servicios. Cuando usamos docker-compose, automáticamente crea una red y conecta los servicios a ella.

Ahora, para iniciar nuestra aplicación y confirmar que se está ejecutando correctamente, ejecute el siguiente comando:
```
docker-compose -f docker-compose.dev.yml up --build
``` 

Pasamos el indicador `--build` para que Docker compile nuestra imagen y luego inicie los contenedores.

Ahora probemos nuestro punto final de API. Abre una nueva terminal y luego haz una solicitud GET al servidor usando los comandos curl:
```bash
$ curl http://localhost:8000/initdb
$ curl http://localhost:8000/widgets
```
