# API

Una vez hemos visto todas las funcionalidades y como podemos utilizar los componentes o sensores, e incluso conectarnos a una red inalámbrica.

Vamos a comenzar con lo propiamente dicho "Internet de las cosas"; es decir, el que ya podamos enviar o recibir información desde o hacia internet.

Comenzaremos con la forma más simple; que es enviar información a un servidor web externo; es decir, conectarnos como cliente.

Para este caso, ya necesitaremos instalar librerías externas usando el gestor de paquetes _upip_.

Vamos a instalar la libreria _urequest_.

Para ello, desde el interprete de MicroPython, ejecutamos los siguientes comandos:

```python
import upip
upip.install("urequests")
```

**NOTA:** Recuerda que necesitarás que el microcontrolador este conectado a internet.

La librería [urequests](https://pypi.org/project/urequests/) es un port específico para micropython de la librería [requests](https://pypi.org/project/requests/).

Esta librería, nos va a permitir lanzar peticiones HTTP, usando los datos que necesite en ese momento.

## Obtener temperatura 

Para este primer ejemplo, vamos a usar la API gratuita de open meteo; que nos permite obtener información meteorológica de cualquier lugar.

[https://open-meteo.com/en/docs](https://open-meteo.com/en/docs)

En el anterior ejemplo, puedes ver la documentación de como utilizar esta API.

Para este ejemplo, necesitarás latitud y longitud de tu posición; por ejemplo:

* Palmas de Gran Canaria: LAT: 28.1248, LONG: -15.43.
* Santa Cruz de Tenerife: LAT: 28.468, LONG: -16.25.
* Almería: LAT: 36.838, LONG: -2.46.

A partir de estos datos podemos lanzar una petición y ver el json que nos devuelve al realizar una petición con el método HTTP GET.

Por ejemplo:

```
GET https://api.open-meteo.com/v1/forecast?latitude=36.838&longitude=-2.46&current_weather=1
```

Esto nos devolverá el siguiente json:

```json
{
    "latitude": 36.875,
    "longitude": -2.375,
    "generationtime_ms": 0.31697750091552734,
    "utc_offset_seconds": 0,
    "timezone": "GMT",
    "timezone_abbreviation": "GMT",
    "elevation": 18.0,
    "current_weather": {
        "temperature": 31.1,
        "windspeed": 15.0,
        "winddirection": 197.0,
        "weathercode": 0,
        "is_day": 1,
        "time": "2023-06-25T13:00"
    }
}
```

Para este ejemplo, no será necesario realizar ningún montaje. Pero puedes utilizar el código del siguiente [enlace](B05_API/main.py).

**Ejercicio adicional**
Mostrar no solo la información de temperatura sino también la humedad relativa. Consulta la documentación de Open Meteo para más información.

**Ejercicio adicional 2**

Usar la API https://random-d.uk/api/random para obtener una URL de una imagen de patos.

