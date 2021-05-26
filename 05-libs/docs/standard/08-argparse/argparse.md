`argparse`: Procesar argumentos
===============================

El módulo **argparse** es la librería oficialmente recomendada para
interpretar los parámetros pasados por linea de comandos.

Existen otros dos módulos en la librería estándar que tienen el mismo
objetivo, una es [getopt]{.title-ref}, una versión equivalente a la
función [getopt()]{.title-ref} del lenguaje C, y otra la librería ya
discontinuada [optparse]{.title-ref}.

Conceptos
---------

Unos cuantos conceptos sobre el uso de opciones en entornos de línea de
comandos.

-   normalmente nos interesa que las opciones tengan unos **valores por
    defecto** razonables y que hagan el programa útil incluso sin ningún
    parámetro. Por ejemplo la orden [ls]{.title-ref} sin ningún
    parámetro muestra un listado de los ficheros en el directorio
    actual.
-   Algunas opciones son **argumentos posicionales**. Se llaman así
    porque el programa espera identificarlos solo por su posición en la
    línea de comandos. Por ejemplo, la orden [cp]{.title-ref} (copiar un
    fichero) espera dos parámetros posicionales, el primero será el
    fichero origen y el segundo el fichero o directorio de destino.
-   Hay también **argumentos opcionales**, que modifican o condicionan
    la forma en que el programa hace su trabajo. Estos parámetros
    opcionales suelen usar el carácter [-]{.title-ref} como prefijo. Por
    ejemplo, la orden [ls -l]{.title-ref} muestra un listado más
    completo del que mostraría la orden [ls]{.title-ref} sola.
-   Los argumentos opcionales a veces se pueden especificar de dos
    maneras, la forma abreviada, que vimos antes, usa un solo guion con
    prefijo y una o dos letras a lo sumo, y la forma extendida, que usa
    dos guiones y normalmente una o dos palabras. En muchos casos
    tenemos la opción abreviada [-h]{.title-ref} y la opción extendida
    [\--help]{.title-ref}, ambas usadas para obtener una descripción de
    que hace un programa y que opciones tiene.

Uso básico
----------

Empezaremos con un breve ejemplo, que prácticamente no hace nada:

    import argparse
    parser = argparse.ArgumentParser()
    parser.parse_args()

Nota: No podemos ejecutar este programa dentro de Jupyter, porque ya
estamos dentro de un programa. Hay que ejecutar este código desde una
consola.

Si lo ejecutamos, deberíamos obtener algo parecido a esto:

    $ python prog.py
    $ python prog.py --help
    usage: prog.py [-h]

    optional arguments:
      -h, --help  show this help message and exit

Vemos que [argparse]{.title-ref} ha definido por nosotros la opción
[-h/\--help]{.title-ref}. Pero Si intentamos usar otros parámetros, no
definidos, [argparse]{.title-ref} nos indicará el error:

    $ python prog.py --verbose
    usage: prog.py [-h]
        prog.py: error: unrecognized arguments: --verbose
    $ python prog.py foo
    usage: prog.py [-h]
    prog.py: error: unrecognized arguments: foo

Vemos aquí una de las ventajas de [argparse]{.title-ref}; tenemos una
pantalla de ayuda sin necesidad de hacer nada. Veremos mas adelante que
a medida que añadimos más opciones, estas aparecerán automáticamente en
la página de ayuda.

La opción de ayuda [-h/\--help]{.title-ref} es la única que incluye
[argparse]{.title-ref} por su cuenta, pero si se especifican opciones
que no hemos incluido, obtendremos un mensaje de error bastante claro,
también \"gratis\".

Añadir parámetros posicionales
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Vamos a añadir un parámetro posicional, que llamaremos \`target\`:

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    args = parser.parse_args()
    print args.target

Si ejecutamos este código, obtenemos algo como:

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

Usando el método [add\_argument()]{.title-ref} hemos especificado que
nuestro programa acepta un parámetro posicional, que en esta ocasión
hemos llamado [target]{.title-ref}. Como este nuevo parámetro no tiene
un valor por defecto, es obligatorio, por lo que ejecutar el programa
sin él, este fallará y nos informara de que necesita ese parámetro.

Vamos también que [parse\_args()]{.title-ref} nos devuelve los datos
sobre las opciones que hemos especificado, es este caso,
[target]{.title-ref}. EL nombre es el mismo que hemos usado para definir
el parámetro.

Fíjate que el mensaje de ayuda hace referencia al nuevo parámetro, pero
la verdad es que se limita a decir que ese valor es necesario; no dice
para que sirve ni lo que hace. Podemos mejorar esto usando el parámetro
[help]{.title-ref} de \`add\_argument\`:

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="texto a mostrar en la pantalla")
    options = parser.parse_args()
    print(options.target)

Ahora mejor:

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

**Ejercicio**: Modificar el programa para que haga algo con el texto que
le pasamos; por ejemplo, que lo imprima pero en mayúsculas.

**Solucion**:

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="texto a mostrar en la pantalla")
    options = parser.parse_args()
    print(options.target.upper())

Vamos con algo un poco más útil. ¿Qué tal un programa que nos devuelva
el cuadrado del número que la pasamos? Vamos a intentarlo:

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="valor a elevar al cuadrado")
    options = parser.parse_args()
    print(options.target**2)

Desgraciadamente, no funciona:

    Traceback (most recent call last):
    File "lab-argparse-05.py", line 8, in <module>
        print(options.num**2)
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

Esto es porque [argparse]{.title-ref} nos pasa todos los valores como
cadenas de texto. Podríamos solucionarlo convirtiendo nosotros ese texto
a entero, pero hay una forma mejor; podemos usar el parámetro
[type]{.title-ref} para indicarle una función transformadora que nos
pase del valor en texto del argumento al tipo de variable que nosotros
queremos. Para esta caso, la función [int]{.title-ref} es perfecta:

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int, help="valor a elevar al cuadrado")
    options = parser.parse_args()
    print(options.num**2)

Ahora, incluso si intentamos pasar un argumento incorrecto, el mensaje
de error será más claro:

    $ python lab-argparse-06.py 22
    484
    $
    $ python lab-argparse-06.py hola
    usage: lab-argparse-06.py [-h] num
    lab-argparse-06.py: error: argument num: invalid int value: 'hola'

Argumentos opcionales
---------------------

Vamos a definir un parámetro pocional para que nos muestre, si asi lo
pedimos, los cálculos previos realizado. Es tan sencillo como definirlos
con uno o dos guiones en el nombre.

Como es opcional, no es necesario especificarlo. si no lo hacemos,
cuando intentemos leer su valor, este será [None]{.title-ref}.

Cono en nuestro caso el valor lo queremos comparar con un entero, nos
viene mejor definir el valor por defecto como, digamos, \$0\$. Para eso
usamos el parametro \`default\`:

    %file ../examples/lab-argparse-07.py

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int, help="valor a elevar al cuadrado")
    parser.add_argument(
        "--explicacion",
        help="Muestra los pasos previos",
        type=int,7 x 1 = 7
        default=0,
        )
    options = parser.parse_args()

    if options.explicacion > 0:
        print(f"{options.num}^2 = {options.num**2}")
    else:
        print(options.num**2)

Veamos si funciona:

    $ python lab-argparse-07.py 1024 --explicacion 1
    1024^2 = 1048576
    $
    $ python lab-argparse-07.py 1024
    1048576

Una cosa que podemos mejorar es que, para este caso, realmente no
debería ser necesario especificar ningun valor, es mas bien una opción
de tipo lógico, booleano. Podemos modificar esto para que el argumento
`--explicacion` no requiera ningún valor. Para ello usaremos un
parámetro del método `add_argument` llamado `action`:

    %file ../examples/lab-argparse-08.py
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int, help="valor a elevar al cuadrado")
    parser.add_argument(
            "--explicacion",
            help="Muestra los pasos previos",
            action='store_true',
            )

    options = parser.parse_args()
    if options.explicacion:
        print(f"{options.num}^2 = {options.num**2}")
    else:
        print(options.num**2)

Veamos si funciona:

    $ python lab-argparse-08.py 782
    611524
    $ python lab-argparse-08.py 782 --explicacion
    782^2 = 611524

Vemos que no es necesario especificar ni [type]{.title-ref} ni
[default]{.title-ref}, al usar [action=\'store\_true\']{.title-ref} la
librería puede concluir cuales serian estos valores (Si se especificara
[store\_false]{.title-ref}, seguiría siendo un valor booleano pero por
defecto sería [True]{.title-ref}). La opción [explicación]{.title-ref}
es ahora lo que se suele llamar un *flag*, que puede estar activo o no.

### Opciones abreviadas

Ahra tenemos un valor opcional especificado con un argumento extendido
[\--explicaciomn]{.title-ref}. ¿Cómo definimos la opción abreviada, por
ejemplo [-e]{.title-ref}. Muy facil, solo hay que indicar las dos
opciones como primeros parametros de [add\_argument]{.title-ref}. Para
nuestro ejemplo, cambiar la definición a:

    parser.add_argument(
        "-e", "--explicacion",
        help="Muestra los pasos previos",
        action='store_true',
        )

::: {.note}
::: {.admonition-title}
Note
:::

**Ejercicio**: Añadir la opción abreviada. Probar que funciona.
:::

El módulo [argparse]{.title-ref} ofrece muchas más opciones para
controlar los argumentos que acepta nuestro programa. Con el parámetro
[choices]{.title-ref}, por ejemplo, podemos limitar los valores posibles
de un argumento, podemos hacer opciones que sean mutualmente
excluyentes, etc.

Para aprender más, podemos consultar la \[documentación ofical de
[argparse]{.title-ref}\](<https://docs.python.org/2/howto/argparse.html>).

Miniproyecto: Hacer un script que imprima una tabla de multiplicar, con
un parametro obligatorio para indicar que tabla queremos. Si indicamos
el parametro opcional [\--examen]{.title-ref}, en vez de imprimir los
resultados, que deje un espacio vacio.

Es decir, si hacemos [python tabla.py 7]{.title-ref}, la salida deberia
ser algo como:

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

Pero si usamos la opción [python tabla.py 7 \--examen]{.title-ref} la
salida debería parecerse a:

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

Un punto extra si se usa la opcion [choices]{.title-ref} para evitar que
se puedan imprimir tablas que no sean las del \$1\$ al \$9\$.
