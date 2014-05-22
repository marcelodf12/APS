from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.proyectos.models import Proyectos
from .models import lineasBase, relacionItemLineaBase
# Create your views here.

class crear(TemplateView):
    def get(self, request, *args, **kwargs):
        idProyecto = kwargs['id']
        proyecto = Proyectos.objects.get(id=idProyecto)
        listaFases = fases.objects.filter(proyecto=proyecto)
        return render(request, 'lineaBase/crear.html',{'fases':listaFases})

    def post(self, request, *args, **kwargs):
        idFase = request.POST['idFase']
        fase = fases.objects.get(id=idFase)
        proyecto = fase.proyecto
        nombre = request.POST['nombre']
        nuevaLineaBase = lineasBase(nombre=nombre, fase=fase, estado='cerrado')
        url = '/proyectos/detalles/' + str(proyecto.id)
        return HttpResponseRedirect(url)


class crearEnFase(TemplateView):
    def post(self, request, *args, **kwargs):
        pass