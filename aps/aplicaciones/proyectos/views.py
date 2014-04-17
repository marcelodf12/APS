""" Los nombres de clases son los nombres de las vistas que posteriormente son invocadas en el archivo URLS.py
Las vistas son definidas en base a los modelos definidos en el archivo MODELS.py
"""
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, FormView
from aps.aplicaciones.proyectos.models import Proyectos
from django.core.urlresolvers import reverse_lazy
from aps.aplicaciones.proyectos.forms import ComentariosLog

# Create your views here.
class crearProyecto(CreateView):
    """ Vista de creacion de proyectos, hereda atributos y metodos de la clase CreateView """
    template_name = 'proyectos/crearProyecto.html'      # Se define la direccion y nombre del template
    model = Proyectos                                   # Se asocia al modelo 'items'
    success_url = reverse_lazy('listar_proyectos')      # Se mostrara la vista 'listar_proyecto' en el caso de registro exitoso
    #fields = ['nombre','fechaInicio','cantFases']

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        proyecto = form.save()
        proyecto.estado='creado'
        proyecto.save()
        return super(crearProyecto, self).form_valid(form)

class adminProyecto(TemplateView):
    """ Vista de administracion de proyectos, hereda atributos y metodos de la clase TemplateView """
    template_name = 'proyectos/admin.html'

class listarProyectos(ListView):
    """ Vista de listado de proyectos, hereda atributos y metodos de la clase ListView """
    template_name = 'proyectos/verProyectos.html'
    model = Proyectos
    context_object_name = 'proyectos'           # Se define un nombre para los objetos de esta clase (utilizado por
                                                # ejemplo para iterar en el template)
class listarProyectosNoIniciados(ListView):
    """ Vista de listado de proyectos no iniciados, hereda atributos y metodos de la clase ListView """
    template_name = 'proyectos/listanoiniciados.html'
    queryset = Proyectos.objects.filter(estado='creado')    # Se usa un filtro para mostrar los proyectos con estado creado
    context_object_name = 'proyectos'

class modificarProyectos(UpdateView):
    """ Vista de modificacion de proyectos, hereda atributos y metodos de la clase UpdateView """
    model = Proyectos
    fields = ['nombre']     # Permite modificar solo el campo 'nombre'
    template_name = 'proyectos/update.html'
    success_url = reverse_lazy('listar_proyectos')      # Se mostrara la vista 'listar_proyecto' en el caso de modificacion exitosa

    def get_object(self, queryset=None):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = Proyectos.objects.get(id=self.kwargs['id'])
        return obj

class eliminarProyectos(FormView):
    """ Vista de eliminacion de proyectos, hereda atributos y metodos de la clase FormView """
    form_class = ComentariosLog
    template_name = 'proyectos/eliminar.html'
    success_url = reverse_lazy('listar_proyectos')      # Se mostrara la vista 'listar_proyectos' en el caso de eliminacion exitosa

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        proyecto = Proyectos.objects.get(id=self.kwargs['id'])
        proyecto.estado='eliminado'
        proyecto.save()
        return super(eliminarProyectos, self).form_valid(form)

class iniciarProyecto(FormView):
    """ Vista de inicio de proyectos, hereda atributos y metodos de la clase FormView """
    form_class = ComentariosLog
    template_name = 'proyectos/iniciar.html'
    success_url = reverse_lazy('listar_proyectos')

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        proyecto = Proyectos.objects.get(id=self.kwargs['id'])
        proyecto.estado='activo'
        proyecto.save()
        return super(iniciarProyecto, self).form_valid(form)

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
