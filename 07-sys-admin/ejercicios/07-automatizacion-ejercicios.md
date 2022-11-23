# Ejercicios de automatización

## Crear una mini-wikipedia

Crear una api con FastApi a la cual le puedas pasar un término de búsqueda por la URL y te devuelva en formato json los principales campos de la wikipedia para el término introducido.

Podéis encontrar la documentación de la API aquí: https://www.mediawiki.org/wiki/API:Tutorial

Un ejemplo de url: 'http://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=carol shaw&format=json'

## Descargar los comics de XKCD
Los blogs y otros sitios web que se actualizan periódicamente suelen tener una página principal con la publicación más reciente, así como un botón Anterior en la página que lo lleva a la publicación anterior: esa publicación anterior también tendrá un botón Anterior, y así sucesivamente, creando un rastro desde la página más reciente hasta la primera publicación en el sitio.

Imagina que queremos hacer una copia del contenido del blog para leer cuando no está en línea, o simplemente una copia de seguridad por si algún día la web no está disponible. Este trabajo puede ser bastante tedioso, así que vamos a escribir un programa para hacerlo.

XKCD es un popular webcomic publicado en una web que se ajusta a esta estructura. La página principal en https://xkcd.com/ tiene un botón Anterior que guía al usuario a través de cómics anteriores. Descargar cada cómic a mano llevaría una eternidad, así que este ejercicio consiste en escribir un script que descargue los comics (para que sea más rápido, podemos descargar un máximo de 10 comics) y los guarde en una carpeta de nuestro sistema.

Lo que hará el script es:
Here’s what your program does:
- Cargar la página de XKCD usando la librería requests
- Parsear el hml que devuelve con la librería `beautifulsoup` (`pip install beautifulsoup4`)
  * para encontrar el elemento con la imagen, puedes probar `soup.select('#comic img')` y `comic_element[0].get('src')` para obtener la url del comic actual
- Guardar el contenido de la url del comic en un fichero
  * para esto puedes probar algo como:
    ```python
    with open(os.path.join(folder_name, os.path.basename(comic_url)), 'wb') as f:
        f.write(res.content)
    ```
- Buscar el enlace del botón "Previous"
  * para esto prueba con algo como `soup.select('a[rel="prev"]')[0]`
- Realizar todo el proceso anterior con esa nueva URL

## Copia de seguridad de una carpeta en un archivo ZIP

Digamos que está trabajando en un proyecto cuyos archivos guarda en una carpeta llamada `/tmp/python-files/`. 

Le preocupa perder su trabajo, por lo que le gustaría crear "instantáneas" de archivos ZIP de toda la carpeta. 

Además te gustaría mantener diferentes versiones, por lo que desea que el nombre de archivo del archivo ZIP aumente cada vez que se crea; por ejemplo, python-files_1.zip, python-files_2.zip, python-files_3.zip, etc.

Puede hacer esto a mano, pero es bastante molesto y podría equivocarse en la numeración accidental de los nombres de los archivos ZIP. Sería mucho más sencillo ejecutar un programa que haga esta aburrida tarea por ti.

## Generación de archivos de cuestionarios aleatorios

Supongamos que es profesor de geografía con 35 estudiantes en su clase y desea realizar un examen sorpresa sobre las capitales de los estados de EE.UU. Por desgracia, su clase tiene algunos alumnos avispados y no puede confiar en que los estudiantes no hagan trampa. Le gustaría aleatorizar el orden de las preguntas para que cada prueba sea única, lo que hace imposible que alguien pueda copiar las respuestas de otra persona. Por supuesto, hacer esto a mano sería un asunto largo y aburrido. Afortunadamente, conoces algo de Python.

Esto es lo que hace el programa:
- Crea 35 cuestionarios diferentes.
- Crea 50 preguntas de opción múltiple para cada cuestionario, en orden aleatorio
- Proporciona la respuesta correcta y tres respuestas incorrectas aleatorias para cada pregunta, en orden aleatorio
- Escribe los cuestionarios en 35 archivos de texto.
- Escribe las claves de respuesta en 35 archivos de texto.

Esto significa que el código deberá hacer lo siguiente:

- Guarda los estados y sus capitales en un diccionario
- Llame a open(), write() y close() para los archivos de texto de preguntas y respuestas
- Use random.shuffle() para aleatorizar el orden de las preguntas y las opciones de opción múltiple


Por ejemplo, para el fichero `capitalsquiz1.txt`, la salida será algo como esto:
```
Name:
Date:
Period:

                    State Capitals Quiz (Form 1)

1. What is the capital of West Virginia?
    A. Hartford
    B. Santa Fe
    C. Harrisburg
    D. Charleston

2. What is the capital of Colorado?
    A. Raleigh
    B. Harrisburg
    C. Denver
    D. Lincoln
```
... hasta 50

---

Y para el fichero `capitalsquiz_answers1.txt` la salida tiene que ser:
```
    1. D
    2. C
    3. A
    4. C
```  
... hasta 50


```python
capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}
```
