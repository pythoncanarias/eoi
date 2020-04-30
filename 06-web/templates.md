Plantillas
==========

Vamos a reimplementar el ejemplo del hola, mundo, usado plantillas.
Vamos a ir haciendo la cosas de forma prograsiva: Empezaremos por hacer
las cosas rápido y mal, e iremos mejorándolas hasta llegar a la forma
\"correcta\". Así entenderemos mejor el porqué de algunas de las
decisiones tomadas en el diseño de Django.

Las plantillas son simplemente documentos de texto, normalmente html,
aunque nada impide que se use con cualquier otro tipo de textos, como
XML o código C. En el texto de las plantillas hay ciertos marcas o
etiquetas (*template tags*) que indican que en ese sitio falta
contenido, el cual será incluido más adelante. La etiqueta más sencilla
tiene la forma:

    {{ nombre }}

Esto indica que, en el resultado final, sustituiremos todo el texto
comprendido entre las marcas `{{` y `}}` (Incluyendo las marcas) por el
contenido de una variable llamada `nombre`. Como siempre, es más fácil
verlo con un ejemplo.

Podemos crear una plantilla instanciandola de la clase
`django.template.Template`. Al instanciarla, podemos indicarle el texto
que queremos usar:

    from django.templates import Template

    t = Template('Hola, {{ nombre }}. ¿Cómo estás?')

Podemos ahora fusionar esta plantilla `t` con algo que tenga el dato que
queremos incluir, el nombre. Para ello se usa un objeto de la clase
`Context`, que podemos crear pasándole un diccionario con las parejas
nombre/valor que queremos usar en la plantilla. Este objeto será el
**contexto** que usa la plantilla para producir un resulltado final.
Dicho y hecho:

    from django.template import Template, Context

    t = Template('Hola, {{ nombre }}. ¿Cómo estás?')
    ctx = Context({'nombre': 'Stan Lee'})

La fusión de plantilla se realiza con el método `render` de la
plantilla. Le pasamos el contexto deseado y devuelve el texto final, con
los datos sustituyendo las marcas. Diferentes contextos producen
diferentes resultados para la misma plantilla:

    from django.template import Template, Context

    t = Template('Hola, {{ nombre }}. ¿Cómo estás?')
    ctx = Context({'nombre': 'Stan Lee'})
    assert t.render(ctx) == 'Hola, Stan Lee. ¿Cómo estás?'
    ctx = Context({'nombre': 'Jack Kirby'})
    assert t.render(ctx) == 'Hola, Jack Kirby. ¿Cómo estás?'

Usando plantillas, nuestra primera aproximación podría ser:

    from django.http import HttpResponse
    from django.template import Template, RequestContext

    def homepage(request):
        t = Template('''<html>
        <head>
          <title>Shield.com</title>
        </head>
        <body>
        <h1>Bienvenidos a S.H.I.E.L.D.</h1>
        <p>{{ message }}</p>
        </body>
        </html>''')
        ctx = RequestContext(request, {
            'message': '¡En obras! Pronto abriremos',
            })
        return HttpResponse(t.render(ctx))

El primer cambio es sustituir el objeto `Context` por una versión más
potente (será de utilidad más adelante) llamada `RequestContext`. Esta
versión funciona igual que el `Context` pero nos añade información
sacándola de la petición `request`, el primer parámetro de todas las
vistas. Para instanciar un `RequestContext` le pasamos el objeto
`request` y como segundo parámetro un diccionario con nuestros datos.

Obviamente, cargar el texto de la plantilla desde el propio código no es
muy operativo. Podríamos usar una función para leer el contenido de la
plantilla desde ficheros externos, pero como pasa a menudo, la gente de
Django se nos ha adelantado. Podemos confiar en el cargador de
plantillas de Django para que cargue las plantillas desde el sistema de
ficheros. Veamos como funciona.

Si le decimos a Django que nos busque una plantilla determinada,
indicándole el nombre de un fichero, por ejemplo, `hola.html`, el
cargador que viene activo por defecto busca dentro de cada una de las
aplicaciones instaladas una carpeta que se llame `templates`. Si en
cualquiera de esos directorios encuentra un archivo que se llame
`hola.html`, creará una plantilla a partir del texto de ese fichero. Si
existe más de un fichero `hola.html`, usará el primero que encuentre.
Esto puede ser útil en ciertas ocasiones. También puede ser fuente de
errores y frustración en otras.

Por tanto, creemos un directorio `templantes` dentro de nuestra única
aplicación por ahora, y dentro escribimos un fichero `homepage.html`. El
código quedaría ahora así:

    from django.http import HttpResponse
    from django.template import Template, RequestContext
    from django.templae.loader import get_template

    def homepage(request):
        t = get_template('homepage.html')
        ctx = RequestContext(request, {
            'message': '¡En obras! Pronto abriremos',
            })
        return HttpResponse(t.render(ctx))

Es tan frecuente esta secuencia de operaciones: Obtener una plantilla,
fusionarla con una serie de datos que hemos obtenido o calculado
previamente, usando un `RequestContext`, y devolver el resultado en
forma de `HttpResponse` que hay una forma abreviada para hacerlo todo en
un solo paso: la función `django.shortcuts.render`. Usándola, el código
final quedaría asi:

    from django.shortcuts import render

    def homepage(request):
        ctx = { 'message': '¡En obras! Pronto abriremos' }
        return render(request, 'homepage.html', ctx)

Ya no hace falta importar `get_template`, `RequestContext` ni
`HttpResponse`.

Vamos a realizar un par de ejercicios de ejemplo

> -   Mostrar una lista de superheroes.
> -   Mostrar una lista de superheroes, pero que se vean los nombres en
>     negrita o de color rojo (o cualquier otra cosa que sirva para
>     destacarlos) si su nivel es de 5 o superior y verde si es 4 o
>     inferior

Para ello vamos a necesitar dos etiquetas nuevas: `for` e `if`.

Herencia de plantillas
----------------------

Una de las partes más potentes de las plantillas es que mantiene un
sistema de herencia, equivalente al que podemos encontrar en cualquier
sistema orientado a objetos. Al igual que en estos sistemas, se parte de
un concepto general, que se va particularizando mediante herencias.

En los sistemas de plantillas que no tiene herencia, lo normal es que
tengan la posibilidad de incluir otros ficheros. La herencia de
plantillas es similar, pero con un pequeño giro conceptual que lo hace a
la vez más sencillo y más potente, una vez se entiende su funcionamieno.

En un sistema que trabaja con inclusión de ficheros, normalmente tenemos
un fichero de cabecera y un fichero de pie, que van respectivamente al
principio y al final de cada página. El código se limita a incluir la
cabecera, hacer su trabajo y a continuación incluir el pie. Con este
sistema, lo que hacemos es definir en los ficheros a incluir **las
partes que son iguales para todas lás páginas**.

Imaginemos que en el pie de cada página está nuestro teléfono de
asistencia, y que dicho número ha cambiado. Queremos que el cambio se
refleje en todas las páginas hechas hasta ahora. Como hemos tenido la
precaución de separar el contenido del pie en un único fichero, el
cambio es fácil.

Sin embargo, otros cambios no son tan fáciles. Imaginemos que nos piden
ahora otro cambio aparentemente trivial: que en el *title* de cada
página vaya, añadido al final, la dirección acortada de nuestra web. Es
decir, que una página titulada \"Acerca de\", deberá titularse ahora
\"Acerca de -shield.com\". Esto implica que la página de cabecera, que
antes era *igual* para cada página, ahora es *distinta* para cada
página.

Con el sistema de Django, partimos de una página base, una página que
dice: \"Todas las paginas de este sitio como yo\", y le indicamos,
usando las tag `block` y `endblock`, las distintas zonas que pueden ser
diferentes. Podemos crear una plantilla hija o derivada de esta
plantilla base, que reescribe esas zonas diferentes.

Veamos un ejemplo. Supongamos que tenemos en este momento 4 páginas web:
El siguiente esquema muestra en gris las partes que son iguales en todas
las páginas, y en verde las que son diferentes:

![image](docs/herencia_plantillas_ejemplo_01.png)

Vemos que hay una cabecera con espacio reservado para el titulo que
varía en cada página. Aparte de eso, la cabecera es igual, con el logo y
el nombre del sitio. Las páginas A y C son casi iguales. La página B
incluye una sección de anuncios, ausente en las demas. La página D, por
otro lado, define un recurso diferente en el pie, que las demás no
tiene.

Con el sistema de plantillas, definimos primero una página base, que
incluya todo lo que necesite cualquiera de las paginas hijas. En esta
página base se definiran diferentes zonas o bloques, algunos de ellos
posiblemente vacios, para indicar las partes que pueden cambiar. Luego
cada una de las paginas hijas redefine solo las partes que le interesen.
Podemos representarlo en el siguiente gráfico, donde las zonas vacias en
la plantilla base se indican en azul claro:

![image](docs/herencia_plantillas_ejemplo_02.png)

Ahora, realizar un cambio que afecte a todas lás páginas solo implica
tocar la plantilla base. Además, no hace falta marcar todas las zonas
previamente. En el ejemplo anterior, todas las páginas tienen el mismo
logo; si ahora nos pidieran crear una nueva página, la quinta, pero con
un logo diferente, solo tenemos que editar la plantilla base, definir la
zona del logo como un bloque reemplazable, dejar el logo actual como
contenido por defecto, y crear luego una nueva plantilla para la nueva
página, derivada de base y que reescriba la parte del logo.

No hay límite en los níveles de herencia. por ejemplo, si nuestro site
se divide en cuatro secciones: A, B,C, D, podemos definir una plantilla:
`base.html`, luego una base para cada una de la secciones:
`base_a.html`, `base_b.html`, `base_c.html` y `base_d.html` (todas
ellas, derivadas de `base.html`), y finalmente las plantilla de páginas
finales, que extienden de la plantilla [base\_\*.html]{.title-ref}\` que
corresponda.

Para marcar una zona como modificable por las plantillas hijas se usan
las marcas `block` y `endblock`. Con el tag de inicio se define el
nombre que le vamos a dar al bloque, para identificarlo. En la marca de
fin de bloque no es necesario especificar el nombre, pero podemos
hacerlo si queremos. Para nuestras páginas iniciales partimos de este
esquema, bastante espartano, hay que reconocerlo:

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>{{ title }}</title>
      </head>
      <body>

        <h1>Bienvenidos a S.H.I.E.L.D.</h1>
        <h2>Sistema Homologado de Inteligencia, Espionaje, Logística, y Defensa</h2>
        <h3>{{ title }}</h3>

        {% block content %}

        {% endblock content %}

      </body>
    </html>

Solo hay un bloque, que hemos llamado `content`, el título de la página
lo hemos incluido como una variable, que cada vista definirá de la forma
que crea conveniente,pero es solo una preferencia por mi parte; se
podría haber especificado el título con un bloque perfectamente.

La plantilla de la página que nos presenta la lista de superheroes puede
ser tan sencilla como:

    {% extends "base.html" %}

    {% block content %}
      <ul>
        {% for h in heroes %}
          <li>{{ h.name }} ({{ h.level }})</li>
        {% endfor %}
      </ul>
    {% endblock content %}

Hemos usado la etiqueta `extends` para indicar que esta plantilla es
hija de `base.html`. La etiqueta `extends`, si se usa, tiene que ser
obligatoriamente la primera que aparezca en la página. No se permite
herencia múltiple, es decir, una plantilla solo puede tener un padre.

La vista que podriamos escribir para esta plantillas podría ser:

    from metahumans import SuperHero

    def view_all_heroes(request):
        return render(request, 'view_all_heroes.html', {
            'heroes': SuperHero.objects.all(),
            'title': 'Listado de superhéroes',
            })

¿Se puede hacer aun más sencillo? Si, con las vistas genéricas, que
veremos más adelante, pero por ahora es bastante compacto.

Ventajas de las plantillas
--------------------------

El uso de un buen sistema de plantillas presenta muchas ventajas:

> -   Las plantillas pueden ser editadas y modificadas por especialistas
>     en diseño o experiencia de usuario sin necesitar conocimientos de
>     programación. Al fin y al cabo, son como cualquier otra página
>     web, solo que con algunas marcas especiales más.
> -   El sistema de herencias y la inclusión de plantillas es realmente
>     potente, y permite realizar modificaciones globales en la
>     aplicación tocando un solo fichero.
> -   El sistema deja que algunos problemas se puedan resolver usando
>     etiquetas y filtros, y permite incluir un poco de lógica en las
>     vistas, pero el sistema está diseñado expresamente para que
>     etiquetas y filtros sean, desde el punto de vista de un
>     programador, pobres.

Aunque puede parecer extraño diseñar una parte del sistema para que sea
débil, existe una razón. La idea es forzar a hacer las tareas realmente
complejas en la vista, donde disponemos de toda la potencia del lenguaje
Python, y que lo hagan los programadores. La lógica de la vista está
pensada para ayudar a los los diseñadores, no para crear un segundo
lenguaje de programación.
