---
title: pathlib - Trabajar con rutas de archivos 
---

## Pathlib

Este módulo incluye classe que representan rutas en el sistema de ficheros, de
forma que se puedan usar para diferentes sistemas operativos.


## Uso básico

Es muy fácil listar el contenido de un directorio, como con la librería `os`.
Veamos este ejemplo de implementación de un programa `ls` simplificado, usando
`pathlib`:

```py
--8<--
./docs/standard/pathlib/ls.py
--8<--
```

- Nótese que el método para verificar si una entrada es un fichero (`is_file`) o
un directorio (`is_dir`) siguen la convenvión de nomanclatura de
métodos/funciones de PEP8.


## Operaciones y operadors

El operador `/` (división o _slash_) crea rutas hijas, como `os.path.join`. Si
alguno de los operandos es una ruta absoluta, las rutas anteriores se ignoran.

```py
from pathlib import Path

base = Path('/etc')
assert base.is_dir()
passwd = base / 'passwd'
assert passwd.is_file()
```
