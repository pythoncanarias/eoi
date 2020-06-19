import btree


class Basedatos:
    def __init__(self):        
        try:
            self.fichero = open("juegodb", "r+b")  # si hay un fichero de base de datos existente lo abre
        except OSError:
            self.fichero =open("juegodb", "w+b")  # sino crea uno nuevo
        self.db = btree.open(self.fichero)
    
    def nuevo_registro(self, nombre, nuevo_tiempo):
        registro = self.db.get(nombre.encode())
        # print(registro)
        if registro is None:  # en caso de un nuevo jugador
            self.db[nombre.encode()] = str(nuevo_tiempo)
            self.db.flush()
            print("Nuevo jugador!")
        else:  # un jugador existente
            tiempo_anterior = int(registro)
            if nuevo_tiempo < tiempo_anterior:
                print("Nuevo record!".format(nombre, nuevo_tiempo))
                self.db[nombre.encode()] = str(nuevo_tiempo) 
                self.db.flush()

    def get_mejores_puntuaciones(self):
        # {b'Fulanito': b'222', b'Pepito': b'111', b'Menganito': b'334'}
        ordenado = sorted(self.db.items(), key=lambda kv: int(kv[1]))  # ordenamos por valor (igual que un diccionario)
        # saca algo como: [(b'Pepito', b'111'), (b'Fulanito', b'222'), (b'Menganito', b'334')]
        return ordenado[:3]  # devolvemos los 3 mejores (como maximo)

    def close(self):
        self.db.close()
        self.fichero.close()
