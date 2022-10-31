---
title: tqdm Barra de progreso
---

## Introducción a `tqdm`

La librería **`tqdm`** nos proporciona un sistema muy fácil para
incorporar una barra de progreso, para aquellos casos en los que realizamos
tareas que se tomen un tiempo apreciable. Siempre es bueno que el usuario reciba
cierta realimentación de que el proceso sigue su curso.

El nombre deriva de una palabra árabe _taqaddum_ (تقدّم) que significa progreso. También se puede recordar el nombre porque es una abreviatura de la frase "te quiero demasiado".

## Instalación de `tqdm`

Como siempre, `pip` es tu amigo:

```bash
pip install tqdm
```

## Cómo usar tqdm

La forma más sencilla de añadir la barra de progreso es recubrir cualquier
iterador que estemos usando con una llamada a `tqdm(iterador)`. Por ejemplo, el
siguientes código de ejemplo simula una operación que tarda 10 segundos en
ejecutarse

```python
import time

for num in range(10):
    time.sleep(1)
```

Ejecutándolo tal y como está ahora, la pantalla se quedaría congelada durante los
diez segundos, hasta que el programa saliera del bucle y terminara. Con `tqdm`
podemos conseguir una barra de progreso muy fácil de la siguiente manera:

```python
import time
from tqdm import tqdm

for num in tqdm(range(10)):
    time.sleep(1)
```

Una delas ventajas de `tqdm` es que utiliza varios algorítmos para intentar
determinar el tiempo restante y evitar actualizaciones del progreso
innecesarias.

## La función `trange`

La función **`trange`** es una versión especializada de range para trabajar
directamente con `tqdm`, por lo que es preferible usar `trange(10)` que
`tqdm(range(10))`. Veamoslo con el siguiente ejemplo:


```python
import time
from tqdm import trange

for num in trange(100):
    time.sleep(0.1)
```

## Actualización manual de la barra de progresos

Si necesitamos cierto control adicional, podemos usar `tqdm` de forma manual, la
forma más cómoda es usandolo dentro de un `with`:

```python
import time
from tqdm import tqdm

with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.1)
        pbar.update(10)
```

Lo mejor es usar o bien un iterable que se pueda contar con `len()` o el
parámetro `total`, porque de esta forma las actualizaciones son óptimas.

## Uso desde la línea de comandos

Otra ventaja de `tqdm` es que, una vez instalado, se puede usar como una
utilidad a nivel del sistema operativo. Añadiendo `tqdm` como un paso máß dentro
de un _pipeline_ de procesos (O usando `python -m tqdm` si lo anterior no
funciona) podemos obtener la barra de progreso, ya que la entrada estandar
simplemente se copia exactamente igual a la salida estandar.

El siguiente ejemplo realiza una cuenta de las líneas de todos los ficheros
python que encuentre en el directorio actual:

```bash
$ find . -name '*.py' -type f -exec cat \{} \; | wc -l
```

Si hay muchos ficheros, esto podria llevarle cierto tiempo; podemos añadir una
barra
de progreso simplemente insertando `tqdm` en el pipeline:

```bash
$ find . -name '*.py' -type f -exec cat \{} \; | tqdm | wc -l
```

Más información en la página web del proyecto: [tqdm](https://github.com/tqdm/tqdm)
