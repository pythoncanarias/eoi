# Docker

1. Descarga el código de la aplicación django-polls en tu workspace si no la tienes

```bash
git clone git@github.com:aliciapj/django_polls.git
```

2. Crea un entorno virtual e instala las librerías del proyecto

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Ejecuta las migraciones y carga los datos del fixture inicial
```bash
python manage.py migrate
python manage.py loaddata fixtures/polls_data.json
```

4. Comprueba que la aplicación funciona
```bash
python manage.py runserver 0.0.0.0:8000
curl http://localhost:8000/
```

## Dockerización por copia del proyecto

Crea un fichero llamado `Dockerfile` en la raíz del proyecto

En el fichero ve añadiendo el siguiente contenido:

- La primera línea será la directiva de sintaxis. Aunque es opcional, esta línea le indica a Docker qué sintaxis debe usar para leer el fichero Dockerfile, y permite a las versiones más antiguas que sigan funcionando. En nuestro caso pondremos la versión 1

```yaml
# syntax=docker/dockerfile:1
```

- Las imágenes de docker pueden heredar el comportamiento base de otras imágenes. Esto es útil porque así nos podemos ahorrar las tareas más básicas de montar el entorno, como por ejemplo, instalar Python. En nuestro caso, utilizaremos la imagen `python:3.9-slim-buster` (puedes ver todas las imágenes de python disponibles [aquí](https://hub.docker.com/_/python) y en concreto qué esta haciendo la `python:3.9-slim-buster` [aquí](https://github.com/docker-library/python/blob/d9ab222fcd828888b102e3581c03931eac344097/3.9/buster/slim/Dockerfile)

```yaml
FROM python:3.9-slim-buster
```

- A continuación le diremos a Docker cuál es el directorio de trabajo, en nuestro caso `/app`

```
WORKDIR /app
```

- Ahora tenemos que preparar el entorno de ejecución. Para ello, vamos a copiar el fichero `requirements.txt` a la imagen para posteriormente instalar todas las dependencias necesarias

```
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
```

- Ahora copiaremos los ficheros de código a la imágen. Si el código estuviera subido a un repo, podríamos descargarlo directamente de Github. Por ahora, copiaremos todo el contenido del directorio a la imagen de Docker con el siguiente comando:

```
COPY . .
```

- Y por último, arranca la aplicación django:

```
CMD [ "python3", "manage.py" , "runserver" , "0.0.0.0:8000"]
```

El fichero `Dockerfile` debería haber quedado así

```yaml
# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py" , "runserver" , "0.0.0.0:8000"]
```

Para construir la imagen a partir del fichero que acabas de crear, ejecuta el siguiente comando en la consola:

```bash
Sending build context to Docker daemon  424.5MB
Step 1/6 : FROM python:3.9-slim-buster
3.9-slim-buster: Pulling from library/python
69692152171a: Already exists 
59773387c0e7: Pull complete 
3fc84e535e87: Pull complete 
68ebeebdab6f: Pull complete 
3d3af2ef8baa: Pull complete 
Digest: sha256:80b238ba357d98813bcc425f505dfa238f49cf5f895492fc2667af118dccaa44
Status: Downloaded newer image for python:3.9-slim-buster
 ---> 609da079b03a
Step 2/6 : WORKDIR /app
 ---> Running in f09477c7fe05
Removing intermediate container f09477c7fe05
 ---> 9be45d367f92
Step 3/6 : COPY requirements.txt requirements.txt
 ---> fc6a0f1d7d5f
Step 4/6 : RUN pip3 install -r requirements.txt
 ---> Running in f553cc9ef108
Collecting asgiref==3.3.4
  Downloading asgiref-3.3.4-py3-none-any.whl (22 kB)
Collecting Django==3.2.3
  Downloading Django-3.2.3-py3-none-any.whl (7.9 MB)
Collecting pytz==2021.1
  Downloading pytz-2021.1-py2.py3-none-any.whl (510 kB)
Collecting sqlparse==0.4.1
  Downloading sqlparse-0.4.1-py3-none-any.whl (42 kB)
Installing collected packages: sqlparse, pytz, asgiref, Django
WARNING: Running pip as root will break packages and permissions. You should install packages reliably by using venv: https://pip.pypa.io/warnings/venv
Successfully installed Django-3.2.3 asgiref-3.3.4 pytz-2021.1 sqlparse-0.4.1
Removing intermediate container f553cc9ef108
 ---> ef1ba4a17e64
Step 5/6 : COPY . .
 ---> 19663b4b8c53
Step 6/6 : CMD [ "python3", "manage.py" , "runserver" , "0.0.0.0:8000"]
 ---> Running in 082c3ff5e23e
Removing intermediate container 082c3ff5e23e
 ---> 30630b8dcb67
Successfully built 30630b8dcb67
Successfully tagged python-docker:latest
 ```

Para ver las imágenes que están generadas en tu máquina, puedes ejecutar el siguiente comando:

```bash
docker images
```
salida:
```
REPOSITORY      TAG               IMAGE ID       CREATED         SIZE
python-docker   latest            30630b8dcb67   4 minutes ago   536MB
python          3.9-slim-buster   609da079b03a   7 days ago      115MB
hello-world     latest            d1165f221234   2 months ago    13.3kB
```

**Correr la imagen en un contenedor**

Para lanzar el contenedor a partir de la imagen que acabamos de crear, ejecuta el siguiente comando en la consola:

```bash
docker run python-docker
```

Si accedes a la url de la aplicación flask en el navegador, comprobarás que no puedes acceder a ella. También puedes comprobarlo con el siguiente comando de `curl`:

```bash
curl localhost:8000
```
salida:
```
curl: (7) Failed to connect to localhost port 8000: Connection refused
```

Esto es porque la aplicación ha sido arrancada en un entorno aislado, fuera de la red local. Para que sea visible en nuestra red local, tenemos que parar el contenedor y lanzalo con el parámetro `--publish`

```bash
docker run --publish 8000:8000 python-docker
```

Ahora debería funcionar:
```bash
curl localhost:8000
```

Pero como puedes ver en la consola, el proceso se queda abierto. Lo ideal sería que se quedase corriendo en segundo plano y pudieramos gestionarlo de forma asíncrona.

Para ello, para el worker y arráncalo en segundo plano con el siguiente comando:

```bash
docker run -d -p 8000:8000 python-docker
```
salida:
```
648c686c1e8e8e9cab76f748675630f11bc61c07d7da9219c3527a8676a84976 
```

> Comprueba que la aplicación sigue funcionando en tu navegador o usando `curl`

- Para comprobar los contenedores que están ejecutándose en la máquina:
    
```bash
docker ps
```
salida:
```
CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS         PORTS                                       NAMES
c419f354cbc5   python-docker   "python3 manage.py r…"   5 seconds ago   Up 4 seconds   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   sharp_mendeleev
```

- Para parar un contenedor activo (utiliza el campo `NAMES` del `docker ps`:

```bash
docker stop sharp_mendeleev
```

- Para reiniciarlo:

```
docker restart sharp_mendeleev
```

- Para eliminar un contenedor:
```
docker rm sharp_mendeleev
```
