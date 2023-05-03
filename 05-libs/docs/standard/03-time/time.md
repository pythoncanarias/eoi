---
title: time. Gestión básica del tiempo
---

## Introducción a `time`

Esté modulo proporciona funciones para trabajar con tiempos y fechas. La
mayoría de las funciones realizan llamadas al Sistema operativo.

Algunas consideraciones y terminología:

- **UTC** es el tiempo coordinado Universal, anteriormente conocido como GMT o
  Hora de Greenwich (El acrónimo UTC es un compromiso entre el inglés y el
  francés)

- **DST** es el ajuste de horario de verano (*Daylight Saving Time*) una
  modificación de la zona horaria, normalmente de una hora, que se realiza
  durante parte del año. Las reglas de los DST son, en la práctica, pura magia
  (dependen de las leyes locales) y pueden cambiar de año a año,

Los valores de tiempo devueltos por `gmtime()`, `localtime()` y `strptime()`, y
aceptados por `asctime()`, `mktime()` y `strftime()` son tuplas (En realidad,
`namedtuple`) de 9 enteros: año, mes, día, horas, minutos, segundos, día de la
semana, día dentro del año y un indicador de si se aplica o no el horario de
verano.

Algunas funciones definidas en este módulo:

## `time()`

Devuelve el tiempo en segundos trascurridos desde el **epoch**, en forma de
número de coma flotante. 

El **[Epoch](https://en.wikipedia.org/wiki/Epoch)** es una marca temporal fija que
se estableció como el inicio del tiempo para los sistemas Unix. Está definido
como el 1 de enero de 1970, a las cero horas, cero minutos, cero segundos UTC.
Los valores anteriores al _epoch_ son, por tanto, negativos.

[ ] **Ejercicio**: Ejecutar `time.time()`, dejar pasar unos segundos y volver a
ejecutarlo. Ver la diferencia entre los valores devueltos.


## `gmtime([secs])`

Convierte un tiempo, indicado en segundos desde el _epoch_, en una tupla de nueve elementos.
 Si no se indica el tiempo, se tomará el momento actual. 

La tupla devuelta en realidad es una [named
tuple](https://docs.python.org/3/library/collections.html#collections.namedtuple),
y por lo tanto podemos acceder también por nombre, además de por posición. La
siguiente tabla muestra los valores contenidos en la tupla:

| Posición | Nombre     | Valor                                   |
|---------:|------------|-----------------------------------------|
| 0        | `tm_year`  | Año                                     |
| 1        | `tm_mon`   | Mes [1..12]                             |
| 3        | `tm_mday`  | Día del mes [1..31]                     |
| 4        | `tm_hour`  | Hora [0..23]                            |
| 5        | `tm_min`   | Minutos [0..59]                         |
| 6        | `tm_sec`   | Segundos [0..61]                        |
| 7        | `tm_wday`  | Día de la semana [0..6], 0 es el Lunes  |
| 8        | `tm_yday`  | Dia del año [1..366]                    |
| 9        | `tm_isdst` | Ajuste horario de verano {-1, 0, 1}     |


El valor final, `tm_isdst`, tiene tres posibles valores: $1$ significa que
el horario de verano está activo, $0$ indica que está inactivo y el valor
especial $-1$ indica que no se sabe.
	
!!! note "Para programadores de C, C++, Java y otros"

    El més se indica en el rango $[1..12]$, por lo que enero
    es el mes $1$. En C y en la mayoría de los lenguajes
    derivados enero es el $0$.

Esta función siempre trabaja con respecto a UTC 0, por lo que es más
conveniente por lo general usar la siguiente función, `localtime`.


## `localtime([secs])`

Como `gmtime()`, pero convertido a tiempo local. El indicador final se pone a
uno si en ese momento estaba activo el horario de verano.

**Ejercicio**: Averiguar si en la fecha actual estamos dentro de la DST u
horario de verano.

## `mktime(t)`

La inversa de `localtime()`. Su argumento es una tupla de 9 elementos. Podemos
poner los tres valores finales a $0$, ya que normalmente no los conocemos --De
hecho, normalmente hacemos esta llamada para averiguarlos. Devuelve un número de
segundos desde el _epoch_.

[ ] **Ejercicio**: Averiguar el día de la semana en que nacieron -O cualquier otra
fecha que les interese-. Si no quieren revelar datos personales, averiguar en que
día de la semana nació [Stan Lee](https://es.wikipedia.org/wiki/Stan_Lee). Su
fecha de nacimiento es el 28 de diciembre de 1922.

![Stan Lee](stan-lee.png)


## `sleep(secs)`

Suspender la ejecución del programa durante el tiempo en segundos indicado como
parámetro.

[ ] **Ejercicio**: Hacer un programa que nos ayude a preparar un té verde. El
programa solo debe esperar por el tiempo perfecto que debe reposar el té verde,
y luego imprimir un mensaje para que retiremos las hojas. El tiempo estimado
ideal de reposo del té verde es de 3 minutos.
