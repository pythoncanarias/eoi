<h1> IOT (Internet de las cosas)</h1>

- [Descripcion](#descripcion)
- [Hardware](#hardware)
  - [Atom Lite](#atom-lite)
- [Instalar MicroPython en el microcontrolador](#instalar-micropython-en-el-microcontrolador)
  - [Linux](#linux)
  - [Windows](#windows)
- [Instalar extension de VSCode](#instalar-extension-de-vscode)
- [Como usar los ejemplos](#como-usar-los-ejemplos)
- [Atribuciones](#atribuciones)


# Descripcion

Para el desarrollo de este modulo, utilizaremos `Micropython`. Micropython es una implementacion de Python 3 optimizada para microcontroladores y dispositivos de recursos reducidos. Tambien contiene un subconjunto de las librerias estandar de Python.


# Hardware

## Atom Lite


Utilizaremos la placa de desarrollo [Atom Lite](https://m5stack.com/products/atom-lite-esp32-development-kit), de [M5Stack](https://m5stack.com), basada en el chip [ESP32-Pico](https://www.espressif.com/en/products/socs/esp32) de [espressif](https://www.espressif.com/)


<table><rd>
    <td><img src="imgs\Atom_lite_01.png" alt="Atom_lite" title="Atom_lite" width="90%" /></td>
    <td><img src="imgs\Atom_lite_02.png" alt="Atom_lite" title="Atom_lite" width="90%" /></td>
</rd></table>


# Instalar MicroPython en el microcontrolador

Para poder trabajar con microcontrolaores, debemos flashear (instalar) el interprete de micropython. Cada familia de microcontroladores tiene sus herramientas para esto (toolkit). En el caso de la familia ESP, utilizaremos esptools. Lo instalamos escribiendo:
```
pip install esptool
```
descargar el interprete de micropython en [micropython.org](https://micropython.org/download/) de tu placa (ESP8266 o ESP32)

La ultima version estable a dia de hoy es 

[esp32-idf3-20200902-v1.13](https://micropython.org/resources/firmware/esp32-idf3-20200902-v1.13.bin)

ahora para subir este firmware a la placa, dependera de tu sistema operativo:


## Linux

```
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 115200 write_flash -z 0x1000 esp32-idf3-20200902-v1.13.bin
```
<em>NOTA cambia el nombre del archivo bin por la version que has descargado</em>

## Windows

Conecta tu placa ESP al ordenador, toca la tecla de windows para buscar y abre `Administrador de dispositivos`

Despliega `Puertos (COM y LPT)` y te apareceran los puertos COM de los dispositivos conectados a tu ordenador, recuerda el numero asignado (8 en el ejemplo)
  
![administrador_dispositivos](imgs\administrador_dispositivos.png)

Si no te aparece este apartado, el equipo no ha reconocido el dispositivo. Esto puede ser normalmente porque te falta el driver, o por que el cable no sea el adecuado (solo tenga alimentacion y no datos) prueba con otro cable.

Abre `PowerShell`  y escribe:

```
cd Downloads  # o donde hayas descargado el archivo bin
esptool.py --port COM8 erase_flash
esptool.py --chip esp32 --port COM8 --baud 115200 write_flash -z 0x1000 esp32-idf3-20200902-v1.13.bin

```
<em>NOTA cambia el numero del puerto COM por el de tu placa, y el nombre del archivo bin por la version que has descargado</em>


# Instalar extension de VSCode

Durante el curso trabajaremos con VSCode y la extension [Pymakr](https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr)

**Antes** de instalar la extension, hay que instalar [Node.js](https://nodejs.org) (recomendado version LTE)


# Como usar los ejemplos

Para utilizar los ejemplos que se conectan a internet, necesitamos crear un fichero 
llamado `credenciales.py` que contenga lo siguiente:
```
ssid = "El_nombre_de_mi_wifi"
password = "la_contraseña_de_mi_wifi"
```
Este fichero tiene que estar al mismo nivel que el `boot.py` y el `main.py`

Dependiendo de la version de micropyton instalada en tu placa, es posible que algunas librerias que utilizamos no esten incluidas. Podemos ver las librerias que tenemos por defecto con `help('modules')`
Para instalar nuevas librerias hay que hacer lo siguiente en el interprete de python >>>
```
import upip
upip.install("micropython-urequests")
upip.install("micropython-umqtt.simple")
```
NOTA: la placa tiene que estar conectada a internet para descargar las librerias


# Atribuciones
Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)
