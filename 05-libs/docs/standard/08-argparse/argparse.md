---
title: argparse - Procesar argumentos
---
## Introducción a `argparse`

El módulo **argparse** es la librería oficialmente recomendada para interpretar
los parámetros pasados por línea de comandos.

Existen otros dos módulos en la librería estándar que tienen el mismo objetivo,
una es `getopt`, una versión equivalente a la función `getopt()` del lenguaje
C, y otra la librería ya discontinuada `optparse`.

Conceptos
---------

Unos cuantos conceptos sobre el uso de opciones en entornos de línea de
comandos:

- Normalmente nos interesa que las opciones tengan unos **valores por defecto**
  razonables y que hagan el programa útil incluso sin ningún parámetro. Por
  ejemplo la orden `ls` sin ningún parámetro muestra un listado de
  los ficheros en el directorio actual.

- Algunas opciones son **argumentos posicionales**. Se llaman así porque el
  programa espera identificarlos solo por su posición en la línea de comandos.
  Por ejemplo, la orden `cp` (copiar un fichero) espera dos
  parámetros posicionales, el primero será el fichero origen y el segundo el
  fichero o directorio de destino.

- Hay también **argumentos opcionales**, que modifican o condicionan la forma
  en que el programa hace su trabajo. Estos parámetros opcionales suelen usar
  el carácter `-` como prefijo. Por ejemplo, la orden `ls -l` muestra un
  listado más completo del que mostraría la orden `ls` sola.

- Los argumentos opcionales a veces se pueden especificar de dos maneras, la
  forma abreviada, que vimos antes, usando un solo guión con prefijo y una o
  dos letras a lo sumo, y la forma extendida, que usa dos guiones y normalmente
  una o dos palabras. En muchos casos tenemos la opción abreviada `-h` y la
  opción extendida `--help`, ambas usadas para obtener una descripción del
  uso de un programa y de las opciones que soporta.

### Uso básico

Empezaremos con un breve ejemplo, que prácticamente no hace nada:

```python
{% include 'standard/08-argparse/lab-argparse-01.py' %}
```

Si lo ejecutamos, deberíamos obtener algo parecido a esto:

```shell
$ python prog.py
$ python prog.py --help
usage: prog.py [-h]

optional arguments:
    -h, --help  show this help message and exit
```

Vemos que `argparse` ha definido por nosotros la opción `-h` y `--help`. Pero
si intentamos usar otros parámetros, no definidos, nos indicará el error:

```shell
$ python prog.py --verbose
usage: prog.py [-h]
    prog.py: error: unrecognized arguments: --verbose
$ python prog.py foo
usage: prog.py [-h]
prog.py: error: unrecognized arguments: foo
```

Vemos aquí una de las ventajas de `argparse`; tenemos una pantalla de ayuda sin
necesidad de hacer nada. Veremos más adelante que a medida que añadimos nuevas
opciones, estas aparecerán automáticamente en la página de ayuda.

La opción de ayuda `-h/--help` es la única que incluye `argparse` por su
cuenta, pero si se especifican opciones que no hemos incluido, obtendremos un
mensaje de error bastante claro, también _gratis_.

### Añadir parámetros posicionales

Vamos a añadir un parámetro posicional, que llamaremos `target`:

```python
{% include 'standard/08-argparse/lab-argparse-02.py' %}
```

Si ejecutamos este código, obtenemos algo como:

```shell
$ python lab-argparse-02.py
usage: lab-argparse-02.py [-h] target
lab-argparse-02.py: error: the following arguments are required: target
$
$ python lab-argparse-02.py --help
usage: lab-argparse-02.py [-h] echo

positional arguments:
    target

optional arguments:
    -h, --help  show this help message and exit
$ python lab-argparse-02.py foo
foo
```

Usando el método `add_argument()` hemos especificado que nuestro programa
acepta un parámetro posicional, que en esta ocasión hemos llamado `target`.
Como este nuevo parámetro no tiene un valor por defecto, es obligatorio, por lo
que ejecutar el programa sin él, este fallará y nos informara de que necesita
ese parámetro.

Vamos también que `parse_args()` nos devuelve los datos sobre las opciones que
hemos especificado, es este caso, `target`. EL nombre es el mismo que hemos
usado para definir el parámetro.

Fíjate que el mensaje de ayuda hace referencia al nuevo parámetro, pero
la verdad es que se limita a decir que ese valor es necesario; no dice
para que sirve ni lo que hace. Podemos mejorar esto usando el parámetro
`help` de `add_argument`:


```python
{% include 'standard/08-argparse/lab-argparse-03.py' %}
```

Ahora mejor:

```python
$ python lab-argparse-03.py
usage: lab-argparse-03.py [-h] target
lab-argparse-03.py: error: the following arguments are required: target
$
$ python lab-argparse-03.py --help
usage: lab-argparse-03.py [-h] target

positional arguments:
    target      texto a mostrar en la pantalla

optional arguments:
    -h, --help  show this help message and exit
$
$ python lab-argparse-03.py funciona
funciona
```

**Ejercicio**: Modificar el programa para que haga algo con el texto que le
pasamos; por ejemplo, que lo imprima pero en mayúsculas.

**Solucion**:

```python
{% include 'standard/08-argparse/lab-argparse-04.py' %}
```

Vamos con algo un poco más útil. ¿Qué tal un programa que nos devuelva
el cuadrado del número que la pasamos? Vamos a intentarlo:

```python
{% include 'standard/08-argparse/lab-argparse-05.py' %}
```

Desgraciadamente, no funciona:

```python
Traceback (most recent call last):
File "lab-argparse-05.py", line 8, in <module>
    print(options.num**2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
```

Esto es porque `argparse` nos pasa todos los valores como cadenas de texto.
Podríamos solucionarlo convirtiendo nosotros ese texto a entero, pero hay una
forma mejor; podemos usar el parámetro `type` para indicarle una función
transformadora que nos pase del valor en texto del argumento al tipo de
variable que nosotros queremos. Para esta caso, la función `int` es perfecta:

```python
{% include 'standard/08-argparse/lab-argparse-06.py' %}
```

Ahora, incluso si intentamos pasar un argumento incorrecto, el mensaje
de error será más claro:

```shell
$ python lab-argparse-06.py 22
484
$
$ python lab-argparse-06.py hola
usage: lab-argparse-06.py [-h] num
lab-argparse-06.py: error: argument num: invalid int value: 'hola'
```

### Argumentos opcionales

Vamos a definir un parámetro pocional para que nos muestre, si asi lo pedimos,
los cálculos previos realizado. Es tan sencillo como definirlos con uno o dos
guiones en el nombre.

Como es opcional, no es necesario especificarlo. si no lo hacemos, cuando
intentemos leer su valor, este será `None`.

Cono en nuestro caso el valor lo queremos comparar con un entero, nos viene
mejor definir el valor por defecto con el parámetro `default` para que
valga, digamos$0$:

```python
{% include 'standard/08-argparse/lab-argparse-07.py' %}
```

Veamos si funciona:

```shell
$ python lab-argparse-07.py 1024 --explicacion 1
1024^2 = 1048576
$
$ python lab-argparse-07.py 1024
1048576
```

Una cosa que podemos mejorar es que, para este caso, realmente no
debería ser necesario especificar ningun valor, es mas bien una opción
de tipo lógico, booleano. Podemos modificar esto para que el argumento
`--explicacion` no requiera ningún valor. Para ello usaremos un
parámetro del método `add_argument` llamado `action`:

```python
{% include 'standard/08-argparse/lab-argparse-08.py' %}
```

Veamos si funciona:

```shell
$ python lab-argparse-08.py 782
611524
$ python lab-argparse-08.py 782 --explicacion
782^2 = 611524
```

Vemos que no es necesario especificar ni `type` ni `default`, al usar
`action="store_true"` la librería puede concluir cuales serian estos valores.
Si se especificara `store_false`, seguiría siendo un valor booleano pero por
defecto sería `True`. La opción `--explicacion` es ahora lo que se suele llamar
un *flag*, que puede estar activo o no.

### Opciones abreviadas

Ahra tenemos un valor opcional especificado con un argumento extendido
`--explicacion`. ¿Cómo definimos la opción abreviada, por ejemplo `-e`. Muy
facil, solo hay que indicar las dos opciones como primeros parametros de
`add\_argument`. Para nuestro ejemplo, cambiar la definición a:

```python
parser.add_argument(
    "-e", "--explicacion",
    help="Muestra los pasos previos",
    action='store_true',
    )
```

**Ejercicio**: Añadir la opción abreviada. Probar que funciona.

El módulo `argparse` ofrece muchas más opciones para controlar los argumentos
que acepta nuestro programa. Con el parámetro `choices`, por ejemplo, podemos
limitar los valores posibles de un argumento, podemos hacer opciones que sean
mutualmente excluyentes, etc.

Para aprender más, podemos consultar la [documentación ofical de
argparse](https://docs.python.org/es/3/library/argparse.html).

Miniproyecto: Hacer un script que imprima una tabla de multiplicar, con un
parametro obligatorio para indicar que tabla queremos. Si indicamos el
parametro opcional `--examen`, en vez de imprimir los resultados, que deje un
espacio vacio.

Es decir, si hacemos:

```shell
python tabla.py 7
```

La salida deberia ser algo como:

```shell
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

Pero si usamos la opción:

```shell
python tabla.py 7 --examen
```

La salida debería parecerse a:

```python
7 x 1 = [    ]
7 x 2 = [    ]
7 x 3 = [    ]
7 x 4 = [    ]
7 x 5 = [    ]
7 x 6 = [    ]
7 x 7 = [    ]
7 x 8 = [    ]
7 x 9 = [    ]
7 x 10 = [    ]
```

Un punto extra si se usa la opcion `choices` para evitar que se puedan imprimir
tablas que no sean las del $1$ al $9$.
