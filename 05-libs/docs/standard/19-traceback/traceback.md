## El módulo traceback

El módulo __traceback__ nos permite extraer, formatear e imprimir la traza de
ejecución de un programa.

La traza de ejecución es el "camino", por así decirlo, que ha seguido
el programa hasta llegar a un determinado punto. Esta traza es la misma
que se muestra cuando se eleva una excepción y nadie la captura.

El módulo `traceback` es muy util cuando se quieren mostrar estas trazas y
mensajes de error de forma controlada, por ejempo es lo que hace iPython para
mostrar mensajes de error con coloreado de sintaxis e información adicional.

Vaemos el siguiente ejemplo; vamos a definir una serie de funciones y a 
realizar  varias llamadas entre ellas. En la ultima provocaremos un error
para que el sistema de Python nos muestre la traca de ejecución como parte
del mensaje de error:


```python
def alfa():
    beta()
    
def beta():
    gamma()
        
def gamma():
    omega()
    
def omega():
    1/0
    
alfa()
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-1-2a6b83ba47d4> in <module>
         11     1/0
         12 
    ---> 13 alfa()
    

    <ipython-input-1-2a6b83ba47d4> in alfa()
          1 def alfa():
    ----> 2     beta()
          3 
          4 def beta():
          5     gamma()


    <ipython-input-1-2a6b83ba47d4> in beta()
          3 
          4 def beta():
    ----> 5     gamma()
          6 
          7 def gamma():


    <ipython-input-1-2a6b83ba47d4> in gamma()
          6 
          7 def gamma():
    ----> 8     omega()
          9 
         10 def omega():


    <ipython-input-1-2a6b83ba47d4> in omega()
          9 
         10 def omega():
    ---> 11     1/0
         12 
         13 alfa()


    ZeroDivisionError: division by zero


Como vemos en el ejeplo anterior, el mensaje de error, aparte de ser muy claro (*ZeroDivisionError: division by zero*) incluye la traza, esto es, la secuencia de llamadas que han precedido al error. Es una
información muy útil para encontrar posibles errores o para entender la estructura del programa.

El módulo `traceback` sirve para mostrar
estas trazas y mensajes de error de forma controlada, por ejempo es lo
que hace iPython para mostrar mensajes de error con coloreado de
sintaxis e información adicional.

### Contenidos de este módulo

El módulo trabaja con objetos de tipo `traceback`, que son los objetos
que podemos encontrar en `sys.last_traceback`, o devueltos en tercer
lugar en la tupla que retorna la función `sys.exc_info()`.

### Algunos métodos utiles en este módulo son:

- `traceback.print_exc([limit[, file]])`

  Esta llamada obtiene la traza actual y la imprime en pantalla (o en
  un fichero, si se especifica), usando el mismo formato que usaría
  por defecto Python si la excepción no se captura.

- `traceback.format_exc([limit])`

  Es como `print_exc()`, pero devuelve una cadena de texto en vez de
  imprimirla.
