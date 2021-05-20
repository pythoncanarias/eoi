---
title: Modelo de Entidad/Relacion (E/R)
---
## Modelo de Entidad/Relación

Un modelo entidad-relación es una herramienta para el modelo de datos, la cual
facilita la representación de entidades de una base de datos. Fue definido por
Peter Chen en 1976.

En este modelo se trabajan con los siguientes conceptos

- Entidades

- Atributos

- Relaciones


### Entidad

Una __entidad__ Representa un  objeto o concepto del mundo real, con existencia independiente, es decir, se diferencia de otro objeto o cosa, incluso siendo del mismo tipo. En un diagrama E/R se representa con un **rectangulo**.

Algunos ejemplos:

- Una persona: se diferencia de cualquier otra persona, incluso siendo gemelos.

- Un automóvil: aunque sean de la misma marca, el mismo modelo, etc, tendrán atributos diferentes, por ejemplo, el número de chasis.

- Una casa: aunque sea exactamente igual a otra, aún se diferenciará en su dirección.

Una entidad puede ser un objeto con existencia física (una persona, una máquina, una estrella, etc. (entidad concreta); o un objeto con existencia conceptual (Un puesto de trabajo, una asignatura de clases, una
habilidad, etc. (entidad abstracta).

Una entidad está descrita y se representa por sus características o atributos. 
Por ejemplo, una entidad Persona puede tener como características: Nombre, Apellido,
Género, Estatura, Peso, Fecha de nacimiento...


### Atributos

Los **atributos** son las características que definen o identifican a una
entidad. Estas pueden ser muchas, y el diseñador utiliza o implementa las
que considere relevantes. En un diagrama de E/R se representan con una
**circunferencia** o una **elipsis**. Los atributos se unen con líneas
a las entidades a las que correspondan.

En un conjunto de entidades del mismo tipo, cada entidad tiene valores
específicos asignados para cada uno de sus atributos, de esta forma, es posible
su identificación unívoca.

Ejemplos:

A la colección de entidades *alumnos*, con el siguiente conjunto de atributos en
común, (id, nombre, edad, semestre), pertenecen las entidades:

    (1, Sophia, 15 años, 2)
    (2, Josefa, 19 años, 5)
    (3, Carlos, 20 años, 2)
    ...

Cada una de las entidades pertenecientes a este conjunto se diferencia de las
demás por el valor de sus atributos. Nótese que dos o más entidades diferentes
pueden tener los mismos valores para algunos de sus atributos, pero nunca para
todos.

En particular, los **atributos identificativos** son aquellos que permiten
diferenciar a una instancia de la entidad de otra distinta. Cualquier atrubuto
o conjunto de atributos que permita diferenciar cualquier entidad del resto de
ellas se denomina **clave candidata**.

Para cada atributo, existe un **dominio** del mismo, este hace referencia al
tipo de datos que será almacenado a restricciones en los valores que el atributo
puede tomar (cadenas de caracteres, números, solo dos letras, solo números
mayores que cero, solo números enteros...).

Cuando algún atributo correspondiente a una entidad no tiene un valor
determinado, recibe el valor nulo, bien sea porque no se conoce, porque no
existe o porque no se sabe nada al respecto del mismo.

### Relaciones

Una __relación__ Consiste en una colección, o conjunto, de relaciones de la
misma naturaleza. las relaciones se representan en los diagramas de E/R con un
**rombo**.

Ejemplo:

Dados los conjuntos de entidades "Habitación" y "Huésped", todas las relaciones
de la forma habitación-huésped, permiten obtener la información de los huéspedes
y sus respectivas habitaciones.

La dependencia o asociación entre los conjuntos de entidades es llamada
participación. En el ejemplo anterior los conjuntos de entidades "Habitación" y
"Huésped" participan en el conjunto de relaciones habitación-huésped.

Se llama grado del conjunto de relaciones a la cantidad de conjuntos de
entidades participantes en la relación.

Es importante hacer notar que todas las relaciones entre modelos deben
representarse con relaciones, y por tanto nunca sera posible tener
una línea que una directamente a un modelo con otro, siempre habrá de pasar
por una relación intermedia.

### Restricciones

Son reglas que deben respetar las entidades y relaciones almacenadas en la base
de datos.

**Correspondencia de cardinalidad**: Dado un conjunto de relaciones en el que
participan dos o más conjuntos de entidades, la cardinalidad de la
correspondencia indica el **número de entidades** con las que puede estar
relacionada una entidad dada.

Dado un conjunto de relaciones binarias y los conjuntos de entidades A y B, las
cardinalidades pueden ser:

* __Uno a Uno__: (1:1) Una entidad A se relaciona con solo una entidad B.
  (ejemplo dos entidades, profesor y departamento: si un profesor solo puede ser jefe
  de un departamento y un departamento solo puede tener un jefe).

* __Uno a Varios__: (1:N) Una entidad en A se relaciona con cero o más entidades
  B. Pero los registros de B solamente se relacionan con un registro en A.
  (ejemplo: dos entidades, vendedor y ventas: un vendedor puede tener muchas
  ventas pero una venta solo puede tener un vendedor).

* __Varios a Uno__: (N:1) La inversa de la anterior. Una entidad A se relaciona
  exclusivamente con una entidad B. Pero una entidad en B se puede relacionar
  con 0 o más entidades en A (ejemplo empleado-centro de trabajo).

- **Varios a Varios**: (N:M) Una entidad en A se puede relacionar con 0 o con
  más entidades en B y viceversa (ejemplo asociaciones-ciudadanos, donde muchos
ciudadanos pueden pertenecer a una misma asociación, y cada ciudadano puede
pertenecer a muchas asociaciones distintas).

Chen propuso las siguientes reglas informales para mapear
descripciones en lenguaje natural a los conceptos usados en
los diagramas E/R.

| estructura gramatical     |     | Concepto E/R                 |
|--------------------------:|:---:|------------------------------|
| Sustantivo                |  ⇆  | Entidad  ☐                   |
| Verbo transitivo          |  ⇆  | Relación ◊                   |
| Verbo intransitivo        |  ⇆  | Atributo ◯                   |
| Adjetivo                  |  ⇆  | Atributo ◯ (De una entidad)  |
| Adverbio                  |  ⇆  | Atributo ◯ (De una relacion) |

### Ejemplo 

![Shield](img/shield.svg)

![Nick Fury](img/nick-fury.jpg)

Primera mision: Una página web con un listado de nombres de supers
y su nivel de peligro.

[superheroes.csv](superheroes.csv)


