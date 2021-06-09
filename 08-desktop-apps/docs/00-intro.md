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


-   **Qt5** (PyQt5, pyQt6, PySide) es un binding de la biblioteca
    gráfica Qt para Python. La biblioteca está desarrollada por la firma
    británica Riverbank Computing y está disponible para Windows,
    GNU/Linux y Mac OS X bajo diferentes licencias.
    [PYQT5](https://pygobject.readthedocs.io/en/latest/index.html).
    
    Entre sus
    ventajas destaca su potencia y amplio numero de controles, asi como
    una integración muy bueno con el sistema operatico
    
-   [**Kivy**](https://kivy.org/) es un marco Python gratuito y de código abierto para
    desarrollar aplicaciones móviles y otro software de aplicación
    multitáctil con una interfaz de usuario natural. Se distribuye según
    los términos de la licencia MIT y se puede ejecutar en Android, iOS,
    Linux, macOS y Windows.

-   [**pygtk3**](http://pygtk.org/) GTK o The GIMP Toolkit es una biblioteca de componentes
    gráficos multiplataforma para desarrollar interfaces gráficas de
    usuario (GUI). Está licenciado bajo los términos de la GNU LGPL5,
    por lo que permite la creación de tanto software libre como software
    privativo. **PyGTK** es un binding de la biblioteca gráfica GTK para
    el lenguaje de programación Python. La biblioteca GTK se usa para
    desarrollar el entorno gráfico GNOME, así como sus aplicaciones, a
    la vez que algunos otros entornos gráficos.

-   [**wxPython**](https://wxpython.org/) Con wxPython tenemos unas
    librerías de desarrollo multiplataforma, que nos permiten crear
    aplicaciones que utilizan realmente las interfaces nativas de cada
    sistema, de forma que nuestras aplicaciones pueden ejecutarse sobre
    Windows, MAC o Linux con pocas o ninguna modificación. Como aspecto
    negativo, la funcionalidad sele estar limitada al minimo comun de
    todas las plataformas

-   pyside

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
