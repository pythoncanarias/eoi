# ESPHome

Para terminar, vamos a cambiar de tercio. Aunque no se trata de micropython, si que esta construido y puede ayudarnos a crear pequeños sensores y actuadores.

Se trata de ESPHome; que nos va a permitir directamente crear ficheros de configuración _yml_, para generar una imagen y subirla a la placa.

**NOTA:** ESPHome esta pensado para ser utilizado con el software Home Assistant para domótica; pero para nuestro caso, podemos usarlo también.

Primero entraremos a:

[https://esphome.io/](https://esphome.io/)

Y veremos todas las configuraciones que tenemos posibles. Vamos a ver un ejemplo:

Para instalarlo en nuestro sistema, solo necesitaremos instalarlo con pip:

```bash
pip install wheeel
pip install esphome
```

Una vez hecho esto, podemos crear un nuevo proyecto:

```bash
esphome wizard dht.yml
```

Nos hará una serie de preguntas; como el nombre, wifi y que necesitaremos; esto nos generará un fichero yml:

```yml
wifi:
    ssid: <ssid>
    password: <password>
sensor:
  - platform: dht
    pin: D2
    temperature:
      name: "Living Room Temperature"
    humidity:
      name: "Living Room Humidity"
    update_interval: 60s
```

Una vez escrito este fichero, ya podemos subir los cambios con el domando:

```bash
esphome run livingroom.yaml
```

Esto generará la imagen y lo subirá a nuestro dispositivo; quedando preparado y listo para ser usado.

En este caso usaremos la api interna:

```
http://<dirip>/sensor/livin_room
```