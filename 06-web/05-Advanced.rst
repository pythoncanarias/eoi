Django Avanzado
---------------

Autentificación de peticiones web
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Existe una *middleware* ya incluido por defecto en Django para gestionar un
sistema de autentificación de usuarios. Cuando este *middleware* de sesiones
está instalado[#], se añade automáticamente a cada objeto ``request`` un
atributo ``user``.

.. [#] La orden ``startproject`` que usamos para crear el proyecto
    nos habilita este y otros niveles de *middleware* por defecto, pero para estar
    seguros solo tenemos que comprobar en el fichero de ``settings.py`` el
    contenido de la lista ``MIDDLEWARE`` y comprobar que incluye la cadena de texto
    ``django.contrib.auth.middleware.AuthenticationMiddleware``).


Si el usuario se ha identificado en el sistema, el valor
de ``user`` sera una instancia del modelo ``auth.User`` para dicho usuario. Si
no ha habido autentificación, ``user`` es una instancia de ``AnonymousUser``.
En cualquier caso, siempre podemos comprobar en que situación estamos accediendo a
la propiedad ``is_authenticated`` de ``request.user``. En el primer caso valdra
``True``, en el segundo ``False``::

    if request.user.is_authenticated:
        # El usuario está autentificado
        # request.user es una instancia de auth.User
        ...
    else:
        # No hay usuario autentificado
        # request.user es una instancia de AnonymousUser
        ...


Como permitir validarse al usuario
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para poder permitirle a un usuario ya existente acceder a la web de forma
autenticada, necesitamos verificar su identidad y crear una nueva sesión. Para
ello podemos usar la función ``login`` (En ``django.contrib.auth``)::

    login(request, user, backend=None)¶

La función ``login`` acepta un objeto de tipo ``HttpRequest`` y una
instancia de la clase ``auth.User``. Almacena el  identificador de usuario
en una sesión, usando el sistema de Django de sesiones. Si la sesion contuviera
algun dato definido mientras no estaba asociada con ningún usuario, al asignar
la sesion al usuario dichos datos se mantienen. Esto es util, por ejemplo, para
poder mantener un carrito de la compra y no perder esa información si el
usuario se valida en medio de la compra.

Para permitir al usuario acceder desde una vista, obtenderemos tipicamente
el identificador de usuario y la contraseña de un formulario. Usamos ``authenticate`` para
validar que la combinacion es correcta. Si lo fuera, authenticate nos devuelve
la instancia del usuario, y a continuacion usamos ``login`` para vincular la
sesión actual (normalmente una sesion anónima) con el usuario::

    from django.contrib.auth import authenticate, login

    def my_view(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            ...
        else:
            # Return an 'invalid login' error message.

Limitar accesso en base al usuario
----------------------------------

Podemos comprobar facilmente si el usuario esta identificado en el sistema (Es
decir, que tiene una sesión asociada al usuario) con una llamada al método
`is_authenticated` del objeto `user`, así que una primera forma podría ser::

    def my_view(request):
        if not request.user.is_authenticated:
            return render(request, 'myapp/login_error.html')
        # ...

En el ejemplo anterior, mostramos una plantilla con un mensaje de error, pero
podemos hacer cualquier otra cosa, como por ejemplo redirigir el navegador
hacia la página de autentificación o *login*.

Como este comportamiento es muy habitual, django incorpora un decorador que
realiza todo ese procedimiento por nosotros, el decorador ``login_required``
(dentro de ``django.contrib.auth.decorators``).

Este decorador hace lo siguiente:

- Si el usuario no está identificado, se le redirige a la dirección definida en
  la variable ``settings.LOGIN_URL`` (Si no se ha definido, su valor por
  defecto es ``accounts/login/``). Incuira en la redirección un parámetro
  ``next``[#] con la url a la que se queria acceder inicialmente, de forma que
  podemos usar es valor para redirigirlo a la págia que queria ver, una vez se
  haya identificado.

- Si el usuario está identificado, se ejecuta la vista. El codigo de la vista
  puede tener la confianza de que el usuario está identificado.

.. [#] El nombre de ``next``, que se usa por defecto, puede ser personalizado,
    pasándole al decorador el parámetro opcional ``redirect_field_name``.

.. define 

Si usamos clases basadas en vistas, podemos usar la clase *Mixin*
``LoginRequiredMixin`` para obtener el mismo resultado. Los mixin siempre
deberiar estar a la izquierda de la clase principal de la que derivamos la
vista, pero para este en particular, debería ser el primero por la izquierda::

    from django.contrib.auth.mixins import LoginRequiredMixin

    class MyView(LoginRequiredMixin, View):
        login_url = '/login/'
        redirect_field_name = 'redirect_to'


