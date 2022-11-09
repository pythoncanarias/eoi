---
title: Optimizar el rendimiento de Django
tags:
    - web
    - performance
    - django
---

## Mejorar el rendimiento de Django

La primera regla a la hora de optimizar es:

> La optimización prematura es la raíz de todo mal<br> 
> -- [Donald knuth](https://es.wikipedia.org/wiki/Donald_Knuth)

Creo que mucha gente prefiere entenderla como: "No optimices", y no es
eso. La cita completa de Knuth es:

> Programmers waste enormous amounts of time thinking about, or worrying
> about, the speed of noncritical parts of their programs, and these
> attempts at efficiency actually have a strong negative impact when
> debugging and maintenance are considered. We should forget about small
> efficiencies, say about 97% of the time: **premature optimization is
> the root of all evil**. Yet we should not pass up our opportunities in
> that critical 3%.

Ddesde mi punto de vista: No optimices hasta que tengas código
operativo. En ese momento, mide tu rendimiento para ver clase de mejoras
se pueden obtener. Si complicas todo el programa para obtener, por
ejemplo, una mejora del 0.3%, lo único que has conseguido es perder el
tiempo.

Un par de consideraciones más:

- Esto no es una excusa para programar mal.

- Si puedes optimizar algo con poco esfuerzo, en menos de 5 minutos,
  y sin impacto en el resto del código, ve a por ello. Si no,
  déjalo.

- Elige métricas objetivas, verificables y repetibles. Cuando las
  tengas, ponte a optimizar.

Dicho esto, vamos a ver como podemos sacarle un poco más de jugo a
nuestro Django.

## Usar conexiones persistentes

Desde Django 1.6 podemos indicarle a Django que la conexión a la base de
datos puede ser persistente, es decir, que podemos reutilizar una
conexión para servir varias peticiones. Si no le decimos nada, usará el
sistema **no** persistente, y hará una nueva conexión en cada solicitud.
El tiempo de establecer una conexión no es demasiado grande (entre 20 y
80 ms) y depende del gestor de base de datos que usemos, pero es una
optimización muy sencilla y no compromete nuestro código.

Para indicar que la conexión a la base de datos sea persistente hay que
añadir la entrada `CONN_MAX_AGE` al diccionario `DATABASES`, en el
fichero `settings.py`. El valor es el número de segundos durante los
cuales se podrá reutilizar la conexión. Por ejemplo:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'CONN_MAX_AGE': 900,
    }
}
```

Establece un tiempo máximo de 15 minutos (900 segundos), tras eso, la conexión
se descarta y se solicita una nueva. No es conveniente reutilizar durante
demasiado tiempo la conexión, por si hubiera problemas de fugas de memoria o
conexiones bloqueadas. Lo normal es entre 5 y 20 minutos. Se pueden usar
valores más grandes, pero probablemente no tendrán demasiado impacto en el
rendimiento.


## Cachear la carga de plantillas

Los cargadores de plantillas que usa Django por defecto buscan y cargan siempre
las plantillas. Esto suele ser conveniente, porque de esta forma los cambios en
las plantillas se reflejan inmediatamente, sin necesidad de tener que parar y
arrancar el servidor web.

Pero si vemos que la carga de las plantillas está dilatando el tiempo de
respuesta, podemos activar el cacheo de plantillas, de forma que estas se
mantienen en memoria una vez se cargan. Para ello usamos un cargador especial:
`django.template.loaders.cached.Loader`. Un fichero `settings.py` tiene
normalmente algo así:

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Por defecto (al no especificar nada) esto establece dos cargadores de
plantillas: `filesystem.Loader` y `app_directories.Loader`, ambos definidos en
`django.template.loaders`. Queremos eso mismo pero _cacheando_ las plantillas,
por lo que usaremos `django.template.loaders.cached.Loader`. La entrada
`TEMPLATES` quedaría así:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

El inconveniente, como señalamos antes, es que los cambios en las plantillas no
se verán reflejados hasta que se reinicie el servidor.  Obviamente, este tipo
de rendimiento debe aplicarse solo en el servidor, en desarrollo es totalmente
desaconsejado.

En general el sistema de plantillas es bastante rápido. Usa esta
optimización solo si, por la razón que sea, estás perdiendo mucho tiempo
en la carga de plantillas. Mejor aún, investiga por qué tarda tanto la
carga de las plantillas, que puede ser el auténtico problema.


## Optimizar la carga de las sesiones

Por defecto, las sesiones se almacenan en la propia base de datos. Esto implica
que, para cada petición hecha por un usuario registrado, habrá varias consultas
a la base de datos: como mínimo una para obtener la sesión, y luego otra para
obtener los datos del usuario. Se puede configurar Django para que las sesiones
se almacenen en sistemas más rápidos, como [Memcached](http://memcached.org/) o
[Redis](http://redis.io/).

Para ello, tenemos que configurar nuestro sistema de caches. Primero es
necesario, claro está, tener un sistema _Memcached_ o _Redis_ configurado y
en funcionamiento. Una vez hecho esto, se especifican los detalles en la
entrada `CACHES` del fichero `settings.py`. Para usar _Memcached_, por
ejemplo, podría ser algo así:

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
```

Para usar _Redis_, de forma similar:

```python
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '/var/run/redis/redis.sock',
    },
}
```

Los parámetros dependen, claro, de la forma que hayamos configurado
_Redis_ o _memcached_.

Podemos aprender más cosas sobre el sistema de Caches de Django en la
documentación de Django: [Django's cache framework](https://docs.djangoproject.com/en/1.8/topics/cache/). 

Para configurar Redis como cache en Django, podemos consultar [Using Redis as
Django's session store and cache backend](http://michal.karzynski.pl/blog/2013/07/14/using-redis-as-django-session-store-and-cache-backend/)

Una vez configurada la cache, definimos en el fichero `settings.py` la
entrada `SESSION_ENGINE`, para indicarle que debe usar el sistema de
_cachés_ previamente definido:

```
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
```

Instalar un sistema como _Redis_ o _Memcached_ es el primer paso que
deberías dar si estás interesado en mejorar el rendimiento.


## Usar joins en las consultas (El problema de las N+1 consultas)

Cuando accedemos a una instancia de un modelo, Django usa un sistema
[Lazy Loading](https://es.wikipedia.org/wiki/Lazy_loading) o de carga
diferida para acceder a los modelos relacionados. Eso es normalmente
bueno para el rendimiento. Por ejemplo, podemos obtener un modelo de
Tarea con:

```python
> task = models.Task.objects.get(pk=1)
```

Esto carga solo los datos del modelo. Si ahora pretendemos acceder al
proyecto al que pertenece la tarea, Django realiza **justo en ese
momento** una segunda consulta para obtenerlo. Es generalmente un
comportamiento deseable: Si nunca llegamos a preguntar por el proyecto, la
segunda consulta no se ejecuta nunca. Pero a veces sabemos con
seguridad que vamos a necesitar esos datos relacionados.

A modo de ejemplo, supongamos que queremos un listado de tareas que
incluya el nombre del proyecto al que pertenecen. El siguiente código
funciona:

En la vista:

```python
{% raw %}
tasks = models.Task.objects.all()
{% endraw %}
```

En la plantilla:

```html
{% raw %}
{% for task in tasks %}
    <p>{{ task.name }} - {{ task.project|default:"Ninguno" }}
{% endfor %}
{% endraw %}
```

Esto funciona, pero hace **muchas más peticiones de las estrictamente necesarias**; si
hubiera, digamos, **100** tareas en la base de datos. hará **101**
consultas: una para el listado de tareas, y una para cada vez que accede
al atributo `project` del mismo.

En vez de eso, podemos pedirle al _ORM_ de Django que se prepare por
adelantado y realice la consulta de tareas haciendo un
[Join](https://es.wikipedia.org/Join) a nivel de base de datos, de forma
que se incluya los datos del proyecto. De ese modo, el tributo `project` será
un objeto directamente accesible. Esto reduce el número de consultas en
nuestro ejemplo de **101 a 1**.

Para ello es para lo que sirve el método `select_related`. El código de
la vista se modifica a:

```python
tasks = models.Task.objects.select_related('project').all()
```

Tocamos una única línea de código, y reducimos de forma drástica el
número de consultas a la base de datos. Este es el tipo de
optimizaciones que pertenecen al 3% que hablaba Knuth.

El método `prefetch_related` es lo mismo, pero para relaciones
`ManyToManyField`. La mejora del rendimiento puede ser muy bueno si
tenemos pocas entradas en la tabla intermedia para los registros en la
tabla del modelo, si la tabla del modelo es enorme. En el resto de los
casos no suele resultar tan útil como `select_related`, y por lo tanto
se usa menos.

Nota: ¿Cómo podemos estar seguros de que estas optimizaciones están
funcionando? La única forma es midiendo los tiempos de respuestas; una
opción muy buena es
[django-toolbar](https://django-debug-toolbar.readthedocs.org/en/1.3/).


## Cachear llamadas a métodos

Como vimos en la sección anterior, cuando obtenemos un objeto desde la
base de datos, si el objeto tiene un atributo que a su vez es otro
objeto -La típica _ForeignKey_-, este se carga de forma automática cuando
es accedido. Eso significa que podemos usar el atributo cuantas veces
queramos, que solo se realiza la consulta la primera vez:

```python
task = models.Task.objects.get(pk=1)
task.project  # Accede a la base de datos
task.project  # NO accede a la base de datos. está cacheado
```

Pero esto no ocurre así, en general, para las llamadas a métodos:

```python
project = models.Project.objects.get(pk=1)
project.task_set.all()  # Se consulta la base de datos
project.task_set.all()  # Se consulta la base de datos otra vez
```

Hay que tener especial cuidado con esto en las plantillas. Aunque usemos
un método como `all`, sin paréntesis, sigue siendo una llamada a un
método y, por tanto, no se cacheará. Como antes, el uso de
_django-toolbar_ es de un valor incalculable para depurar estos fallos.
Podemos resolver esto en la plantillas usando la etiqueta `with`.

Para nuestros propios métodos, podemos implementar a mano el cacheo de
los resultados o puede ser más cómodo usar simplemente el decorador
`cached_property`, que permite acceder a nuestro método como si fuera un
atributo cacheado.


## Obtener solo los datos necesarios (A.K.A. Proyectar)

A veces solo necesitas consultar determinados atributos de un objeto que
obtienes de la base de datos, pero el modelo tiene muchos atributos más,
incluso puede que algunos de ellos sean bastante grandes (`FextField` o
`FileField`, por ejemplo). La consulta normal te trae todos los campos, lo que
puede hacer que la consulta tarde más, solo para traernos datos que no vamos a
utilizar.

Podemos especificar que solo queremos cargar determinados campos usando el
método `only`. El resto de los atributos no se cargan pero siguen estando
disponibles si se solicitan, usando *lazy loading*.

Por ejemplo, un listado donde solo muestro el nombre de la tarea y su
prioridad, se puede resolver con:

```python
tasks = models.Task.objects.all()
```

Pero podemos proyectar solo las columnas que nos interesan y esto hace
que la transferencia de datos se optimice:

```python
tasks = models.Task.objects.only('name', 'priority').all()
```

## Enlaces interesantes

-[Performance and optimization | Django documentation](https://docs.djangoproject.com/en/4.1/topics/performance/)

- [Databases | Django documentation | Django](https://docs.djangoproject.com/en/4.1/ref/databases/)

- [An optimization story with Django &#8211; one thousand times faster! | Mozilla Web Development](https://blog.mozilla.org/webdev/2011/12/15/django-optimization-story-thousand-times-faster/)

- [Some quick Django optimisation lessons - lukeplant.me.uk](http://lukeplant.me.uk/blog/posts/some-quick-django-optimisation-lessons/)

- [Django: optimizing queries - Stack Overflow](http://stackoverflow.com/questions/4568086/django-optimizing-queries)

- [Django Performance: 4 Simple Things](http://www.revsys.com/blog/2015/may/06/django-performance-simple-things/)


