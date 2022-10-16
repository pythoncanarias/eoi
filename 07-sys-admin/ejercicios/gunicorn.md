### Instalar Gunicorn
```
pip install gunicorn
```

# Ejercicio 1: Flask con Gunicorn

https://www.digitalocean.com/community/tutorials/como-preparar-aplicaciones-de-flask-con-gunicorn-y-nginx-en-ubuntu-18-04-es

1. Creamos una carpeta para el proyecto Flask

```
mkdir ~/my-flask-project
cd ~/my-flask-project
```

2. Creamos un entorno virtual para almacenar los requisitos de Python de nuestro proyecto de Flask escribiendo lo siguiente:

```
python3 -m venv .venv
```

3. Activamos el entorno virtual:
    
```
source .venv/bin/activate
```

4. Instalamos las dependencias para el proyecto:

```
pip install wheel gunicorn flask
```

5. Vamos a crear una aplicacion Flask muy simple, en un solo fichero llamado `myproject.py`

```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
```

6. Probamos que la aplicación Flask funciona:
```
python myproject.py
```

En tu navegador accede a la url `http://localhost:5000/` y deberíamos ver algo como esto:


<h1 style='color:blue'>Hello There!</h1>

## Ejecutando la aplicación con Gunicorn

7. A continuación, crearemos un archivo llamado `wsgi.py` que servirá como punto de entrada para nuestra aplicación, y que indicará a Gunicorn cómo interactuar con ella:

```
from myproject import app

if __name__ == "__main__":
    app.run()
```

8. A partir de este momento, podemos probar la integración con Gunicorn de la siguiente forma:  
```
gunicorn --bind 0.0.0.0:5000 wsgi:app
```  
Deberíamos ver un resultado similar a esto:  
```
Output
[2018-07-13 19:35:13 +0000] [28217] [INFO] Starting gunicorn 19.9.0
[2018-07-13 19:35:13 +0000] [28217] [INFO] Listening at: http://0.0.0.0:5000 (28217)
[2018-07-13 19:35:13 +0000] [28217] [INFO] Using worker: sync
[2018-07-13 19:35:13 +0000] [28220] [INFO] Booting worker with pid: 28220
```  
Después de esto, para la aplicación con `ctrl + c`

## Ejecutando la aplicación como servicio

9. A continuación, crearemos el archivo de unidad de servicio systemd.  
Crear un archivo de unidad systemd permitirá que el sistema init de Ubuntu inicie automáticamente Gunicorn y haga funcionar la aplicación de Flask cuando el servidor se cargue.  
Creamos un archivo de unidad terminado en `.service` dentro del directorio `/etc/systemd/system`:  
```
sudo nano /etc/systemd/system/myproject.service
```  
El contenido del fichero `/etc/systemd/system/myproject.service` será el siguiente:

```
[Unit]
Description=Gunicorn instance to serve myproject
After=network.target
  
[Service]
User=vagrant
Group=www-data
WorkingDirectory=/home/vagrant/my-flask-project
Environment="PATH=/home/vagrant/my-flask-project/.venv/bin"
ExecStart=/home/vagrant/my-flask-project/.venv/bin/gunicorn --workers 3 --bind --bind 0.0.0.0:5000 -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```

- La sección `[Unit]` se usa para especificar metadatos y dependencias. Aquí agregaremos una descripción de nuestro servicio e indicaremos al sistema init que lo inicie solo tras haber alcanzado el objetivo de red
- La sección `[Service]` especificará el usuario y el grupo con los cuales deseamos que se ejecute el proceso. Otorgaremos la propiedad del proceso a nuestra cuenta de usuario normal, ya que tiene la propiedad de todos los archivos pertinentes. También otorgaremos la propiedad del grupo al grupo www-data para que Nginx pueda comunicarse fácilmente con los procesos de Gunicorn.  
A continuación, planearemos los detalles del directorio de trabajo y estableceremos el entorno variable PATH para que el sistema init sepa que los ejecutables para el proceso están ubicados dentro de nuestro entorno virtual. También especificaremos el comando para iniciar el servicio. Este comando hará lo siguiente:  
    - Iniciar 3 procesos de trabajadores (debería, no obstante, ajustar esto si es necesario)
    - Especifique el nombre del archivo del punto de entrada de WSGI junto con el elemento invocable de Python dentro de ese archivo (wsgi:app).
- La sección `[Install]` indicará a systemd a qué deberá vincular este servicio si lo habilitamos para que se cargue en el inicio (queremos que este servicio se inicie cuando el sistema multiusuario normal esté en funcionamiento)

10. Iniciamos el servicio Gunicorn que hemos creado y lo activamos para que se cargue en el inicio:
```
sudo systemctl start myproject
sudo systemctl enable myproject
```

11. Comprobamos el estado:  
```
sudo systemctl status myproject
```  
Deberíamos ver algo como esto:
```
$ sudo systemctl status myproject                                                                                                                                                                                           ● myproject.service - Gunicorn instance to serve myproject                                                                                                                                                                                        Loaded: loaded (/etc/systemd/system/myproject.service; enabled; vendor preset: enabled)                                                                                                                                                      Active: active (running) since Sun 2021-04-25 22:00:35 UTC; 37s ago                                                                                                                                                                        Main PID: 1294 (gunicorn)                                                                                                                                                                                                                       Tasks: 4 (limit: 1112)                                                                                                                                                                                                                      Memory: 51.1M                                                                                                                                                                                                                                CGroup: /system.slice/myproject.service                                                                                                                                                                                                              ├─1294 /home/vagrant/my-flask-project/.venv/bin/python3 /home/vagrant/my-flask-project/.venv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app                                                                             ├─1307 /home/vagrant/my-flask-project/.venv/bin/python3 /home/vagrant/my-flask-project/.venv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app                                                                             ├─1308 /home/vagrant/my-flask-project/.venv/bin/python3 /home/vagrant/my-flask-project/.venv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app                                                                             └─1309 /home/vagrant/my-flask-project/.venv/bin/python3 /home/vagrant/my-flask-project/.venv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app                                                                                                                                                                                                                                                                                                             Apr 25 22:00:35 vagrant systemd[1]: Started Gunicorn instance to serve myproject.                                                                                                                                                            Apr 25 22:00:35 vagrant gunicorn[1294]: [2021-04-25 22:00:35 +0000] [1294] [INFO] Starting gunicorn 20.1.0                                                                                                                                   Apr 25 22:00:35 vagrant gunicorn[1294]: [2021-04-25 22:00:35 +0000] [1294] [INFO] Listening at: unix:myproject.sock (1294)                                                                                                                   Apr 25 22:00:35 vagrant gunicorn[1294]: [2021-04-25 22:00:35 +0000] [1294] [INFO] Using worker: sync                                                                                                                                         Apr 25 22:00:35 vagrant gunicorn[1307]: [2021-04-25 22:00:35 +0000] [1307] [INFO] Booting worker with pid: 1307                                                                                                                              Apr 25 22:00:35 vagrant gunicorn[1308]: [2021-04-25 22:00:35 +0000] [1308] [INFO] Booting worker with pid: 1308                                                                                                                              Apr 25 22:00:35 vagrant gunicorn[1309]: [2021-04-25 22:00:35 +0000] [1309] [INFO] Booting worker with pid: 1309                                                                                                                              Apr 25 22:00:48 vagrant systemd[1]: myproject.service: Current command vanished from the unit file, execution of the command list won't be resumed.  
```

# Ejercicio 2: Django con Gunicorn
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/gunicorn/
