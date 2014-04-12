from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from aps.aplicaciones.items.models import items

""" Los nombres de clases son los nombres de las vistas que posteriormente son invocadas en el archivo URLS.py """
""" Las vistas son definidas en base a los modelos definidos en el archivo MODELS.py """

# Create your views here.
class adminItems(TemplateView):
    """ Vista de administracion de items, hereda atributos y metodos de la clase TemplateView """
    template_name = 'items/admin.html'         # Se define la direccion y nombre del template

class crearItem(CreateView):
    """ Vista de creacion de items, hereda atributos y metodos de la clase CreateView """
    model = items                               # Se asocia al modelo 'items'
    template_name = 'items/crear.html'
    success_url = reverse_lazy("admin_items")   # Se mostrara la vista 'admin_items' en el caso de creacion exitosa
    #fields = ['nombre', 'complejidad']         # PENDIENTE???????

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