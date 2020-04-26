### La librería statistics

La librería **statisctics** incluye funciones matemáticas para realizar
cálculos estadísticos.

#### Alcance y limitaciones

Esta librería está muy lejos de la potencia de otras librerías de terceros
como numPy, sciPy y otros, pero tiene la ventaja de que viene incorporade
en lo librería standars (desde Pythn 3.4), y tiene funcionalidad suficiente
para realizar varias gráficas y cálculos relativamente complejos.

Estas funciones trabajan con números enteros, en coma flotante (*float*),
decimales (``Decimal``) y raciones (``Fraction``). Pero es muy
recomendable trabajar con listas y otras colecciones que los datos
sean homogeneos. Por ejemplo, una lista de enteros solo deberia tener 
enteros.

#### Funciones de medias y medidas similares

La funcion **mean** calcula la media arietmética de un conjunto de datos
(Una poblacion o una muestra, en terminis estadisticsos)

Ejercicio: Calcular la media arietmética de 23, 76, 99, 12


la función **geometric_mean()** es equivalente a la anterior, pero calcula
media geométrica.

La media geométrica de $n$ numeros es la raíz n-ésima del producto de todos
los números. Se usa por ejemplo para promediar intereses compuestos.
	
Por ejemplo, la media geométrica de 2 y 18 es

$$ {\displaystyle {\sqrt[{2}]{2\cdot 18}}={\sqrt[{2}]{36}}=6} $$


Otro ejemplo, la media de 1, 3 y 9 sería

$$ {\displaystyle {\sqrt[{3}]{1\cdot 3\cdot 9}}={\sqrt[{3}]{27}}=3} {\displaystyle {\sqrt[{3}]{1\cdot 3\cdot 9}}={\sqrt[{3}]{27}}=3} $$


La función **median()** nos veuelve la mediana de una serie de valores, es
decir, el valor que está en la posición central en un conjunto de datos ordenados. Si
el número de datos es impar, la posicion central es unica y el valor que esté
ahí es la medianda, pero si son pares, el valor de la mediana es la media de
los dos valores que estan a la mitad.

Por ejemplo, la serie [3, 6, 9, 12, 24], como tiene 5 elementos, impar, la
posicion de la mediana es 3 y para este caso la mediana vale 9.

Pero si el número de elementos es par, como en [3, 6, 9, 12], no hay una
posición central única, el centro podrias ser bien la segunda posicion
o la tercera. Asi que lo que se hace es tomar la media de los valores en
esa posicion, $3$ y $6$, asi que la mediana es $4.5$.

La función **mode()** nos da la moda, esto es, el valor o valores
que más se repite dentro de la serie.

Por ejemplo, para los valores [1, 2, 4, 4, 4, 4, 7, 39142], la moda es
4.

Esta función es la única dentro de esta librería que, además de aceptar
numeros, tambien acepta valores discretos, por ejemplo:

>>> mode(["red", "blue", "blue", "red", "green", "red", "red"])
'red'


Ejercicio: Dado el siguiente texto:

- Haga el favor de poner atención en la primera cláusula porque es muy
  importante. Dice que… la parte contratante de la primera parte será
  considerada como la parte contratante de la primera parte. ¿Qué tal, está muy
  bien, eh?

- No, eso no está bien. Quisiera volver a oírlo.

- Dice que… la parte contratante de la primera parte será considerada como la
  parte contratante de la primera parte.

- Esta vez creo que suena mejor.

- Si quiere se lo leo otra vez.

- Tan solo la primera parte.

- ¿Sobre la parte contratante de la primera parte?

- No, solo la parte de la parte contratante de la primera parte.

- Oiga, ¿por qué hemos de pelearnos por una tontería como ésta? La cortamos.

- Sí, es demasiado largo. ¿Qué es lo que nos queda ahora?

- Dice ahora… la parte contratante de la segunda parte será considerada como la
  parte contratante de la segunda parte.

- Eso si que no me gusta nada. Nunca segundas partes fueron buenas. Escuche:
  ¿por qué no hacemos que la primera parte de la segunda parte contratante sea
  la segunda parte de la primera parte? 

1) Usat `statstics.mean` para encontrar la media de la longitud de las palabras

2) Usar `statistics.mode` para encontrar la palabra más repetida

Podemos usar esta función a la que le pasamos un texto y nos devuelve 
todas las palabras que lo contienen en forma de lista, manteniendo el
orden pero eliminando simpbolos como `-`, `?`, `!`...


def text_to_words(text):
    pat_seps = re.compile("[\-\s!?¿+\.,;:]+")
    words = (w.strip().lower() for w in pat_seps.split(text))
    return words
    

Usar ahora esta version mejorada que elimina pal;abras demasiado comunes.

def text_to_words(text):
    exclude_words = ['', 'el', 'la', 'los', 'las', 'y', 'o']
    pat_seps = re.compile("[\-\s!?¿+\.,;:]+")
    words = (w.strip().lower() for w in pat_seps.split(text))
    return [for w in words if w not in exclude_words]
    

	
 La función **multimode(data)** es como la anterior, pero devuelve
 varios valores, si encuentra que hay varias modas. La función
 anterior siempre devuelve un único valor (Si hay varias modas,
 devuelve la primera que encotró). Por ejemplo:

    >>> import satadistics
    >>> sample = 'aabbbbccddddeeffffgg'
    >>> stadistics.multimode(sample), stadistics.mode(sample)

La función **stdev(data, xbar=None)** devuelve la desviación estándar (esto
es, la raiz cuadrada de la varianza). Tambien podemos calcular
directamente la varianza con la funcion **variance(data, xbar=None)**.
Las dos funciones usan los mismo parámetros, y estas dos medidas se
usan para medir la variabilidad, es decir, si los datos estan muy
dispersdos o muy agrupados). Un numero alto indica que los datos
estan muy dispersos, un numero pequeño, que estan muy agrupados.
Un valor de cero significaria que no hay disperson en absoluto; todos
los valores son iguales


Por úlgimo, la funcion **harmonic_mean(data)** devuelve la media
armónica. Esta es muy útil en conjuntos de números que se definen
en relación con alguna unidad, por ejemplo la velocidad 
(distancia por unidad de tiempo).


$${\displaystyle {\bar {x}}=n\cdot \left(\sum _{i=1}^{n}{\frac {1}{x_{i}}}\right)^{-1}}$$

La media armónica es la inversa de la media arietmetica, aplicado a los inversos
de los valores. Es decir, que donde la media divide, ahora multiplicamos, pero
la suma no se hace con los valores, sino con los inversos de los valores.

Por ejemplo, la media armónica de los números: 34, 27, 45, 55, 22, y 34 es:

$${\displaystyle {\frac {6}{{\frac {1}{34}}+{\frac {1}{27}}+{\frac {1}{45}}+{\frac {1}{55}}+{\frac {1}{22}}+{\frac {1}{34}}}}\approx 33,018} {\frac {6}{{\frac {1}{34}}+{\frac {1}{27}}+{\frac {1}{45}}+{\frac {1}{55}}+{\frac {1}{22}}+{\frac {1}{34}}}}\approx 33,018$$

Nota: Si alguno de los valores es cero, la meia armónica se considera 0

Para que sirve la media armocica? para aquellos valores que sean proporciones
o rarios, por ejemplo las velocidades.

Pregunta: Supongamos un coche que circula 10 kilometros a 40 km/h, luego otros 10 km a
60 km/h. ¿Cuál es su velocidad media?

    >>> statiastic.harmonic_mean([40, 60])
    48.0

Pregunta: Supongamos un inversor que ha invertido la misma cantidad en tres
compañias, que le proporcionan un ratio de ganancias (Precio/Beneficio) 
de 2.5, 3 y 10. Cual es el ratio de ganancias de toda la cartera?

    >>> statistic.harmonic_mean([2.5, 3, 10])

Miniproyecto: Calcular el tamaño medio de todos los archivos que hay en un 
una carpeta determinada. Usa el esqueleto que vimos en la librería **os**
para recorrer un arbol de directorios con la funcion `walk`.

Bonus: Informa tambien de los valores maximo, minimo y desviacion estandar
de la media
