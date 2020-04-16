La librería csv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El formato de fichero llamado :term:CSV (*Comma Separated Values* o
Valores separados por comas) es uno de los más habitualmente usados
para el intercambio de información de hojas de cálculo o bases de
datos. A pesar de eso, no hay ningún estandar ni norma escrita, así
que el formato esta definido de forma más o menosinformal por
el conjunto de aplicaciones que pueden leerlo o escribirlo.

Esta carencia de estandares provoca que haya multiples, variadas y
pequeñas diferencias entre los datos producidos o consumidos por
diferentes aplicaciones. Por esta razón, trabajar con distinto
ficheros CVS provinientes de distintas fuentes suele dar más de un
dolor de cabeza. A pesar de estas divergencias (empezando por que
caracter usar como separador de campos), es posible escribir un módulo
que pueda maniputar de forma eficiente estos datos, ocultado al
programador los detalles específicos de leer o escribir estos
ficheros,

El módulo csv permite escribir y leer estos archivos. El programador
puede especificar, por ejemplo, "escribe este archivo en el formato
preferido por excel", o "lee este fichero como fuera de excel, pero
usando el carácter `:` como separador de campos". También nos
permite definir nuestros propios formatos de uso particular, que el
módulo denomina "dialectos".

Las funciones `reader()` y `writer()` leen y escriben secuencias.

Un ejemplo sencillo de lectura:

    import csv
    with open('some.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print row

Y uno de escritura:

    import csv
    datos = [
        ('Leonardo', 'Azul', 1452),
        ('Raphael', 'Rojo', 1483),
        ('Michelangelo', 'Naranja', 1475),
        ('Donatello', 'Violeta', 1386),
        ]
    with open('some.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(datos)

