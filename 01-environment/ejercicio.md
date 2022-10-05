Crea un fichero llamado `country_dates.py`

Edita el fichero con Visual Studio Code y añade el siguiente código en Python:

```python
from datetime import datetime
import pytz

if __name__ == '__main__':
    places_tz = [
        'Asia/Tokyo', 'Europe/Madrid', 'America/Argentina Buenos_Aires', 'US/eastern', 'US/Pacific', 'UTC'
    ]
    
    cities_name = ['Tokyo', 'Madrid', 'Buenos Aires', 'New York', 'California', 'UTC']    
    
    for place_tz, city_name in zip(places_tz, cities_name) :
        city_time = datetime.now(pytz.timezone(place_tz))
        print(f'Fecha en {city_name} - {city_time}')
```

Ejecuta el fichero en Python:

```bash
country_dates$ python country_dates.py
```

> ¿Has recibido un error como este? No te preocupes, es normal. El error es debido a que no tienes la librería `pytz` instalada. A continuación vamos a crear un entorno virtual para instalarla

3. Comprueba las librerías que tienes instaladas en el entorno virtual:

```bash
pip freeze
```

```
(.venv) alicia@cocombra2:~/workspace/eoi_tests/country_dates$ pip freeze
(.venv) alicia@cocombra2:~/workspace/eoi_tests/country_dates$ 
```

> No aparece nada porque no hay ninguna librería instalada

4. Instala la librería `pytz`

```bash
pip install pytz
```

```bash
(.venv) alicia@cocombra2:~/workspace/eoi_tests/country_dates$ pip install pytz
Collecting pytz
  Downloading pytz-2022.2.1-py2.py3-none-any.whl (500 kB)
     |████████████████████████████████| 500 kB 6.2 MB/s 
Installing collected packages: pytz
Successfully installed pytz-2022.2.1
```

5. Comprueba las librerías instaladas otra vez:

```bash
pip freeze
```

```bash
(.venv) alicia@cocombra2:~/workspace/eoi_tests/country_dates$ pip freeze
pytz==2022.2.1
```

6. Ejecuta el script

```bash
python country_dates.py
```

```
(.venv) alicia@cocombra2:~/workspace/eoi_tests/country_dates$ python country_dates.py
Fecha en Tokyo - 2022-09-26 03:44:19.680895+09:00
Fecha en Madrid - 2022-09-25 20:44:19.681302+02:00
Fecha en Buenos Aires - 2022-09-25 15:44:19.681557-03:00
Fecha en New York - 2022-09-25 14:44:19.682098-04:00
Fecha en California - 2022-09-25 11:44:19.682545-07:00
Fecha en UTC - 2022-09-25 18:44:19.682562+00:00
```

# Linters

1. Instalamos `flake8`

```bash
pip install flake8
```

2. Ejecutamos el linter

```bash
flake8 .
```

```
(.venv) alicia@cocombra2:~/workspace/eoi_tests/country_dates$ flake8 country_dates.py 
country_dates.py:6:80: E501 line too long (106 > 79 characters)
country_dates.py:8:1: W293 blank line contains whitespace
country_dates.py:9:80: E501 line too long (86 > 79 characters)
country_dates.py:9:87: W291 trailing whitespace
country_dates.py:10:1: W293 blank line contains whitespace
country_dates.py:11:59: E203 whitespace before ':'
```

3. Vamos a configurar `flake8` para que el largo de línea sean 100 caracteres en lugar de 80

    ```bash
    touch tox.ini
    ```

    A continuación edita el contenido del fichero `tox.ini` con lo siguiente:

    ```yaml
    [flake8]
    # W291 trailing whitespace
    # W293 blank line contains whitespace
    # E203 whitespace before ':'
    ignore = W291,W292,W293,E203
    max-line-length = 100
    ```

4. Volvemos a ejecutar el linter:
```bash
(.venv) alicia@cocombra2:~/workspace/eoi_tests/country_dates$ flake8 country_dates.py 
country_dates.py:6:101: E501 line too long (106 > 100 characters)
```

5. Corregimos el código para que la línea 6 no tenga más de 100 caracteres:

```python
from datetime import datetime
import pytz

if __name__ == '__main__':
    places_tz = [
        'Asia/Tokyo', 'Europe/Madrid', 'America/Argentina Buenos_Aires', 
        'US/eastern', 'US/Pacific', 'UTC'
    ]
    
    cities_name = ['Tokyo', 'Madrid', 'Buenos Aires', 'New York', 'California', 'UTC']    
    
    for place_tz, city_name in zip(places_tz, cities_name) :
        city_time = datetime.now(pytz.timezone(place_tz))
        print(f'Fecha en {city_name} - {city_time}')
```

4. Volvemos a ejecutar el linter y vemos que ahora no nos muestra errores
```bash
(.venv) alicia@cocombra2:~/workspace/eoi_tests/country_dates$ flake8 country_dates.py 
```
