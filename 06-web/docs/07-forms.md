---
title: Formularios
---

In this tutorial, we'll show you how to work with HTML Forms in Django, and, in particular, the easiest way to write forms to create, update, and delete model instances.

Vamos a crear en primer lugar un formulario de busqueda que nos permite
buscar por el titulo de las tareas, y luego crearemos formularios para dar de
alta, editar y borrar tareas.

## Overview

An HTML Form is a group of one or more fields/widgets on a web page, which can be used to collect information from users for submission to a server. Forms are a flexible mechanism for collecting user input because there are suitable widgets for entering many different types of data, including text boxes, checkboxes, radio buttons, date pickers

## El formulario de búsqueda (Primera versión)

Vamos a empezar con un sencillo formulario de busqueda, escrito directamente
en HTML:

```html
<form action="/search/" method="post">
  <label for="txt_query">Buscar: </label>
  <input
    id="txt_query"
    type="search"
    name="query"
    placeholder="texto a buscar">
  <input type="submit" value="OK">
</form>
```

Este formulario solo tiene un campo de entrada, aunque lo más
normal es que haya varios. El atributo `name` es imprescindible
para definir el nombre que usaremos posteriormente para recuperar
el valor tecleado por el usuario. El campo `id` se utiliza para identificar el
control pero solo para Html, CSS y/o javascript. En el servidor, lo único que
nos interesa es el nombre.

El control de tipo `submit` es el botón que enviará los datos del formulario a
su destino, esto es, la URL indicada en el campo `action` del formulario.


- `action`

:   The resource/URL where data is to be sent for processing when the form is
    submitted. If this is not set (or set to an empty string), then the form
    will be submitted back to the current page URL.

- `method`

:   The HTTP method used to send the data: post or get.  The POST method
    should always be used if the data is going to result in a change to the
    server's database, because it can be made more resistant to cross-site
    forgery request attacks.  The GET method should only be used for forms that
    don't change user data (for example, a search form). It is recommended for
    when you want to be able to bookmark or share the URL.

The role of the server is first to render the initial form state — either
containing blank fields or pre-populated with initial values. After the user
presses the submit button, the server will receive the form data with values
from the web browser and must validate the information. If the form contains
invalid data, the server should display the form again, this time with
user-entered data in "valid" fields and messages to describe the problem for
the invalid fields. Once the server gets a request with all valid form data, it
can perform an appropriate action (such as: saving the data, returning the
result of a search, uploading a file, etc.) and then notify the user.

As you can imagine, creating the HTML, validating the returned data,
re-displaying the entered data with error reports if needed, and performing the
desired operation on valid data can all take quite a lot of effort to "get
right". Django makes this a lot easier by taking away some of the heavy lifting
and repetitive code!

The main things that Django's form handling does are:

1.- Display the default form the first time it is requested by the user.

    - The form may contain blank fields if you're creating a new record, or it
      may be pre-populated with initial values (for example, if you are
      changing a record, or have useful default initial values).

    - The form is referred to as unbound at this point, because it isn't
      associated with any user-entered data (though it may have initial
      values).

2.- Receive data from a submit request and bind it to the form.

    - Binding data to the form means that the user-entered data and any errors
      are available when we need to redisplay the form.

3.- Clean and validate the data.
    
    - Cleaning the data performs sanitization of the input fields, such as
      removing invalid characters that might be used to send malicious content
      to the server, and converts them into consistent Python types.

    - Validation checks that the values are appropriate for the field (for
      example, that they are in the right date range, aren't too short or too
      long, etc.)

4.- If any data is invalid, re-display the form, this time with any user populated values and error messages for the problem fields.

5.- Si todos los datos son válidos, realizar la acción: Salvar los datos,
enviar un correo, devolver los resultados de una busqueda, etc.

6.- Finalmente, redirigir al usuario a otra página, especialmente si hemos
hecho alguna operación que realize modificaciones.

## La clase `Form`

Para ayudar en todas estos pasos, Django define la clase `Form`. Esta clase
ayuda en dos cosas principalmente, visualizar el formulario y validar los datos
iontroducidos por el usuario.

Para definir un formulario de búsqueda similar al anterior, primero
creamos un fichero `forms.py` y definimos el siguiente código:

```py
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label="Buscar")
```

Coimo vemos, la declaración es muy similar a la de un modelo. Definimos
campos con unos nombres, `query`, que son de un determinado tipo, `CharField`.
Sin embargo, en el modelo heredamos de la mcase `Model`, y aqui heredamos
de la clas `Form`.

Con respecto a los tipos de datos, en el siguiente listado mostramos los
disponibles, que sin duda nos recuerdan a los de la definición de los modelos.

- `BooleanField`
- `CharField`
- `ChoiceField`
- `TypedChoiceField`
- `DateField`
- `DateTimeField`
- `DecimalField`
- `DurationField`
- `EmailField`
- `FileField`
- `FilePathField`
- `FloatField`
- `ImageField`
- `IntegerField`
- `GenericIPAddressField`
- `MultipleChoiceField`
- `TypedMultipleChoiceField`
- `NullBooleanField`
- `RegexField`
- `SlugField`
- `TimeField`
- `URLField`
- `UUIDField`
- `ComboField`
- `MultiValueField`
- `SplitDateTimeField`
- `ModelMultipleChoiceField`
- `ModelChoiceField`

Algunos de los parámetros comunes a todos estos tipos son:

- `**required**`: Si esta a `True` (Que es el valor por defecto), el campo es
  obligatorio, es decir, tiene que tener un valor. Si queremos tener campos
  opcionales hay que acordarse de usar `required=False`.

- `**label**`: La etiqueta que se mostrará al lado del control. Si no se
  especifica, Django imporvisará una a partir del nombre.

- `**label_suffix**`: Seprador a usar entre la etiqueta y el control. Por
  defecto vale `:`.

- `**initial**`: El valor inicial a mostrar en el control.

- `**widget**`: El tipo de control a usar.

- `**help_text**`: Es un texto adicional, que se puede mostrar en el formulario
  como ayuda al usuario.

- `**error_messages**`: Una lista de errores asociados al campo. Esto permite
  reescribir estos mensajes, si fuera necesario.

- `**validators**`: Una lista de funciones (validadores) que seran ejecutadas para cada campo a fin de validar el contenido.

- `**disabled**`: El control se mostrara desabilitado si pasamos este parámetre
  como `True`. POr defecto es `False`, logicaente.

## Validación de formularios

Django proporciona diferentes formas, no excluyentes, de validar los valores
contenidos en un formulario. La forma más sencilla es usar el parámetro
`vaidators` que acabamos de ver en la definición de los campos.

Una segunda forma es escribir un método que se llame `clean_<fieldname>()`. POr
ejemplo, para validar un campo que se llame `due_date`, escribiriamos un método
en la clase `Form` que se llame `clean_due_date`. 

Al ser un método, `clean_due_date` tiene acceso a todo el formulario, en su
parámetro `self`, así que puede ser interensate en aquellos casos en los que la
validación de un campo necesite los datos de otro campo. Por ejemplo, si
tuvieramos una fecha de publicacion de la tarea, podriamos verifica que la
fecha de entrega tiene que ser posterior a la fecha de publicación (Aunque para
estos casos existe una alternativa mejor que es el método `clean`, que veremoas
más adelante).


```py
class TaskForm(Form):
    due_date = DateTimeField(...)
    pub_date = DateTimeField(...)
    ...

    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']
        pub_date = self.cleaned_data['due_date']
        if due_date <= pub_date:
            raise ValidationError(
                'Fecha de entrega invalida. Debe ser'
                ' posterior a la fecha de publicación'
                )
        # Remember to always return the cleaned data.
        return due_date
```

A diferencia de las funciones de validación especificas de cada campo, los
métodos `clean_<fieldname>` puede acceder a los datos en `cleaned_data` (porque
la primera ronda de validaciones ya se ha realizado sin problemas) y además, y
esto es importante, tienen que **devolver el campo, siempre**. Aquí está
permitido realizar un cambio en el dato, si  nos interesa, cosa que no podemos
hacer con las validaciones normales. Por ejemplo, para textos, se podría
eliminar espacios antes y después del escrito por el usuario, si los hubiera.
La idea es que este método deberia limpiar el dato y presentarl en su forma
final.

Finalmente, está el método general `clean`, orientado a validar el formulario
en su totalidad. Como el método es usado por el framework, el primer paso será
casi con toda seguridad llamar a la versión de nuestro antecesor, y luego
realizar el ressto de validaciones que queramos sobre `cleaned_data`. 

La validación anterior quizá seria mas recomendable realizarla aqui, ya que no
sabemos en realildad si es la fecha de entrega o la fecha de publicación la que
esta mal.

```py
class TaskForm(Form):
    due_date = DateTimeField(...)
    pub_date = DateTimeField(...)
    ...

    def clean(self):
        cleaned_data = super().clean()
        due_date = cleaned_data['due_date']
        pub_date = cleaned_data['due_date']
        if due_date <= pub_date:
            raise ValidationError(
                'Fecha de entrega invalida. Debe ser'
                ' posterior a la fecha de publicación'
                )
        return cleaned_data
```

Los errores detectados aquí no se pueden asigna a un campo concreto (Si no
fuera asi, los tendriamos como validaciones de campo), así que estan accesibles
en `form.non_field_errors`.

## La vista que procesa el formulario

[TODO]






