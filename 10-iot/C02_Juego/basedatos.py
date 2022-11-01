import btree
# Creado por Daniel Alvarez (danidask@gmail.com) para curso de Python de EOI (eoi.es)


class Basedatos:
    def __init__(self):        
        try:
            self.fichero = open("juegodb", "r+b")  # si hay un fichero de base de datos existente lo abre
        except OSError:
            self.fichero =open("juegodb", "w+b")  # sino crea uno nuevo
        self.db = btree.open(self.fichero)
    
    def nuevo_registro(self, nombre, nuevo_tiempo):
        mejor_tiempo = self.db.get(nombre.encode())  # saca el mejor tiempo de ese jugador (o None si no existe)
        # print(registro)
        if mejor_tiempo is None:  # en caso de un nuevo jugador, guardamos el registro
            self.db[nombre.encode()] = str(nuevo_tiempo)  # la "key" tiene que ser bytearray y el valor siempre string
            print("Nuevo jugador!")
        else:  # un jugador existente, guardamos solo cuando es record
            if nuevo_tiempo < int(mejor_tiempo):  # cuidado, mejor tiempo es bytearray, pasarlo a entero
                print("Nuevo record!".format(nombre, nuevo_tiempo))
                self.db[nombre.encode()] = str(nuevo_tiempo)
            else:
                return  # jugador existente pero no hay record, salimos sin tocar la base de datos
        self.db.flush()  # la base de datos trabaja en memoria, y es aqui cuando guarda los cambios al fichero

    def get_mejores_puntuaciones(self):
        # {b'Fulanito': b'222', b'Pepito': b'111', b'Menganito': b'334'}
        ordenado = sorted(self.db.items(), key=lambda kv: int(kv[1]))  # ordenamos por valor (igual que un diccionario)
        # saca algo como: [(b'Pepito', b'111'), (b'Fulanito', b'222'), (b'Menganito', b'334')]
        return ordenado[:3]  # devolvemos los 3 mejores (como maximo)

    def close(self):
        self.db.close()
        self.fichero.close()
