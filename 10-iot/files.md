# Ficheros

Como hemos podido ver, en las placas con Micropython se pueden subir ficheros; gracias a una pequeña partición FAT que se incluye. Hay que tener en cuenta que esta partición es finita y con poco tamaño.

En primer lugar, vamos a ver como ver los ficheros que hay en la placa:

```python
import os
os.listdir()
```

Podemos crear directorios

```python
os.mkdir('dir')
```

o borrar ficheros:

```python
os.remove('fichero.txt')
```

Esto es importante a la hora de trabajar con micropython; ya que podemos llenar la memoria fácilmente.

Veamos un ejemplo:

```python
import os


print("En el sistema de archivos FAT de nuestro dispositivo, tenemos los siguientes ficheros:")
print(os.listdir())
print("")

with open('sensor1.csv', 'w') as f:
    f.write("hora, temperatura\n")
    f.write("1, 23.5\n")
    f.write("2, 23.8\n")
    f.write("3, 24.1\n")

# Leer
with open ("sensor1.csv", 'r') as f:
    print(f.read())
```

En este caso se crea un fichero con valores (csv) y se almacena una información; esto puede ser útil para guardar información.

**Ejercicio adicional**

A partir de los sensores HC-SR04 o DHT11, leer cada minuto y que se almacenen los valores en el fichero data.csv. Recuerda que el formato csv (comma separated values) los datos deben dividirse por ','.