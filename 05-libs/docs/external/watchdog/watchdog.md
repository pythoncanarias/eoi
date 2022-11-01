---
title: "Watchdog - Monitorizar cambios en el sistema de ficheros"
---

### Contenido y objetivos del módulo Watchdog

**Watchdog** es una librería y un conjunto de utilidades para monitorizar
eventos del sistema de ficheros.

### Instalar watchdog

Se puede instalar con `pip`:

```shell
pip install watchdog
```

### Monitorizar el sistema de ficheros

Con esta librería podemos establecer un programa que monitorice o vigile
(de ahí lo de *watchdog*) una parte del sistema de archivos. Cuando
ocurra algún evento en este sistema, como que se cree un archivo o un
directorio, se renombre un fichero, etc. se nos notifica para que
actuemos en consecuencia.

Por ejemplo, podríamos poner la configuración de un _router_ en un
directorio, y monitorizar con `watchdog` el mismo. Si se salva una nueva
versión del fichero de configuración, podríamos leer la nueva configuración,
chequear que no hay errores, enviársela al _router_ y reiniciarlo.

Vamos a ver un ejemplo:

```python
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
```

Creamos un manejador de eventos, que es el objeto que va a recibir las
notificaciones del sistema de ficheros y actuará en consecuencia, con
la clase `PatternMatchingEventHandler`. Al crear el objeto podemos
decirle en que clase de eventos estamos interesados. En este caso estamos
interesados en todos.

```python
patterns = "*"
ignore_patterns = ""
ignore_directories = False
case_sensitive = True

my_event_handler = PatternMatchingEventHandler(
    patterns,
    ignore_patterns,
    ignore_directories,
    case_sensitive
)
```

Ahora que hemos creado el manejador o _handler_, podemos escribir el código a
ejecutar cuando se produzcan los eventos.

Vamos a definir uno para cuando se crea un fichero:

```python3
def on_created(event):
    print(f"hay un nuevo fichero: {event.src_path}")
```

Ahora asignamos el evento a esta función:

```python
my_event_handler.on_created = on_created
```

Aun necesitamos otro objeto, conocido como el observador (_Observer_),
que será el que monitorice el sistema de ficheros.

Vamos a crearlo:

```python3
path = "."

my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=True)
```

Ya hemos creado el observador, y le hemos pasado nuestro manejador de
eventos. Lo hemos puesto vigilando el directorio actual (`.`). Indicamos
que estamos interesados también en los subdirectorios con el parámetro
`recursive`.

Ahora ya podemos iniciar el observador. Este proceso inicia un ciclo
infinito, ya que la condición de salida del `while` es la constante
`True`, que obviamente nunca va a cambiar de valor. La única manera
de salir de ese bucle infinito es provocando una interrupción en el nivel
superior del sistema operativo, con la combinación ++ctrl+c++.

```python
my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
```

Ahora podemos abrir otra terminal, y crear un archivo desde el sistema
operativo. Con Linux/Mac, lo mas fácil es usar el comando `touch`:

```shell
touch hola.txt
```

Para Windows una forma podria ser:

```shell
fsutil file createnew hola.txt 0
```

En la primera terminal, la que está ejecutando nuestro código `watchdog`,
deberíamos ver el mensaje indicando la creación del fichero.
