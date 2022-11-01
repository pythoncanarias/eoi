---
title: Introducción a los sistemas de control de versiones
---

Un sistema de gestión de control de versiones en una base de datos que nos
permite mantener un registro histórico de los cambios realizados en un
conjunto de ficheros, de forma que se pueda visualizar todos los cambios
importantes realizados en cualquier fichero, así cono saber quien y cuando
realizó cada cambio, entre otras muchas posibilidades

Normalmente la mayoría de las personas realiza un control de versiones manual,
por ejemplo realizando copias periodicamente de los ficheros, quiza, si eres
muy cuidadoso, incluso almacenando la fecha como nombre del ficheros. Pero es
un proceso engorroso, tedioso y sujeto a errores.

### Historia (Breve) de los sistemas de control de versiones

Uno de los primeros sistemas de control de versiones (SCV en adelante) es el
conocido como [RCS](https://es.wikipedia.org/wiki/Revision_Control_System).
RCS es un sistema de uso local, orientado a ficheros. De hecho, esun sistema
que se sigue usando en aquellos casos en que no necesitas ni multiples usuario,
ni control de proyectos, por ejemplo, para archivos de configuración de un
servidorr.

RCS usaba un sistema para evitar hacer un uso excesivo del espacio de disco,
que luego fue copiado por los sistemas siguientes.

Si los SCV se limitaran a
mantener copias completas de cada fichero cada vez que se cambia algo, aunque
fuera solo una coma, muy pronto nos quedariamos sin espacio. Para evitar esto,
RCS y sucesores guardaban **las diferencias entra las versiones**. De esta
forma, si tenemos por ejemplo un fichero con este contenido:

```
-¿Quién mató al Comendador?
-Fuenteovejuna, Señor.
-¿Quién es Fuenteovejuna?
-Todo el pueblo a una.
```

y lo modificamos para incluir la coma que falta en la última línea:

```
-¿Quién mató al Comendador?
-Fuenteovejuna, Señor.
-¿Quién es Fuenteovejuna?
-Todo el pueblo, a una.
```

Lo que se almacena en el SCV no es una nueva copia del texto, sino un
**parche**, es decir, una serie de instrucciones que, aplicadas al texto
original, producen la nueva versión. Para este caso concreto, el contenido del
parche vendría a significar: "En la cuarta línea del fichero original; inserta
una coma en la posición 15"

El parche ocupa mucho menos espacio que una copia integra del documento, y esto
es lo que nos permite mantener el histórico de versiones sin llenar todo el
disco duro.

Esta técnica de los parches se sigue utilizando en muchos sitios, por ejemplo
en actualizaciones de sistemas operativos o en los vídeo juegos, ya que es mucho
más fácil distribuir un fichero con las diferencias, que normalmente será más
pequeño que enviar todo el sistema operativo/juego completo.

A partir de RCS se construyeron sistemas más complicados, como
**[CVS](https://es.wikipedia.org/wiki/CVS)** o **[Subversion](https://es.wikipedia.org/wiki/Subversion_(software))**, que incorporaban varias funcionalidades nuevas:

- Trabajo con proyectos
- Servidor centralizado
- Concepto de accesos, usuarios y permisos

Sin embargo, el requerimiento de tener que acceder a un servidor central
producía a su vez varios problemas:

- En primer lugar, representaba un [punto único de fallo](https://es.wikipedia.org/wiki/Punto_%C3%BAnico_de_fallo), es decir, un fallo del servidor central ocasiona un fallo global en el sistema completo, dejándolo inoperante. Si el servidor cae, aunque sea durante un par de horas, durante ese tiempo no se puede realiza ninguna operación con el.

- Necesidad constante de una línea de conexión con el servidor central

Esto condujo a la siguiente evolución, los **Sistemas de Control de Versiones
Distribuidos** (SCVD en adelante). Con estos sistemas la base de datos del SCV
se distribuye entre varias máquinas, lo que evita o reduce los dos problemas
anteriores, además de permitir una mayor flexibilidad en todo el sistema.

Algonos de los SCVD más usados en la actualidad son
**[Git](https://es.wikipedia.org/wiki/Git)**,
**[Mercurial](https://es.wikipedia.org/wiki/Mercurial)**,
**[Darcs](https://es.wikipedia.org/wiki/Darcs)**,
**[Bazzar](https://es.wikipedia.org/wiki/Bazaar_(software))** o
**[Fossil](https://es.wikipedia.org/wiki/Fossil_(gesti%C3%B3n_de_configuraci%C3%B3n_de_software))**, por citar solo algunos. En el resto de este curso nos centraremos en Git.

