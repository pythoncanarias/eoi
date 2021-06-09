### Introducción al desarrollo de aplicaciones de escritorio

Una aplicación de escritorio es aquella que se encuentra 
instalado localmente en el ordenador, y que presentan al usuario
una interfaz gráfica que suele usar metaforas comunes en todos
los sistemas operativos modernos, como ventanas, menus, controles,
barras de scroll, iconos, etc.

Una ventaja de las aplicaciones de escritoprio es que, al estar instaladas
localmente, no requieren acceso a Internet para funcionar, y pueden aprovechar
mejor los recursos de la maquina sobre la que se estan ejecutando. Entre los
inconvenientes, habria que destacar:

- Normalmente son mas complicadas de desarrollar

- Dependiendo de la tecnología usada,puede que solo funcionen
  en una plataforma determinada.

- Los cambios en el programa implican una reinstalacion del mismo.

Se pueden escribir aplicaciones de escritorio con cualquier lenguaje moderno, lo
que incluye por supuesto a Python. Además, al ser Python
multiplataforma, los *frameworks* y librerias para desarroloos de escritorio
también suelen ser multiplataforma, lo que nos permite tener una misma aplicacion, o con pequeñas diferencias, funcionando en Windows, Linux o Mac. En ese aspecto una de las más potentes es Kivy, que es sobre la que vamos a trabajar mas en profuncidad, ya que nos permite escribir aplicaciones que funciones en Linux, Windows, OS X, Android, iOS, and Raspberry Pi

### Opciones par desarrollo de aplicaciones de escritorio Python

En Python existen muchas librerias y *frameworks* de desarrollo de aplicaciones de
escritorio, cada una con sus ventajas e inconvenientes. En el siguiente listado 
podemos ver algunas de las
más habituales, y comentaremos ventajas e inconvenientes de cadauna de ellas. Entre los factores que consideraremos estan la facilidad de instalacion y uso, la capacidad
multiplataforma, los controles incorporads y la integración con el sistema operativo, es decir, si la aplicacion :

- [**TK/tkinter**](https://docs.python.org/es/3/library/tkinter.html) Es
  la opción mas básica, y tiene la gran virtud de que viene instalada de serie,
  es una de las librerias estándar de Python (Excepto en Mac, ero eso es por sus
  historias). No es muy buena en el aspecto de estética ni de integración con el
  sistema operativo

- [**Qt5**](https://pygobject.readthedocs.io/en/latest/index.html)
  (PyQt5, pyQt6, PySide) es un binding de la biblioteca gráfica Qt para Python.
  La biblioteca está desarrollada por la firma británica Riverbank Computing y
  está disponible para Windows, GNU/Linux y Mac OS X bajo diferentes licencias.
  [PYQT5](). Entre sus ventajas destaca su potencia y amplio numero de
  controles, asi como una integración muy buena con el sistema operatico. Antes
  era un poco más complicado de instalar en Windows pero se ha mejorado mucho en
  ese aspecto.  Es una instalacion algo pesada, pero es un framework de mucha
  calidad, muy probado y muy potente.

- [**Kivy**](https://kivy.org/) es un marco Python gratuito y de código abierto
  para desarrollar aplicaciones móviles y otro software de aplicación
  multitáctil con una interfaz de usuario natural. Se distribuye según los
  términos de la licencia MIT y se puede ejecutar en Android, iOS, Linux, macOS
  y Windows. Es fácil de instalar, pero la integración con el sistema Operativo
  subyacente no es la mejor. De hecho, toman la dirección contraria: se pretende
  que la estética de los aplicaciones hechas en kivy sean idénticas en todas las
  plataformas.  Sus principales virtudes son el poder desarrollar, ademas de
  para las lataformas de PC, para movilas Andriod y iOS. Relativamente sencillo
  de instalar. Define un lenguaje propio para separar la representacion

- [**pygtk3**](http://pygtk.org/) GTK o _The GIMP Toolkit_ es una
  biblioteca de componentes gráficos multiplataforma para desarrollar interfaces
  gráficas de usuario (GUI). Está licenciado bajo los términos de la GNU LGPL5,
  por lo que permite la creación de tanto software libre como software
  privativo. **PyGTK** es un binding de la biblioteca gráfica GTK para el
  lenguaje de programación Python. La biblioteca GTK se usa para desarrollar el
  entorno gráfico GNOME, así como sus aplicaciones, a la vez que algunos otros
  entornos gráficos.

- [**wxPython**](https://wxpython.org/) Con wxPython tenemos unas
  librerías de desarrollo multiplataforma, que nos permiten crear aplicaciones
  que utilizan realmente las interfaces nativas de cada sistema, de forma que
  nuestras aplicaciones pueden ejecutarse sobre Windows, MAC o Linux con pocas o
  ninguna modificación. Como aspecto negativo, la funcionalidad sele estar
  limitada al minimo comun de todas las plataformas

### Ejemplos en cada uno de estos frameworks

En tkinter:

```python
{% include 'hola-tkinter.py' %}
```

En Qt5:

```python
{% include 'hola-qt5.py' %}
```

En WxPython:

```python
{% include 'hola-wx.py' %}
```

En Gtk:

```python
{% include 'hola-gtk.py' %}
```

Y finalmente en kivy:

```python
{% include 'hola-kivy.py' %}
```

Como vemos, a pesar de las diferencias, hay mucho en comun en
todas las versiones:

1) Normalmente tenemos el concepto de  *App*
que representa la aplicacion em si, de la cual solo hay una instancia, y luego 
tenemos algun tipo de ventana. En los ejemplos mostrados solo
se crea una ventana, pero lo normal es tener varias ventanas
disponibls, de las cuales una es la principal

2) se usan componentes estandar, como etiquetas o botones, Ademas de lo visto en los ejemplos, tenemos mas tipos de controles que podemos encontrarnos:

- La etiqeuta
- El botón

- La lista de elementos

- Entrada de texto

- El ComboBox o Combo: Una combinación de entrada de texto y lista. Normalente
  se muestra como un cuador de texto acompañado por una flecha que despliega
  la lista de opciones

- Radio Buttons

- Checkbox

La mayoria de estos tipos de controles ya estaban disponibles en la primera plataforma que soportaba en SmallTalk-76

![Smalltak-76](smalltalk-76.png)

3) Normalmente hay una fase previa de preparación de los controles y ventanas necesarios, para luego ceder finalmente el control al propio framework. A partir de ahí, sera este el que invocará a nuestros funiones o métodos en base a las acciones del usuario. Esto se conoce
generalmente como programción orientada a eventos.

**Pregunta** Tanto la opción de checkbox como los radio buttons nos permite marcra
opciones de tipo binario o Si/No. ¿Cuál es la diferencia entre ellas?

![ejmplo de checkboxs](checkboxs.png)

![ejmplo de radio buttons](radios.png)

**Respuesta**: Las diferentes opciones, si se usan checkbox, son independientes entre si, pero si se usan radio buttons, entonces las distintas opciones son mutuamente excluyentes entre si, es decir, solo puede haber una seleccionada.

Estas convenciones y muchas más que reconocemos aun sin darnos quiza cuenta , como por ejemplo la tacla F1 para la función de ayuda, cerrar una ventana con Alt-F4, etc. fueron definidas en un documento llamada [Common User Access](https://en.wikipedia.org/wiki/IBM_Common_User_Access) definido por IBM a finales de los 80. Junto con la guia de Apple
[HIG Human interface guidelines](https://en.wikipedia.org/wiki/Human_interface_guidelines)
son documentos que convien por lo menos repasar para no romper las reglas que la mayoría de usuarios esperan encontrar en un programa.


Bibliografía
------------

-   wxPython 2.8 Application Development Cookbook, Cody Precord (Packt
    Publishing)
    \- \[Packt
    Publishing\](<https://www.packtpub.com/product/wxpython-2-8-application-development-cookbook/9781849511780>)
    -   \[Amazon\](<https://www.amazon.es/Wxpython-2-8-Application-Development-Cookbook/dp/1849511780>)

Enlaces
-------

-   [The Python GTK+ 3
    Tutorial](https://python-gtk-3-tutorial.readthedocs.io/en/latest/)
