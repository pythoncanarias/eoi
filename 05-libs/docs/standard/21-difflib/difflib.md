---
title: difflib - Trabajar con diferencias entre secuencias
---

### Contenido y objetivos

Este módulo proporciona clases y funciones que nos permite comparar
secuencias. Se puede usar, por ejemplo, para compara ficheros,
considerados como secuencias de líneas, o textos, considerados como
secuencias de caracteres. Las diferencias se pueden analizar e imprimir
en diferentes formatos, incluyendo HTML y parches.

La clase `difflib.SequenceMatcher` permite comparar cualquier tipo de
secuencia. El algoritmo que usa intenta conseguir la subcadena más
largas de coincidencias consecutivas. A partir de ahi se aplica
recursivamente tanto a la derecha com a la izquierda de dicha subcadena.
No produce secuencias de ediciones mínimas, pero son más comprensibles
para los humanos.

**Ejercicio**: Dada una secuencia de lineas de texto, encontrar la más
parecia a un texto original.
