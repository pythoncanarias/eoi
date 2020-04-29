Para poder trabajar con Django, debemos de hacerlo fuera de Jupyter.
Trabajaremos desde la consola y desde un edior de textos. El primer
paso es abrir la consola en el directorio de trabajo que queremos
y comprobar que tenemos la version de Python correcta instalada
y disponible

Ejecutemos desde la terminal:

    python -V

o

    python3 -V

En el resto de la documentacion, solo ejecutaré `python` y `pip`, sin el 3 después. Si
lo tienes instalado como `python3` o `pip3` haz el cambio mentalmente.

Para verificar que Django está instalado haremos

    python -c "import django"

De nuevo, la ausencia de mensajes de error es buena noticia. Si diera un
error, instalar django como pip:

    pip install django


Ahora, el siguiente paso será crear nuestra aplicación. Django, al instalarse, he añadido 
una utilidad muy cómoda que permite crear una aplicación mínima al toque.
Podemos ejecutar esta utilidad haciendo:

    django-admin

Si todo ha ido bien, deberíamos ver un resultado como este, en el que la
utilidad nos señala amablemente que no le hemos indicado ninguna acción a
ejecutar, y a continuacón, lista las acciones que podemos ejecutar:

    $ django-admin

    Type 'django-admin help <subcommand>' for help on a specific subcommand.

    Available subcommands:

    [django]
        check
        compilemessages
        createcachetable
        dbshell
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
        makemigrations
        migrate
        runserver
        sendtestemail
        shell
        showmigrations
        sqlflush
        sqlmigrate
        sqlsequencereset
        squashmigrations
        startapp
        startproject
        test
        testserver





De todas esas acciones que podemos hacer, la que nos interesa ahora mismo
es `startproject`. Esta acción es la que crea una aplicación básica, o como
se dice a veces, el *esqueleto* de una aplicación.

Antes de ejecutar la acción, tenemos que pensar el nombre de la misma, ya que 
va a crear un directorio con ese mismo nombre. En este curso vamos a crear
varias aplicaciones diferentes, asi que esta la vamos a crear con el nombre
`hola`. 

Para crear la aplicación, por tanto, ejecutamos:

    django-admin startprojec hola

Como es habitual, la falta de mensajes de error es indocativo de que todo ha ido
bien. El resultado de la ejecución es que se ha creado una carpeta nueva 
con el nombre de la aplicacion, 'hola' en este caso (habria dado un error si
ya existiera una carpeta con ese nombre; esto es así para evitar destruir un
proyecto ya existente por descuido.

**Ejercicio**: Intentar crear nuevamente la aplicación `hola`. Describir lo que
pasa.

### Examinado la aplicacion `hola`

Vamos a ver los contenidos que 


