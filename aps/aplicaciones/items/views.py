
""" Los nombres de clases son los nombres de las vistas que posteriormente son invocadas en el archivo URLS.py
Las vistas son definidas en base a los modelos definidos en el archivo MODELS.py """
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, FormView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect

from .models import *
from .forms import ComentariosLog
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.proyectos.models import Proyectos

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

class listarItemParaCrearRelacion(TemplateView):
    def get(self, request, *args, **kwargs):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        itemHijo = items.objects.get(id=kwargs['id'])
        faseAct = itemHijo.fase
        listaItems=items.objects.filter(fase=faseAct).exclude(id=itemHijo.id)
        if(faseAct.orden>1):
            proyecto = faseAct.proyecto
            faseAnt = fases.objects.get(proyecto=proyecto, orden=faseAct.orden-1)
            listaItems=(items.objects.filter(fase=faseAct).exclude(id=itemHijo.id) | items.objects.filter(fase=faseAnt))
        return render(self.request, 'relaciones/crearRelacion.html', {'items':listaItems, 'id':itemHijo.id})

class crearRelacion(TemplateView):
    def post(self, request, *args, **kwargs):
        Padre=items.objects.get(id=request.POST['itemPadre'])
        Hijo=items.objects.get(id=request.POST['itemHijo'])
        if(relacion.objects.filter(itemHijo=Hijo, itemPadre=Padre)==[]):
            print 'no se creo'
        else:
            r = relacion()
            r.itemHijo=Hijo
            r.itemPadre=Padre
            r.estado=True
            r.save()
            print 'se creo'
        url = '/items/relaciones/listar/' + str(Padre.fase.proyecto.id)
        return HttpResponseRedirect(url)


class listarRelaciones(TemplateView):
    def get(self, request, *args, **kwargs):
        queryset = relacion.objects.filter(itemHijo__fase__proyecto__id=kwargs['id'])
        proyecto = Proyectos.objects.get(id=kwargs['id'])
        return render(self.request, 'relaciones/listar.html',{'relaciones':queryset, 'proyecto':proyecto.nombre})

class eliminarRelacion(DeleteView):
    model = relacion
    template_name = 'relaciones/delete.html'
    success_url = reverse_lazy('listar_proyectos')
    def get_object(self, queryset=None):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = relacion.objects.get(id=self.kwargs['id'])
        return obj

class agregarAtributo(CreateView):
    template_name = 'items/agregarAtributo.html'
    model = atributo
    success_url = reverse_lazy('listar_proyectos')
    fields = ['nombre','descripcion']

    def form_valid(self, form):
        item = items.objects.get(id=self.kwargs['id'])
        versionNueva = item.versionAct + 1
        atributosAnt = atributo.objects.filter(item=item, version=item.versionAct).order_by('pk')
        for a in atributosAnt:
            nuevo = atributo(nombre=a.nombre, descripcion=a.descripcion, item=item, version=versionNueva)
            nuevo.save()
        atrib = form.save()
        atrib.item = item
        atrib.version = versionNueva
        item.versionAct = versionNueva
        atrib.save()
        item.save()
        return super(agregarAtributo, self).form_valid(form)

class mostrarDetalles(TemplateView):
    def get(self, request, *args, **kwargs):
        item = items.objects.get(id=kwargs['id'])
        atributos = atributo.objects.filter(item=item, version=item.versionAct).order_by('pk')
        return render(self.request, 'items/listarAtributos.html',{'item':item, 'atributos':atributos})

class mostrarDetallesV(TemplateView):
    def get(self, request, *args, **kwargs):
        item = items.objects.get(id=kwargs['id'])
        atributos = atributo.objects.filter(item=item, version=kwargs['idV']).order_by('pk')
        return render(self.request, 'items/listarOtrasVersiones.html',{'item':item, 'atributos':atributos, 'version':kwargs['idV']})

class listarVersiones(TemplateView):
    def get(self, request, *args, **kwargs):
        item = items.objects.get(id=kwargs['id'])
        return render(self.request, 'items/listarVersiones.html',{'item':item, 'range':range(1,item.versionAct+1)})

class ReversionVersiones(TemplateView):
    def get(self, request, *args, **kwargs):
        item = items.objects.get(id=kwargs['id'])
        return render(self.request, 'items/reversion.html',{'item':item, 'range':range(1,item.versionAct+1)})


class reversionar(TemplateView):
    def post(self, request, *args, **kwargs):
        item = items.objects.get(id=request.POST['idItem'])
        versionVieja = request.POST['version']
        atributos = atributo.objects.filter(item=item, version=versionVieja).order_by('pk')
        versionNueva = item.versionAct + 1
        for a in atributos:
            nuevo = atributo(nombre=a.nombre, descripcion=a.descripcion, item=item, version=versionNueva)
            nuevo.save()
        item.versionAct = versionNueva
        item.save()
        url = '/items/atributos/listar/' + str(item.id)
        return HttpResponseRedirect(url)