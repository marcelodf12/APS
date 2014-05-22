from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.proyectos.models import Proyectos
from aps.aplicaciones.items.models import items
from .models import lineasBase, relacionItemLineaBase
from django.core import serializers
from django.http import HttpResponse
# Create your views here.

class crear(TemplateView):
    def get(self, request, *args, **kwargs):
        idProyecto = kwargs['id']
        proyecto = Proyectos.objects.get(id=idProyecto)
        listaFases = fases.objects.filter(proyecto=proyecto)
        return render(request, 'lineaBase/crear.html',{'fases':listaFases})

    def post(self, request, *args, **kwargs):
        idFase = request.POST['idFase']
        if idFase!='Seleccione la fase':
            fase = fases.objects.get(id=idFase)
            proyecto = fase.proyecto
            nombre = request.POST['nombre']
            nuevaLineaBase = lineasBase(nombre=nombre, fase=fase, estado='cerrado')
            nuevaLineaBase.save()
            lista = request.POST.getlist('idItems')
            for l in lista:
                elementoNuevo = relacionItemLineaBase(item=items.objects.get(id=l), linea=nuevaLineaBase)
                elementoNuevo.save()
            url = '/proyectos/detalles/' + str(proyecto.id)
            return HttpResponseRedirect(url)
        else:
            return render(request, 'error/general.html',{'mensaje':'No selecciono la fase'})


class retornarItemsDeFaseAJAX(TemplateView):
    def get(self, request, *args, **kwargs):
        idFase=request.GET['idFase']
        rel = relacionItemLineaBase.objects.filter(linea__fase__id = idFase)
        itemsEnlb = []
        for r in rel:
            itemsEnlb.append(r.item.id)
        print itemsEnlb
        i = items.objects.filter(fase__id=idFase).exclude(pk__in=itemsEnlb)
        data = serializers.serialize('json',i,fields=('nombre','id'))
        return HttpResponse(data, content_type='application/json')