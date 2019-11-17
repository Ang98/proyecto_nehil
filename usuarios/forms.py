""""usuario formularios"""


from django import forms

class perfilForm (forms.Form):

    numero = forms.CharField(max_length=9,required=True)
    tipo_usuario = forms.CharField(max_length=20, required=True)


class profesorForm(forms.Form):

       profesion = forms.CharField(max_length=20, required=True)


class alumnoForm(forms.Form):

    imagen = forms.ImageField()
