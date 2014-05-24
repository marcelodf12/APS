from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from aps.aplicaciones.lineasBase.models import lineasBase, relacionItemLineaBase
from aps.aplicaciones.items.models import items
from aps.aplicaciones.solicitudCambio.models import solicitudCambio, votos
from aps.aplicaciones.proyectos.models import Proyectos, Miembros
from django.core import serializers
from django.http import HttpResponse
# Create your views here.
class crearSolicitudCambio(TemplateView):
    def get(self, request,*args, **kwargs):
        item = items.objects.get(id= kwargs ['id'])
        return render(request, 'solicitudCambio/crear.html',{'item':item})

    def post(self, request, *args, **kwargs):
        idItem = request.POST['idItem']
        itemRellb = relacionItemLineaBase.objects.get(item__id=idItem)
        if idItem!=0:
            item = items.objects.get(id=idItem)
            descripcion = request.POST['descripcion']
            costoAdicional = request.POST['costoAdicional']
            nuevaSolicitudCambio = solicitudCambio(descripcion=descripcion, costoAdicional=costoAdicional, estado='pendiente', item=item,usuario=request.user, lineaBase=itemRellb.linea)
            nuevaSolicitudCambio.save()
            url = '/proyectos/detalles/' + str(itemRellb.linea.fase.proyecto.id)
            comite = Miembros.objects.filter(proyecto=item.fase.proyecto, comite=True).exclude(miembro=item.fase.proyecto.lider)
            for c in comite:
                nuevoVoto = votos(usuario=c.miembro, solicitud=nuevaSolicitudCambio)
                nuevoVoto.save()
            nuevoVoto = votos(usuario=item.fase.proyecto.lider, solicitud=nuevaSolicitudCambio)
            nuevoVoto.save()
            return HttpResponseRedirect(url)
        else:
            return render(request, 'error/general.html',{'mensaje':'No selecciono ningun item'})

