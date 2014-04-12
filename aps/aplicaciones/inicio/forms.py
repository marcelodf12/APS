from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    """ Definicion del formulario personalizado UserForm """
    nombre = forms.Field()
    apellido = forms.Field()
    correo = forms.Field()