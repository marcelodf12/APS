from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.proyectos.forms import ComentariosLog


# Create your views here.
class adminFases(TemplateView):
    template_name = 'fases/admin.html'
class crearFase(CreateView):
    model = fases
    template_name = 'fases/crear.html'
    success_url = reverse_lazy("admin_fases")


    def form_valid(self, form):
        fase = form.save()
        fase.estado = 'creado'
        fase.save()
        return super(crearFase, self).form_valid(form)

class listarFases(ListView):
    model = fases
    template_name = 'fases/listar.html'
    context_object_name = 'fases'

class modificarFases(UpdateView):
    """ Vista de modificacion de fases, hereda atributos y metodos de la clase UpdateView """
    model = fases
    fields = ['nombre']     # Permite modificar solo el campo 'nombre'
    template_name = 'fases/update.html'
    success_url = reverse_lazy('listar_fases')      # Se mostrara la vista 'listar_fases' en el caso de modificacion exitosa

    def get_object(self, queryset=None):

        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = fases.objects.get(id=self.kwargs['id'])
        return obj

class eliminarFase(FormView):
    """ Vista de eliminacion de fases, hereda atributos y metodos de la clase FormView """
    form_class = ComentariosLog
    template_name = 'fases/eliminar.html'
    success_url = reverse_lazy('listar_fases')      # Se mostrara la vista 'listar_proyectos' en el caso de eliminacion exitosa

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        fase = fases.objects.get(id=self.kwargs['id'])
        fase.estado='eliminado'
        fase.save()
        return super(eliminarFase, self).form_valid(form)