
Glosario
=======================================================================

.. glossary::

   DBMS

      `DBMS`_ son las iniciales de (*Data Base Management System*),
      también se conoce en español con el acrónimo **SGBD** (Sistema de
      Gestión de Bases de Datos). Es un *software* que permite
      administrar una base de datos. Proporciona el método de
      organización necesario para el almacenamiento y recuperación
      flexible de grandes cantidades de datos. Esto significa que
      mediante este programa se facilita el utilizar, configurar y
      extraer información almacenada. Los usuarios pueden acceder a la
      información usando herramientas específicas de consulta y de
      generación de informes, o bien mediante aplicaciones al efecto. 

      .. _DBMS: https://es.wikipedia.org/wiki/Sistema_de_gesti%C3%B3n_de_bases_de_datos

   Django

      `Django`_ es un *Framework** para el desarrollo de páginas Web
      escrito en Python. Su nonmbre es una alusión al guitarrista de 
      jazz gitano Django Reinhardt.

      .. _Django: https://www.djangoproject.com/

   idempotente

      Una operación que produce los mismos resultados si se ejecuta una
      o varias veces. Esto puede tener diferentes significados,
      dependiendo del contexto en que se aplique. En el caso de métodos
      o llamados a funciones con efectos secundarios, por ejemplo, esto
      significa que el estado modificado permanece igual luego de la
      primera llamada.

      Esta es una propiedad muy útil en numerosas situaciones, ya que
      permite que la operación pueda ser repetida tantas veces como sea
      necesario sin causar efectos involuntarios. Con operaciones no
      idempotentes, habría que mantener un registro de si la operación
      ha sido realizada ya o no.

   píxel

      En informática, la unidad mínima que forma una imagen digital.  Un
      píxel usualmente se visualiza como un punto o un cuadrado, pero
      conceptualmente no tiene una forma determinada. Se puede decir que
      se trata de una muestra abstracta o una unidad de medida de
      resolución de pantalla. 

   Pygame

      `Pygame`_ es una librería de videojuegos en 2D para el lenguaje de
      programación Python. Está basada en `SDL`_, que es una librería
      escrita en C que da acceso de bajo nivel al audio, teclado, ratón
      y al *hardware* gráfico de nuestro ordenador.
       
      .. _Pygame: https://www.pygame.org/
      .. _SDL: https://www.libsdl.org/

   queryset

      Un objeto que almacena una consulta a la base de datos. Tienen la
      particularidad de ser *lazy*, esto es, solo se ejecuta la consulta
      a la base de datos cuando realmente es necesario.

      Por ejemplo, si creamos un queryset, pero nunca lo llegamos a
      utilizar, la consulta nunca se accede a la base de datos. Pero si,
      por ejemplo, iteramos un queryset con un bucle ``for``, ya no se
      puede postergar más la realización de la consulta, así que en ese
      momento (Al inicio del bucle) se realiza la consulta.

   Redis

      `Redis`_ es un motor de base de datos en memoria, basado en el
      almacenamiento en tablas de *hashes* (clave/valor) pero que
      opcionalmente puede ser usada como una base de datos durable o
      persistente. Está escrito en ANSI C por Salvatore Sanfilippo,
      quien es patrocinado por Redis Labs.

      .. _Redis: https://redis.io/ 

   UUID

      Un **IDentificador  Único Universal** (*Universally Unique
      IDentifier, `UUID`_*) es un número de 128 bits, con lo que el número
      de posibles UUID diferentes sería de :math:`2^128`, o unos 
      :math:`3,4\times 10^{38}`. En
      su forma canónica un UUID se expresa mediante 32 dígitos
      hexadecimales divididos en cinco grupos separados por guiones de
      la forma 8-4-4-4-12 lo que da un total de 36 caracteres (32
      dígitos y 4 guiones). Por ejemplo:
      550e8400-e29b-41d4-a716-446655440000

      .. _UUID: https://es.wikipedia.org/wiki/Identificador_%C3%BAnico_universal
