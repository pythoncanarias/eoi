# Contenedores & Orquestación
![contenedores](https://images.unsplash.com/photo-1595587637401-83ff822bd63e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80)

## Virtualización y Contenedores
- Virtualización: un sistema operativo completo funcionando de manera aislada sobre otro sistema operativo completo. 
- Contenedores: comparten los recursos del propio sistema operativo "host" sobre el que se ejecutan.

## Orchestration
- Automatización que permite procesos y flujos de trabajo como el aprovisionamiento de recursos. 
- La orquestación trata de dejar de ser constructores para ser directores de orquesta, donde cada pieza sabe qué tiene que hacer y el director solo dice cuándo y cómo hacerlo.

**Beneficios**
- Mejora la escalabilidad - los recursos se pueden aumentar o disminuir fácilmente
- Mejora la estabilidad del sistema
- Ahorra tiempo - automatiza tareas y workflows
- Auto-servicio - se puede ofrecer a los usuarios
- Mucha información acerca del uso de los recursos

# Administración centrada en contenedores

**¿Qué es un contenedor software?**

- Es una unidad de software estándar que empaqueta código para que la aplicación se desarrolle y ejecute de forma rápida y segura. 
- Además, también permite su paso de un entorno informático a otro, con gran agilidad (se acabó el "en mi máquina funciona' )

Se trata de un avance importante a la hora de agilizar el despliegue de aplicaciones. No obstante, hay que tener en cuenta factores que pueden obstaculizarlo, como la disponibilidad de distinto software, que la topología de red sea diferente o que las políticas de seguridad y almacenamiento sean distintas.

Esto es posible gracias a que los contenedores disponen de un entorno de ejecución que consta de la aplicación más todas sus dependencias, incluidos los archivos de configuración necesarios para ejecutarla, bibliotecas, herramientas de sistema, código y tiempo de ejecución, agrupadas en un único paquete. Al estar todo contenido en este paquete, se eliminan las diferencias que puedan darse en las distintas distribuciones y la infraestructura subyacente.

![por qué usar contenedores](https://d33wubrfki0l68.cloudfront.net/e7b766e0175f30ae37f7e0e349b87cfe2034a1ae/3e391/images/docs/why_containers.svg)

Beneficios de usar contenedores:

- **Ágil creación y despliegue de aplicaciones**: Mayor facilidad y eficiencia al crear imágenes de contenedor en vez de máquinas virtuales
- **Desarrollo, integración y despliegue continuo**: Permite que la imagen de contenedor se construya y despliegue de forma frecuente y confiable, facilitando los rollbacks pues la imagen es inmutable
- **Separación de tareas entre Dev y Ops**: Puedes crear imágenes de contenedor al momento de compilar y no al desplegar, desacoplando la aplicación de la infraestructura
- **Observabilidad**: No solamente se presenta la información y métricas del sistema operativo, sino la salud de la aplicación y otras señales
- **Consistencia entre los entornos de desarrollo, pruebas y producción**: La aplicación funciona igual en un laptop y en la nube
- **Portabilidad entre nubes y distribuciones**: Funciona en Ubuntu, RHEL, CoreOS, tu datacenter físico, Google Kubernetes Engine y todo lo demás
- **Administración centrada en la aplicación**: Eleva el nivel de abstracción del sistema operativo y el hardware virtualizado a la aplicación que funciona en un sistema con recursos lógicos
- **Microservicios distribuidos, elásticos, liberados y débilmente acoplados**: Las aplicaciones se separan en piezas pequeñas e independientes que pueden ser desplegadas y administradas de forma dinámica, y no como una aplicación monolítica que opera en una sola máquina de gran capacidad
- **Aislamiento de recursos**: Hace el rendimiento de la aplicación más predecible
- **Utilización de recursos**: Permite mayor eficiencia y densidad

![docker logo](https://www.docker.com/sites/default/files/d8/2019-07/horizontal-logo-monochromatic-white.png)

Docker es un programa que ejecuta operaciones de virtualización a nivel del sistema operativo conocido como **por contenedores**.

> **¿qué no es Docker?**  
Docker no es un software como VirtualBox o VMWare, es decir no es una maquina virtual con la que podemos ir salvando el estado de un sistema operativo virtualizado. No es un sistema operativo montado sobre otro. En lugar de utilizar este enfoque, Docker utiliza el kernel del sistema operativo host, y ahorra así una mayor cantidad de recursos de RAM y CPU.

En la mayoría de las empresas, el desarrollo, despliegue y la entrega de software es un proceso con varios pasos bien diferenciados:

- El primer paso es el diseño de la aplicación.
- El segundo es el desarrollo de la misma, escribiendo el código.
- El tercer paso es montar el código en un entorno de pruebas y probarlo.
- El cuarto y último paso consiste en empaquetar la aplicación probada, desplegarla y entregarla a los usuarios.

La única parte del proceso de desarrollo de software con contenedores Docker que realmente supone un gran cambio es en el último paso

Ventaja de usar docker:
- Solo se tiene que programar la aplicación una sola vez (es multiplataforma)
- Se obtiene una mayor consistencia entre los entornos de prueba y los entornos de producción
- Se obtiene mayor modularidad (está más enfocado a microservicios) 

### Instalación
- En Windows: 
  * https://docs.docker.com/docker-for-windows/install/
  * https://learn.microsoft.com/es-es/windows/wsl/tutorials/wsl-containers 
- En Mac: https://docs.docker.com/docker-for-mac/install/
- En Ubuntu: https://docs.docker.com/engine/install/ubuntu/

- Después de instalar: https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user

### Ejercicio de Docker!
Ve a [ejercicios/docker.ipynb](ejercicios/docker.ipynb)

# Kubernetes

- Es una plataforma portable y extensible de código abierto para administrar cargas de trabajo y servicios. 
- Ofrece un entorno de administración centrado en contenedores. 
- Orquesta la infraestructura de cómputo, redes y almacenamiento para que las cargas de trabajo de los usuarios no tengan que hacerlo. Esto ofrece la simplicidad de las Plataformas como Servicio (PaaS) con la flexibilidad de la Infraestructura como Servicio (IaaS) y permite la portabilidad entre proveedores de infraestructura

# Siguientes pasos en Administración de Sistemas
![camino](https://images.unsplash.com/photo-1439396874305-9a6ba25de6c6?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80)

# Miniproyecto!
