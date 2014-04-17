from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from aps.aplicaciones.permisos.models import Permisos
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.
class admin(TemplateView):
    """ Vista de administracion de proyectos, hereda atributos y metodos de la clase TemplateView """
    template_name = 'permisos/admin.html'

class listar(ListView):
    """ Vista de listado de proyectos, hereda atributos y metodos de la clase ListView """
    template_name = 'permisos/listar.html'
    model = User
    context_object_name = 'usuarios'

class crear(CreateView):
    """ Vista de creacion de proyectos, hereda atributos y metodos de la clase CreateView """
    template_name = 'permisos/crear.html'      # Se define la direccion y nombre del template
    model = Permisos                                  # Se asocia al modelo 'items'
    success_url = reverse_lazy('listar_permisos')      # Se mostrara la vista 'listar_proyecto' en el caso de registro exitoso

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        permiso = form.save()
        permiso.save()
        return super(crear, self).form_valid(form)

from django.core import serializers
from django.http import HttpResponse
class permisos_ajax(TemplateView):
    def get(self, request, *args, **kwargs):
        id_usuario = request.GET['idusuario']
        permisos = Permisos.objects.filter(usuario__id=id_usuario)
        data = serializers.serialize('json',permisos,fields=('permiso','tipoObjeto','proyecto','fase','item'))
        return HttpResponse(data, mimetype='application/json')

class eliminar(DeleteView):
    """ Vista para Eliminar un permiso """
    model = Permisos
    template_name = 'permisos/delete.html'
    success_url = reverse_lazy('listar_permisos')      # Se mostrara la vista 'listar_permisos' en el caso de modificacion exitosa

    def get_object(self, queryset=None):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = Permisos.objects.get(id=self.kwargs['id'])
        return obj