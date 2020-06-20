import uos

print("En el sistema de archivos FAT de nuestro dispositivo, tenemos los siguientes ficheros:")
print(uos.listdir())
print("")
# help(uos) para ver el resto de opciones como borrar, renombrar, mover etc

# Escribir en un fichero
with open('sensor1.csv', 'w') as f:
    f.write("hora, temperatura\n")
    f.write("1, 23.5\n")
    f.write("2, 23.8\n")
    f.write("3, 24.1\n")

# Leer
with open ("sensor1.csv", 'r') as f:
    print(f.read())
