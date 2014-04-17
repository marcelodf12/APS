""" Los nombres de clases son los nombres de las vistas que posteriormente son invocadas en el archivo URLS.py """

from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User, Group
from aps.aplicaciones.inicio.forms import UserForm, ActualizarPass
from django.shortcuts import render, HttpResponseRedirect

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

class UpdateUser(UpdateView):
    model = User
    template_name = "inicio/modificar.html"
    success_url = reverse_lazy('home')
    fields= ['first_name', 'last_name','email']

    def get_object(self, queryset=None):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = User.objects.get(id=self.kwargs['id'])
        return obj

class ActualizarPassView(FormView):
    form_class = ActualizarPass
    template_name = 'inicio/modificarPassword.html'
    success_url = reverse_lazy('inicio')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        usuario=request.user
        if form.is_valid():
            return self.form_valid(form, usuario, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def form_valid(self, form, usuario):
        nombre=form.cleaned_data['usuario']
        passAnt=(form.cleaned_data['passAnt'])
        pass1=form.cleaned_data['pass1']
        pass2=form.cleaned_data['pass2']
        if pass1==pass2:
            if(usuario.check_password(passAnt)):
                usuario.set_password(pass1)
                usuario.save()
        return HttpResponseRedirect('/inicio/')

class CrearGrupo(CreateView):
    model = Group
    template_name = 'inicio/crearGrupo.html'
    success_url = reverse_lazy('home')
    fields = ['name']

class adminGrupos(TemplateView):
    """ Vista de administracion de proyectos, hereda atributos y metodos de la clase TemplateView """
    template_name = 'inicio/adminGrupos.html'

class listarGrupos(ListView):
    """ Vista de listado de proyectos, hereda atributos y metodos de la clase ListView """
    template_name = 'inicio/listarGrupos.html'
    model = Group
    context_object_name = 'grupos'

class eliminarGrupo(DeleteView):
    """ Vista para Eliminar un Grupo """
    model = Group
    template_name = 'inicio/deleteGrupo.html'
    success_url = reverse_lazy('listar_grupos')      # Se mostrara la vista 'listar_permisos' en el caso de modificacion exitosa

    def get_object(self, queryset=None):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = Group.objects.get(id=self.kwargs['id'])
        return obj

class listarUsuarios(ListView):
    """ Vista de listado de proyectos, hereda atributos y metodos de la clase ListView """
    template_name = 'inicio/listarUsuarios.html'
    model = User
    context_object_name = 'usuarios'

class asignarGrupo(UpdateUser):
    template_name = 'inicio/asignarGrupo.html'
    fields = ['groups']

class listarUsuriosDeGrupo(ListView):
    template_name = 'inicio/listarUsuariosDeGrupo.html'
    context_object_name = 'usuarios'

    def get_object(self, queryset=None):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = User.objects.filter(id=self.kwargs['id'])
        return obj