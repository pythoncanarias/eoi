
<h3>Librerias y Entornos virtuales</h3>

- [Requisitos previos del entorno](#requisitos-previos-del-entorno)
- [Instalar librerias](#instalar-librerias)
  - [Requisitos](#requisitos)
  - [Uso](#uso)
- [Entornos virtuales con venv](#entornos-virtuales-con-venv)
  - [Requisitos previos](#requisitos-previos)
  - [Uso](#uso-1)


# Requisitos previos del entorno

Durante este curso trabajaremos con python3. Para evitar confusiones entre si hay que poner python o python3, vamos a crear un alias para poder utilizar ambas formas indistintamente, para eso hay que editar un fichero llamado .bashrc

 ```  
cd  # esto nos asegura que estamos en el directorio home/usuario
nano .bashrc
```

esto nos abre el editor de texto nano, bajamos al final del todo y añadimos las siguientes líneas:

``` 
alias python=python3
alias pip=pip3
```

Salimos con la combinación de teclas *CTRL+X*, pulsamos Y para decir que si queremos guardar, y ENTER para confirmar el nombre
Es necesario cerrar la consola de linux y volverla a abrir para que los cambios tengan efecto.


# Instalar librerias

## Requisitos

Necesitaremos tener instalado pip que es la herramienta de gestión de paquetes (librerías) de python. 
En la consola de linux, escribiremos:

`sudo apt install python3-pip`

## Uso

Para instalar una librería, escribiremos:

`pip3 install nombredelalibreria`

Si la librería ya la tenemos y queremos actualizarla:

`pip3 install nombredelalibreria --upgrade`

**IMPORTANTE** Las librerías estarán disponibles en todo el sistema. Si quereos instalar librerías solo para un entorno virtual (entorno aislado) deberemos asegurarnos de que estamos dentro de ese entorno. Sabremos que estamos dentro de ese entorno si vemos el prefijo (.venv), algo así:

`(.venv) usuario@DESKTOP:~/miproyecto$`


# Entornos virtuales con venv

## Requisitos previos

En la consola de linux, escribiremos:

`sudo apt install python3-venv`

## Uso

Para crear un entorno virtual, usamos el comando cd para movernos a la carpeta raiz de nuestro proyecto, y desde ahí escribimos:

`python -m venv .venv`

Esto nos crea dentro de nuestro proyecto, una carpeta llamada .venv que contendrá tanto el intérprete de python como las librerías que instalemos que estarán disponibles exclusivamente para este proyecto.

Para entrar en ese entorno, desde la raíz del proyecto escribiremos:

`source .venv/bin/activate`

Sabremos que estamos dentro de ese entorno si vemos el prefijo (.venv)

para salir del entorno:

`deactivate`
