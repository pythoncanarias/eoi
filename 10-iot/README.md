# IOT (Internet de las cosas)

# Dependencias

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
