La librería xml
===============

Los diferentes módulos de Python para trabajar con ficheros XML están agrupados
en el paquete ``xml``.

Las dos formas más habituales de trabajar con un fichero XML son :term:DOM
(*Document Object Model*) y :term:SAX (*Simple API for XML*). Ambas están
disponibles en los módulos ``xml.dom`` y ``xml.sax`` respectivamente.

Usando el modelo DOM tenemos acceso a todo el árbol de una sola vez, lo que
puede ser costoso en terminos de almacenamiento en memoría. Con SAX procesamos
el árbol paso a paso, respondiendo ante ciertos eventos, a medida que se van
abriendo y cerrando los nodos. Con esta segunda forma perdemos cierta
flexibilidad pero no tenemos el problema del almacenamiento completo del árbol
en memoria.

XML es un formato de datos jerárquico, con lo que la forma maás habitual de
representarlo es un árbol. Para eso se definen las clases ``ElementTree``, que
representa todo el documento XML a tratar, y ``Element``, que representa a un
nodo dentro del árbol. Las interacciones con el documento como un todo, como
por ejemplo leerlo o guardarlo en un fichero en disco, se hacen normalmente a
nivel de ``ElementTree``. Las interacciones con un elemento XML o sus
subelementos se realizan en el nivel de ``Element``.

Usaremos para explicar estos módulos el siguiente documento XML:

.. literalinclude:: country_data.xml
    :language: xml

Lo más básico es importar y leer estos datos desde un fichero.  Lo podemos
hacer con el siguiente código::

    import xml.etree.ElementTree as ET
    tree = ET.parse('country_data.xml')
    root = tree.getroot()

O también podemos leer los datos a partir de una variable de tipo string:

    root = ET.fromstring(country_data_as_string)

Como ``root`` es un elemento (un objeto de la clase ``Element``), tiene una
etiqueta (``tag``) y un conjunto de atributos, en forma de diccionario::

    >>> root.tag
    'data'
    >>> root.attrib
    {}
    >>>

También tiene una serie de hijos, sobre los que podemos iterar::

    >>> for child in root:
    ...   print(child.tag, child.attrib)
    ...
    country {'name': 'Liechtenstein'}
    country {'name': 'Singapore'}
    country {'name': 'Panama'}
    >>>

También podemos acceder a los hijos usando índices::

    >>> root[0][1].text
    '2008'
    >>>

La clase ``Element`` define una serie de método que nos ayudan a recorrer
recursivamente todo el subárbol que haya debajo de él (Sus hijos, nietos,
etc...). Por ejemplo, el método ``iter()``::

    >>> for neighbor in root.iter('neighbor'):
    ...   print(neighbor.attrib)
    ...
    {'name': 'Austria', 'direction': 'E'}
    {'name': 'Switzerland', 'direction': 'W'}
    {'name': 'Malaysia', 'direction': 'N'}
    {'name': 'Costa Rica', 'direction': 'W'}
    {'name': 'Colombia', 'direction': 'E'}
    >>>

El método ``Element.findall()`` localiza sólo los elementos de una determinada
etiqueta que son hijos directos del nodo actual. El método ``Element.find()``
encuentra el primer hijo que cumpla esta misma condición. Con ``Element.text``
podemos acceder al contenido textual del elemento, y con ``Element.get``
podemos acceder a los valores de sus atributos::

    >>> for country in root.findall('country'):
    ...   rank = country.find('rank').text
    ...   name = country.get('name')
    ...   print(name, rank)
    ...
    Liechtenstein 1
    Singapore 4
    Panama 68
    >>>

Se pueden hacer operaciones de búsqueda aun más sofisticadas
usando Xpath_.
