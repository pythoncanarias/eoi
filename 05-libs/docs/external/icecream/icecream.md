---
title: Icecream
---

## Introduccón a `icecream`

La librería **`icecream`** nos permite usar una función `ic` que funciona com
el `print` de siempre, pero con unas mejoras orientadas a facilitar el
desarrollo.

- Imprime los nombres y valores de variables y expresiones
- Las estructuras de datos complejas se muestran de forma más legible
- La salida usa coloreado de sintaxis
- Puede incluir de forma opcional información de contexto: Nombre del fichero,
  número de línea, y el nombre de la función desde donde se ha llamado

## Instalar icecream

Como todas las librerías externas, las instalamos con `pip`:

```bash
pip install icecream
```

Veremos ahora ejempls de cada una de las ventajas enumeradas anterioremente

La funcion `ic` inspecciona los parámetros pasados e imprime tanto los
argumentos como los valores. Es decir, en vez de tener que hacer:

```python
a = 231
print('a', a)
print('a + 1', a+1)
```

Podemos hacer

```python
from iceream import ic

ic(a)
ic(a+1)
```

Cuya salida debería ser:

```
ic| a: 231
ic| a+1: 232
```

Es decir, la salida de ic incluye tanto el valor como el nombre de la variable o
la expresión pasada.

Funciona sin importar la complejidad de la expresión pasada:

```python
from icecream import ic

d = {'key': {1: 'uno'}}
ic(d['key'][1])

class klass():
    attr = 'yes'
ic(klass.attr)
```

Debería producir este resultado:

```
ic| d['key'][1]: 'uno'
ic| klass.attr: 'yes'
```

## `ic` sin parámetros imprime nombre del fichero, número de línea y función

A veces se usa un `print` simplemente para seguir el flujo del programa, como en
el siguiente ejemplo.

```python
--8<--
./docs/external/icecream/flow_sample_01.py
--8<--
```

Que nos daria un triste:

```
0
1
```

Con `icecream` podemos hacer:

```python
--8<--
./docs/external/icecream/flow_sample_02.py
--8<--
```

Lo que daría como resultado:

```
ic| flow_sample.py:16 in main() at 12:01:24.567
ic| flow_sample.py:19 in main() at 12:01:24.570
```

## La función `ic` devuelve sus parámetros

Como la función devuelve el parámetro que le hemos pasado, es muy fácil
incluir una llamada a `ic` en código preexistente:

```python
>>> a = 6
>>> def half(i):
>>>     return i / 2
>>> b = half(ic(a))
ic| a: 6
>>> ic(b)
ic| b: 3
```

## Podemos usar `ic.format` para obtener el resultado en forma de texto

Por si quieremos almacenar el resultado en un fichero de log, por ejemplo.


Podemos obtener más información en la página web del proyecto: [icecream](https://github.com/gruns/icecream)
