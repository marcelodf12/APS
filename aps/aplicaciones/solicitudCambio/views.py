from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from aps.aplicaciones.lineasBase.models import lineasBase, relacionItemLineaBase
from aps.aplicaciones.items.models import items
from aps.aplicaciones.solicitudCambio.models import solicitudCambio, votos
from aps.aplicaciones.proyectos.models import Proyectos, Miembros
from datetime import date, timedelta
from django.core import serializers
from django.http import HttpResponse
# Create your views here.
class listarVotaciones(TemplateView):
    """
       Vista que lista todas las votaciones pendientes
    """
    def get(self, request, *args, **kwargs):
        usuario = request.user
        votaciones = votos.objects.filter(usuario=usuario, estado='pendiente')
        return render(request, 'solicitudCambio/listarVotaciones.html',{'votaciones':votaciones})

class votar(TemplateView):
    """
        Vista que Muestra los detalles de una solicitud, permite votar para aceptar o rechazar una solicitud, y abre la linea base en caso que ya no haya votos pendientes y se haya mayoria de votos en aceptado
        Si hay un empate el voto del lider desempata
    """
    def get(self, request, *args, **kwargs):
        voto = votos.objects.get(id=kwargs['id'])
        return render(request, 'solicitudCambio/votar.html', {'voto':voto})

    def post(self, request, *args, **kwargs):
        voto = votos.objects.get(id=request.POST['id'])
        if request.POST['voto'] == 'True':
            voto.aceptar = True
        else:
            voto.aceptar = False
        voto.estado = 'listo'
        voto.save()
        faltantes = votos.objects.filter(solicitud=voto.solicitud, estado='pendiente')
        if not faltantes:
            aFavor = len(votos.objects.filter(solicitud=voto.solicitud, aceptar=True))
            enContra = len(votos.objects.filter(solicitud=voto.solicitud, aceptar=False))
            print 'Fin de la votacion ' + str(aFavor) + 'a favor contra ' + str(enContra) + 'en contra'
            if aFavor > enContra:
                voto.solicitud.estado = 'aceptada'
                voto.solicitud.fechaExpiracion = date.today() + timedelta(days=7)
            elif enContra > aFavor:
                voto.solicitud.estado = 'rechazada'
            else:
                print 'empate'
                if votos.objects.get(usuario=voto.solicitud.item.fase.proyecto.lider).aceptar:
                    print 'lider voto aceptar'
                    voto.solicitud.estado = 'aceptada'
                    voto.solicitud.fechaExpiracion = date.today() + timedelta(days=7)
                else:
                    print 'lider voto rechazar'
                    voto.solicitud.estado = 'rechazada'
            voto.solicitud.save()
            if voto.solicitud.estado == 'aceptada':
                lb = relacionItemLineaBase.objects.get(item=voto.solicitud.item).linea
                lb.estado = 'abierto'
                lb.save()
        else:
            print 'falta todavia'
        usuario = request.user
        votaciones = votos.objects.filter(usuario=usuario, estado='pendiente')
        return render(request, 'solicitudCambio/listarVotaciones.html',{'votaciones':votaciones})


class crearSolicitudCambio(TemplateView):
    """
    Vista que permite crear una nueva solicitud de cambio
    """
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
            nuevaSolicitudCambio = solicitudCambio(descripcion=descripcion, costoAdicional=costoAdicional, estado='pendiente', item=item,usuario=request.user, lineaBase=itemRellb.linea, orden=item.versionAct)
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

