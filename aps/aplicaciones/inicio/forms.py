from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

class UserForm(UserCreationForm):
    """ Definicion del formulario personalizado UserCreationForm """
    nombre = forms.Field()
    apellido = forms.Field()
    correo = forms.Field()

class ActualizarPass(forms.Form):
    usuario=forms.CharField(max_length=30, label='Nombre Usuario')
    passAnt=forms.CharField(widget=forms.PasswordInput(), label='Password Anterior')
    pass1=forms.CharField(widget=forms.PasswordInput(), label='Nuevo Password', min_length=6)
    pass2=forms.CharField(widget=forms.PasswordInput(), label='Confirmacion')
