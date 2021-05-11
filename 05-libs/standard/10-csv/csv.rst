``csv``: Trabajar con ficheros CSV
==================================

El formato de fichero llamado :term:CSV (*Comma Separated Values* o Valores
separados por comas) es uno de los más habitualmente usados para el intercambio
de información de hojas de cálculo o bases de datos. A pesar de eso, no hay
ningún estandar ni norma escrita, así que el formato esta definido de forma más
o menos informal por el conjunto de aplicaciones que pueden leerlo o
escribirlo.

Esta carencia de estandares provoca que haya multiples, variadas y pequeñas
diferencias entre los datos producidos o consumidos por diferentes
aplicaciones. Por esta razón, trabajar con distinto ficheros CVS provinientes
de distintas fuentes suele dar más de un dolor de cabeza. A pesar de estas
divergencias (empezando por que caracter usar como separador de campos), es
posible escribir un módulo que pueda maniputar de forma eficiente estos datos,
ocultado al programador los detalles específicos de leer o escribir estos
ficheros,

El módulo ``csv`` nos permite escribir y leer estos archivos. El programador
puede especificar, por ejemplo, "escribe este archivo en el formato preferido
por excel", o "lee este fichero como si fuera de excel, pero usando el carácter
`:` como separador de campos". También nos permite definir nuestros propios
formatos de uso particular, que el módulo denomina "dialectos".

Este seria un ejemplo defichero CSV:

.. literalinclude:: ninja-turtles.csv


Las funciones `reader()` y `writer()` son las más usadas de este módulo y sirve
para leer y escriben secuencias en el fichero, respectivamente.

Las dos funciones aceptan como primer argumento un fichero abierto (o algo que
se comporte de forma parecida, esto es, basicamente que tenga un método
``read`` para leer y un método ``write`` para escribir). Si trabajamos con
ficheros, estos deben estar abiertos de la forma adecuada, es decir, ``'r'``
para leer, ``'w'`` o ``'a'`` para escribir.

La función ``reader``
---------------------

Esta función nos devuelve un iterador, que irá devolviendo las distintas líneas
del fichero. Las línea han sido procesadas, de forma que ya todos los problemas
que nos podriamos encontrar están resueltos; los campos están separados, los
campos que vengan entrecomillados has sido procesados y nos llegan como
esperamos, etc.  Un ejemplo sencillo de lectura usando ``reader``::

    import csv
    with open('marvel-wikia-data.csv', 'r') as f:
    with open('marvel-wikia-data.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            print(row)
            if i > 10:
                break
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            print(row)
            if i > 10:
                break


La función ``writer``
---------------------

La funcion ``writer`` se usa de forma similar, aceptando como parámetro
un fichero (o algo similar) abierto para escribir:

Ejemplo de escritura::

    import csv

    datos = [
        ('Leonardo', 'Azul', 1452),
        ('Raphael', 'Rojo', 1483),
        ('Michelangelo', 'Naranja', 1475),
import csv

csv.register_dialect('marvel', delimiter=',', quoting=csv.QUOTE_NONE, escapechar="\\")

filename = "../../files/marvel-wikia-data.csv"
with open(filename, 'r') as f:
    reader = csv.reader(f, dialect="marvel")
    next(reader)  # Ignorar la primera linea
    for i, row in enumerate(reader):
        year = int(row[-1] if row[-1] else 0)
        if 1972 <= year <= 1974:
            print(row[1], year)
        if i == 24:
            break
                    ('Donatello', 'Violeta', 1386),
        ]
    with open('some.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(datos)

**Ejercicio**: Incluir un campo adicional, incluyendo una cuarta columna con 
el arma favorita de cada quelonio. (Pista para los no-tan-friquis: Espadas para
Leonardo, Nunchakus para Michelangelo, bastón Bo para Donatello y Sai para Raphael.

Dialectos
---------

Con los dialectos podemos definir varios factores que pueden cambiar de un
fichero CSV a otro. En el caso del fichero CSV de los personajes marvel,
vemos que no usa ningun delimitar de textos, mientras
que el dialecto por defecto espera comillas dobles: ``"``. Al no usar
delimitadores de texto, necesita alguna ofmra de poder *escapar* el simbolo
usado como separador si estuviera
usado en algun campo de texto. De lo contrario el ``reader`` lo interpretaria
como un salto de columna.

Existe dialectos relaticamente estándar que viene ya definidos en el modulo,
pero en el peor de los casos podemos definir nuestro propio dialecto. Una vez
definido, tenemos que registralo para que tanto la funcion ``reader`` como
``writeer`` sepan de su existencia.


Para el caso de este fichero, podemos definir y registrar el siguiete
dialecto::

    import csv

    csv.register_dialect('marvel', delimiter=',', quoting=csv.QUOTE_NONE, escapechar="\\")

Con este dialecto, el resultado de reader es mucho más limpio::

    import csv

    csv.register_dialect('marvel', delimiter=',', quoting=csv.QUOTE_NONE, escapechar="\\")
    with open('marvel-wikia-data.csv', 'r') as f:
        reader = csv.reader(f, dialect='marvel')
        for i, row in enumerate(reader):
            print(row)
            if i > 10:
                break


**Ejercicio**:  Usar el codigo del ejemplo anterior y listar todos los personajes de marvel creados en la decada de los 70 (De 1971 a 1980)

import csv

csv.register_dialect('marvel', delimiter=',', quoting=csv.QUOTE_NONE, escapechar="\\")
filename = "marvel-wikia-data.csv"
with open(filename, 'r') as f:
    reader = csv.reader(f, dialect="marvel")
    next(reader)  # Ignorar la primera linea
    for i, row in enumerate(reader):
        year = int(row[-1] if row[-1] else 0)
        if 1972 <= year <= 1974:
            print(row[1], year)
        if i == 24:
            break


