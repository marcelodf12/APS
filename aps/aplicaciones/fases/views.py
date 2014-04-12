from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from aps.aplicaciones.fases.models import fases


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