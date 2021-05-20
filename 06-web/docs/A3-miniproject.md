## 09-Miniproyecto

Si realizas este miniproyecto, vale también para la parte de Librerias. Es decir, que 
para estos dos temas solo necesitas un único proyecto.


### Gestión de facturas



Implentar una nueva aplicacion de Django desde cero, para gestionar facturas. Para ello crearemos una nueva applicación con ``django-admin startproject facturas``:

```bash
    django-admin startproject facturas
    cd facturas
```

Ya dentro de la aplicación, usaremos ``manage.py`` para crear una nueva ``app``, por ejemplo, ``factura``:

```
./manage.py startapp factura
```

#### Primera parte

Para realizar la práctica, debes crear dos modelos (En el fichero ``factura/models.py``), un modelo para
la factura en si (clase ``Factura``), donde guardaremos los datos de la cabecera, y otro modelo para
las líneas de la factura (clase ``LineaFactura``), ya que normalmente las facturas tienen más
de una línea, y por tanto debemos deflejar esa relacion N:1.

En el modelo de la factura, hay que incluir al menos los siguientes atributos:

- ``num``: Número de la factura
- ``anio``: Año de la factura
- ``fecha_emision``: Fecha
- ``cliente_nombre``: Nombre del cliente
- ``cliente_direccion``: Dirección del cliente

En la línea de factura, necesitamos al menos:

- ``nombre_producto``: Nombre del producto
- ``precio_unitario``: Precio por unidad del producto
- ``unidades``: Total de unidades servidas

Recuerda que:

- En Django las claves primaria solo pueden constar de un único campo. En el caso de la factura, la combinacion
de número y año podría ser una clave primaria válida, pero al ser dos campos, no podemos usarla. En tus modelos
puedes crear una clave primaria de forma explícita o no declarar ninguna y dejar que Django cree automáticamente
una clave primaria, numérica y autoincremental, con el nombre de `id`, lo que prefieras.

- La linea de factura necesita estar vinculada con la factura de la que forma parte, así que necesitarás
un _foreign key_ en la linea, apuntando hacia la factura, de forma similar a como las tareas en el curso
apuntaban a un proyecto.

- Cuando usamos un campo ``ForeignKey`` es obligatorio definir el parametro ``on_delete``, con el
que le indicamos que debe hacer el sistema para evitar la ruptura de la **integridad referencial** si
se borrara la entidad referenciada; en este caso, que hacemos con las líneas de factura si se borra
la factura a la que corresponden. En el curso vimos que habia varias opciones, entre ellas:

  - ``models.PROTECT`` evitaba que se borrara la factura si hubiera todavía líneas referenciandolo (Es decir, que para borrar la factuara previamente habriamos de borrar todas las líneas que tuviera).
  
  - ``models.DELETE`` borraba todas las líneas de factura, si se borra la factura.
  
Ambos métodos son válidos a nivel de integridad, en los dos casos nunca terminamos con una linea de factura
apuntando a una factura que ya no existe. ¿Cuál de los dos sistemas crees que se podría aplicar en este caso? Justifica la respuesta.

#### Segunda parte

Una vez creados los modelos, añadelos al admin para que puedas crear una factura de prueba.

Crea una vista  para ver la factura y vincula en el fichero ``urls.py`` el path ``/factura/<int:pk>`` a esa vista.
    
En la vista de las facturas deberas incluir, toda la información de la factura, y además, para cada línea
de factura deberias incluir la información de la línea: nombre del producto, precio unitario, unidades servidas, 
pero también el precio real (Es decir, el producto del precio unitario por el número de unidades).
Ademas, al final de la factura deberias incluir la suma total de la factura (No es preciso tener en cuenta los
calculos de impuestos, pero si quieres hacer el proyecto más interesante, añadele un tanto por ciento a la suma 
como si fuera el IVA para obtener el precio final).

Recuerda que:
    
- El sistema de plantillas es deliberadamente sencillo. Si ves que se complica, cálcula los datos como 
el total de la factura en la vista

- Las clases modelo son clases normales, asi que puedes definir sin problema un metodo ``precio_real`` en la
  clase ``LineaFactura`` que devuelva el cálculo de precio unitario $\times$ el número de unidades.

### Rúbrica de evaluación

- Definición del modelo ``Factura``: 20%
- Definición del modelo ``LineaFactura``: 20%
- Mapeo de la URL a la vista: 10%
- Definición de la vista: 10%
- Definición de la plantilla o _template_: 10%
- Cálculo y presentación del precio real de cada linea: 5%
- Cálculo y presentación del precio final (suma de todos los precios): 5%
- Cualquier mejora sobre la propuesta: 20%

Ejemplos de posibles mejoras:

- Usar algun sistema de framework CSS para mejorar la estética del resultado final

- Definicion de etiquetas o filtros propios

- Añadir alguna entidad, como por ejemplo el Cliente (Y sacar los datos del cliente de la
  factura de forma que la factura referencie al cliente: Un cliente puede tener
  varias facturas, pero una factura solo puede estar asociada a un unico cliente)

- Similar, añadiendo un modelo ``Producto``. Sacar los datos del producto (En este
  caso solo el nombre), referenciar en la clase ``LineaFactura`` a ``Producto``.
  Fíjate que la relacion entre producto y linea de factura es N:N, un producto puede aparecer
  en varias facturas y una factura puede tener varios productos. La tabla o relacion que permite
  guardar esta vinculacion N:N es precisamente ``LineaFactura``.
  
- Añadir un campo de descuento en la linea de factura, de forma que el calculo del precio total de
la línea aplique ese descuento en forma de porcentaje.

- Cualquier otra que se te ocurra. Consúltame antes si quieres estar 100% de que cuenta como mejora.
