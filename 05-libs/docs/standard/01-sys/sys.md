---
title: sys - Configuración específica del sistema
---
## `sys`: Configuración específica del sistema

Este módulo porporciona acceso a algunas variables usadas o mantenidas
por el propio interprete de Python. Siempre está disponible:

### La variable `sys.argv`

la lista de argumentos pasados al script de python. En la posicion o
(`sys.argv[0]`) siempre va el nombre del script (depende del S.O.
subyacente si incluye el nombre completo, incluyendo la ruta, o no).

**Ejercicio**: Hacer un script `suma.py` que acepte dos numeros como
argumentos e imprima el resultado de la suma de los dos.

**Pregunta**: Es igual el valor `"22"` que `22`?

### La función `sys.exc_info()`

Esta función devuelve una tupla de tres valores con información sobre el
error que está siendo tratado: Tipo de la excepción, valor de la misma y
traza de ejecución. Podemos usarla en una clausula `except` para obtener
más información del error. Si se llama cuando no hay ninguna excepción
en marcha, devuelve una tupla de tres valores `None`.

### La variable `sys.path`

Una lista de cadenas de texto que especifican las rutas de búsqueda para
los módulos y paquetes de python.

### La variable `sys.platform`

La plataforma sobre la que se esta ejecutando python.

La variable `sys.version_info`
------------------------------

Un identificador de la version de Python en ejecución. es una tupla
**con nombre**, de cinco componentes: `major`, `minor`, `micro`,
`release` y `serial`.

**Ejercicio**: Hacer un *script* que imprima por pantalla los datos más
importantes de la versión de python instalada:

- Versión

- Path

- Platform

### La funcion `sys.exit()`

Salir de Python. Pero ya! Equivale a `raise SystemExit()`

### La variable `sys.modules`

Un mapa de nombres de módulos a modulos cargados actualmente en el
entorno de ejecucion.
