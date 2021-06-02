---
title: Anexo 1 - Miniproyecto Librerías
---

Si realizas este miniproyecto, vale también para la parte web. Es decir, que 
para estos dos módulos solo necesitas un único proyecto.

### Programa de copia de seguridad

Implementar un programa de línea de comandos, llamado `weeko.py`, para realizar
una copia de seguridad semanal de los archivos que hay en una carpeta que se le
indicará al programa.

El programa aceptará un parámetro obligatorio -la ruta de la carpeta 
a copiar- y otros dos parámetros opcionales:

- `--exclude`: lista de extensiones que no se deben incluir en la copia de
seguridad. Por ejemplo podría ser: `weeko.py ejemplos/ --exclude="pyc,tmp"`. Esto
debería descartar cualquier fichero con las extensiones `.pyc` y `.tmp`.

- `--verbose`: Además de realizar la copia, imprime por pantalla los nombres
   y valores MD5 de todos los ficheros a medida que los copia.

Nota: Puedes usar
[`arpgarse`](https://docs.python.org/3/library/argparse.html)
o [`fire`](https://google.github.io/python-fire/guide/) para interpretar la
línea de ordenes, o cualquier otra que prefieres, como
[`click`](https://palletsprojects.com/p/click/) o
[`docopt`](http://docopt.org/).

Todos los movimientos de archivo que hagas se deben almacenar en un fichero log
llamado `weeko.log`.

Cuando se ejecute, debe determinar en primer lugar donde se deben guardar los
archivos, en base al día de la semana actual. Si se ejecuta un lunes, las
copias deben guardarse en una carpeta que se llame `lunes/`, si se ejecuta el
sábado, en la carpeta `sabado/` (no hacen falta acentos en los nombres de las
carpetas). Recuerda que los objetos de clase
[`datetime.date`](https://docs.python.org/es/3/library/datetime.html) tienen un
método `weekday()` que devuelve un entero para cada día de la semana, siendo el
`0` el lunes y `6` el domingo.

Puedes usar el módulo
[`shutils`](https://docs.python.org/es/3/library/shutil.html) para realizar la
copia, tiene una función, `copyfile` que es más que suficiente. Solo hay que
pasarle la ruta del fichero de origen y la ruta del fichero de destino.

En _pseudocódigo_, el programa haría lo siguiente:

- leer las opciones de la línea de comando.

- calcular que día es hoy y, por tanto, la carpeta a usar como destino
  de las copias. Si no existe la carpeta, crearla.

- leer los contenidos del directorio origen, el que tenemos como
  parámetro obligatorio. Recuerda que la función 
  [`os.listdir(path)`](https://docs.python.org/3/library/os.html#os.listdir)
  te devuelve una lista de cadenas de texto con los nombres de los ficheros
  que hay en ese directorio.

- para cada fichero de ese directorio, siempre y cuando la extensión no esté en
  la lista de ficheros excluidos:

    - Calcular el MD5 del fichero de origen.

    - Si se ha especificado el parámetro `--verbose`, mostrar por pantalla
      tanto el código hash MD5 como el nombre del fichero

    - Copiar el fichero del directorio de origen al de destino.

    - Guardar registro de cada operación en el fichero log. Por ejemplo, `Copia
      de ejemplo/sources.py (MD5 f1e069787ece74531d112559945c6871) a la
      carpeta lunes`.


### Rúbrica de evaluación

- Si ejecuto el programa sin el parámetro obligatorio, me lo indica con un
  mensaje de error y me muestra las opciones como si lo hubiera llamado con 
  `--help`: 5%

- El programa acepta todos los parámetros esperados, y los muestra si lo llamo
  con la opción `--help`: 15%

- El programa crea la carpeta donde guarda las copias, según corresponda al día
  de la semana en que estemos. Es decir, si lo ejecuto un miércoles y no
  existe la carpeta `miercoles`, el programa crea dicha carpeta: 15%

- El programa escribe en un fichero log cada operación de copia que hace: 10%

- El programa realiza la copia de los ficheros desde la carpeta indicada a
  la carpeta de la copia de seguridad: 25%

- Ademas de realizar la copia, excluye los ficheros que se la han 
  indicado con la opción `--exclude`: 10%

- La opción `--verbose` funciona y muestra los MD5 correctos: 10%

- Cualquier mejora adicional que quieras realizar: 10%

Ejemplos de mejora:

 - Usar [colorama](https://pypi.org/project/colorama/) para mostrar la salida
   del programa con colores.

 - Usar [tqdm](https://pypi.org/project/tqdm/) para presentar una barra animada
   que indique el progreso de la copia.

 - Usar [zipfile](https://docs.python.org/3/library/zipfile.html) para que las
   copias se guarden en ficheros .zip, en vez de en directorios. Por ejemplo
   si ejecuto el programa un jueves, debe crear un archivo `jueves.zip` con los
   archivos de la copia.

 - Usar [playsound](https://pypi.org/project/playsound/) para tocar una
   fanfarria cuando el programa termina de efectuar las copias.

 - Añadir una opción de línea de comando, no obligatoria, `--logfile <ruta>`
   para poder definir la ruta del fichero log. Si no se especifica debería
   ser `weeko.log`.
    
Coméntame si tienes una idea de mejora para ver si es aceptable. Casi seguro
que te diré que si, siempre y cuando uses alguna librería, tanto si la
hemos visto como si no.
