Para poder trabajar con Django, debemos de hacerlo fuera de Jupyter.
Trabajaremos desde la consola y desde un edior de textos. El primer
paso es abrir la consola en el directorio de trabajo que queremos
y comprobar que tenemos la version de Python correcta instalada
y disponible

Ejecutemos desde la terminal:

    python -V

o

    python3 -V

En el resto de la documentacion, solo ejecutaré `python` y `pip`, sin el 3 después. Si
lo tienes instalado como `python3` o `pip3` haz el cambio mentalmente.

Para verificar que Django está instalado haremos

    python -c "import django"

De nuevo, la ausencia de mensajes de error es buena noticia. Si diera un
error, instalar django como pip:

    pip install django


Ahora, el siguiente paso será crear nuestra aplicación. Django, al instalarse, he añadido 
una utilidad muy cómoda que permite crear una aplicación mínima al toque.
Podemos ejecutar esta utilidad haciendo:




