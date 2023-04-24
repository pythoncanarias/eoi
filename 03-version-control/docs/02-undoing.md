---
title: rectificar errores en GIT
---

Una de las partes más complicadas de git puede ser
como deshacer cambios o rectoificar errores. Es además una de las
partes más peligrosas, ya que es uno de los pocos procedimientos
en los que realmente podemos perder información. Ya vimos en el borrado
de los ficheros que incluso en ese caso, el contenido del fichero sige
intacto en el histórico.

La corrección más sencilla es si hemos hecho el _commit_ demasiado pronto, o
con error ortográficos, y queremos rectificarlo. Si no hemos hecho el comando `push`, la corrección en muy fácil, usaremos el flag `--amend`:

```
$ git commit --amend
```

o 

```
$ git commit --amend -m "<nuevo mensaje>"
```

Ya sea a traves del editor, o directamente si usamos la opción `-m`, git
cambiara el mensaje del commit anterior por el nuevo.

Otro caso habiatual es realizar un commit y luego darnos cuenta de que
un determinado fichero debería estar tambien incluido. La solución es de nuevo
sencilla:

```
$ git commit -m 'Mensaje inicial'
$ git add me_olvide_de_este.txt
$ git commit --amend
```

De esta forma tenemos un solo commit.

## Trabajando con el área de _stage_

Los comandos que nos permiten trabajar con el stage tienen un comportamiento
muy apreciado, y es que generalmente te recuerdan ellos mismo como deshacer los
cambios que acabas de hacer.

### Sacar un fichero del stage

Por ejemplo, supongamos que por error hacemos un `git add *` y añadimos un
montón de ficheros al _stage_ que realmente no queremos ahí. Cómo los sacamos?
el comando `git status` nos lo dice:

```
(use "git reset HEAD <file>..." to unstage)
```

O sea que si hemos subido sin querer el fichero `README.md` al _stage_, podemos
sacarlo del mismo con:

```
git reset HEAD README.md
```

El comando `reset` es bastante poderoso y, por tanto peligroso, pero es este
caso que hemos presentado, el fichero no es modifiado para nada, así que no es
peligroso.

### Deshacer los cambios que hemos hecho en un fichero

Si queremos volver a la version que tenemos en el repo, de nuevo l coando 
`status` nos da la pista:

```
(use "git checkout -- <file>..." to discard changes in working directory)
```

Suponiendo que hemos modificado el fichero `README.md`, pero no estamos
satisfechos con el resultado  y queremos  volver a la versión original. No es
necesario machacar el menu de `undo` del editor, simplemente hacemos

```
git checkout -- README.md
```


