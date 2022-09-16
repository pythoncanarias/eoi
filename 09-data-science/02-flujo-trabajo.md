# Flujo de trabajo de un proyecto de ML

- [Flujo de trabajo de un proyecto de ML](#flujo-de-trabajo-de-un-proyecto-de-ml)
  - [1. Conseguir los datos](#1-conseguir-los-datos)
    - [Origen de los datos](#origen-de-los-datos)
    - [Cargar los datos](#cargar-los-datos)
  - [2. Análisis exploratorio](#2-análisis-exploratorio)
    - [Librerías importantes](#librerías-importantes)
    - [Tipos de datos](#tipos-de-datos)
    - [Medidas de tendencia central](#medidas-de-tendencia-central)
    - [Medidas de simetría y curtosis](#medidas-de-simetría-y-curtosis)
    - [Distribución de los datos](#distribución-de-los-datos)
    - [Medidas de posición no central](#medidas-de-posición-no-central)
    - [Medidas de dispersión](#medidas-de-dispersión)
  - [3. Preparar los datos](#3-preparar-los-datos)
    - [Valores nulos](#valores-nulos)
    - [Valores atípicos (outliers)](#valores-atípicos-outliers)
    - [Distintos órdenes de magnitud](#distintos-órdenes-de-magnitud)
    - [Selección de variables](#selección-de-variables)
    - [Desbalanceo de los datos](#desbalanceo-de-los-datos)
    - [Gestión de datos categóricos](#gestión-de-datos-categóricos)
  - [4. Elegir un modelo](#4-elegir-un-modelo)
    - [Tipos de aprendizaje del modelo](#tipos-de-aprendizaje-del-modelo)
    - [Consideraciones al elegir un algoritmo](#consideraciones-al-elegir-un-algoritmo)
  - [5. Entrenar el modelo](#5-entrenar-el-modelo)
    - [Preparación del dataset de entrenamiento](#preparación-del-dataset-de-entrenamiento)
    - [Validación cruzada](#validación-cruzada)
  - [6. Evaluar el modelo](#6-evaluar-el-modelo)
    - [Ajuste del modelo: overfitting vs underfitting](#ajuste-del-modelo-overfitting-vs-underfitting)
    - [Modelos de regresión](#modelos-de-regresión)
    - [Modelos de clasificación](#modelos-de-clasificación)
  - [7. Poner en producción el modelo](#7-poner-en-producción-el-modelo)

---

## 1. Conseguir los datos

### Origen de los datos
1. Alguien nos entrega los datos :tada:
2. Datasets públicos: , [scikit learn](https://scikit-learn.org/stable/datasets.html), [tensorflow](https://www.tensorflow.org/datasets?hl=es-419), [Kaggle](https://www.kaggle.com/), [UCI Machine learning Repository](https://archive.ics.uci.edu/ml/datasets.php), [Datos Gobierno de España](https://datos.gob.es/), [Datos Madrid](https://datos.madrid.es/portal/site/egob), [Datos Castilla la Mancha](https://datosabiertos.castillalamancha.es/), [Datos BOE (Civio)](https://datos.civio.es/datasets/)
3. Internet of Things
4. [Web crawling & APIs: Scrapy](https://scrapy.org/)

### Cargar los datos
- Texto
  * CSV
  * JSON
- Imagen
  * Pillow
  * OpenCV
- Audio
  * Wavio
  * PyAudio

**CSV**

**JSON**

**Pillow**

**OpenCV**

**Wavio**

**PyAudio**

## 2. Análisis exploratorio

### Librerías importantes
- Numpy
- Pandas
- Scipy
- Matplot Lib
- Seaborn

**Numpy**
Extensión de Python, que le agrega mayor soporte para vectores ymatrices, constituyendo una biblioteca de funciones matemáticas de alto nivel para operar con esos vectores o matrices.  
* [Cheatsheet de datacamp](https://www.datacamp.com/communityblog/python-numpy-cheat-sheet)
* [Tutorial](_numpy.ipynb)
    * [Ejercicios](ejercicios/numpy_ejercicios.ipynb)

**Pandas**
Extensión de NumPy para manipulación y análisis de datos para ellenguaje de programación Python. En particular, ofrece estructuras de datos y operaciones para manipular tablas numéricas y series temporales.
* [Cheatsheet de datacamp](https://www.datacamp.com/communityblog/python-pandas-cheat-sheet)
* [Tutorial](_pandas.ipynb)
    * [Ejercicios](ejercicios/pandas_ejercicios.ipynb)

**Scipy**
Biblioteca open source de herramientas y algoritmos matemáticospara Python que nació a partir de la colección original de Travis Oliphant que consistía de módulos de extensión para Python, lanzada en 1999 bajo el nombre de Multipack
* [Cheatsheet de datacamp](https://www.datacamp.com/communityblog/python-scipy-cheat-sheet)

**Matplot Lib**
Biblioteca para la generación de gráficos a partir de datoscontenidos en listas o arrays en el lenguaje de programación Python y su extensión matemática NumPy. Proporciona una API, pylab, diseñada para recordar a la de MATLAB.
* [Cheatsheet de datacamp](https://www.datacamp.com/communityblog/python-matplotlib-cheat-sheet)
* [Tutorial](_matplotlib.ipynb)
    * [Ejercicios](ejercicios/matplotlib.ipynb)

**Seaborn**
Seaborn es una librería de visualización de datos en Python basadaen matplotlib.   
La idea de Seaborn es que los data scientists dispongan de unainterfaz para hacer gráficos estadísticos atractivos e explicativos: el objetivo es visualizar datos complejos de forma sencilla y extraer conclusiones.
* [Cheatsheet de datacamp](https://www.datacamp.com/communityblog/seaborn-cheat-sheet-python)
* [Tutorial](_seaborn.ipynb)
    * [Ejercicios](ejercicios/seaborn_ejercicios.ipynb)

**Extra!**
Recomendaciones sobre buenas visualizaciones
[The python graph gallery](https://python-graph-gallery.com/)

### Tipos de datos

- **Variables cuantitativas**
    - Variables discretas: Toma valores aislados
        - `Edad: 2, 5, 7, 12, 15, 26, 45, 47, 50, 54, 65, 73`
    - Variables continuas: Valores comprendidos entre dos números
        - `Altura: 1.25, 1.27, 1.29, 1.54, 1.67, 1.71, 1.75`
- **Variables cualitativas**
    - Variable cualitativa nominal (no tienen orden)
        - `Sexo: hombre, mujer`
    - Variable cualitativa ordinal o cuasi-cuantitativa (existe un orden)
        - `Nivel: bajo, medio, alto`

### Medidas de tendencia central
Un conjunto N de observaciones puede que por sí solo no nos diganada. En cambio, si se conoce que están situados alrededor de uno o varios valores centrales ya tenemos una referencia que sintetiza la información

- Media
- Mediana
- Moda

```python
import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(27000, 15000, 10000)
plt.hist(incomes, 50)
plt.show()
np.mean(incomes)
print(f'Media sin outliers np.mean(incomes)}')

## Ahora introducimos un outlier:
incomes = np.append(incomes, [1000000000])
print(f'Media con outliers np.mean(incomes)}')
```
```python
# Generamos datos de edades random para 500 personas:
ages = np.random.randint(18, high=90, size=500)
ages[:10]

from scipy import stats
stats.mode(ages)
```

### Medidas de simetría y curtosis
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
vals = np.random.normal(0, 1, 10000)
plt.hist(vals, 50)
plt.show()
# A skewness value > 0 means that there is more weight in the lefttail of the distribution
print(f'Skew:     skew(vals)}') 
print(f'Kurtosis: kurtosis(vals)}') 
```

```python
from scipy.stats import gamma
# https://docs.scipy.org/doc/scipy-0.13.0/reference/generated/scipystats.skew.html
data_gamma = gamma.rvs(a=10, size=10000)
plt.hist(data_gamma, 50)
plt.show()
print(f'Skew:     skew(data_gamma)}') 
print(f'Kurtosis: kurtosis(data_gamma)}') 
```

### Distribución de los datos

**Distribución de probabilidad**
- Una distribución de probabilidad permite conocer elcomportamiento de la variable, describir y entender cómo varían los valores de la característica estudiada en los individuos.
- Proporciona información sobre los valores que puede tomar unavariable en los individuos observados y la frecuencia con que ocurren.

__Distribución normal o Gaussiana__
- Asociada a fenómenos naturales:
  - caracteres morfológicos de una especie (talle, peso,distancia...)
    - caracteres fisiológicos (efecto de un fármaco...)
    - caracteres sociológicos (notas de un exámen...)

```python
from scipy.stats import norm
import matplotlib.pyplot as plt
x = np.arange(-3, 3, 0.001)
plt.plot(x, norm.pdf(x))
```
```python
import numpy as np
import matplotlib.pyplot as plt
mu = 5.0
sigma = 2.0
values = np.random.normal(mu, sigma, 10000)
plt.hist(values, 50)
plt.show()
```

### Medidas de posición no central

- __Cuartiles (Q)__
    - Encuentran el valor acumulado al 25%, 50% y 75%,respectivamente.

- __Deciles (D)__
    - Representan el 10%, 20%, ... , 90% de los datos acumulados respectivamente.

- __Percentiles (P)__
    - Representan el 1%, 2%, ... , 99% de los datos acumuladosrespectivamente

```python
import numpy as np
import matplotlib.pyplot as plt
vals = np.random.normal(0, 0.5, 10000)
plt.hist(vals, 50)
plt.show()
np.percentile(vals, 50)
np.percentile(vals, 90)
np.percentile(vals, 20)
```

### Medidas de dispersión

Varianza y  Desviación típica
- Es la raíz cuadrada positiva de la varianza
- Es la mejor medida de dispersión y la más utilizada
- Si la distribución de frecuencias se aproxima a una normal severifica:
    - El 68% de los valores de la variable están comprendidos entre± σ
    - El 95% de los valores de la variable están comprendidos entre± 2 σ
    - El 99% de los valores de la variable están comprendidos entre± 3 σ
    
```python
import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 50.0, 10000)
plt.hist(incomes, 50)
plt.show()
```
```python
incomes.std()
incomes.var()
```

## 3. Preparar los datos
_En Machine Learning, hay una regla de 80/20. Cada data scientist suele dedicar un 80% de tiempo al preprocesamiento de datos y un 20% a realizar el análisis_


Los problemas más comunes a resolver en el preprocesamiento de datos son:
    1. Valores nulos
    2. Valores atípicos
    3. Distintos órdenes de magnitud
    4. Selección de variables
    5. Desbalanceo de los datos
    6. Gestión de datos categóricos


### Valores nulos

Tipos de valores nulos
1. **Missing completely at random (MCAR)**: el hecho que falte una observación no está relacionado con el o los valores faltantes ni con los valores existentes. Por ejemplo, fallos en el equipamiento de medida, fallos humanos o que el mal tiempo haga que el equipo no funcione

2. **Missing at random (MAR)**: una o varias características registradas pueden explicar la distribución de los datos faltantes. Por ejemplo: que las personas con depresión puedan tener más reparos a revelar sus ingresos por creer que son más pequeños (aunque no lo sean en realidad y no afecten a la media)

3. **Missing not at random (MNAR)**: los datos faltantes probablemente dependen o están relacionados con datos no observados. Por ejemplo: que lersonas con enfermedad mental no informen de su “estado mental” (lo cual afecta a la distribución de esta variable)

```python
import pandas as pd

df = pd.DataFrame({'a':[None, 3, None, 5, 6], 'b':[1, 3, 4, 3, None], 'c':[54, None, None, 32, 21])
print(df)
```

**Reconocer los valores nulos**

Con `isnull` obtenemos una tabla booleana con `True` si el valor es un `NaN` o `False` si no lo es.
```python
df_bool = pd.isnull(df)
    print(df_bool)
```

**Eliminación de registros**

- Es la más sencilla de todas y puede ser la más eficaz si disponemos de una cantidad importante de datos
- Pandas proporciona la función `dropna()` para eliminar columnas o filas con datos faltantes.
```python
print(f'{df \\n\\n')

df_sin_nan = df.dropna()
print(df_sin_nan)
```

**Imputación simple**

- Generando valores aleatorios para cada variable
- Ordenando los datos de acuerdo a alguna variable y usando el valor de una celda adyacente (hot-deck)
- Realizando el mismo proceso pero con datos de otro dataset (cold-deck)
- Reemplazo a la media

Pandas proporciona la función `fillna()` para reemplazar valores perdidos con un valor específico.


```python
# reemplaza todos los NaN por 3
df_nuevo = df.fillna(value=3)

# Reemplaza los NaN con el valor promedio de cada columna:
df_nuevo = df.fillna(df.mean())

# Reemplaza los NaN con el valor anterior o posterior del NaN: 
# - 'pad' para reemplazarlo con el valor anterior 
# - 'bfill' con el posterior. 
df_nuevo = df.fillna(method='pad')

# Reemplazar los NaN interpolando con el resto de datos conocidos:
df_nuevo = df.interpolate(method='linear')

from sklearn.impute import SimpleImputer
import numpy as np

imp = SimpleImputer(strategy='most_frequent')
df_nuevo = imp.fit_transform(df)
```

### Valores atípicos (outliers)

Un valor atípico (outlier) es un valor de una variable muy distante a otras observaciones de la misma variable

- Errores en los instrumentos de medida
- Picos aleatorios en una variable
- La distribución tiene una cola muy “pesada” (heavily-tailed distribution)
    - Cuidado con hacer asunciones sobre la normalidad de la distribución


**Cómo detectarlos**
    
- **Z-score**: Es una forma de describir un dato en función de su relación con la media y la desviación estándar del conjunto de datos. 

```python
import numpy as np
import pandas as pd

dataset= [10, 12, 12, 13, 12, 11, 14, 13, 15, 10, 10, 10, 100, 12, 14, 13, 12, 13, 18, 150, 10, 10, 11, 12, 15, 12, 13, 12, 11, 14, 13, 15, 10, 15, 12, 10, 14, 13, 15 ,10]
len(dataset)
```

```python
outliers=[    
    threshold = 3
    mean_1 = np.mean(dataset)
    std_1 =np.std(dataset)
    
    for y in dataset:
        z_score= (y - mean_1)/std_1 
        if np.abs(z_score) > threshold:
            outliers.append(y)
    
    print(outliers)
```

- **IQR - Recorrido inter-cuartílico**: IQR indica cómo se distribuyen los valores medios. Se puede usar para saber cuándo un valor está demasiado lejos del medio.
```python
q1, q3= np.percentile(dataset,[25,75])
    print(f'Cuartil 1: {q1 -- Cuartil 3: {q3')
    
    iqr = q3 - q1
    print(f'IQR: {iqr')
    
    lower_bound = q1 - (1.5 * q1)
    upper_bound = q3 + (1.5 * q3)
    print(f'Lower bound: {lower_bound -- Upper bound: {upper_bound')
```

[Ref](https://medium.com/datadriveninvestor/finding-outliers-in-dataset-using-python-efc3fce6ce32)


**Cómo tratarlos**

- __Mantenerlos__ y usar un estadístico robusto frente a valores atípicos (la mediana, por ejemplo)
    - No siempre es posible

- __Eliminarlos__: si el dataset es suficientemente grande, puede ser una opción razonable
- Distribución normal: usar medidas como
    - 1.5 * IQR: recorrido intercuartílico (boxplot)
    - Seis sigma: ±3 veces la desviación típica (o desviación absoluta de la mediana)
    - Problema de regresión: distancia de Cook (influencia de una medida en una variable del modelo)
- Trimming: eliminar el x% de los datos en ambos extremos


- __Transformarlos__
    - “Winsorización”: parecido al trimming pero, en lugar de eliminar los valores, los transformamos en los límites de valores admitidos en los percentiles considerados
    - Reemplazo de outliers por NaNs e imputación de valores nulos


- __Examen visual__
    - Si los datos son pocos, podemos representarlos gráficamente y tomar la decisión manualmente

- __Integrarlos en el modelo__
        - Modelos estratificados o mixtures que integren los outliers como parte del modelo
        - Interesante cuando los valores atípicos no provienen de medidas erróneas


### Distintos órdenes de magnitud

- Normalización vs. Estandarización
    Estos dos términos se usan muchas veces de manera intercambiable
    - __Normalización__: escalado de valores en el intervalo \\[0, 1\\    
    - __Estandarización (z-score)__: transformación de la distribución para que tenga media 0 y desviación estándar 1


**¿Por qué es necesario?**
Muchos algoritmos de clasificación calculan distancias como parte del aprendizaje

Si algunas variables tienen rangos muy distintos (\\[0, 1\\] vs. \\[0, 1.000.000\\]) la de mayor rango tendrá mucha más influencia en el modelo


- En otros casos, que la distribución tenga una desviación típica de 1 puede ser beneficioso para el modelo (por ejemplo, Perceptrón Multicapa)
    - Disminuye de la velocidad de convergencia de algunos algoritmos (como ANNs o Gradient Descent)
    - Que los valores estén centrados en la media puede simplificar algunos cálculos (como la matriz de covarianza)
    - Puede ser recomendable aplicarla después de imputar valores nulos y eliminar valores atípicos


**Tipos de normalización**

- La **normalización L1** trabaja con las desviaciones mínimas, y funciona asegurándose de que la suma de los valores absolutos sea 1 en cada fila. En general, la técnica de normalización L1 se considera más robusta que la técnica de normalización L2 porque es resistente a los valores atípicos en los datos.

- La **normalización L2** trabaja con mínimos cuadrados y funciona asegurándose de que la suma de cuadrados sea 1. Si estamos resolviendo un problema donde los valores atípicos son importantes, tal vez la normalización de L2 sea  mejor opción.

```python
from sklearn.preprocessing import Normalizer

data = np.array([1.0, 2.0])

n_max = Normalizer(norm='max')
n_max.fit_transform(data.reshape(1, -1))
```
```python
n_l1 = Normalizer(norm='l1')
n_l1.fit_transform(data.reshape(1, -1))

n_l2 = Normalizer(norm='l2')
    n_l2.fit_transform(data.reshape(1, -1))
```


### Selección de variables

Algunos conjuntos de datos pueden tener un gran número de variables
- Difícil representación gráfica (si es necesaria)
- Pueden dificultar la construcción de un modelo (valores engañosos, por ejemplo)
- Pueden afectar a la velocidad de convergencia del algoritmo (cálculo de muchas distancias)
- Mayor capacidad de generalización (pueden ayudar a prevenir el overfitting)

**Técnicas**
- Selección de atributos
    - Filter: pre-procesado previo al algoritmo de aprendizaje
    - Wrapper: selección evaluando en el contexto del algoritmo de aprendizaje
- Análisis de Componentes Principales (Principal Component Analysis, PCA)
- Análisis de correlación

```python
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

titanic = sns.load_dataset('titanic')

correlation = titanic.corr()
sns.heatmap(correlation, annot=True, cbar=True, cmap=\RdYlGn\)

# Survived -> Se encuentra en 2 valores 0 si murió en la trajedia y 1 si sobrevivió 
# Pclass -> Determina la clase del pasajero, 1ra, 2da o 3era clase.
# SibSp -> Número de parientes como Hermano, Hermana, Hermanastra, Hermanastro, Esposo o Esposa. 
# Parch -> Número de parientes como Madre, Padre, Hijo, Hija, Hijastro, Hijastra 
# Fare -> Tarifa del pasaje
```

### Desbalanceo de los datos

- Algunos datasets presentan grandes diferencias en el número de instancias de cada una de las clases
    - Ejemplo: clasificador que reconozca terroristas puede tener un 99.99% de precisión prediciendo la clase mayoritaria 
- Existen técnicas que intentan minimizar el efecto de este balanceo
    - Re-muestreando instancias
    - Asociando un peso (coste) distinto a predecir cada una de las clases

**Resampling**
- Podemos considerar, básicamente, dos opciones para igualar el número de instancias de cada clase
    - Undersampling de la clase mayoritaria
    - Oversampling de la clase minoritaria



### Gestión de datos categóricos

En muchos problemas de clasificación, el conjunto de datos de destino está formado por etiquetas categóricas que no pueden procesarse inmediatamente con ningún algoritmo. 

**LabelEncoder**
- Funciona como un diccionario, asignando a cada valor categórico un número entero autoincremental
- Inconveniente: todas las etiquetas se convierten en números secuenciales. Un clasificador que trabaja con valores reales considerará números similares según su distancia, sin ninguna preocupación por la semántica.


```python
import numpy as np

X = np.random.uniform(0.0, 1.0, size=(10, 2))
Y = np.random.choice(('Male','Female', 'NonBin'), size=(10))

print(X)
print()
print(Y)
```
```python
from sklearn.preprocessing import LabelEncoder
    
le = LabelEncoder()
yt = le.fit_transform(Y)
print(yt)
print()
print(le.classes_)

output = [1, 0, 1, 1, 2, 0, 0, 2]
decoded_output = [le.classes_[i] for i in output    decoded_output]
```

**LabelBinarizer**
- Funciona como un diccionario, asignando a cada valor categórico un valor en binario
```python
from sklearn.preprocessing import LabelBinarizer

lb = LabelBinarizer()
Yb = lb.fit_transform(Y)
print(Yb.tolist())
print()
print(lb.inverse_transform(Yb))
```

## 4. Elegir un modelo

Para categorizar tu problema tienes que llevar a cabo 2 pasos:

- Categorizar la entrada
- Categorizar la salida

**Categorizar la entrada**

- Si tienes datos etiquetados, es un problema de aprendizaje supervisado
- Si no tienes etiquetas y quieres encontrar una estructura o patrón, es aprendizaje supervisado
- Si quieres optimizar una función objetivo interactuando con el entorno, es aprendizaje supervisado

**Categorizar la salida**

- Si la salida de tu modelo es un número, es un problema de **regresión**
- Si la salida de tu modelo es una clase, es un problema de **clasificación**
- Si la salida de tu modelo es una serie de grupos, es un problema de **clustering**

### Tipos de aprendizaje del modelo

**Aprendizaje supervisado**

Se refiere al proceso de construir un modelo de aprendizaje automático que se basa en datos de capacitación etiquetados.

Por ejemplo, digamos que queremos construir un sistema para predecir automáticamente el ingreso de una persona, en función de diversos parámetros como la edad, la educación, la ubicación, etc. Para hacer esto, necesitamos crear una base de datos de personas con todos los detalles necesarios y etiquetarla. Al hacer esto, le estamos diciendo a nuestro algoritmo qué parámetros corresponden a qué ingresos. Sobre la base de este mapeo, el algoritmo aprenderá cómo calcular los ingresos de una persona utilizando los parámetros que se le proporcionan

**Aprendizaje no supervisado**

Se refiere al proceso de construir un modelo de aprendizaje automático sin depender de los datos de capacitación etiquetados. Dado que no hay etiquetas disponibles, debe extraer información basada únicamente en los datos que se le proporcionaron.

Por ejemplo, digamos que queremos construir un sistema donde tenemos que separar un conjunto de puntos de datos en varios grupos. Lo complicado aquí es que no sabemos exactamente cuáles deberían ser los criterios de separación. Por lo tanto, un algoritmo de aprendizaje no supervisado debe separar el conjunto de datos dado en un número de grupos de la mejor manera posible.

**Aprendizaje por refuerzo**

En esta técnica nuestros modelos aprenden a partir de la experiencia. En un coche autónomo, cuando toma una mala decisión, se le “castiga”. A partir de sus premios y castigos, va aprendiendo a realizar su tarea mejor.

Esta es una técnica de prueba y error, y de utilizar una función de premio que vaya optimizando. Esta es una de las técnicas más prometedoras porque no requieren grandes cantidades de datos. En esta técnica se está haciendo mucha investigación.

image.png

### Consideraciones al elegir un algoritmo

**Precisión**

- No siempre es necesario obtener la respuesta más precisa posible.
- A veces, una aproximación ya es útil, según para qué se la desee usar. Si es así, puede reducir el tiempo de procesamiento de forma considerable al usar métodos más aproximados.
- Otra ventaja de los métodos más aproximados es que tienden naturalmente a evitar el sobreajuste.

**Tiempo de entrenamiento**

- La cantidad de minutos u horas necesarios para entrenar un modelo varía mucho según el algoritmo.
- A menudo, el tiempo de entrenamiento depende de la precisión (generalmente, uno determina al otro).
- Además, algunos algoritmos son más sensibles a la cantidad de puntos de datos que otros.
- Si el tiempo es limitado, esto puede determinar la elección del algoritmo, especialmente cuando el conjunto de datos es grande.

**Linealidad**

- Muchos algoritmos de aprendizaje automático hacen uso de la linealidad.
- Los algoritmos de clasificación lineal suponen que las clases pueden estar separadas mediante una línea recta (o su análogo de mayores dimensiones).
- Entre ellos, se encuentran la regresión logística y los SVM.
- Los algoritmos de regresión lineal suponen que las tendencias de datos siguen una línea recta.
- Estas suposiciones no son incorrectas para algunos problemas, pero en otros disminuyen la precisión.

**Cantidad de parámetros**

- Los parámetros son los números que afectan al comportamiento del algoritmo, como la tolerancia a errores o la cantidad de iteraciones, o bien opciones de variantes de comportamiento del algoritmo.
- El tiempo de entrenamiento y la precisión del algoritmo a veces pueden ser muy sensibles y requerir solo la configuración correcta. Normalmente, los algoritmos con un gran número de parámetros requieren más prueba y error para encontrar una buena combinación.


## 5. Entrenar el modelo

Cuando trabajamos en un problema de clasificación debemos prevenir problemas como el overfitting
Para ello, muchos investigadores dividen su conjunto de datos en dos subconjuntos: entrenamiento y validación

Sin embargo, esto es, en general, insuficiente para ajustar los parámetros del algoritmo de aprendizaje
Una mejor aproximación sería dividir el conjunto de datos en: entrenamiento, validación y test

### Preparación del dataset de entrenamiento

Aprender los parámetros de una función de predicción y probarla con los mismos datos es un error metodológico: un modelo que simplemente repetiría las etiquetas de las muestras que acaba de ver tendría una puntuación perfecta pero no podría predecir nada en datos que no haya visto.

Esta situación se llama overfitting, y para evitarlo, es una práctica común cuando se realiza un experimento de aprendizaje automático (supervisado) mantener parte de los datos disponibles como un conjunto de prueba: X_test, y_test.

```python
import numpy as np
from pylab import *

np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)
```

```python
trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]

trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

scatter(trainX, trainY)
```

```python
scatter(testX, testY)
```

```python
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
import numpy as np
from sklearn.model_selection import train_test_split

X, y = np.arange(10).reshape((5, 2)), list(range(5))
print(f'X: {X}')
print(f'\ny: {y}')

X: [[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]

y: [0, 1, 2, 3, 4]

X_train, X_test, y_train, y_test = train_test_split( , test_size=0.2, random_state=42)

print(f'X_train: \n {X_train} \n')
print(f'y_train: \n {y_train} \n')
print(f'X_test: \n {X_test} \n')
print(f'y_test: \n {y_test} \n')

X_train: 
 [[8 9]
 [4 5]
 [0 1]
 [6 7]] 

y_train: 
 [4, 2, 0, 3] 

X_test: 
 [[2 3]] 

y_test: 
 [1] 

# https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
iris.data.shape, iris.target.shape

((150, 4), (150,))

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.4, random_state=0)

print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

(90, 4) (90,)
(60, 4) (60,)

```

A veces dividir el conjunto de entrenamiento en 2 grupos no es suficiente
Al evaluar diferentes configuraciones ("hiperparámetros") para estimadores, como algunas configuraciones se deben establecer manualmente (por ejemplo, para un SVM), existe el riesgo de que el conjunto de pruebas se adapte demasiado porque los parámetros se pueden ajustar hasta que el estimador funcione de manera óptima.
De esta manera, el conocimiento sobre el conjunto de pruebas puede "filtrarse" en el modelo y las métricas de evaluación ya no informan sobre el rendimiento de la generalización.

Para resolver este problema, podemos crear otro conjunto de datos llamado "validación" para ajustar los parámetros del train y así, cuando el experimento parezca tener éxito, la evaluación final se pueda hacer en el conjunto de prueba.

Sin embargo, al dividir los datos disponibles en tres conjuntos, reducimos drásticamente el número de muestras que se pueden usar para aprender el modelo, y los resultados pueden depender de una elección aleatoria particular para el par de conjuntos (entrenamiento, validación).

### Validación cruzada

La validación cruzada es una técnica para evaluar modelos de ML mediante el entrenamiento de varios modelos de ML en subconjuntos de los datos de entrada disponibles y evaluarlos con el subconjunto complementario de los datos.
Se utiliza para detectar el sobreajuste, es decir, en aquellos casos en los que no se logre generalizar un patrón.

El conjunto de prueba aún debe mantenerse para la evaluación final, pero el conjunto de validación ya no es necesario cuando se realiza un CV.
En el enfoque básico, denominado k-fold CV, el conjunto de entrenamiento se divide en k conjuntos más pequeños y se sigue el siguiente procedimiento para cada uno de los k "pliegues":
- Se entrena un modelo utilizando K - 1 folds como dato de entrenamiento.
- El modelo resultante se valida en la parte restante de los datos.

grid_search_cross_validation.png ref

**K-Fold**
K-Fold divide todas las muestras en k grupos de muestras, llamados folds de igual tamaño (si es posible).
La función de predicción se aprende utilizando los folds k − 1, y el fold omitido se usa para la prueba.

```python
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold
import numpy as np
from sklearn.model_selection import KFold

X = ["a", "b", "c", "d"]
kf = KFold(n_splits=2)
for train, test in kf.split(X):
    print("%s %s" % (train, test))
```

kfold_cv.png

**LeaveOneOut**

Es un tipo de K-Fold, donde cada conjunto de aprendizaje se crea tomando todas las muestras excepto una, y el conjunto de prueba es la muestra que se omite.
Por lo tanto, para n muestras, tenemos n conjuntos de entrenamiento diferentes y n conjunto de pruebas diferentes.
Este procedimiento de validación cruzada no desperdicia mucha información, ya que solo se elimina una muestra del conjunto de entrenamiento

```python
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#sklearn.model_selection.LeaveOneOut
from sklearn.model_selection import LeaveOneOut

X = [1, 2, 3, 4]
loo = LeaveOneOut()
for train, test in loo.split(X):
    print("%s %s" % (train, test))

[1 2 3] [0]
[0 2 3] [1]
[0 1 3] [2]
[0 1 2] [3]
```

## 6. Evaluar el modelo

### Ajuste del modelo: overfitting vs underfitting

Comprender el ajuste del modelo es importante para comprender la causa raíz para una precisión deficiente del modelo.
Esta información le ayudará a tomar medidas correctivas.
Podemos determinar si un modelo predictivo presenta underfitting u overfitting de los datos de entrenamiento observando el error de predicción en los datos de entrenamiento y los datos de evaluación.

**Bias-Variance tradeoff - (Ajuste sesgo-varianza)**

Existe una relación entre la capacidad de un modelo para minimizar el sesgo y la varianza.
Lograr una comprensión adecuada de estos errores nos ayudaría no solo a construir modelos precisos, sino también a evitar el error de overfitting y underfitting.

bias_variance2.png

**Bias / sesgo**
- Es la diferencia entre la predicción promedio de nuestro modelo y el valor correcto que estamos tratando de predecir.
- Un modelo con alto sesgo presta muy poca atención a los datos de entrenamiento y simplifica en exceso el modelo.
- Siempre conduce a un alto error en la formación y los datos de prueba.

**Varianza / Variance**
- Es la variabilidad de la predicción del modelo para un punto de datos determinado o un valor que nos indica la difusión de nuestros datos.
- El modelo con alta variación presta mucha atención a los datos de entrenamiento y no generaliza los datos que no ha visto antes.
- Como resultado, tales modelos funcionan muy bien con los datos de entrenamiento pero tienen altos índices de error en los datos de prueba.

**Underfitting**

Se produce cuando un modelo no puede capturar el patrón subyacente de los datos.
Estos modelos suelen tener alto sesgo y baja varianza.
Ocurre cuando tenemos mucha menos cantidad de datos para construir un modelo preciso o cuando intentamos construir un modelo lineal con datos no lineales.
Además, este tipo de modelos son muy simples para capturar los patrones complejos en datos como la regresión lineal y logística.

Cómo evitarlo:
- Probar modelos más complejos. El overfitting puede deberse a que el modelo es demasiado sencillo (las características de entrada no son suficientemente expresivas) como para describir el destino adecuadamente.
- La precisión en los datos de entrenamiento y prueba podría ser deficiente porque el algoritmo de aprendizaje no tenía datos suficientes de los que aprender:
    - Aumentar el número de ejemplos de datos de entrenamiento.
    - Aumentar el número de pases en los datos de entrenamiento existentes
- Añadir nuevas características específicas del dominio y más productos cartesianos de características, y cambie los tipos de procesamiento de características utilizado (por ejemplo, aumentando el tamaño n-grams).
    Reducir la cantidad de regularización utilizada.

**Overfitting**

Ocurre cuando el modelo presenta un buen rendimiento con los datos de entrenamiento pero no con los datos de evaluación.
Estos modelos tienen bajo sesgo y alta varianza.
Esto se debe a que el modelo memoriza los datos que ha visto y no puede generalizar para los ejemplos no vistos.
Estos modelos suelen ser muy complejos, como los árboles de decisión (que son propensos al overfitting).

Cómo evitarlo:
- Selección de características: considerar el uso de combinaciones de características, la reducción del tamaño n-grams y la reducción del número de contenedores de atributos.
- Aumente la cantidad de regularización utilizada.

bias_variance.png ref


### Modelos de regresión

**Mean absolute error**

Es una medida de la diferencia entre dos variables continuas.
El error absoluto promedio (MAE) es la distancia vertical promedio entre cada punto y la línea de identidad.
MAE es también la distancia horizontal promedio entre cada punto y la línea de identidad.

```python
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error
from sklearn.metrics import mean_absolute_error

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
print(f'MAE 1: {mean_absolute_error(y_true, y_pred)}')

y_true = [[0.5, 1], [-1, 1], [7, -6]]
y_pred = [[0, 2], [-1, 2], [8, -5]]
print(f'MAE 2: {mean_absolute_error(y_true, y_pred)}')
```

**Mean squared error**

- El error cuadrático medio (ECM) de un estimador mide el promedio de los errores al cuadrado, es decir, la diferencia entre el estimador y lo que se estima.
- El ECM es una función de riesgo, correspondiente al valor esperado de la pérdida del error al cuadrado o pérdida cuadrática.
- La diferencia se produce debido a la aleatoriedad o porque el estimador no tiene en cuenta la información que podría producir una estimación más precisa

```python
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error
from sklearn.metrics import mean_squared_error
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

print(f'MAE 1: {mean_squared_error(y_true, y_pred)}')

y_true = [[0.5, 1], [-1, 1], [7, -6]]
y_pred = [[0, 2], [-1, 2], [8, -5]]

print(f'MAE 2: {mean_squared_error(y_true, y_pred)}')
```

### Modelos de clasificación

**Matriz de confusión**

- Es una herramienta que permite la visualización del desempeño de un algoritmo que se emplea en aprendizaje supervisado.
- Cada columna de la matriz representa el número de predicciones de cada clase, mientras que cada fila representa a las instancias en la clase real.
- Uno de los beneficios de las matrices de confusión es que facilitan ver si el sistema está confundiendo dos clases.

**Accuracy**

Calcula el número de predicciones que se corresponden con la etiqueta correcta en el dataset etiquetado

```python
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score
from sklearn.metrics import accuracy_score

y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]

print(f'Normalizado: {accuracy_score(y_true, y_pred)}')
print(f'Sin normalizar: {accuracy_score(y_true, y_pred, normalize=False)}')
```

**Precision**

- Es la capacidad de no clasificar como positivos ejemplos que son negativos
- Es el ratio tp / (tp + fp) donde tp es el número de true positives y fp el número de false positives.
- El rango va de 0 a 1. El mejor valor es 1 y el peor es 0
- Un mayor valor indica una mayor exactitud predictiva

```python
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html
from sklearn.metrics import precision_score

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]

# precision by class
print(f'None: {precision_score(y_true, y_pred, average=None)}')

# micro: calculate metrics globally by counting the total true positives, false negatives and false positives
print(f'Micro: {precision_score(y_true, y_pred, average="micro")}')

# macro: calculate metrics for each label, and find their unweighted mean. 
# This does not take label imbalance into account.
print(f'Macro: {precision_score(y_true, y_pred, average="macro")}')
```

**Recall**

- Es la capacidad del modelo de encontrar todos los casos positivos.
- Es el ratio tp / (tp + fn) donde tp es el número de true positives y fn el número de false negatives.
- El rango va de 0 a 1. El mejor valor es 1 y el peor es 0

```python
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html
from sklearn.metrics import recall_score

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]

# precision by class
print(f'None: {recall_score(y_true, y_pred, average=None)}')

# micro: calculate metrics globally by counting the total true positives, false negatives and false positives
print(f'Micro: {recall_score(y_true, y_pred, average="micro")}') 

# macro: calculate metrics for each label, and find their unweighted mean. 
# This does not take label imbalance into account.
print(f'Macro: {recall_score(y_true, y_pred, average="macro")}')
```

264px-Precisionrecall.svg.png By Walber - Own work, CC BY-SA 4.0

**F-Score**

- También se conoce como F1-Score y F-measure
- Puede interpretarse como la media ponderada del precision y el recall, donde F1 alcanza su mejor valor en 1 y el peor puntaje en 0.
- La fórmula del F-Score es F1 = 2 * (precision * recall) / (precision + recall)

```python
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score
from sklearn.metrics import f1_score

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]

# precision by class
print(f'None: {f1_score(y_true, y_pred, average=None)}')

# micro: calculate metrics globally by counting the total true positives, false negatives and false positives
print(f'Micro: {f1_score(y_true, y_pred, average="micro")}') 

# macro: calculate metrics for each label, and find their unweighted mean. 
# This does not take label imbalance into account.
print(f'Macro: {f1_score(y_true, y_pred, average="macro")}')
```

**Area Under the Receiver Operating Characteristic Curve (ROC AUC)**

ROC_space-2.png

Curvas.png

```python
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score
import numpy as np
from sklearn.metrics import roc_auc_score

y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])

roc_auc_score(y_true, y_scores)
```


## 7. Poner en producción el modelo

