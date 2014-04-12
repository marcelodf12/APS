""" Los nombres de clases son los nombres de las vistas que posteriormente son invocadas en el archivo URLS.py """

from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from django.views.generic import FormView
from aps.aplicaciones.inicio.forms import UserForm
from django.core.urlresolvers import reverse_lazy
from aps.aplicaciones.inicio.models import Usuario  # se importan los modelos definidos en el archivo MODELS.py



class home(TemplateView):
    """ Vista de bienvenida (login exitoso), hereda atributos y metodos de la clase TemplateView """

    template_name = 'inicio/inicio.html'    # Se define la direccion y nombre del template


class Registrarse(FormView):
    """ Vista para registrar un usuario, hereda atributos y metodos de la clase FormView """
     #No posee ninguna vista asociada?????????????????

    template_name = 'inicio/registro.html'
    form_class = UserForm                   # ???????????
    success_url = reverse_lazy('login')     # Se mostrara la vista 'login' en el caso de registro exitoso

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """

        user = form.save()          # Se guardan los datos del formulario en 'item'????????
        usuarioNuevo = Usuario()    # Se crea un objeto de tipo Usuario

        # Se guarda los datos del formulario en el objeto 'UsuarioNuevo' creado anteriormente
        usuarioNuevo.user = user
        usuarioNuevo.nombre = form.cleaned_data['nombre']
        usuarioNuevo.apellido = form.cleaned_data['apellido']
        usuarioNuevo.correo = form.cleaned_data['correo']
        usuarioNuevo.estado = 'activo'
        usuarioNuevo.save()
        return super(Registrarse, self).form_valid(form)