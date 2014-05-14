
""" Los nombres de clases son los nombres de las vistas que posteriormente son invocadas en el archivo URLS.py
Las vistas son definidas en base a los modelos definidos en el archivo MODELS.py """
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy

from .models import items
from .forms import ComentariosLog
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.items.models import items_versiones
from django.http import HttpResponse

# Create your views here.
class adminItems(TemplateView):
    """ Vista de administracion de items, hereda atributos y metodos de la clase TemplateView """
    template_name = 'items/admin.html'         # Se define la direccion y nombre del template

class crearItem(CreateView):
    """ Vista de creacion de items, hereda atributos y metodos de la clase CreateView """
    model = items                               # Se asocia al modelo 'items'
    template_name = 'items/crear.html'
    success_url = reverse_lazy("admin_items")   # Se mostrara la vista 'admin_items' en el caso de creacion exitosa
    fields = ['nombre', 'complejidad', 'costo']

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        item=form.save()        # Se guardan los datos del formulario en 'item'????????
        item.versionAct = 1     # Se define un valor predeterminado para la version del item
        item.estado = 'creado'
        item.save()
        return super(crearItem, self).form_valid(form)

class crearItemEnFase(CreateView):
    model = items
    template_name = 'items/crear.html'
    success_url = reverse_lazy('listar_proyectos')
    fields = ['nombre', 'complejidad', 'costo']

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        f= fases.objects.get(id=self.kwargs['id'])
        item=form.save()        # Se guardan los datos del formulario en 'item'????????
        item.versionAct = 1     # Se define un valor predeterminado para la version del item
        item.estado = 'creado'
        item.fase = f
        item.save()
        return super(crearItemEnFase, self).form_valid(form)

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
    fields = ['nombre','complejidad','costo']     # Permite modificar solo el campo 'nombre'
    template_name = 'items/update.html'
    success_url = reverse_lazy('listar_item')      # Se mostrara la vista 'listar_proyecto' en el caso de modificacion exitosa

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

class items_ajax(TemplateView):
    def get(self, request, *args, **kwargs):
        id_item = request.GET['iditems']
        print 'id items: ' + str(id_item)
        version = items_versiones.objects.filter(item_id=id_item)
        print 'versiones '
        print version
        datajson = '['
        c=1
        for v in version:
            print 'vuelta' + str(c)
            c+=1
            proyecto=fase=item=atributo='none'
            tipo=v.version
            print 'Version: ' + str(tipo)
            #pk_id=v.id_fk
            # if tipo =='proyecto' and pk_id!=0:
            #     proyecto=items_versiones.objects.get(id=pk_id).nombre
            #     print 'entro por proyecto' + str(proyecto)
            # elif tipo =='fase':
            #     fase=fases.objects.get(id=pk_id).nombre
            #     print 'entro por fase' + str(fase)
            # elif tipo =='item':
            #     item=items.objects.get(id=pk_id).nombre
            #     print 'entro por item' + str(item)
            datajson+='{"pk": ' + str(v.id) + ', "model": "items.items.versiones", "fields": {'
            # datajson+='"permiso": "' + v.permiso + '", '
            # datajson+='"tipoObjeto": "' + v.tipoObjeto + '", '
            # datajson+='"proyecto": "' + proyecto + '", '
            # datajson+='"fases": "' + fase + '", '

            datajson+='"version": "' + tipo + '"}},'

            print 'HASTA AQUI ' + str(tipo)
            print 'json1--> ' + datajson
        if (len(datajson)>1):
            datajson=datajson[:-1]
        datajson+=']'
        print 'json2--> ' + datajson
        #data = serializers.serialize('json',permisos,fields=('permiso','tipoObjeto','proyecto','fases','items'))
        #print data
        print 'LLEGUE AL FINAL'
        return HttpResponse(datajson, content_type = 'application/json')

class listarVersiones(ListView):
    """ Vista de listado de proyectos, hereda atributos y metodos de la clase ListView """
    template_name = 'items/listarAJAX.html'
    model = items
    context_object_name = 'items'