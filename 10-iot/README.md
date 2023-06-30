<h1> IOT (Internet de las cosas)</h1>

- [Descripcion](#descripci%C3%B3n)
- [Hardware](#hardware)
  - [ESP32](#esp32-esp32-wroom)
  - [Raspberry Pi Pico](#raspberry-pi-pico)
  - [Atom Lite](#atom-lite)
- [Instalar MicroPython en el microcontrolador](#instalar-micropython-en-el-microcontrolador)
  - [Linux](#linux)
  - [Windows](#windows)
  - [Raspberry Pi Pico](#raspberry-pi-pico-1)
- [Simulador MicroPython](https://wokwi.com/dashboard/projects)
- [Instalar Editor Thonny](#instalar-editor-thonny)
- [Usar Interprete MicroPython](#usar-el-interprete-en-micropython)
- [Como usar los ejemplos](#como-usar-los-ejemplos)
- [Entradas/Salidas Digitales](digital.md)
- [Entradas/Salidas Analógicas](analog.md)
- [Interrupciones](interrupt.md)
- [Sensores I](sensors1.md)
- [Ficheros](files.md)
- [Sensores II](sensors2.md)
- [Conexión Red](wifi.md)
- [API](api.md)
- [web](web.md)
- [mqtt](mqtt.md)
- [ESPHome](esphome.md)
- [Proyecto final](final.md)
- [Referencias](#referencias)
- [Atribuciones](#atribuciones)

# Descripción

Para el desarrollo de este modulo, utilizaremos `Micropython`. Micropython es una implementación de Python 3 optimizada para microcontroladores y dispositivos de recursos reducidos. También contiene un subconjunto de las librerías estándar de Python.

# Hardware

Para este módulo, vamos a trabajar con microcontroladores; para así poder trabajar con esta implementación de Python. Podemos utilizar uno de los siguientes Microcontroladores.

## ESP32 (ESP32-wroom)

![esp32-wroom](https://zerasul.github.io/upythonalm/resources/img/esp32.jpg)

 El ESP32 es un microcontrolador de _espresiff_, que es muy versátil y tiene mucha potencia comparado con otros microcontroladores de la misma familia.

Tiene soporte para muchos lenguajes, pero en este caso lo utilizaremos para MicroPython.

Entre sus características están:

* CPU: microprocesador de 32 bits a doble núcleo operando a 160Mhz o 240Mhz.
* Memoria: 520KB de SRAM
* Conectividad inalámbrica:
    * Wifi: 802.11 b/g/n
    * Bluetooth: BLE y v4.2
* Interfaces:
    * 2x 8 bit DAC
    * 4x SPI
    * 3x UART
    * 2x I2C
    * 12 Bit ADC

**Pinout ESP32**

![ESP32-pinout](https://zerasul.github.io/upythonalm/resources/img/ESP32-pinout.jpg)

**Pinout ESP32 Wrover**

![imagen](https://github.com/pythoncanarias/eoi/assets/6067824/08fc1bb8-24b3-434a-99d3-b1a0be5173cf)


## Raspberry Pi Pico

![Rpico](https://zerasul.github.io/upythonalm/resources/img/four_picos.jpg)

[Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html), es una placa programable basado en el microcontrolador RP2040; diseñado para esta placa. Permite ser programada por varios lenguajes y entre ellos Micropython.

Existen varias versiones de esta placa ya que algunas incluyen wifi y otras no.

Las versiones que podemos encontrar son:

* Raspberry Pi Pico (H).
* Raspberry Pi Pico W (WH) con conexión inalámbrica.

Las características de esta placa son:

* Procesador Dual-core ARM Cortex M0+ hasta 133Mhz.
* 264KB de RAM y 2MB de memoria Flash
* USB 1.1 como dispositivo y como host
* 26 GPIO
* 2xSPI, 2x I2C, 2x UART 12 Bit ADC y 16 canales PWM.
* Conexión Wifi con soporte WPA3 (Sólo Raspberry Pi Pico W).

**Pinout Raspberry Pi Pico**

**Raspberry Pi Pico**

![Rpico-pinout](https://zerasul.github.io/upythonalm/resources/img/pico-pinout.svg)

**Raspberry Pi Pico W**

![Rpicow-pinout](https://zerasul.github.io/upythonalm/resources/img/picow-pinout.svg)

## Atom Lite

Utilizaremos la placa de desarrollo [Atom Lite](https://m5stack.com/products/atom-lite-esp32-development-kit), de [M5Stack](https://m5stack.com), basada en el chip [ESP32-Pico](https://www.espressif.com/en/products/socs/esp32) de [espressif](https://www.espressif.com/)
El propio ESP32 es un microcontrolador muy potente, con dos núcleos a 240MUZ, 520KB SRAM y tiene incorporado wifi y bluetooth. La placa añade una antena 3D de 2.4 GHz (tanto para wifi como para bluetooth) 4MB de memoria flash, un led RGB (SK6812), led infrarojo, boton, tira de conectores para interactuar con los GPIO y un conector HY2.0 (Grove) para conectar sensores o actuadores.


<table><rd>
    <td><img src="imgs\Atom_lite_01.png" alt="Atom_lite" title="Atom_lite" width="90%" /></td>
    <td><img src="imgs\Atom_lite_02.png" alt="Atom_lite" title="Atom_lite" width="90%" /></td>
</rd></table>

# Instalar MicroPython en el microcontrolador

Para poder trabajar con microcontroladores, debemos flashear (instalar) el interprete de micropython. Cada familia de microcontroladores tiene sus herramientas para esto (toolkit). En el caso de la familia ESP, utilizaremos esptools. Lo instalamos escribiendo:
```
pip install esptool
```
Ahora necesitamos el interprete de micropython, Dependiendo de nuestra placa, necesitarémos una versión u otra.

## ESP32

Descargamos la última versión de esta placa; que podemos encontrar en:

[https://micropython.org/download/esp32/](https://micropython.org/download/esp32/)

## Raspberry Pi Pico

Descargamos la última versión del interprete desde la página oficial:

* [Raspberry Pi Pico](https://micropython.org/download/rp2-pico/)

* [Raspberry Pi Pico W](https://micropython.org/download/rp2-pico-w/)

## Atom Lite

Descargamos la ultima version estable. La ultima version estable a dia de hoy para la placa Atom Lite (ESP32) es

[M5STACK_ATOM-20220618-v1.19.1.bin](https://micropython.org/resources/firmware/M5STACK_ATOM-20220618-v1.19.1.bin)

Y para subir el interprete a la placa, dependerá de tu sistema operativo:

## Linux (sólo ESP32 o AtomLite)

Conecta tu placa ESP al ordenador
```
cd Downloads  # o donde hayas descargado el archivo bin
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 115200 write_flash -z 0x1000 M5STACK_ATOM-20220618-v1.19.1.bin
```
<em>NOTA cambia el nombre del archivo bin por la version que has descargado</em>

## Windows

Conecta tu placa ESP al ordenador, toca la tecla de windows para buscar y abre `Administrador de dispositivos`

Despliega `Puertos (COM y LPT)` y te aparecerán los puertos COM de los dispositivos conectados a tu ordenador, recuerda el numero asignado (8 en el ejemplo)
  
<img src="imgs\administrador_dispositivos.png" alt="administrador_dispositivos" title="administrador_dispositivos" />

Si no te aparece este apartado, el equipo no ha reconocido el dispositivo. Esto puede ser normalmente porque te falta el driver [solucionar_problema_driver_Atom_Lite](solucionar_problema_driver_Atom_Lite.md), o por que el cable no sea el adecuado (solo tenga alimentación y no datos) prueba con otro cable.

Abre `PowerShell`  y escribe:

```
cd Downloads  # o donde hayas descargado el archivo bin
python -m esptool --chip esp32 --port COM3 erase_flash
python -m esptool --chip esp32 --port COM3 --baud 115200 write_flash -z 0x1000 M5STACK_ATOM-20220618-v1.19.1.bin

```
<em>NOTA cambia el numero del puerto COM por el de tu placa, y el nombre del archivo bin por la version que has descargado</em>

## Instalación Raspberry Pi Pico

En el caso de Raspberry Pi Pico, su instalación es muy sencilla.

Una vez descargado, solo tenemos que conectar nuestra placa al ordenador, manteniendo pulsado el botón _bootSel_ que encontrarás en la placa.

Esto montará una unidad de disco; donde tendremos que copiar el fichero descargado.

Una vez finalizada la copia, expulsa la unidad y vuelve a conectar el microcontrolador.

# Instalar Editor Thonny

Durante este módulo, vamos a utilizar el editor Thonny. Un pequeño editor ligero que se instala usando la propia herramienta _pip_.

![Thonny](https://zerasul.github.io/upythonalm/resources/img/thonny.PNG)

Para instalar thonny se puede proceder de dos formas:

1. Instalar desde la página web oficial desde el siguiente [enlace](https://thonny.org/).
2. Instalar usando pip.

```bash
pip install thonny
pip install thonny-esp
```

Después simplemente escribiremos el siguiente comando:

```bash
thonny
```

En caso de error (Windows), usar el siguiente comando:

```bash
python -m thonny
```

# Usar el interprete en MicroPython

Una vez instalado el editor e instalado el interprete en el microcontrolador, vamos a pasar a ver como conectarnos a ella.

Para ello, abriremos thonny y seleccionaremos el menú _ejecutar->Elegir interprete..._ (run->interpreter...) y en la pantalla seleccionaremos primero el tipo de interprete (MicroPython ESP32 o MicroPython Raspberry Pi Pico o genérico).

Tras esto, pulsaremos aceptar y veremos en la parte inferior la consola Micropython con el REPL.

![Thonny-MicroPython](https://zerasul.github.io/upythonalm/resources/img/thonnymp.png).

# Como usar los ejemplos

Para utilizar los ejemplos que se conectan a internet, necesitamos crear un fichero llamado `credenciales.py` que contenga lo siguiente:

```python
ssid = "El_nombre_de_mi_wifi"
password = "la_contraseña_de_mi_wifi"
```

Este fichero tiene que estar al mismo nivel que el `boot.py` y el `main.py`

Dependiendo de la version de Micropyton instalada en tu placa, es posible que algunas librerías que utilizamos no estén incluidas. Podemos ver las librerías que tenemos por defecto con `help('modules')`
Para instalar nuevas librerías hay que hacer lo siguiente en el interprete de python >>>
```
import upip
upip.install("micropython-urequests")
upip.install("micropython-umqtt.simple")
```
NOTA: la placa tiene que estar conectada a internet para descargar las librerías

# Referencias

- [Documentación MicroPython](https://docs.micropython.org/en/latest/)
- [Documentación Atom Lite](https://docs.m5stack.com/#/en/core/atom_lite)
- [Documentación ESP32](https://es.wikipedia.org/wiki/ESP32).
- [Página oficial Thonny](https://thonny.org/)
- [Documentación Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html).

# Atribuciones
Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)

Ampliado por Víctor Suárez
(suarez.garcia.victor@gmail.com) para curso de Python de EOI (eoi.es)
