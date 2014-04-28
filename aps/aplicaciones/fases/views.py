from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import fases
from aps.aplicaciones.proyectos.forms import ComentariosLog
from aps.aplicaciones.proyectos.models import Proyectos


# Create your views here.
class adminFases(TemplateView):
    template_name = 'fases/admin.html'

class crearFaseEnProyecto(CreateView):
    model = fases
    template_name = 'fases/crear.html'
    success_url = reverse_lazy("admin_proyecto")
    fields = ['nombre', 'fechaInicioP', 'fechaInicioR','presupuesto']

    # def form_valid(self, form):
    #     p=Proyectos.objects.get(id=self.kwargs['id'])
    #     fas=fases.objects.filter(proyecto=p)
    #     cant_act=0
    #     for f in fas:
    #         cant_act+=1
    #     if(p.cantFases>cant_act):
    #         fase = form.save()
    #         fase.estado = 'creado'
    #         fase.proyecto = p
    #         fase.save()
    #         print fase
    #         return super(crearFaseEnProyecto, self).form_valid(form)
    #     else:
    #         return render(self.request, 'error/general.html', {'mensaje':'Ya no se pueden agregar fases'})

class listarFases(ListView):
    model = fases
    template_name = 'fases/listar.html'
    context_object_name = 'fases'

class modificarFases(UpdateView):
    """ Vista de modificacion de fases, hereda atributos y metodos de la clase UpdateView """
    model = fases
    fields = ['nombre']     # Permite modificar solo el campo 'nombre'
    template_name = 'fases/update.html'
    success_url = reverse_lazy('listar_proyectos')      # Se mostrara la vista 'listar_proyectos' en el caso de modificacion exitosa

    def get_object(self, queryset=None):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = fases.objects.get(id=self.kwargs['id'])
        return obj

class eliminarFase(FormView):
    """ Vista de eliminacion de fases, hereda atributos y metodos de la clase FormView """
    form_class = ComentariosLog
    template_name = 'fases/eliminar.html'
    success_url = reverse_lazy('listar_proyectos')      # Se mostrara la vista 'listar_proyectos' en el caso de eliminacion exitosa

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        fase = fases.objects.get(id=self.kwargs['id'])
        fase.estado='eliminado'
        fase.save()
        return super(eliminarFase, self).form_valid(form)