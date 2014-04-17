from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import fases


# Create your views here.
class adminFases(TemplateView):
    template_name = 'fases/admin.html'

class crearFase(CreateView):
    model = fases
    template_name = 'fases/crear.html'
    success_url = reverse_lazy("admin_fases")
    #fields = ['nombre', 'complejidad']

    def form_valid(self, form):
        fase=form.save()
        fase.estado = 'creado'
        fase.save()
        return super(crearFase, self).form_valid(form)

class listarFases(ListView):
    model = fases
    template_name = 'fases/listar.html'
    context_object_name = 'fases'

class modificarFases(UpdateView):
    """ Vista de modificacion de proyectos, hereda atributos y metodos de la clase UpdateView """
    model = fases
    fields = ['nombre']     # Permite modificar solo el campo 'nombre'
    template_name = 'fases/update.html'
    success_url = reverse_lazy('listar_fases')      # Se mostrara la vista 'listar_proyecto' en el caso de modificacion exitosa

    def get_object(self, queryset=None):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = fases.objects.get(id=self.kwargs['id'])
        return obj