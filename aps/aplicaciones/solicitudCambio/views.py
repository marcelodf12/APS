from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.proyectos.models import Proyectos
from aps.aplicaciones.lineasBase.models import lineasBase
from aps.aplicaciones.items.models import items
from aps.aplicaciones.solicitudCambio.models import solicitudCambio
from django.core import serializers
from django.http import HttpResponse
# Create your views here.
#class crearSolicitudCambio(template view):
 #   def get(self, request,*args, **kwargs):
  #      lineaBase = lineasBase.objects.get(id= kwargs ['id'])
   #     listaItems = items.objects.filter(lineaBase=lineaBase)
    #    return render(request, 'solicitudCambio/crear.html',{'items':listaItems})

    #def post(self, request, *args, **kwargs):
     #   idItem = request.POST['idFase']
      #  if idItem!='Seleccione el item':
       #     item = items.objects.get(id=idItem)
           #
        #    descripcion= request.POST['descripcion'],\
         #   fechaExpiracion= request.POST['fechaExpiracion'],\
          #  costoAdicional= request.POST['costoAdicional'],\
           # estado= request.POST['fechaExpiracion'],\
            #nuevaSolicitudCambio = solicitudCambio(descripcion=  descripcion, fechaExpiracion= fechaExpiracion, costoAdicional= costoAdicional, estado= 'pendiente', item= item,)
            #nuevaLineaBase.save()
            #lista = request.POST.getlist('idItems')
            #for l in lista:
             #   elementoNuevo = relacionItemLineaBase(item=items.objects.get(id=l), linea=nuevaLineaBase)
              #  elementoNuevo.save()
            #url = '/proyectos/detalles/' + str(proyecto.id)
            #return HttpResponseRedirect(url)
        #else:
         #       return render(request, 'error/general.html',{'mensaje':'No selecciono ningun item'})

