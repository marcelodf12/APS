from django.views.generic import TemplateView, CreateView, ListView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy

from .models import fases
from aps.aplicaciones.items.models import items, relacion
from aps.aplicaciones.proyectos.forms import ComentariosLog
from aps.aplicaciones.proyectos.models import Proyectos
from django.shortcuts import render, HttpResponseRedirect



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

        #todas las fases de este proyecto
        fasesR = fases.objects.filter(proyecto_id=fase.proyecto)
        print fasesR

        return render(self.request, 'fases/listarFinalizadas.html', {'nombreProyecto':fase.proyecto.nombre, 'url':'/proyectos/detalles/'+str(fase.proyecto.id), 'idProyecto':fase.proyecto.id,'fases':fasesR})

class listarFasesFinalizadas(ListView):
    """
        Vista de listado de fases finalizadas, hereda atributos y metodos de la clase ListView
    """
    model = fases
    template_name = 'fases/listarFinalizadas.html'
    context_object_name = 'fases'
