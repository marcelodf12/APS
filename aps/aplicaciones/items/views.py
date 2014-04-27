
""" Los nombres de clases son los nombres de las vistas que posteriormente son invocadas en el archivo URLS.py
Las vistas son definidas en base a los modelos definidos en el archivo MODELS.py """
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import items
from .forms import ComentariosLog

# Create your views here.
class adminItems(TemplateView):
    """ Vista de administracion de items, hereda atributos y metodos de la clase TemplateView """
    template_name = 'items/admin.html'         # Se define la direccion y nombre del template

class crearItem(CreateView):
    """ Vista de creacion de items, hereda atributos y metodos de la clase CreateView """
    model = items                               # Se asocia al modelo 'items'
    template_name = 'items/crear.html'
    success_url = reverse_lazy("admin_items")   # Se mostrara la vista 'admin_items' en el caso de creacion exitosa
    fields = ['nombre','complejidad','fase']

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        item=form.save()        # Se guardan los datos del formulario en 'item'????????
        item.versionAct = 1     # Se define un valor predeterminado para la version del item
        item.estado = 'creado'
        item.save()             # Se guardan ?????????
        return super(crearItem, self).form_valid(form)

class listarItems(ListView):
    """ Vista de listado de items, hereda atributos y metodos de la clase ListView """
    model = items
    template_name = 'items/listar.html'
    context_object_name = 'items'

class listarItemsEliminados(ListView):
    """ Vista de listado de items, hereda atributos y metodos de la clase ListView """
    model = items
    template_name = 'items/listar eliminados.html'
    context_object_name = 'items'

class modificarItems(UpdateView):
    """ Vista de modificacion de proyectos, hereda atributos y metodos de la clase UpdateView """
    model = items
    #fields = ['nombre']     # Permite modificar solo el campo 'nombre'
    template_name = 'items/update.html'
    success_url = reverse_lazy('listar_item')      # Se mostrara la vista 'listar_proyecto' en el caso de modificacion exitosa
    fields = ['nombre','complejidad','fase']

    def get_object(self, queryset=None):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = items.objects.get(id=self.kwargs['id'])
        return obj

class eliminarItems(FormView):
    """ Vista de eliminacion de proyectos, hereda atributos y metodos de la clase FormView """
    form_class = ComentariosLog
    template_name = 'items/eliminar.html'
    success_url = reverse_lazy('listar_item')      # Se mostrara la vista 'listar_proyectos' en el caso de eliminacion exitosa

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        item = items.objects.get(id=self.kwargs['id'])
        item.estado='eliminado'
        item.save()
        return super(eliminarItems, self).form_valid(form)