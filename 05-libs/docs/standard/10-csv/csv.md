---
title: csv - Trabajar con ficheros CSV
---
## Introdución a `csv`

El formato de fichero llamado **CSV** (*Comma Separated Values* o Valores
separados por comas) es uno de los más usados para el intercambio de
información de hojas de cálculo o bases de datos.

A pesar de eso, no hay ningún estándar ni norma escrita, así que el formato
esta definido de forma más o menos informal por el conjunto de aplicaciones que
pueden leerlo o escribirlo.

![estándares](xkcd-standards.png)

Esta carencia de estándares provoca que haya múltiples, variadas y pequeñas
diferencias entre los datos producidos o consumidos por diferentes
aplicaciones. Por esta razón, trabajar con ficheros CVS de distintas fuentes
suele dar más de un dolor de cabeza. A pesar de estas divergencias (empezando
por que carácter usar como separador de campos), es posible escribir un módulo
que pueda manipular de forma eficiente estos datos, ocultado al programador los
detalles específicos de leer o escribir estos ficheros,

El módulo `csv` nos permite escribir y leer estos archivos. El programador
puede especificar, por ejemplo, "escribe este archivo en el formato preferido",
o "lee este fichero como si fuera de *excel*, pero usando el carácter `:` como
separador de campos". También nos permite definir nuestros propios formatos de
uso particular, que el módulo denomina "dialectos".

Este sería un ejemplo de fichero CSV:

```csv
--8<--
./docs/standard/10-csv/ninja-turtles.csv
--8<--
```

Las funciones `reader()` y `writer()` son las más usadas de este módulo y
sirven para leer y escribir secuencias en el fichero, respectivamente.

Las dos funciones aceptan como primer argumento un fichero abierto (o algo que
se comporte de forma parecida, esto es, básicamente que tenga un método `read`
para leer y un método `write` para escribir). Si trabajamos con ficheros, estos
deben estar abiertos de la forma adecuada, es decir, `'r'` para leer, `'w'` o
`'a'` para escribir, y con la codificación que queramos.

Empezaremos con la función `writer`.

### La función `writer`

La función `writer` acepta como parámetro un fichero (o algo similar) abierto
para escribir, y nos devuelve un objeto de tipo `Writer`, que podremos usar
para escribir los valores que queramos en el fichero.

Podemos indicarles algunas preferencias a la hora de salvar los datos en el
fichero. Por ejemplo, con `delimeter` podemos especificar que carácter usar
para separar los distintos campos.

Podemos especificar muchas otras opciones diferentes (producto de la falta de
un estándar): si se debe añadir o no algún tipo de comillas antes y después de
los textos, el carácter a usar como salto de línea, etc. Pero la librería
sugiere, si hay muchas opciones a configurar, agruparlas todas en una
estructura que han dado en llamar dialecto (*dialect*), que veremos más
adelante.

Por ahora, solo necesitamos saber que la librería viene con varios dialectos ya
predefinidos (Puedes obtener una lista con `csv.list_dialects()`), y que aparte
de estos podemos definir y registrar los que necesitemos, personalizados con
nuestras propias opciones:

Además, el objeto tiene un método `writerow(row)`, al cual le pasamos una
secuencia (normalmente una lista o una tupla) de valores y que el objeto
escribe en el fichero de salida.

Lo que es mejor, tiene también un método `writerows(rows)` al cual le podemos
pasar una lista de tuplas, por ejemplo, para guardar todos los valores que
queremos en una única operación:

Veamos un ejemplo de escritura, que recrea el fichero de ejemplo que vimos
inicialmente:

```python
import csv

datos = [
    ('Leonardo', 'Azul', 1452)1452),
    ('Raphael', 'Rojo', 1483),
    ('Michelangelo', 'Naranja', 1475),
    ('Donatello', 'Violeta', ,
    ]

with open('some.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)1452),
    ('Raphael', 'Rojo', 1483),
    ('Michelangelo', 'Naranja', 1475),
    ('Donatello', 'Violeta', 
    writer.writerows(datos)
```

**Ejercicio**: Incluir un campo adicional, incluyendo una cuarta columna con el
arma favorita de cada quelonio. (Pista para los *no-tan-friquis*: Espadas para
Leonardo, Nunchakus para Michelangelo, bastón Bo para Donatello y Sai para
Raphael. **Bonus extra**: Si usas un delimitador diferente, por ejemplo, `;` o
`|`. **Bonus extra plus**: Incluye una primera fila con los nombres de las
columnas.

**Solucion**:

```python
import csv

datos = [
    ('Leonardo', 'Azul', 1452, 'Espadas'),
    ('Raphael', 'Rojo', 1483, 'Sai'),
    ('Michelangelo', 'Naranja', 1475, 'Nunchakus'),
    ('Donatello', 'Violeta', 1386, 'Bastón Bo'),
    ]
with open('some.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['name', 'color', 'year', 'weapon'])
    writer.writerows(datos)
```

### La función `reader`

Esta función nos devuelve un *iterador*, que irá devolviendo las distintas
líneas del fichero. Las línea han sido procesadas, de forma que ya todos los
problemas que nos podríamos encontrar están resueltos; los campos están
separados, los campos que vengan entrecomillados has sido procesados y nos
llegan como esperamos, etc.

Vamos a ver un ejemplo sencillo de lectura usando `reader`, pero veamos
primero la estructura del fichero con el que vamos a trabajar
([marvel-wikia-data.csv](https://raw.githubusercontent.com/pythoncanarias/eoi/master/05-libs/standard/10-csv/marvel-wikia-data.csv)).

Estas son las primeras 4 líneas del fichero:

```csv
page_id,name,urlslug,ID,ALIGN,EYE,HAIR,SEX,GSM,ALIVE,APPEARANCES,FIRST APPEARANCE,Year
1678,Spider-Man (Peter Parker),\/Spider-Man_(Peter_Parker),Secret Identity,Good Characters,Hazel Eyes,Brown Hair,Male Characters,,Living Characters,4043,Aug-62,1962
7139,Captain America (Steven Rogers),\/Captain_America_(Steven_Rogers),Public Identity,Good Characters,Blue Eyes,White Hair,Male Characters,,Living Characters,3360,Mar-41,1941
64786,"Wolverine (James \""Logan\"" Howlett)",\/Wolverine_(James_%22Logan%22_Howlett),Public Identity,Neutral Characters,Blue Eyes,Black Hair,Male Characters,,Living Characters,3061,Oct-74,1974
```

Con este primer vistazo ya podemos deducir varias cosas:

1) La primera línea contiene una cabecera en la que se nos informa de los
nombres de las diferentes columnas. Por ejemplo, la primera se llama `page_id`,
podemos suponer que se trata de un identificador único de cada personaje. La
onceava columna tiene el nombre de `FIRST APPEARANCE`, que se podría traducir
como primera vez que fue publicado, y parece una combinación de mes y año. La
doceava se titula `Year`. Si analizamos los datos, veremos que en realidad es
el año de la primera publicación; *Spiderman* fue publicado por primera vez en
1962, el Capitán América en 1941.

2) El separador entre campos o columnas es la coma.

3) En algunos casos nos encontramos con cosas raras. Por ejemplo, en la
   línea 4, correspondiente a Lobezno o *Wolverine*), vemos que el
   nombre del personaje contiene el carácter comillas dobles (`"`).
   Parece que en estos casos se delimita el nombre completo entre
   comillas dobles y las comillas dobles internas se *escapan* con la
   secuencia `\""`.

   Es decir, que para representar en el fichero el texto:

        Wolverine (James "Logan" Howlett)

   en el fichero CSV, se ha almacenado como:

        "Wolverine (James \""Logan\"" Howlett)"

   La siguiente columna se denomina `urlslug`. Es parte de la URL que
   podemos usar para acceder a la página web de cada personaje. En este
   campo se escapan las barras (`/`), de forma que el valor del
   `slugurl` original:

        /Wolverine_(James_%22Logan%22_Howlett)

   Se ha almacenado en el fichero CSV como:

        \/Wolverine_(James_%22Logan%22_Howlett)

Todas estas particularidades, y muchas más, son las que hacen más complicado
trabajar con ficheros CSV. Aunque podríamos resolver todos estos problemas
usando las capacidades de Python para trabajar con textos, el propósito de la
la librería `csv` es precisamente ayudarnos en esto.

Vamos a usar la función `reader()` para leer los datos. Recordemos que
acepta como parámetro de entrada un fichero abierto para lectura, y que
como resultado nos devuelve un _iterador_, que nos devolverá cada una de
las líneas del fichero, pero ya divididas en forma de lista con los
valores que nos interesan. El siguiente programa muestra solo las 4
primeras filas de valores (porque hay **16377** personajes en este
fichero):

```python
import csv

with open('marvel-wikia-data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        print(row)
        if i > 3:
            break
```

La salida de este programa debería ser algo como esto:

```csv
['page_id', 'name', 'urlslug', 'ID', 'ALIGN', 'EYE', 'HAIR', 'SEX', 'GSM', 'ALIVE', 'APPEARANCES', 'FIRST APPEARANCE', 'Year']
['1678', 'Spider-Man (Peter Parker)', '\\/Spider-Man_(Peter_Parker)', 'Secret Identity', 'Good Characters', 'Hazel Eyes', 'Brown Hair', 'Male Characters', '', 'Living Characters', '4043', 'Aug-62', '1962']
['7139', 'Captain America (Steven Rogers)', '\\/Captain_America_(Steven_Rogers)', 'Public Identity', 'Good Characters', 'Blue Eyes', 'White Hair', 'Male Characters', '', 'Living Characters', '3360', 'Mar-41', '1941']
['64786', 'Wolverine (James \\"Logan\\" Howlett)', '\\/Wolverine_(James_%22Logan%22_Howlett)', 'Public Identity', 'Neutral Characters', 'Blue Eyes', 'Black Hair', 'Male Characters', '', 'Living Characters', '3061', 'Oct-74', '1974']
['1868', 'Iron Man (Anthony \\"Tony\\" Stark)', '\\/Iron_Man_(Anthony_%22Tony%22_Stark)', 'Public Identity', 'Good Characters', 'Blue Eyes', 'Black Hair', 'Male Characters', '', 'Living Characters', '2961', 'Mar-63', '1963']
```

**Ejercicio**: Modificar el código anterior para que nos muestre más personajes
pongamos 16, pero que de cada personaje nos muestre solo su nombre (Columna 2),
alineación (Columna 5) y el año en que fue publicado por primera vez (Columna
13 y última). **Extra bonus** si eliminas del listado los nombres de la columna
que estan en la primera línea del fichero.

Solución:

```python
import csv

with open('marvel-wikia-data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for i, row in enumerate(reader):
        nombre = row[1]
        alineacion = row[4]
        publicacion = row[-1]
        print(
            f"{nombre} ({alineacion}) publicado por primera"
            f" vez en {publicacion}"
            )
        if i > 25:
            break
```

### Dialectos

Con los dialectos podemos definir varios factores que pueden cambiar de un
fichero CSV a otro. En el caso del fichero CSV de los personajes Marvel, vemos
que no usa ningún delimitar de textos, mientras que el dialecto por defecto
espera comillas dobles: `"`. Al no usar delimitadores de texto, necesita alguna
forma de poder *escapar* el símbolo usado como separador si estuviera usado en
algún campo de texto.  De lo contrario el `reader` lo interpretaría como un
salto de columna.

Existe dialectos relativamente estándar que viene ya definidos en el módulo,
pero en el peor de los casos podemos definir nuestro propio dialecto. Una vez
definido, tenemos que registrarlo para que tanto la función `reader` como
`writer` sepan de su existencia.

Para el caso de este fichero, podemos definir y registrar el siguiente dialecto:

```python
import csv

csv.register_dialect('marvel', delimiter=',', quoting=csv.QUOTE_NONE, escapechar="\\")
```

Con este dialecto, el resultado de `reader` es mucho más limpio:

```python
import csv

csv.register_dialect('marvel', delimiter=',', quoting=csv.QUOTE_NONE, escapechar="\\")
with open('marvel-wikia-data.csv', 'r') as f:
    reader = csv.reader(f, dialect='marvel')
    for i, row in enumerate(reader):
            print(row)
        if i > 10:
            break
```

**Ejercicio**: Usar el código del ejemplo anterior y listar todos los
personajes de Marvel creados en el año de tu nacimiento.

**Solución**:

```python
import csv

csv.register_dialect('marvel', delimiter=',', quoting=csv.QUOTE_NONE, escapechar="\\")
filename = "marvel-wikia-data.csv"
with open(filename, 'r') as f:
    reader = csv.reader(f, dialect="marvel")
    next(reader)  # Ignorar la cabecera
    for row in reader:
        year = int(row[-1] if row[-1] else 0)
        if year == 1972:
            print(row[1])
```
