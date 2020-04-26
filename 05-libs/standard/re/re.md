### El módulo re - Expresiones regulares

La librería **`re`** permite trabajar con expresiones regulares.

Una expresión regular viene a definir un conjunto de cadenas de texto que
cumplen un determinado patrón. Si una cadena de texto pertenece al conjunto de
posibles cadenas definidas por la expresión, se dice que casan o que ha habido
una coincidencia o *match*.

Las expresiones regulares se crean combinando expresiones regulares más
pequeñas (o primitivas).

La cadena que define una expresión regular puede incluir caractereres
__normales__ o __especiales__. 

Los caracteres normales solo casan consigo mismo. Por ejemplo, la expresión
regular `a` solo casaría con una a.

Los especiales, como `|` o `.` tienen otros significados; o bien definen
conjuntos de caracteres o modifican a las expresiones regulares adyacentes.

Algunos caracteres con significados especiales son:

| Caracter | Casa con                                                        |
|---------:|-----------------------------------------------------------------|
| `.`      | Cualquier caracter                                              |
| `^`      | El principio de una string                                      | 
| `$`      | El final de una string                                          |
| `*`      | La expresión regular anterior, repetida 0 o más veces           |
| `+`      | La expresión regular anterior, repetida 1 o más veces           |
| `?`      | La expresión regular anterior, 0 o 1 vez                        |
| `{n}`    | La expresión regular anterior, repetida n veces                 |
| `{m,n}`  | La expresión regular anterior, repetida entre m y n veces       |
| `\`      | "Escapa" el significado del caracter a continuación             |
| `|`      | Alernancia entre patrones: `A|B` casa con A o con B             |
| `[...]`  | El conjunto de caracteres definido entre los corchetes          |


En un conjunto Los caracteres se pueden listar individualmente, como por
ejemplo, `[abc]`, que casa con cualquiera de los caracteres `a`, `b` o `c`.
También se pueden espcificar rangos de caracteres, usado el guión para separar
los límites, por ejemplo `[a-z]` casa con cualquier letra minúsucula, `[0-9]`
casa con cualquier dígito. Los caracteres especiales pierden su significado
dentro de los corchetes, por lo que no hace falta escaparlos.

Se puede definir el __complemento del conjunto__ incluyendo como primer
caracter `^`. De esta forma, la expresión regular `[^59]` casa con
cualquier caracter, excepto con los dígitos `5` y `9`.

El uso de expresiones regulares es tremendamente potente y complejo, y
hay varios libros dedicados al tema.

**Ejercicio**: Expresiones regulares para encontrar matrículas de coche.

Escribir una expresión regular para detectar matrículas de coches
españolas.

Según el siguiente texto, que describen en el sistema de matriculación
vigente actualmente en España:

> El 18 de septiembre del año 2000 entró en vigor el nuevo sistema de
> matriculación en españa, introduciendo matrículas que constan de cuatro
> dígitos y tres letras consonantes, suprimiéndose las cinco vocales y las
> letras Ñ, Q, CH y LL. \[...\] Si el vehículo es histórico, y se ha
> matriculado con una placa de nuevo formato, aparece primero una letra H
> en la placa.

El siguiente código lista las matrículas encontradas en el texto:

    import re

    Texto = '''INSTRUIDO por accidente de circulación ocurrido a las 09:43
    entre la motocicleta HONDA 500, matrícula 0765-BBC  y la
    motocicleta HARLEY-DAVIDSON , matrícula 9866-LPX, en el punto
    kilométrico 3.5 de la carretera general del sur, término municipal de
    Arona, Tenerife, y bla, bla, bla...'''

    patron = re.compile('H?[0-9]{4}-?[BCDFGHJKLMNPRSTVWXYZ]{3}', re.IGNORECASE)
    for matricula in patron.findall(Texto):
        print(matricula)

    0765-BBC
    9866-LPX

**Solución** 

El patrón usado es el siguiente:

    H?\[0-9\]{4}-?\[BCDFGHJKLMNPRSTVWXYZ\]{3}
    
Es verdad qye Visto así puede asustar un poco, pero solo es cosa de verlo por
por partes:

- `H?` : Una `H`. Pero como la sigue una interrogación, es opcional.
    Recuerdese que `?` se interpreta como la expresión regular anterior
    (en este caso la H), 0 o 1 vez.

- `[0-9]{4}` : El conjunto de los caracteres del `0` al `9` (`[0-9]`), o
    lo que es lo mismo, cualquier dígito, repetido 4 veces (`{4}`), es
    decir, un número de cuatro dígitos.

-  `-?` : Un guión, opcional, igual que la H para vehículos históricos
    del principio

-   `[BCDFGHJKLMNPRSTVWXYZ\]`{3} : Cualquiera de los caracteres del
    conjunto indicado (letras consonantes excepto la Ñ, Q, CH y LL)
    repetido 3 veces.


