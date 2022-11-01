---
title: sched -  Programador de eventos
---
## Introducción a `sched`

Para algunas aplicaciones (como los *bots* o herramientas de monitorización,
por ejemplo) se necesita ejecutar determinadas acciones en momentos
determinados o a intervalos determinados. El módulo de la librería estándar
**sched** proporciona esta funcionalidad.

Los sistemas operativos proporcionan en muchos casos esta misma funcionalidad,
por ejemplo [cron](https://es.wikipedia.org/wiki/Cron_(Unix)) en Linux o [Task
scheduler](https://es.wikipedia.org/wiki/Planificador_de_tareas_(Windows)) en
*Windows*, la ventaja de usar el módulo de Python es que nos aisla de las
diferencias en las plataformas, y que nos permite incluir estas tareas
programadas como parte de nuestro programa.

La documentación de `sched` es breve, pero se puede entender fácilmente con
algunos ejemplos.

### Ejecutar tareas de forma periódica o desplazadas en el tiempo


Lo más sencillo es programar una tarea para que se ejecute después de un lapso
de tiempo:

``` python
{% include 'standard/06-sched/ejemplo01.py' %}
```

Los pasos que damos son:

1. Se crea una instancia de un objeto `scheduler`.

2. Se define una función, `saytime()`, que en nuestro ejemplo se limita a
   escribir por pantalla la hora actual.

3. Esta es una línea interesante. Lo último que hace la función, justo antes de
   terminar, es reprogramarse a si misma otra vez, para ser llamada o invocada
   otra vez, transcurridos 10 segundos.

4. Se ejecuta el método `run()` del controlador `scheduler`, con el parámetro
   `blocking` a verdadero. En este punto estamos cediendo el control del
   programa al `scheculer`, que ejecutara las tareas que tenga programadas y
   que seguirá haciéndolo hasta que pulsemos la combinación `Ctrl-C`.

**Ejercicio**: Modificar el ejemplo anterior para que se ejecute cada cinco
segundos, en vez de cada 10.

Siendo sinceros, hay un par de cosas en este módulo que resultan un poco
extrañas. Por ejemplo, la obligatoriedad del parámetro `timefunc`, cuando
podría tener el valor por defecto de `time.time()`. Lo mismo al usar el método
`enter`, que nos obliga a definir un valor de prioridad que en principio ni
vamos a usar, y que podría tener perfectamente un valor por omisión. A pesar de
todo, este módulo puede ser interesante siempre que tengamos procesos que se
ejecuten de forma periódica o siguiente un esquema temporal predefinido.

### Ejecutar tareas en un momento determinado

Hemos visto la forma habitual de ejecutar una tarea periódicamente, en este
caso, cada 10 segundos. A veces, sin embargo, lo que necesitamos es ejecutar
ciertas tareas en unos momentos determinados. Por ejemplo, podríamos estar
escribiendo un programa de copias de seguridad que queremos ejecutar a primera
hora de la mañana, digamos a las 08:00 y por la tarde, a las 18:30.

Podríamos hacerlo usando la funcionalidad que ya conocemos, obteniendo el
tiempo actual y calculando el tiempo necesario para que las tareas se ejecuten
en el momento que queremos, pero esto es tedioso y aburrido, así que la
librería proporciona un método específico para estos casos, el método
`enterabs`, en el que simplemente indicamos el momento exacto en que queremos
que se dispare nuestra acción. En el siguiente ejemplo se programa una tarea
para que se ejecute según el esquema previsto, a las 09:00 y a las 18:30:

```python
{% include 'standard/06-sched/ejemplo02.py' %}
```

1. Definimos nuestra función de `backup` (Simulada en este ejemplo)

2. Creamos una instancia de un `scheduler`, como hicimos antes.

3. Obtenemos la fecha actual.

4. En base a la fecha actual, creamos instancias de `datetime` para las ocho de
   la mañana y programamos el *backup* para esa hora.

5. Igual que (4), pero a las cuatro y media de la tarde.

6. Arrancamos el `scheduler` con el método `run`, para que gestione él
   las tareas programadas.


**Ejercicio** Modificar el ejemplo para que se ejecute uno y dos minutos
a partir de la hora actual, para comprobar que el programa está
trabajando correctamente.
:::

La salida debería ser algo similar a esta:

```shell
▶ ./ejemplo02.py 
Esperando por eventos
11:33:00 Empiezo backup /home/jileon/: .......Terminado [OK]
11:34:00 Empiezo backup /home/jileon/: .......Terminado [OK]
```

Esta librería (o por lo menos los conceptos que acabamos de ver de tareas y
eventos) puede ser interesante en los módulo que veremos próximamente,
especialmente en Desarrollo web, *Internet of Things* y desarrollo de juegos.

Se puede conseguir más información en la [documentación oficial de
sched](https://docs.python.org/3/library/sched.html).
