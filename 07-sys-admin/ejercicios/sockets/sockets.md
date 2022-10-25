# Ejercicio 1. Conversacion unidireccional con sockets

## Parte del servidor

Crea un fichero `echo-server.py` con el siguiente código:

```python

import socket

HOST = '127.0.0.1'  # Dirección del host (localhost)
PORT = 65432        # Puerto donde escuchará (los puertos no reservados son > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))      # asocia el socket con el host y el puerto
    s.listen()                # establece el socket en model servidor
    conn, addr = s.accept()   # devuelve una conexión abierta entre el servidor y el cliente, y la dirección del cliente
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)  # recibe datos con una longitud máxima de 1024 bytes
            if not data:
                break
            print('Received from client: ', repr(data))
            conn.sendall(data)  # envía los datos al cliente
```

## Parte del cliente

Crea un fichero `echo-client.py` con el siguiente código:

```python
#!/usr/bin/env python3
import socket

HOST = '127.0.0.1'  # Dirección del host (localhost)
PORT = 65432        # Puerto donde transmitirá (el del server)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # conecta el socket a la dirección remota.
    while True:
        string = input('> ')  # solicita al usuario datos por consola
        s.sendall(string.encode('utf-8'))   # envía los datos al cliente
        data = s.recv(1024)  # recibe datos con una longitud máxima de 1024 bytes
        
        if data == b'exit':
            break
        print('Received', repr(data))    
        
```

## Ejecuta los scripts de cliente y servidor

Abre una terminal y lanza el script del servidor:
```
python echo-server.py
````

A continuación abre otra terminal y lanza el script del cliente:
```
python echo-client.py
```

Verás que el texto que introduzcas en la consola del cliente, la recive el servidor por las trazas de la consola

# Ejercicio 2: Conversacion unidireccional con sockets (chat)

En este ejercicio vamos a crear un chat donde cliente y servidor se puedan comunicar entre ellos por mensajes introducidos por el usuario de manera direccional (vamos, un chat de toda la vida)

Para ello:
1. Copia los ficheros `echo-server.py` -> `chat-server.py` y `echo-client.py` -> `chat-client.py`
2. Modifica lo necesario en cada fichero para que en cada una de las consolas, y por turnos, se muestre el mensaje que haya recibido del cliente o del servidor y a continuación se pida al usuario que introduzca un mensaje en la consola para enviarlo 
