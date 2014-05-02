""" Los nombres de clases son los nombres de las vistas que posteriormente son invocadas en el archivo URLS.py
Las vistas son definidas en base a los modelos definidos en el archivo MODELS.py
"""
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, FormView
from .models import Proyectos
from django.core.urlresolvers import reverse_lazy
from .forms import ComentariosLog
from aps.aplicaciones.permisos.models import Permisos
from django.shortcuts import HttpResponseRedirect, render
from django.template.response import TemplateResponse
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.items.models import items
import datetime

# Create your views here.

class crearProyecto(CreateView):
    """ Vista de creacion de proyectos, hereda atributos y metodos de la clase CreateView """
    template_name = 'proyectos/crearProyecto.html'      # Se define la direccion y nombre del template
    model = Proyectos                                   # Se asocia al modelo 'Proyectos'
    success_url = reverse_lazy('listar_proyectos')      # Se mostrara la vista 'listar_proyecto' en el caso de registro exitoso
    fields = ['nombre','fechaInicio','fechaFinP','cantFases','presupuesto','penalizacion']

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        if(Permisos.valido(usuario=self.request.user,permiso='ADD',tipoObjeto='proyecto',id=0)):
            proyecto = form.save()
            proyecto.estado ='creado'
            proyecto.lider = self.request.user
            proyecto.save()
            return super(crearProyecto, self).form_valid(form)
        else:
            return HttpResponseRedirect('/error/permisos/')


class adminProyecto(TemplateView):
    """ Vista de administracion de proyectos, hereda atributos y metodos de la clase TemplateView """
    def get(self, request, *args, **kwargs):
        if(Permisos.valido(permiso='VER', tipoObjeto='proyecto', usuario=self.request.user, id=0)):
            return TemplateResponse(request, 'proyectos/admin.html', {})
        else:
            return HttpResponseRedirect('/error/permisos/')

class listarProyectosNoIniciados(ListView):
    """ Vista de listado de proyectos no iniciados, hereda atributos y metodos de la clase ListView """
    template_name = 'proyectos/listanoiniciados.html'
    queryset = Proyectos.objects.filter(estado='creado')    # Se usa un filtro para mostrar los proyectos con estado creado
    context_object_name = 'proyectos'

class modificarProyectos(UpdateView):
    """ Vista de modificacion de proyectos, hereda atributos y metodos de la clase UpdateView """
    model = Proyectos
    fields = ['nombre','fechaInicio','fechaFinP','penalizacion','presupuesto']     # Permite modificar solo el campo 'nombre'
    template_name = 'proyectos/update.html'
    success_url = reverse_lazy('listar_proyectos')      # Se mostrara la vista 'listar_proyecto' en el caso de modificacion exitosa

    def get_object(self, queryset=None):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = Proyectos.objects.get(id=self.kwargs['id'])
        return obj

    def form_valid(self, form):
        p=Proyectos.objects.get(id=self.kwargs['id'])
        if(p.estado == 'creado'):
            if(Permisos.valido(usuario=self.request.user,tipoObjeto='proyecto',id=self.kwargs['id'],permiso='MOD')):
                #print 'tiene permiso'
                return super(modificarProyectos, self).form_valid(form)
            else:
                #print 'no tiene permiso'
                return HttpResponseRedirect('/error/permisos/')
        else:
            return render(self.request, 'error/general.html', {'mensaje':'Solo puede modificar un proyecto No iniciado'})


class eliminarProyectos(FormView):
    """ Vista de eliminacion de proyectos, hereda atributos y metodos de la clase FormView """
    form_class = ComentariosLog
    template_name = 'proyectos/eliminar.html'
    success_url = reverse_lazy('listar_proyectos')      # Se mostrara la vista 'listar_proyectos' en el caso de eliminacion exitosa


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        usuario=request.user
        id_proyecto = kwargs['id']
        if form.is_valid():
            if Permisos.valido(usuario=usuario, permiso='DEL', tipoObjeto='proyecto', id=id_proyecto):
                proyecto = Proyectos.objects.get(id=self.kwargs['id'])
                proyecto.estado='eliminado'
                proyecto.save()
                return HttpResponseRedirect('/proyectos/listar/')
            else:
                return HttpResponseRedirect('/error/permisos/')
        else :
            return self.form_invalid(form)

class iniciarProyecto(FormView):
    """ Vista de inicio de proyectos, hereda atributos y metodos de la clase FormView """
    form_class = ComentariosLog
    template_name = 'proyectos/iniciar.html'
    success_url = reverse_lazy('listar_proyectos')

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        proyecto = Proyectos.objects.get(id=self.kwargs['id'])
        fas=fases.objects.filter(proyecto=proyecto)
        cant_act=0
        for f in fas:
            cant_act+=1
        if(proyecto.cantFases==cant_act):
            proyecto.estado='activo'
            proyecto.save()
            return super(iniciarProyecto, self).form_valid(form)
        else:
            return render(self.request, 'error/general.html', {'mensaje':'El proyecto no tiene todas las fases creadas'})

class listarProyectosAJAX(ListView):
    model = Proyectos
    context_object_name = 'projectos'
    template_name = 'proyectos/listarAJAX.html'


from django.core import serializers
from django.http import HttpResponse
class proyectos_ajax(TemplateView):
    def get(self, request, *args, **kwargs):
        estado_proyecto = request.GET['estado']
        proyectos = Proyectos.objects.filter(estado=estado_proyecto)
        data = serializers.serialize('json',proyectos,fields=('nombre','fechaInicio','cantFases'))
        return HttpResponse(data, mimetype='application/json')


class detallesProyecto(TemplateView):
    """ Vista de administracion de proyectos, hereda atributos y metodos de la clase TemplateView """
    def get(self, request, *args, **kwargs):
        p=Proyectos.objects.get(id=self.kwargs['id'])
        f=fases.objects.filter(proyecto=p).order_by('pk')
        i=items.objects.filter(fase__proyecto=p)
        costo_total=0
        for fas in f:
            cos_fas = 0
            aux = items.objects.filter(fase=fas)
            for a in aux:
                cos_fas += a.costo
            fas.costo = cos_fas
            fas.save()
        for it in i:
            costo_total += it.costo
        print costo_total
        hoy=datetime.datetime.now().date()
        diasRestantes = datetime.datetime.strptime(str(p.fechaFinP), '%Y-%m-%d').date() - hoy
        if(diasRestantes.days<0):
            penalizacion = diasRestantes.days * p.penalizacion
        else:
            penalizacion = 0
        saldo = p.presupuesto - costo_total + penalizacion
        print saldo


        # for fas in f:
        #     i.append(items.objects.filter(fase=fas))
        if(True):
            return TemplateResponse(request, 'proyectos/tablaProyecto.html', {
                'proyecto':p ,
                'fases':f,
                'items':i,
                'costoTotal':costo_total,
                'diasRestantes':diasRestantes,
                'penalizacion':penalizacion,
                'saldo': saldo
            })
        else:
            return HttpResponseRedirect('/error/permisos/')