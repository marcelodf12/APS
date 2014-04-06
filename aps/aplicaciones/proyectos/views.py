from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from aps.aplicaciones.proyectos.models import Proyectos
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class crearProyecto(CreateView):
    template_name = 'proyectos/crearProyecto.html'
    model = Proyectos
    success_url = reverse_lazy('listar_proyectos')

class adminProyecto(TemplateView):
    template_name = 'proyectos/admin.html'

class listarProyectos(ListView):
    template_name = 'proyectos/verProyectos.html'
    model = Proyectos
    context_object_name = 'proyectos'