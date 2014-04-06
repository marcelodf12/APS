from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from django.views.generic import FormView
from aps.aplicaciones.inicio.forms import UserForm
from django.core.urlresolvers import reverse_lazy
from aps.aplicaciones.inicio.models import Usuario

class home(TemplateView):
    template_name = 'inicio/inicio.html'


class Registrarse(FormView):
    template_name = 'inicio/registro.html'
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        usuarioNuevo = Usuario()
        usuarioNuevo.user = user
        usuarioNuevo.nombre = form.cleaned_data['nombre']
        usuarioNuevo.apellido = form.cleaned_data['apellido']
        usuarioNuevo.correo = form.cleaned_data['correo']
        usuarioNuevo.estado = 'activo'
        usuarioNuevo.save()
        return super(Registrarse, self).form_valid(form)