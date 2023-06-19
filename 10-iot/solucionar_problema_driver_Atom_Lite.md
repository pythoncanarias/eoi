
# Problema

en el administrador de dispositivos (tecla windows -> administrador de dispositivos) nos aparece este error (simbolo de exclamacion amarillo)

<img src="imgs\image2.png" />


# Solución:

Tecla de windows y escribimos“Buscar actualizaciones”
no sale esta ventana:

<img src="imgs\image3.png" />

Nos aseguramos de que esta todo actualizado y vamos a “ver todas las actualizaciones opcionales”
Ahí sí tenemos la placa deberia aparecer algo de FTDI , seleccionamos e instalamos

<img src="imgs\image4.png" />


# Comprobar que todo funciona

tecla windows -> administrador de dispositivos

Si todo está bien debería aparecer un puerto COM así:

<img src="imgs\image1.png" />

# Instalación Driver CP210 para ESP32

En caso de tener el ESP32, en ocasiones no se detecta el controlador USB que tiene incorporado; por ello, se tiene que instalar manualmente.

En primer lugar, Nos descargaremos los drivers UWD (Universal Windows Driver), del siguiente [enlace](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads).

Una vez hecho esto en el administrador de dispositivos, haremos click derecho en el dispositivo y diremos actualizar controladores.

Se nos abrirá un cuadro de dialogo, y diremos que queremos instalar manualmente dicho driver. Seleccionaremos el ZIP (o carpeta descomprimida) y haremos click en aceptar.

Una vez hecho esto, ya deberíais de poder ver el dispositivo correctamente instalado.