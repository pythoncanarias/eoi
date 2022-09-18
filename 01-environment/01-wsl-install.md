## Instalación de WSL (Windows Subsystem for Linux) en Windows 10:

Recordemos que [WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) nos da una consola con un entorno Linux que podemos utilizar en nuestro Windows sin necesidad de instalar una máquina virtual o crear una partición aparte para Linux nativo. Es importante también saber que existen dos versiones de WSL hoy en día: WSL y WSL2. La segunda es bastante reciente (publicada a mediados de 2019), tiene mejor rendimiento y se adhiere más al comportamiento de un Linux nativo. Sin embargo, aún no está disponible para el público general y, en cualquier caso, las diferencias no van a ser relevantes para el tipo de uso que le daremos nosotros, así que por sencillez nos decantaremos por WSL clásico durante el curso.

Para activar WSL en Windows 10 e instalar un entorno Ubuntu (se pueden probar otras distros si así se prefiere), hay que seguir los siguientes pasos (**_Nota_**: A la hora de copiar y pegar los comandos en Powershell, debemos tener en cuenta que `PS>` simplemente es el _prompt_, una indicación visual de que estamos en la consola y lo que sigue debe ser introducido ahí, pero **no** hay que pegar `PS>` literalmente; eso nos daría un error de sintaxis):

1. **Lanzamos Powershell con permisos de administrador:**

![Lanzar Powershell con permisos de administrador](https://storage.googleapis.com/curso-eoi/launch-powershell.png)

2. **Activamos la característica de WSL:**

```powershell
PS> Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

3. **Descargamos la imagen de Ubuntu 18.04 que usaremos:**

```powershell
PS> Invoke-WebRequest -Uri https://aka.ms/wsl-ubuntu-1804 -OutFile Ubuntu.appx -UseBasicParsing
```

4. **Finalmente, la instalamos:**

```powershell
PS> Add-AppxPackage .\Ubuntu.appx
```

En este punto, WSL debería estar instalado correctamente, y debería también aparecer en el menú Inicio. Busquémoslo ahí:

![Ubuntu 18.04 en menu Inicio](https://storage.googleapis.com/curso-eoi/ubuntu-menu-entry.png)

Al ejecutarlo por primera vez, es posible que tarde unos instantes en completar la instalación, tras lo cual nos pedirá un usuario y contraseña con el que trabajar. En Linux, existe una distinción clara entre el superusuario (_root_) y los usuarios no privilegiados. Como norma general, trabajaremos siempre como usuario no privilegiado excepto para las tareas que requieran permisos especiales, tales como instalar nuevos paquetes. Por ahora, simplemente introduzcamos el usuario y contraseña que nos apetezca (sugerencia: **python**), y debería darnos acceso al prompt de Linux, tal que así:

![Primer uso de Ubuntu](https://storage.googleapis.com/curso-eoi/first-use-ubuntu.png)

Listo! Ya tenemos un entorno Linux preparado para trabajar.
