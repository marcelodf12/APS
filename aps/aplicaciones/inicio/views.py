""" Los nombres de clases son los nombres de las vistas que posteriormente son invocadas en el archivo URLS.py """

from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from django.views.generic import FormView
from aps.aplicaciones.inicio.forms import UserForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User


class home(TemplateView):
    """ Vista de bienvenida (login exitoso), hereda atributos y metodos de la clase TemplateView """

    template_name = 'inicio/inicio.html'    # Se define la direccion y nombre del template


class Registrarse(FormView):
    """ Vista para registrar un usuario, hereda atributos y metodos de la clase FormView """

    template_name = 'inicio/registro.html'
    form_class = UserForm                   # Formulario a utilizar para la vista
    success_url = reverse_lazy('login')     # Se mostrara la vista 'login' en el caso de registro exitoso

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        user = form.save()
        user.first_name = form.cleaned_data['nombre']
        user.last_name = form.cleaned_data['apellido']
        user.email = form.cleaned_data['correo']
        user.save()
        return super(Registrarse, self).form_valid(form)