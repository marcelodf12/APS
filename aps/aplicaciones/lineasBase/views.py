""" Los nombres de clases son los nombres de las vistas que posteriormente son invocadas en el archivo URLS.py
Las vistas son definidas en base a los modelos definidos en el archivo MODELS.py """

from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.proyectos.models import Proyectos
from aps.aplicaciones.items.models import items
from .models import lineasBase, relacionItemLineaBase
from django.core import serializers
from django.http import HttpResponse
# Create your views here.

class crear(TemplateView):
    """
        Vista para crear una Linea Base, hereda metodos y atributos de la clase TemplateView
    """
    def get(self, request, *args, **kwargs):
        idProyecto = kwargs['id']
        proyecto = Proyectos.objects.get(id=idProyecto)
        listaFases = fases.objects.filter(proyecto=proyecto)
        return render(request, 'lineaBase/crear.html',{'fases':listaFases, 'nombreProyecto':proyecto.nombre, 'proyecto':proyecto})

    def post(self, request, *args, **kwargs):
        idFase = request.POST['idFase']
        if idFase!='Seleccione la fase':
            fase = fases.objects.get(id=idFase)
            proyecto = fase.proyecto
            nombre = request.POST['nombre']
            if nombre == '':
                return render(request, 'error/general.html',{'mensaje':'El campo nombre es obligatorio'})
            nuevaLineaBase = lineasBase(nombre=nombre, fase=fase, estado='cerrado')
            nuevaLineaBase.save()
            lista = request.POST.getlist('idItems')
            if lista:
                for l in lista:
                    item=items.objects.get(id=l)
                    elementoNuevo = relacionItemLineaBase(item=item, linea=nuevaLineaBase)
                    item.estado='finalizado'
                    item.save()
                    elementoNuevo.save()
                url = '/proyectos/detalles/' + str(proyecto.id)
                return HttpResponseRedirect(url)
            else:
                return render(request, 'error/general.html',{'mensaje':'No selecciono ningun item'})
        else:
            return render(request, 'error/general.html',{'mensaje':'No selecciono la fase'})


class retornarItemsDeFaseAJAX(TemplateView):
    """
        Vista que permite el retorno de una lista de items que pertenecen a una fase especifica, hereda metodos y atributos de la clase TemplateView
    """
    def get(self, request, *args, **kwargs):
        idFase=request.GET['idFase']
        rel = relacionItemLineaBase.objects.filter(linea__fase__id = idFase)
        itemsEnlb = []
        for r in rel:
            itemsEnlb.append(r.item.id)
        print itemsEnlb
        i = items.objects.filter(fase__id=idFase).exclude(pk__in=itemsEnlb).filter(estado='finalizado')
        data = serializers.serialize('json',i,fields=('nombre','id'))
        return HttpResponse(data, content_type='application/json')

class listarLineasBase(TemplateView):
    """
        Vista que permite listar todas las Lineas Base, hereda metodos y atributos de la clase TemplateView
    """
    def get(self, request, *args, **kwargs):
        proyecto=Proyectos.objects.get(id=kwargs['id'])
        listaLineasBase=lineasBase.objects.filter(fase__proyecto=proyecto)
        print listaLineasBase
        return render(request, 'lineaBase/listar.html', {'lineasBase': listaLineasBase,\
                                                         'url':'/proyectos/detalles/'+str(kwargs['id']),\
                                                         'nombreProyecto':proyecto.nombre,\
                                                         'proyecto':proyecto})

class listarDetallesLineasBase(TemplateView):
    """
        Vista que permite visualizar en detalle los datos asociados a una Linea Base en particular, hereda metodos y atributos de la clase TemplateView
    """
    def get(self, request, *args, **kwargs):
        lb = lineasBase.objects.get(id=kwargs['id'])
        proyecto = lb.fase.proyecto
        listaDetalles=relacionItemLineaBase.objects.filter(linea__id=kwargs['id'])
        return render(request, 'lineaBase/listarDetalles.html', {'detalles':listaDetalles,\
                                                         'url':'/proyectos/detalles/'+str(proyecto.id),\
                                                         'nombreProyecto':proyecto.nombre, 'lineaBase':lb})