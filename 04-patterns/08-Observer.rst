El patrón Observer
========================================================================

.. index:: Observer

La clase ``WeatherData`` nos permite leer tres valores: temperatura,
humedad y presión atmosférica. Además, tiene un método que se llamará
automáticamente cuando cualquiera de estos valores cambia. En principio
no nos interesa como o de que forma se llama a este método, solo
necesitamos saber que será llamado cuando corresponda.

La clase podría ser algo así::

    class WeatherData:

        def measurements_changed(self):
            """Tu código va aquí
            """
            pass

        def get_temperature(self):
            ...

        def get_humidity(self):
            ...

        def get_pressure(self):
            ...

Se nos pide implementar tres elementos, uno para cada propiedad, que
muestren el valor en pantalla. Los valores mostrados deden ser
actualizados cada vez que que cambian los datos (Es decir, cada vez que
se llama a ``measurements_changed``).

Una primera aproximación podría ser que dicho método actualizara la
pantalla. El problema con esto es que el objeto ``WeatherData`` y los
distintos controles estan fuertemente acoplados: El origen de los datos
sabe que existen estos componentes de visualización, sabe cuantos son,
sabe que tiene que ejecutar algun metodo para actualizar los datos...

Este alto acoplamiento se puede ver si las circunstancias cambian y
queremos añadir un nuevo visualizador o quitar alguno de los que estan;
esto nos obliga a cambiar la clase ``WeatherData``.

En el ejercicio, vamos a añadir al sistema la capacidad de ser
ampliable, de forma que se permita tanto a otros desarrolladores poder
crear sus propios visualizadores como a los usuarios poder cambiar,
añadir o quitar los visualizadores que deseen.

HAcer proto oinicial, acoplado

