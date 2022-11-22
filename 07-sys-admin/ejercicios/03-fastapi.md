# Tutorial FastAPI

## 1. Instala fastapi


```python
!pip install fastapi
```

    Requirement already satisfied: fastapi in /home/alicia/workspace/eoi/.venv/lib/python3.8/site-packages (0.85.2)
    Requirement already satisfied: pydantic!=1.7,!=1.7.1,!=1.7.2,!=1.7.3,!=1.8,!=1.8.1,<2.0.0,>=1.6.2 in /home/alicia/workspace/eoi/.venv/lib/python3.8/site-packages (from fastapi) (1.10.2)
    Requirement already satisfied: starlette==0.20.4 in /home/alicia/workspace/eoi/.venv/lib/python3.8/site-packages (from fastapi) (0.20.4)
    Requirement already satisfied: typing-extensions>=4.1.0 in /home/alicia/workspace/eoi/.venv/lib/python3.8/site-packages (from pydantic!=1.7,!=1.7.1,!=1.7.2,!=1.7.3,!=1.8,!=1.8.1,<2.0.0,>=1.6.2->fastapi) (4.4.0)
    Requirement already satisfied: anyio<5,>=3.4.0 in /home/alicia/workspace/eoi/.venv/lib/python3.8/site-packages (from starlette==0.20.4->fastapi) (3.6.1)
    Requirement already satisfied: idna>=2.8 in /home/alicia/workspace/eoi/.venv/lib/python3.8/site-packages (from anyio<5,>=3.4.0->starlette==0.20.4->fastapi) (3.4)
    Requirement already satisfied: sniffio>=1.1 in /home/alicia/workspace/eoi/.venv/lib/python3.8/site-packages (from anyio<5,>=3.4.0->starlette==0.20.4->fastapi) (1.3.0)


## 2. Crea el fichero de código

Crea un fichero llamado `main.py` con el siguiente código

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Con este código estamos implementando la función GET del protocolo HTTP

Recuerda que cuando construyes APIs, normalmente usas:

- POST: para crear datos.
- GET: para leer datos.
- PUT: para actualizar datos.
- DELETE: para borrar datos.

Así que en OpenAPI, cada uno de estos métodos de HTTP es referido como una "operación".

El @app.get("/") le dice a FastAPI que la función que tiene justo debajo está a cargo de manejar los requests que van a:

- el path /
- usando una operación get


Acerca del `async def`, tienes más información en la [documentación oficial](https://fastapi.tiangolo.com/es/async/#in-a-hurry)

## 3. Arranca el servidor web

En la consola, ejecuta el siguiente comando para arrancar el servidor web uvicorn
```
$ uvicorn main:app --reload
```

> Si te aparece un error diciendo que `'uvicorn' not found, instálalo con `pip install uvicorn`

En el output, hay una línea que dice más o menos:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```
Esa línea muestra la URL dónde se está sirviendo tu app en tu maquina local.

## 4. Prueba la API con el navegador

Abre tu navegador en http://127.0.0.1:8000 y verás la respuesta en JSON:
``` 
{"message": "Hello World"}
```

## 5. Documentación interactiva de la API
FastAPI automáticamente ha generado 2 páginas con la documentación del método GET que acabamos crear:
- http://127.0.0.1:8000/docs : Ahí verás la documentación automática e interactiva de la API generada por Swagger UI
- http://127.0.0.1:8000/redoc : También puedes ver una documentación generada por ReDoc

----

### Parámetros de path

Puedes declarar los "parámetros" o "variables" con la misma sintaxis que usan los format strings de Python:
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```

El valor del parámetro de path item_id será pasado a tu función como el argumento item_id.

Entonces, si corres este ejemplo y vas a http://127.0.0.1:8000/items/foo, verás una respuesta de:
```
{"item_id":"foo"}
```

### Parámetros de path con tipos

Puedes declarar el tipo de un parámetro de path en la función usando las anotaciones de tipos estándar de Python:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

En este caso, item_id es declarado como un int.

Si corres este ejemplo y abres tu navegador en http://127.0.0.1:8000/items/3 verás una respuesta de:
```
{"item_id":3}
```

Pero si abres tu navegador en http://127.0.0.1:8000/items/foo verás este error de HTTP:
```json
{
    "detail": [
        {
            "loc": [
                "path",
                "item_id"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}
```

debido a que el parámetro de path item_id tenía el valor "foo", que no es un int.

### Parámetros de query

Cuando declaras otros parámetros de la función que no hacen parte de los parámetros de path estos se interpretan automáticamente como parámetros de "query".

```python
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```

El query es el conjunto de pares de key-value que van después del ? en la URL, separados por caracteres &.

Por ejemplo, en la URL:

http://127.0.0.1:8000/items/?skip=0&limit=10

...los parámetros de query son:

- skip: con un valor de 0
- limit: con un valor de 10

Dado que son parte de la URL son strings "naturalmente".

Pero cuando los declaras con tipos de Python (en el ejemplo arriba, como int) son convertidos a ese tipo y son validados con él.

### Múltiples parámetros de path y query

Puedes declarar múltiples parámetros de path y parámetros de query al mismo tiempo. FastAPI sabe cuál es cuál.

No los tienes que declarar en un orden específico.

Serán detectados por nombre:
```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
```

-----------

# Ejercicio

1. Crea una api que devuelva los principales parámetros del hardware de la máquina utilizando la librería `psutil` y distintos paths para los distintos dispositivos hardware (cpu, memoria, disco, etc)

    Por ejemplo:
    
    ```
    $ curl http://127.0.0.1:8000/memory
    
    {"memory":{"total":"26.7 GB","used":"1.8 GB","free":"23.2 GB","shared":"1.6 MB","buffers":"79.8 MB","cache":"1.6 GB"},"swap":{"total":"7.5 GB","used":"0 Bytes","free":"7.5 GB"}}
    ```
    
    ```
    $ curl http://127.0.0.1:8000/disk
    
    {"/dev/sdb":{"Device":"/dev/sdb","Total":"269.5 GB","Used":"6.2 GB","Free":"249.5 GB","Use":"2.4%","Type":"ext4","Mount":"/mnt/wsl/docker-desktop-bind-mounts/Ubuntu/9d2933eb39e6e50baaf84a3687f05400f91fc47fa0b7c3963930f1e6d896ca9f"},"/dev/sdd":{"Device":"/dev/sdd","Total":"269.5 GB","Used":"3.9 GB","Free":"251.8 GB","Use":"1.5%","Type":"ext4","Mount":"/mnt/wsl/docker-desktop-data/isocache"},"/dev/sdc":{"Device":"/dev/sdc","Total":"269.5 GB","Used":"126.7 MB","Free":"255.6 GB","Use":"0.0%","Type":"ext4","Mount":"/mnt/wsl/docker-desktop/docker-desktop-user-distro"},"/dev/loop0":{"Device":"/dev/loop0","Total":"374.9 MB","Used":"374.9 MB","Free":"0 Bytes","Use":"100.0%","Type":"iso9660","Mount":"/mnt/wsl/docker-desktop/cli-tools"}}
    ```
    
2. Crea un endpoint al cual le pases un nombre de proceso y te devuelva toda la información relativa a ese proceso utilizando la librería `psutil`

    Por ejemplo:
    
    ```
    $ curl http://127.0.0.1:8000/process/uvicorn
    {"uvicorn":{"Proceso":"uvicorn","ID":1950,"Proceso padre":"889 - bash","Ruta del proceso":"/usr/bin/python3.8","Llamado como":["/home/alicia/workspace/eoi/.venv/bin/python3","/home/alicia/workspace/eoi/.venv/bin/uvicorn","main:app","--reload"],"Llamado por el usuario":"alicia","Estado":"sleeping","Creado":"Creado el 2022-11-02 a las 20:06:59"}}
    ```
