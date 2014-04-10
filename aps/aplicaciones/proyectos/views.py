from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, FormView
from aps.aplicaciones.proyectos.models import Proyectos
from django.core.urlresolvers import reverse_lazy
from aps.aplicaciones.proyectos.forms import ComentariosLog

# Create your views here.
class crearProyecto(CreateView):
    template_name = 'proyectos/crearProyecto.html'
    model = Proyectos
    success_url = reverse_lazy('listar_proyectos')
    #fields = ['nombre','fechaInicio','cantFases']

    def form_valid(self, form):
        proyecto = form.save()
        proyecto.estado='creado'
        proyecto.save()
        return super(crearProyecto, self).form_valid(form)

class adminProyecto(TemplateView):
    template_name = 'proyectos/admin.html'

class listarProyectos(ListView):
    template_name = 'proyectos/verProyectos.html'
    model = Proyectos
    context_object_name = 'proyectos'

class listarProyectosNoIniciados(ListView):
    template_name = 'proyectos/listanoiniciados.html'
    queryset = Proyectos.objects.filter(estado='creado')
    context_object_name = 'proyectos'

class modificarProyectos(UpdateView):
    model = Proyectos
    fields = ['nombre']
    template_name = 'proyectos/update.html'
    success_url = reverse_lazy('listar_proyectos')

    def get_object(self, queryset=None):
        obj = Proyectos.objects.get(id=self.kwargs['id'])
        return obj

class eliminarProyectos(FormView):
    form_class = ComentariosLog
    template_name = 'proyectos/eliminar.html'
    success_url = reverse_lazy('listar_proyectos')

    def form_valid(self, form):
        proyecto = Proyectos.objects.get(id=self.kwargs['id'])
        proyecto.estado='eliminado'
        proyecto.save()
        return super(eliminarProyectos, self).form_valid(form)

class iniciarProyecto(FormView):
    form_class = ComentariosLog
    template_name = 'proyectos/iniciar.html'
    success_url = reverse_lazy('listar_proyectos')

    def form_valid(self, form):
        proyecto = Proyectos.objects.get(id=self.kwargs['id'])
        proyecto.estado='activo'
        proyecto.save()
        return super(iniciarProyecto, self).form_valid(form)
