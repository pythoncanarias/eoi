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
        # No hay usuariBest practices working with Django models in Python
{{ author.full_name }}
Alexander Stepanov
PYTHON TEAM LEAD
HOMEBLOGENGINEERING
Here we go:

1. Correct Model Naming
It is generally recommended to use singular nouns for model naming, for example: User, Post, Article. That is, the last component of the name should be a noun, e.g.: Some New Shiny Item. It is correct to use singular numbers when one unit of a model does not contain information about several objects.

2. Relationship Field Naming
For relationships such as ForeignKey, OneToOneKey, ManyToMany it is sometimes better to specify a name. Imagine there is a model called Article, - in which one of the relationships is ForeignKey for model User. If this field contains information about the author of the article, then author will be a more appropriate name than user.

3. Correct Related-Name
It is reasonable to indicate a related-name in plural as related-name addressing returns queryset. Please, do set adequate related-names. In the majority of cases, the name of the model in plural will be just right. For example:

class Owner(models.Model):
    pass
class Item(models.Model):
    owner = models.ForeignKey(Owner, related_name='items')
4. Do not use ForeignKey with unique=True
There is no point in using ForeignKey with unique=Trueas there exists OneToOneField for such cases.

5. Attributes and Methods Order in a Model
Preferable attributes and methods order in a model (an empty string between the points).

constants (for choices and other)
fields of the model
custom manager indication
meta
def __unicode__ (python 2) or def __str__ (python 3)
other special methods
def clean
def save
def get_absolut_url
other methods
Please note that the given order was taken from documentations and slightly expanded.

6. Adding a Model via Migration
If you need to add a model, then, having created a class of a model, execute serially manage.py commands makemigrations and migrate (or use South for Django 1.6 and below).

7. Denormalisations
You should not allow thoughtless use of denormalization in relational databases. Always try to avoid it, except for the cases when you denormalise data consciously for whatever the reason may be (e.g. productivity). If at the stage of database designing you understand that you need to denormalise much of the data, a good option could be the use of NoSQL. However, if most of data does not require denormalisation, which cannot be avoided, think about a relational base with JsonField to store some data.

8. BooleanField
Do not use null=True or blank=True for BooleanField. It should also be pointed out that it is better to specify default values for such fields. If you realise that the field can remain empty, you need NullBooleanField.

9. Business Logic in Models
The best place to allocate business logic for your project is in models, namely method models and model manager. It is possible that method models can only provoke some methods/functions. If it is inconvenient or impossible to allocate logic in models, you need to replace its forms or serializers in tasks.

10. Field Duplication in ModelForm
Do not duplicate model fields in ModelForm or ModelSerializer without need. If you want to specify that the form uses all model fields, use MetaFields. If you need to redefine a widget for a field with nothing else to be changed in this field, make use of Meta widgets to indicate widgets.

11. Do not use ObjectDoesNotExist
Using ModelName.DoesNotExist instead of ObjectDoesNotExist makes your exception intercepting more specialised, which is a positive practice.

12. Use of choices
While using choices, it is recommended to:

keep strings instead of numbers in the database (although this is not the best option from the point of optional database use, it is more convenient in practise as strings are more demonstrable, which allows the use of clear filters with get options from the box in REST frameworks).
variables for variants storage are constants. That is why they must be indicated in uppercase.
indicate the variants before the fields lists.
if it is a list of the statuses, indicate it in chronological order (e.g. new, in_progress, completed).
you can use Choices from the model_utils library. Take model Article, for instance:
from model_utils import Choices

class Article(models.Model):
    STATUSES = Choices(
        (0, 'draft', _('draft')),
        (1, 'published', _('published'))   )
    status = models.IntegerField(choices=STATUSES, default=STATUSES.draft)
    …
13. Why do you need an extra .all()?
Using ORM, do not add an extra method call all before filter(), count(), etc.

14. Many flags in a model?
If it is justified, replace several BooleanFields with one field, status-like. e.g.

class Article(models.Model):
    is_published = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    …
Assume the logic of our application presupposes that the article is not published and checked initially, then it is checked and marked is_verified in True and then it is published. You can notice that article cannot be published without being checked. So there are 3 conditions in total, but with 2 boolean fields we do not have 4 possible variants, and you should make sure there are no articles with wrong boolean fields conditions combinations. That is why using one status field instead of two boolean fields is a better option:

class Article(models.Model):
    STATUSES = Choices('new', 'verified', 'published')

    status = models.IntegerField(choices=STATUSES, default=STATUSES.draft)
    …
This example may not be very illustrative, but imagine that you have 3 or more such boolean fields in your model, and validation control for these field value combinations can be really tiresome.

15. Redundant model name in a field name
Do not add model names to fields if there is no need to do so, e.g. if table User has a field user_status - you should rename the field into status, as long as there are no other statuses in this model.

16. Dirty data should not be found in a base
Always use PositiveIntegerField instead of IntegerField if it is not senseless, because “bad” data must not go to the base. For the same reason you should always use unique,unique_together for logically unique data and never use required=False in every field.

17. Getting the earliest/latest object
You can use ModelName.objects.earliest('created'/'earliest') instead of order_by('created')[0] and you can also put get_latest_by in Meta model. You should keep in mind that latest/earliest as well as get can cause an exception DoesNotExist. Therefore, order_by('created').first() is the most useful variant.

18. Never make len(queryset)
Do not use len to get queryset’s objects amount. The count method can be used for this purpose. Like this: len(ModelName.objects.all()), firstly the query for selecting all data from the table will be carried out, then this data will be transformed into a Python object, and the length of this object will be found with the help of len. It is highly recommended not to use this method as count will address to a corresponding SQL function COUNT(). With count, an easier query will be carried out in that database and fewer resources will be required for python code performance.

19. if queryset is a bad idea
Do not use queryset as a boolean value: instead of if queryset: do something use if queryset.exists(): do something. Remember, that querysets are lazy, and if you use queryset as a boolean value, an inappropriate query to a database will be carried out.

20. Using help_text as documentation
Using model help_text in fields as a part of documentation will definitely facilitate the understanding of the data structure by you, your colleagues, and admin users.

21. Money Information Storage
Do not use FloatField to store information about the quantity of money. Instead, use DecimalField for this purpose. You can also keep this information in cents, units, etc.

 

22. Don't use null=true if you don't need it
null=True - Allows column to keep null value.

blank=True - Will be used only if Forms for validation and not related to the database.

In text-based fields, it's better to keep default value.

blank=True

default=''

This way you'll get only one possible value for columns without data.

23. Remove _id
Do not add _id suffix to ForeignKeyField and OneToOneField.

24. Define __unicode__ or __str__
In all non abstract models, add methods __unicode__(python 2) or __str__(python 3). These methods must always return strings.

25. Transparent fields list
Do not use Meta.exclude for a model’s fields list description in ModelForm. It is better to use Meta.fields for this as it makes the fields list transparent. Do not use Meta.fields=”__all__” for the same reason.

26. Do not heap all files loaded by user in the same folder
Sometimes even a separate folder for each FileField will not be enough if a large amount of downloaded files is expected. Storing many files in one folder means the file system will search for the needed file more slowly. To avoid such problems, you can do the following:

def get_upload_path(instance, filename):
    return os.path.join('account/avatars/', now().date().strftime("%Y/%m/%d"), filename)

class User(AbstractUser):
    avatar = models.ImageField(blank=True, upload_to=get_upload_path)
27. Use abstract models

If you want to share some logic between models, you can use abstract models.

class CreatedatModel(models.Model):

    created_at = models.DateTimeField(

        verbose_name=u"Created at",

        auto_now_add=True

    )


    class Meta:

        abstract = True

 

class Post(CreatedatModel):

...

 

class Comment(CreatedatModel):

...
28. Use custom Manager and QuerySet

The bigger project you work on, the more you repeat the same code in different places.

To keep your code DRY and allocate business logic in models, you can use custom Managers and Queryset.

For example. If you need to get comments count for posts, from the example above.

class CustomManager(models.Manager):

    def with_comments_counter(self):

        return self.get_queryset().annotate(comments_count=Count('comment_set'))


Now you can use:


posts = Post.objects.with_comments_counter()

posts[0].comments_count

If you want to use this method in chain with others queryset methods,

you should use custom QuerySet:

class CustomQuerySet(models.query.QuerySet):

    """Substitution the QuerySet, and adding additional methods to QuerySet

    """

    def with_comments_counter(self):

        """

        Adds comments counter to queryset

        """

        return self.annotate(comments_count=Count('comment_set'))


Now you can use:


posts = Post.objects.filter(...).with_comments_counter()

posts[0].comments_count 
 

Go check out our case study page. Or read about the top 10 Python frameworks in 2018.

Learn the compeling reasons to choose Django for your project.o autentificado
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
Best practices working with Django models in Python
{{ author.full_name }}
Alexander Stepanov
PYTHON TEAM LEAD
HOMEBLOGENGINEERING
Here we go:

1. Correct Model Naming
It is generally recommended to use singular nouns for model naming, for example: User, Post, Article. That is, the last component of the name should be a noun, e.g.: Some New Shiny Item. It is correct to use singular numbers when one unit of a model does not contain information about several objects.

2. Relationship Field Naming
For relationships such as ForeignKey, OneToOneKey, ManyToMany it is sometimes better to specify a name. Imagine there is a model called Article, - in which one of the relationships is ForeignKey for model User. If this field contains information about the author of the article, then author will be a more appropriate name than user.

3. Correct Related-Name
It is reasonable to indicate a related-name in plural as related-name addressing returns queryset. Please, do set adequate related-names. In the majority of cases, the name of the model in plural will be just right. For example:

class Owner(models.Model):
    pass
class Item(models.Model):
    owner = models.ForeignKey(Owner, related_name='items')
4. Do not use ForeignKey with unique=True
There is no point in using ForeignKey with unique=Trueas there exists OneToOneField for such cases.

5. Attributes and Methods Order in a Model
Preferable attributes and methods order in a model (an empty string between the points).

constants (for choices and other)
fields of the model
custom manager indication
meta
def __unicode__ (python 2) or def __str__ (python 3)
other special methods
def clean
def save
def get_absolut_url
other methods
Please note that the given order was taken from documentations and slightly expanded.

6. Adding a Model via Migration
If you need to add a model, then, having created a class of a model, execute serially manage.py commands makemigrations and migrate (or use South for Django 1.6 and below).

7. Denormalisations
You should not allow thoughtless use of denormalization in relational databases. Always try to avoid it, except for the cases when you denormalise data consciously for whatever the reason may be (e.g. productivity). If at the stage of database designing you understand that you need to denormalise much of the data, a good option could be the use of NoSQL. However, if most of data does not require denormalisation, which cannot be avoided, think about a relational base with JsonField to store some data.

8. BooleanField
Do not use null=True or blank=True for BooleanField. It should also be pointed out that it is better to specify default values for such fields. If you realise that the field can remain empty, you need NullBooleanField.

9. Business Logic in Models
The best place to allocate business logic for your project is in models, namely method models and model manager. It is possible that method models can only provoke some methods/functions. If it is inconvenient or impossible to allocate logic in models, you need to replace its forms or serializers in tasks.

10. Field Duplication in ModelForm
Do not duplicate model fields in ModelForm or ModelSerializer without need. If you want to specify that the form uses all model fields, use MetaFields. If you need to redefine a widget for a field with nothing else to be changed in this field, make use of Meta widgets to indicate widgets.

11. Do not use ObjectDoesNotExist
Using ModelName.DoesNotExist instead of ObjectDoesNotExist makes your exception intercepting more specialised, which is a positive practice.

12. Use of choices
While using choices, it is recommended to:

keep strings instead of numbers in the database (although this is not the best option from the point of optional database use, it is more convenient in practise as strings are more demonstrable, which allows the use of clear filters with get options from the box in REST frameworks).
variables for variants storage are constants. That is why they must be indicated in uppercase.
indicate the variants before the fields lists.
if it is a list of the statuses, indicate it in chronological order (e.g. new, in_progress, completed).
you can use Choices from the model_utils library. Take model Article, for instance:
from model_utils import Choices

class Article(models.Model):
    STATUSES = Choices(
        (0, 'draft', _('draft')),
        (1, 'published', _('published'))   )
    status = models.IntegerField(choices=STATUSES, default=STATUSES.draft)
    …
13. Why do you need an extra .all()?
Using ORM, do not add an extra method call all before filter(), count(), etc.

14. Many flags in a model?
If it is justified, replace several BooleanFields with one field, status-like. e.g.

class Article(models.Model):
    is_published = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    …
Assume the logic of our application presupposes that the article is not published and checked initially, then it is checked and marked is_verified in True and then it is published. You can notice that article cannot be published without being checked. So there are 3 conditions in total, but with 2 boolean fields we do not have 4 possible variants, and you should make sure there are no articles with wrong boolean fields conditions combinations. That is why using one status field instead of two boolean fields is a better option:

class Article(models.Model):
    STATUSES = Choices('new', 'verified', 'published')

    status = models.IntegerField(choices=STATUSES, default=STATUSES.draft)
    …
This example may not be very illustrative, but imagine that you have 3 or more such boolean fields in your model, and validation control for these field value combinations can be really tiresome.

15. Redundant model name in a field name
Do not add model names to fields if there is no need to do so, e.g. if table User has a field user_status - you should rename the field into status, as long as there are no other statuses in this model.

16. Dirty data should not be found in a base
Always use PositiveIntegerField instead of IntegerField if it is not senseless, because “bad” data must not go to the base. For the same reason you should always use unique,unique_together for logically unique data and never use required=False in every field.

17. Getting the earliest/latest object
You can use ModelName.objects.earliest('created'/'earliest') instead of order_by('created')[0] and you can also put get_latest_by in Meta model. You should keep in mind that latest/earliest as well as get can cause an exception DoesNotExist. Therefore, order_by('created').first() is the most useful variant.

18. Never make len(queryset)
Do not use len to get queryset’s objects amount. The count method can be used for this purpose. Like this: len(ModelName.objects.all()), firstly the query for selecting all data from the table will be carried out, then this data will be transformed into a Python object, and the length of this object will be found with the help of len. It is highly recommended not to use this method as count will address to a corresponding SQL function COUNT(). With count, an easier query will be carried out in that database and fewer resources will be required for python code performance.

19. if queryset is a bad idea
Do not use queryset as a boolean value: instead of if queryset: do something use if queryset.exists(): do something. Remember, that querysets are lazy, and if you use queryset as a boolean value, an inappropriate query to a database will be carried out.

20. Using help_text as documentation
Using model help_text in fields as a part of documentation will definitely facilitate the understanding of the data structure by you, your colleagues, and admin users.

21. Money Information Storage
Do not use FloatField to store information about the quantity of money. Instead, use DecimalField for this purpose. You can also keep this information in cents, units, etc.

 

22. Don't use null=true if you don't need it
null=True - Allows column to keep null value.

blank=True - Will be used only if Forms for validation and not related to the database.

In text-based fields, it's better to keep default value.

blank=True

default=''

This way you'll get only one possible value for columns without data.

23. Remove _id
Do not add _id suffix to ForeignKeyField and OneToOneField.

24. Define __unicode__ or __str__
In all non abstract models, add methods __unicode__(python 2) or __str__(python 3). These methods must always return strings.

25. Transparent fields list
Do not use Meta.exclude for a model’s fields list description in ModelForm. It is better to use Meta.fields for this as it makes the fields list transparent. Do not use Meta.fields=”__all__” for the same reason.

26. Do not heap all files loaded by user in the same folder
Sometimes even a separate folder for each FileField will not be enough if a large amount of downloaded files is expected. Storing many files in one folder means the file system will search for the needed file more slowly. To avoid such problems, you can do the following:

def get_upload_path(instance, filename):
    return os.path.join('account/avatars/', now().date().strftime("%Y/%m/%d"), filename)

class User(AbstractUser):
    avatar = models.ImageField(blank=True, upload_to=get_upload_path)
27. Use abstract models

If you want to share some logic between models, you can use abstract models.

class CreatedatModel(models.Model):

    created_at = models.DateTimeField(

        verbose_name=u"Created at",

        auto_now_add=True

    )


    class Meta:

        abstract = True

 

class Post(CreatedatModel):

...

 

class Comment(CreatedatModel):

...
28. Use custom Manager and QuerySet

The bigger project you work on, the more you repeat the same code in different places.

To keep your code DRY and allocate business logic in models, you can use custom Managers and Queryset.

For example. If you need to get comments count for posts, from the example above.

class CustomManager(models.Manager):

    def with_comments_counter(self):

        return self.get_queryset().annotate(comments_count=Count('comment_set'))


Now you can use:


posts = Post.objects.with_comments_counter()

posts[0].comments_count

If you want to use this method in chain with others queryset methods,

you should use custom QuerySet:

class CustomQuerySet(models.query.QuerySet):

    """Substitution the QuerySet, and adding additional methods to QuerySet

    """

    def with_comments_counter(self):

        """

        Adds comments counter to queryset

        """

        return self.annotate(comments_count=Count('comment_set'))


Now you can use:


posts = Post.objects.filter(...).with_comments_counter()

posts[0].comments_count 
 

Go check out our case study page. Or read about the top 10 Python frameworks in 2018.

Learn the compeling reasons to choose Django for your project.
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

Best practices working with Django models in Python
---------------------------------------------------

Source: https://steelkiwi.com/blog/best-practices-working-django-models-python/
Alexander Stepanov - PYTHON TEAM LEAD

1. Correct Model Naming
   
It is generally recommended to use singular nouns for model naming, for example: User, Post, Article. That is, the last component of the name should be a noun, e.g.: Some New Shiny Item. It is correct to use singular numbers when one unit of a model does not contain information about several objects.

2. Relationship Field Naming
For relationships such as ForeignKey, OneToOneKey, ManyToMany it is sometimes better to specify a name. Imagine there is a model called Article, - in which one of the relationships is ForeignKey for model User. If this field contains information about the author of the article, then author will be a more appropriate name than user.

3. Correct Related-Name
It is reasonable to indicate a related-name in plural as related-name addressing returns queryset. Please, do set adequate related-names. In the majority of cases, the name of the model in plural will be just right. For example:

class Owner(models.Model):
    pass
class Item(models.Model):
    owner = models.ForeignKey(Owner, related_name='items')
4. Do not use ForeignKey with unique=True
There is no point in using ForeignKey with unique=Trueas there exists OneToOneField for such cases.

5. Attributes and Methods Order in a Model
Preferable attributes and methods order in a model (an empty string between the points).

constants (for choices and other)
fields of the model
custom manager indication
meta
def __unicode__ (python 2) or def __str__ (python 3)
other special methods
def clean
def save
def get_absolut_url
other methods
Please note that the given order was taken from documentations and slightly expanded.

6. Adding a Model via Migration
If you need to add a model, then, having created a class of a model, execute serially manage.py commands makemigrations and migrate (or use South for Django 1.6 and below).

7. Denormalisations
You should not allow thoughtless use of denormalization in relational databases. Always try to avoid it, except for the cases when you denormalise data consciously for whatever the reason may be (e.g. productivity). If at the stage of database designing you understand that you need to denormalise much of the data, a good option could be the use of NoSQL. However, if most of data does not require denormalisation, which cannot be avoided, think about a relational base with JsonField to store some data.

8. BooleanField
Do not use null=True or blank=True for BooleanField. It should also be pointed out that it is better to specify default values for such fields. If you realise that the field can remain empty, you need NullBooleanField.

9. Business Logic in Models
The best place to allocate business logic for your project is in models, namely method models and model manager. It is possible that method models can only provoke some methods/functions. If it is inconvenient or impossible to allocate logic in models, you need to replace its forms or serializers in tasks.

10. Field Duplication in ModelForm
Do not duplicate model fields in ModelForm or ModelSerializer without need. If you want to specify that the form uses all model fields, use MetaFields. If you need to redefine a widget for a field with nothing else to be changed in this field, make use of Meta widgets to indicate widgets.

11. Do not use ObjectDoesNotExist
Using ModelName.DoesNotExist instead of ObjectDoesNotExist makes your exception intercepting more specialised, which is a positive practice.

12. Use of choices
While using choices, it is recommended to:

keep strings instead of numbers in the database (although this is not the best option from the point of optional database use, it is more convenient in practise as strings are more demonstrable, which allows the use of clear filters with get options from the box in REST frameworks).
variables for variants storage are constants. That is why they must be indicated in uppercase.
indicate the variants before the fields lists.
if it is a list of the statuses, indicate it in chronological order (e.g. new, in_progress, completed).
you can use Choices from the model_utils library. Take model Article, for instance:
from model_utils import Choices

class Article(models.Model):
    STATUSES = Choices(
        (0, 'draft', _('draft')),
        (1, 'published', _('published'))   )
    status = models.IntegerField(choices=STATUSES, default=STATUSES.draft)
    …
13. Why do you need an extra .all()?
Using ORM, do not add an extra method call all before filter(), count(), etc.

14. Many flags in a model?
If it is justified, replace several BooleanFields with one field, status-like. e.g.

class Article(models.Model):
    is_published = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    …
Assume the logic of our application presupposes that the article is not published and checked initially, then it is checked and marked is_verified in True and then it is published. You can notice that article cannot be published without being checked. So there are 3 conditions in total, but with 2 boolean fields we do not have 4 possible variants, and you should make sure there are no articles with wrong boolean fields conditions combinations. That is why using one status field instead of two boolean fields is a better option:

class Article(models.Model):
    STATUSES = Choices('new', 'verified', 'published')

    status = models.IntegerField(choices=STATUSES, default=STATUSES.draft)
    …
This example may not be very illustrative, but imagine that you have 3 or more such boolean fields in your model, and validation control for these field value combinations can be really tiresome.

15. Redundant model name in a field name
Do not add model names to fields if there is no need to do so, e.g. if table User has a field user_status - you should rename the field into status, as long as there are no other statuses in this model.

16. Dirty data should not be found in a base
Always use PositiveIntegerField instead of IntegerField if it is not senseless, because “bad” data must not go to the base. For the same reason you should always use unique,unique_together for logically unique data and never use required=False in every field.

17. Getting the earliest/latest object
You can use ModelName.objects.earliest('created'/'earliest') instead of order_by('created')[0] and you can also put get_latest_by in Meta model. You should keep in mind that latest/earliest as well as get can cause an exception DoesNotExist. Therefore, order_by('created').first() is the most useful variant.

18. Never make len(queryset)
Do not use len to get queryset’s objects amount. The count method can be used for this purpose. Like this: len(ModelName.objects.all()), firstly the query for selecting all data from the table will be carried out, then this data will be transformed into a Python object, and the length of this object will be found with the help of len. It is highly recommended not to use this method as count will address to a corresponding SQL function COUNT(). With count, an easier query will be carried out in that database and fewer resources will be required for python code performance.

19. if queryset is a bad idea
Do not use queryset as a boolean value: instead of if queryset: do something use if queryset.exists(): do something. Remember, that querysets are lazy, and if you use queryset as a boolean value, an inappropriate query to a database will be carried out.

20. Using help_text as documentation
Using model help_text in fields as a part of documentation will definitely facilitate the understanding of the data structure by you, your colleagues, and admin users.

21. Money Information Storage
Do not use FloatField to store information about the quantity of money. Instead, use DecimalField for this purpose. You can also keep this information in cents, units, etc.

 

22. Don't use null=true if you don't need it
null=True - Allows column to keep null value.

blank=True - Will be used only if Forms for validation and not related to the database.

In text-based fields, it's better to keep default value.

blank=True

default=''

This way you'll get only one possible value for columns without data.

23. Remove _id
Do not add _id suffix to ForeignKeyField and OneToOneField.

24. Define __unicode__ or __str__
In all non abstract models, add methods __unicode__(python 2) or __str__(python 3). These methods must always return strings.

25. Transparent fields list
Do not use Meta.exclude for a model’s fields list description in ModelForm. It is better to use Meta.fields for this as it makes the fields list transparent. Do not use Meta.fields=”__all__” for the same reason.

26. Do not heap all files loaded by user in the same folder
Sometimes even a separate folder for each FileField will not be enough if a large amount of downloaded files is expected. Storing many files in one folder means the file system will search for the needed file more slowly. To avoid such problems, you can do the following:

def get_upload_path(instance, filename):
    return os.path.join('account/avatars/', now().date().strftime("%Y/%m/%d"), filename)

class User(AbstractUser):
    avatar = models.ImageField(blank=True, upload_to=get_upload_path)
27. Use abstract models

If you want to share some logic between models, you can use abstract models.

class CreatedatModel(models.Model):

    created_at = models.DateTimeField(

        verbose_name=u"Created at",

        auto_now_add=True

    )


    class Meta:

        abstract = True

 

class Post(CreatedatModel):

...

 

class Comment(CreatedatModel):

...
28. Use custom Manager and QuerySet

The bigger project you work on, the more you repeat the same code in different places.

To keep your code DRY and allocate business logic in models, you can use custom Managers and Queryset.

For example. If you need to get comments count for posts, from the example above.

class CustomManager(models.Manager):

    def with_comments_counter(self):

        return self.get_queryset().annotate(comments_count=Count('comment_set'))


Now you can use:


posts = Post.objects.with_comments_counter()

posts[0].comments_count

If you want to use this method in chain with others queryset methods,

you should use custom QuerySet:

class CustomQuerySet(models.query.QuerySet):

    """Substitution the QuerySet, and adding additional methods to QuerySet

    """

    def with_comments_counter(self):

        """

        Adds comments counter to queryset

        """

        return self.annotate(comments_count=Count('comment_set'))


Now you can use:


posts = Post.objects.filter(...).with_comments_counter()

posts[0].comments_count 
 

Go check out our case study page. Or read about the top 10 Python frameworks in 2018.

Learn the compeling reasons to choose Django for your project.
