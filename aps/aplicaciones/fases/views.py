from django.views.generic import TemplateView, CreateView, ListView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy

from .models import fases
from aps.aplicaciones.items.models import items, relacion
from aps.aplicaciones.proyectos.forms import ComentariosLog
from aps.aplicaciones.proyectos.models import Proyectos
from django.shortcuts import render, HttpResponseRedirect
from aps.aplicaciones.permisos.models import Permisos
import datetime


# Create your views here.
class adminFases(TemplateView):
    """
        Vista de administracion de fases, hereda atributos y metodos de la clase TemplateView
    """
    template_name = 'fases/admin.html'

class crearFaseEnProyecto(CreateView):
    """
        Vista de creacion de fase en un proyecto especifico, hereda atributos y metodos de la clase CreateView
    """
    model = fases
    template_name = 'fases/crear.html'
    success_url = reverse_lazy("listar_proyectos")
    fields = ['nombre', 'fechaInicioP','presupuesto']

    def form_valid(self, form):
         p=Proyectos.objects.get(id=self.kwargs['id'])
         fas=fases.objects.filter(proyecto=p)
         cant_act=0
         for f in fas:
             cant_act+=1
         if(p.cantFases>cant_act):
             if(p.fechaInicio<form.cleaned_data['fechaInicioP']):
                 fase = form.save()
                 fase.estado = 'creado'
                 fase.proyecto = p
                 fase.save()
                 print fase
                 return super(crearFaseEnProyecto, self).form_valid(form)
             else:
                 return super(crearFaseEnProyecto,self).form_invalid(form)
         else:
             return render(self.request, 'error/general.html', {'mensaje':'Ya no se pueden agregar fases','nombreProyecto':p.nombre,'url':'/proyectos/detalles/'+str(p.id)})

class listarFases(ListView):
    """
        Vista para listar fases de los proyectos, hereda atributos y metodos de la clase ListView
    """
    model = fases
    template_name = 'fases/listar.html'
    context_object_name = 'fases'

class modificarFases(UpdateView):
    """
        Vista de modificacion de fases, hereda atributos y metodos de la clase UpdateView
    """
    model = fases
    fields = ['nombre', 'presupuesto']     # Permite modificar solo el campo 'nombre'
    template_name = 'fases/update.html'

    def get_object(self, queryset=None):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = fases.objects.get(id=self.kwargs['id'])
        self.fase = obj
        return obj

    def form_valid(self, form):
        proyecto = self.fase.proyecto
        if((not Permisos.valido(usuario=self.request.user,permiso='MODF',tipoObjeto='proyecto',id=proyecto.id)) and (not proyecto.lider==self.request.user)):
            return render(self.request, 'error/permisos.html')
        self.fase.nombre = form.cleaned_data['nombre']
        self.fase.presupuesto = form.cleaned_data['presupuesto']
        self.fase.save()
        return HttpResponseRedirect('/proyectos/detalles/'+str(self.fase.proyecto.id))


class eliminarFase(FormView):
    """
        Vista de eliminacion de fases, hereda atributos y metodos de la clase FormView
    """
    form_class = ComentariosLog
    template_name = 'fases/eliminar.html'
    success_url = reverse_lazy('listar_proyectos')      # Se mostrara la vista 'listar_proyectos' en el caso de eliminacion exitosa

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        fase = fases.objects.get(id=self.kwargs['id'])
        fase.estado='eliminado'
        print fase.estado
        fase.save()
        return super(eliminarFase, self).form_valid(form)

class finalizarFase(FormView):
    """
        Vista para finalizar fases de un proyecto, hereda atributos y metodos de la clase FormView
    """
    form_class = ComentariosLog
    template_name = 'fases/finalizar.html'
    success_url = reverse_lazy('listar_fasesFinalizadas')      # Se mostrara la vista 'listar_fasesFinalizadas' en el caso de eliminacion exitosa

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """

        fase = fases.objects.get(id=self.kwargs['id'])
        proyecto = fase.proyecto
        if((not Permisos.valido(usuario=self.request.user,permiso='FINF',tipoObjeto='proyecto',id=proyecto.id)) and (not proyecto.lider==self.request.user)):
            return render(self.request, 'error/permisos.html')
        item=items.objects.filter(fase=fase).exclude(estado='eliminado')

        for i in item:
            #Consultamos si el item ya fue finalizado
            if(i.estado != 'finalizado'):
                return render(self.request, 'error/general.html', {'mensaje':'Se ha encontrado un item no finalizado'})

        #Buscamos la Fase anterior
        ordenAnterior=fase.orden-1
        if ordenAnterior>0:
            faseAnterior = fases.objects.get(orden=ordenAnterior, proyecto=fase.proyecto)

            #Consultamos el estado de la fase anterior
            if(faseAnterior.estado != 'finalizada'):
                return render(self.request, 'error/general.html', {'mensaje':'La fase anterior no ha sido finalizada aun'})

        fase.estado = 'finalizada'
        fase.save()

        ordenPosterior=fase.orden+1
        if ordenPosterior<=fase.proyecto.cantFases:
            fasePosterior = fases.objects.get(orden=ordenPosterior, proyecto=fase.proyecto)
            fasePosterior.fechaInicioR = datetime.datetime.now().date()
            fasePosterior.save()


        #todas las fases de este proyecto
        #fasesR = fases.objects.filter(proyecto_id=fase.proyecto)
        #print fasesR
        if fase.orden == fase.proyecto.cantFases:
            fase.proyecto.estado='finalizado'
            hoy=datetime.datetime.now().date()
            fase.proyecto.fechaFinR = hoy
            diasRestantes = datetime.datetime.strptime(str(fase.proyecto.fechaFinP), '%Y-%m-%d').date() - hoy
            if(diasRestantes.days<0):
                fase.proyecto.penalizacion = diasRestantes.days * fase.proyecto.penalizacion
            else:
                fase.proyecto.penalizacion = 0
            fase.proyecto.save()
            return render(self.request, 'proyectos/listarAJAX.html', {'seFinalizo':True, 'proyecto':fase.proyecto})
        return HttpResponseRedirect('/proyectos/detalles/'+str(fase.proyecto.id))

class listarFasesFinalizadas(ListView):
    """
        Vista de listado de fases finalizadas, hereda atributos y metodos de la clase ListView
    """
    model = fases
    template_name = 'fases/listarFinalizadas.html'
    context_object_name = 'fases'
