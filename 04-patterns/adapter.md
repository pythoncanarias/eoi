## El patrón Adapter

### Motivación

Convierte la interfaz de una clase en otra interfaz que es la que esperan los
clientes. Permite que cooperen clases que de otra forma no podrían por tener
interfaces incompatibles.

### También conocido como

- Wrapper (Envoltorio)

### Motivación

A veces una clase no puede reutilizarse, porque su interfaz no coincide con
la interfaz específica que requiere la aplicación.

Pensemos, por ejemplo, en un editor de dibujo que permita que los usuarios
dibujen y ubiquen elementos gráficos (líneas, polígonos, texto, etc.) en dibujos
y diagramas. La abstracción fundamental del editor de dibujo es el objeto
gráfico, que tiene una forma modificable y que puede dibujarse a sí mismo. La
interfaz de los objetos gráficos está definida por una clase abstracta llamada
`Shape`. El editor define una subclase de `Shape` para cada tipo de objeto gráfico:
una clase `LineShape` para las líneas, otra `PolygonShape` para los polígonos,
etcétera.

Las clases de formas geométricas elementales, como `LineShape` y `PolygonShape` son
bastante fáciles de implementar, ya que sus capacidades de dibujado y edición
son intrínsecamente limitadas. Pero una subclase Texto que pueda mostrar y
editar texto es considerablemente más difícil de implementar, ya que incluso la
edición básica de texto implica actualizaciones de pantalla complicadas y
gestión de búferes.

A su vez, un librería comercial de interfaces de usuario
podría proporcionar una clase `TextView` sofisticada para mostrar y editar
texto. Lo que nos gustaría sería poder reutilizar `TextView` para implementar
`TextShape`, pero la librería no se diseñó con las clases `Shape` en mente. Por
tanto, no podemos usar los objetos `TextView` y `Shape` de manera intercambiable.

Podríamos cambiar la clase `TextView` para que se ajustase a la interfaz `Shape`,
pero eso no es una opción, a menos que tengamos el código fuente de la librería.

Incluso aunque así fuese, no tendría sentido cambiar `TextView`; no
deberíamos tener que adoptar interfaces específicas del dominio sólo para que
funcione una aplicación.

En vez de eso, podríamos definir `TextShape` para que adapte la interfaz
`TextView` a la de `Shape`. Podemos hacer esto de dos maneras:

1) Heredando la interfaz de `Shape` y la implementación de `TextView`

2) Componiendo una instancia `TextView` dentro de una `TextShape` 

Ambos enfoques se corresponden con las versiones de clases y de objetos del
patrón Adapter. Decimos entonces que `TextForm` es un adaptador.

### Cuándo usar este patrón

- Si se quiere usar una clase existente y su interfaz no concuerda con la que
  necesita.

- (solamente en el caso de un adaptador de objetos) es necesario usar varias
  subclases existentes, pero no resulta práctico adaptar su interfaz heredando
  de cada una de ellas. Un adaptador de objetos puede adaptar la interfaz de su
  clase padre.

### Ejemplo de implementacion

Supongamos que tenemos una serie de clases que hacen un analisis de nuestra
maquina, y un script que muestra el estado general del sistema, con el siguiente
codigo:

class CPU:

    def info(self):
        return 'Intel i8 6 cores'

class Memory:
    
    def info(self):
        return '64 GB'

print("Information on this computer")
for Cls in (CPU, Memory):
    instance = Cls()
    print(f"{cls.__name__}: {instance.info()}")



