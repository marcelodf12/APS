from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    """ ALGO AQUI """
    nombre = forms.Field()
    apellido = forms.Field()
    correo = forms.Field()