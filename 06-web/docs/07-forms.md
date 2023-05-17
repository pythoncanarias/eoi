---
title: Formularios
---

El formulario de búsqueda (Primera versión):

```html
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label="buscar")
    priority = forms.MultipleChoiceField(label='Prioridad')
```
