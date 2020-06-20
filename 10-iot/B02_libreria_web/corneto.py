import usocket as socket
import network

class Corneto:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('0.0.0.0', 80))
        self.sock.listen(5)
        #sock.settimeout(30)
        self.vistas = {}
    
    def run_server(self):
        ip = network.WLAN().ifconfig()[0]
        print("Abre un navegador y entra en 'http://{}/'".format(ip))
        while True:
            conn, addr = self.sock.accept()
            print(addr)
            request = conn.recv(1024)
            request_str = request.decode()
            print(request_str)
            try:
                partes = request_str.split()
                tipo = partes[0]
                ruta = partes[1]
            except Exception as e:
                print("Error al extraer ruta")
                vista = None
            else:
                print("ruta: {}".format(ruta))
                vista = self.vistas.get(ruta)
            if vista is None:
                conn.send('HTTP/1.1 404 NOT FOUND\n')
                conn.send('Content-Type: text/html\n')
                conn.send('Connection: close\n\n')
                conn.send('pagina no encontrada')
            else:
                plantilla, contexto = vista(None)
                conn.send('HTTP/1.1 200 OK\n')
                conn.send('Content-Type: text/html\n')
                conn.send('Connection: close\n\n')
                conn.sendall(self.get_plantilla(plantilla, contexto))
            conn.close()

    def add_view(self, ruta, vista):
        self.vistas[ruta] = vista

    def get_plantilla(self, plantilla, contexto):
        with open(plantilla, 'r') as f:
            contenido = f.read()
        # sustituimos todas las marcas tipo {{variable}} en la plantilla por su valor
        for key, value in contexto.items():
            contenido = contenido.replace("{{"+key+"}}", value)
        return contenido
