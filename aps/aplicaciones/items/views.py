
""" Los nombres de clases son los nombres de las vistas que posteriormente son invocadas en el archivo URLS.py
Las vistas son definidas en base a los modelos definidos en el archivo MODELS.py """
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, FormView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect

from .models import items, atributo, relacion, tipoItem
from .forms import ComentariosLog
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.proyectos.models import Proyectos
import pickle


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
    """
    Vista para listar los item candidatos a ser padres y crear una Relacion
    :param id: El identificador del item
    """
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
    """
    Vista para crear una relacion
    :param itemPadre: Identificador el Item Padre
    :param itemHijo: Identificador el Item Hijo
    :return: Se redirecciona a la lista de relaciones del proyecto
    """
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
    """
    Vista que retorna una lista de relaciones
    """
    def get(self, request, *args, **kwargs):
        queryset = relacion.objects.filter(itemHijo__fase__proyecto__id=kwargs['id'])
        proyecto = Proyectos.objects.get(id=kwargs['id'])
        return render(self.request, 'relaciones/listar.html',{'relaciones':queryset, 'proyecto':proyecto.nombre})

class eliminarRelacion(DeleteView):
    """
    Vista que elimina una relacion
    :param id: El identificador de la relacion a eliminar
    :return: Se redirecciona a la lista de relaciones del proyecto
    """
    model = relacion
    template_name = 'relaciones/delete.html'
    success_url = reverse_lazy('listar_proyectos')
    def get_object(self, queryset=None):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = relacion.objects.get(id=self.kwargs['id'])
        return obj

class agregarAtributo(CreateView):
    """
        Vista para agregar un atributo
        :param id: El identificador del item al que se quiere agregar un atributo
        :return: Se redirecciona a la lista de atributos del item
    """
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
        url = '/items/atributos/listar/'+str(item.id)
        return HttpResponseRedirect(url)



class mostrarDetalles(TemplateView):
    """
        Vista que muestra los detalles de un item
        :param id: El identificador del item
    """
    def get(self, request, *args, **kwargs):
        item = items.objects.get(id=kwargs['id'])
        atributos = atributo.objects.filter(item=item, version=item.versionAct).order_by('pk')
        return render(self.request, 'items/listarAtributos.html',{'item':item, 'atributos':atributos})

class mostrarDetallesV(TemplateView):
    """
        Vista que muestra los detalles de un item
        :param id: El identificador del item
    """
    def get(self, request, *args, **kwargs):
        item = items.objects.get(id=kwargs['id'])
        atributos = atributo.objects.filter(item=item, version=kwargs['idV']).order_by('pk')
        return render(self.request, 'items/listarOtrasVersiones.html',{'item':item, 'atributos':atributos, 'version':kwargs['idV']})

class modificarAtributo(UpdateView):
    """
        Vista que modifica un atributo y crea una nueva version del item
        :param id: El identificador del item
        :return: Se redirecciona a la lista de atributos del item
    """
    model = atributo
    template_name = 'items/updateAtributo.html'
    fields = ['descripcion']
    def get_object(self, queryset=None):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = atributo.objects.get(id=self.kwargs['id'])
        nuevo = atributo(nombre=obj.nombre, descripcion=obj.descripcion, item=obj.item, version=obj.version)
        return nuevo

    def form_valid(self, form):
        a=form.save()
        item = a.item
        atrib = atributo.objects.filter(item=item, version=item.versionAct).exclude(nombre=a.nombre).order_by('pk')
        versionNueva = item.versionAct + 1
        for i in atrib:
            nuevo = atributo(nombre=i.nombre, descripcion=i.descripcion, item=item, version=versionNueva)
            nuevo.save()
        a.version = versionNueva
        item.versionAct = versionNueva
        a.save()
        item.save()
        url = '/items/atributos/listar/'+str(item.id)
        return HttpResponseRedirect(url)

class eliminarAtributo(TemplateView):
    """
        Vista para eliminar un atributo
    """
    def get(self, request, *args, **kwargs):
        a = atributo.objects.get(id=kwargs['id'])
        item=a.item
        atributos = atributo.objects.filter(item=item, version=item.versionAct).exclude(id=a.id).order_by('pk')
        versionNueva = item.versionAct + 1
        for i in atributos:
            nuevo = atributo(nombre=i.nombre, descripcion=i.descripcion, item=item, version=versionNueva)
            nuevo.save()
        item.versionAct = versionNueva
        item.save()
        url = '/items/atributos/listar/' + str(item.id)
        return HttpResponseRedirect(url)

class listarVersiones(TemplateView):
    """
        Vista para listar las versiones de un items
    """
    def get(self, request, *args, **kwargs):
        item = items.objects.get(id=kwargs['id'])
        return render(self.request, 'items/listarVersiones.html',{'item':item, 'range':range(1,item.versionAct+1)})

class ReversionVersiones(TemplateView):
    """
        Vista muestra las posibles versiones para reversionar un item
    """
    def get(self, request, *args, **kwargs):
        item = items.objects.get(id=kwargs['id'])
        return render(self.request, 'items/reversion.html',{'item':item, 'range':range(1,item.versionAct+1)})


class reversionar(TemplateView):
    """
        Vista para reversionar un item
    """
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

class crearTipoItem(CreateView):
    """
        Vista para crear un nuevo tipo de items
    """
    model = tipoItem
    fields = ['nombre']
    success_url = reverse_lazy('home')
    template_name = 'items/tipoItem/crear.html'
    def form_valid(self, form):
        ti = form.save()
        ti.atributos = pickle.dumps([])
        ti.save()
        return super(crearTipoItem, self).form_valid(form)

class agregarAtributoAlTipoItem(TemplateView):
    """
        Vista que agrega un nuevo atributo al tipo de item
    """
    def post(self, request, *args, **kwargs):
        ti=tipoItem.objects.get(id=request.POST['id'])
        listaAtributos = pickle.loads(ti.atributos)
        for n in range(1, int(request.POST['cantidad'])+1):
            listaAtributos.append(request.POST['a' + str(n)])
        ti.atributos= pickle.dumps(listaAtributos)
        ti.save()
        url = '/items/tipoItem/mostrar/' + str(ti.id)
        return HttpResponseRedirect(url)

class definirCantidadAtributos(TemplateView):
    """
        Vista que define la cantidad de atributos a agregar a un tipo de items
    """
    def get(self, request, *args, **kwargs):
        return render(request,'items/tipoItem/agregarAtributo.html',{'tipos':tipoItem.objects.order_by('nombre')})

class formularioAgregarAtributoAlTipoItem(TemplateView):
    """
        Vista que muestra un formulario con N atributos nuevos para agregar a un tipo de items
    """
    def post(self, request, *args, **kwargs):
        ti=tipoItem.objects.get(id=request.POST['id'])
        cant=int(request.POST['cantidad'])
        return render(request,'items/tipoItem/agregarAtributosN.html',{'id':ti.id,'range':range(1,cant+1),'cantidad':cant})

class verAtributosTipoItems(TemplateView):
    """
        Vista para ver los atributos de un tipo de items
    """
    def get(self, request, *args, **kwargs):
        ti = tipoItem.objects.get(id=kwargs['id'])
        listaAt = pickle.loads(ti.atributos)
        return render(request, 'items/tipoItem/mostrar.html', {'atributos':listaAt, 'tipo':ti})

class verTipoItems(ListView):
    """
        Ver los detalles de un tipo de items
    """
    model = tipoItem
    context_object_name = 'tipos'
    template_name = 'items/tipoItem/listar.html'

class modificarAtributoDeTipoItem(TemplateView):
    """
        Vista para modificar los atributos de un tipo de items
    """
    def get(self, request, *args, **kwargs):
        ti=tipoItem.objects.get(id=kwargs['id'])
        listati = pickle.loads(ti.atributos)
        listaTupla = []
        c = 0
        for l in listati:
            listaTupla.append((c,l))
            c+=1
        print listaTupla
        return render(request, 'items/tipoItem/modificar.html', {'tipo':ti,'lista':listaTupla})

    def post(self, request, *args, **kwargs):
        id=request.POST['id']
        ti=tipoItem.objects.get(id=id)
        listati = pickle.loads(ti.atributos)
        listaN = []
        c = 0
        for l in listati:
            listaN.append(request.POST[str(c)])
            c+=1
        ti.atributos = pickle.dumps(listaN)
        ti.save()
        url = '/items/tipoItem/mostrar/' + str(id)
        return HttpResponseRedirect(url)

class eliminarTipoItem(DeleteView):
    """
        Vista para eliminar un tipo de Items
    """
    model = tipoItem
    template_name = 'items/tipoItem/delete.html'
    success_url = reverse_lazy('listar_tipoitem')
    def get_object(self, queryset=None):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = tipoItem.objects.get(id=self.kwargs['id'])
        return obj

class importar(TemplateView):
    """
        Vista para importar un tipo de Items
        :param id: Identificador de la fase
        :param tipo: Identificador del tipo de items
        :param nombre: Nombre para el nuevo items
        :param complejidad: Valor que representa la complejidad del Items
        :param costo: Valor que representa el costo del items
    """
    def get(self, request, *args, **kwargs):
        return render(request,'items/importar.html',{'tipos':tipoItem.objects.order_by('id'),'idFase':kwargs['id']})

    def post(self, request, *args, **kwargs):
        fase=fases.objects.get(id=request.POST['id'])
        ti = tipoItem.objects.get(id=request.POST['tipo'])
        listaTipos= pickle.loads(ti.atributos)
        item = items(nombre=request.POST['nombre'], complejidad=request.POST['complejidad'],costo=request.POST['costo'], fase=fase)
        item.save()
        for l in listaTipos:
            nuevo = atributo(nombre=l,descripcion='',version=1,item=item)
            nuevo.save()
        url = '/items/atributos/listar/'+str(item.id)
        return HttpResponseRedirect(url)

class graficar(TemplateView):
    def get(self, request, *args, **kwargs):
        cadena = 'digraph A {\n'
        proyecto = Proyectos.objects.get(id=kwargs['id'])
        listaFases = fases.objects.filter(proyecto=proyecto)
        c = 0
        for fase in listaFases:
            cadena += '\tsubgraph cluster' + str(c) + '{\n'
            c+=1
            cadena += '\tnode [style=filled,color=black];\n'
            cadena += '\tcolor=lightgrey;\n'
            listaitems = items.objects.filter(fase=fase)
            for item in listaitems:
                cadena += '\t\t' + str(item.id) + ' [style=bold,label="'+ item.nombre + '"];\n'
            cadena += '\t\tlabel="'+fase.nombre+'";\n'
            cadena += '\t}\n'
        listaRelaciones = relacion.objects.filter(itemHijo__fase__proyecto=proyecto)
        for r in listaRelaciones:
            cadena += '\t' + str(r.itemPadre.id) + '->' + str(r.itemHijo.id) + ';\n'
        cadena += '}'
        import os
        archivo = 'diagrama'+ str(proyecto.id)
        url = '../media/' + archivo + '.dot'
        diagrama = open(url,'w')
        diagrama.write(cadena)
        diagrama.close()
        comando = 'cd ../media/;dot -Tpng ' + archivo +'.dot -o '+archivo+'.png'
        os.system(comando)
        comando = 'cd ../media/;rm ' + archivo + '.dot'
        os.system(comando)
        return render(request,'relaciones/graficar.html', {'proyecto': proyecto.nombre, 'archivo':archivo})