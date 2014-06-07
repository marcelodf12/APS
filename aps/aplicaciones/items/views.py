
""" Los nombres de clases son los nombres de las vistas que posteriormente son invocadas en el archivo URLS.py
Las vistas son definidas en base a los modelos definidos en el archivo MODELS.py """
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, FormView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect

from .models import items, atributo, relacion, tipoItem
from aps.aplicaciones.lineasBase.models import relacionItemLineaBase, lineasBase
from .forms import ComentariosLog
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.proyectos.models import Proyectos
from aps.aplicaciones.solicitudCambio.models import solicitudCambio
import pickle


# Create your views here.
class adminItems(TemplateView):
    """
        Vista de administracion de items, hereda atributos y metodos de la clase TemplateView
    """
    template_name = 'items/admin.html'         # Se define la direccion y nombre del template

class crearItem(CreateView):
    """
        Vista de creacion de items, hereda atributos y metodos de la clase CreateView
    """
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

class crearItemEnFase(TemplateView):
    """
        Vista de creacion de items en una Fase especifica, hereda atributos y metodos de la clase CreateView
    """
    def get(self, request, *args, **kwargs):
        faseAct = fases.objects.get(id=kwargs['id'])
        listaItems=items.objects.filter(fase=faseAct)
        if(faseAct.orden>1):
            proyecto = faseAct.proyecto
            faseAnt = fases.objects.get(proyecto=proyecto, orden=faseAct.orden-1)
            listaItems=(items.objects.filter(fase=faseAct) | items.objects.filter(fase=faseAnt))
        return render(request, 'items/crear.html', {'listaItems':listaItems, 'nombreProyecto':faseAct.proyecto.nombre,'url':'/proyectos/detalles/'+str(faseAct.proyecto.id)})

    def post(self, request, *args, **kwargs):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        f= fases.objects.get(id=self.kwargs['id'])
        if(request.POST['nombre']=='' or request.POST['complejidad']=='' or request.POST['costo']==''):
            return render(request, 'items/crear.html', {'error':'Todos los campos son requeridos', 'nombreProyecto':f.proyecto.nombre,'url':'/proyectos/detalles/'+str(f.proyecto.id)})
        item=items(\
            nombre=request.POST['nombre'],\
            complejidad=int(request.POST['complejidad']),\
            costo=int(request.POST['costo'])\
        )
        item.versionAct = 1     # Se define un valor predeterminado para la version del item
        item.estado = 'creado'
        item.fase = f
        padre=request.POST['padre']
        if(int(padre)>0):
            item.save()
            itemPadre = items.objects.get(id=padre)
            NuevaRelacion = relacion(itemHijo=item, itemPadre=itemPadre, estado=True)
            NuevaRelacion.save()
        elif(f.orden==1):
            item.save()
        else:
            return render(request, 'error/general.html', {'mensaje':'No puede crear un item en esta fase sin asignarle un padre', 'url':'/proyectos/detalles/'+str(item.fase.proyecto.id)})
        return HttpResponseRedirect('/proyectos/detalles/'+str(item.fase.proyecto.id))

class listarItems(ListView):
    """
        Vista de listado de items, hereda atributos y metodos de la clase ListView
    """
    model = items
    template_name = 'items/listar.html'
    context_object_name = 'items'

class listarItemsEliminados(ListView):
    """
        Vista de listado de items, hereda atributos y metodos de la clase ListView
    """
    model = items
    template_name = 'items/listar eliminados.html'
    context_object_name = 'items'

class modificarItems(UpdateView):
    """
        Vista de modificacion de proyectos, hereda atributos y metodos de la clase UpdateView
    """
    model = items
    fields = ['nombre','complejidad','costo']     # Permite modificar solo el campo 'nombre'
    template_name = 'items/update.html'
    success_url = reverse_lazy('listar_item')      # Se mostrara la vista 'listar_proyecto' en el caso de modificacion exitosa

    def get_object(self, queryset=None):
        """
            Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original
        """
        obj = items.objects.get(id=self.kwargs['id'])
        self.success_url='/proyectos/detalles/'+str(obj.fase.proyecto.id)
        return obj

class eliminarItems(FormView):
    """
        Vista de eliminacion de proyectos, hereda atributos y metodos de la clase FormView
    """
    form_class = ComentariosLog
    template_name = 'items/eliminar.html'
    success_url = reverse_lazy('listar_item')      # Se mostrara la vista 'listar_proyectos' en el caso de eliminacion exitosa

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        item = items.objects.get(id=self.kwargs['id'])
        rel = relacion.objects.filter(itemPadre=item).exclude(estado=False)
        lb = relacionItemLineaBase.objects.filter(item=item)
        if lb:
            return render(self.request, 'error/general.html', {'mensaje':'No puede eliminar este item porque esta en una linea base','url':'/proyectos/detalles/'+str(item.fase.proyecto.id)})
        elif rel:
            return render(self.request, 'error/general.html', {'mensaje':'No puede eliminar este item porque otros depende del el','url':'/proyectos/detalles/'+str(item.fase.proyecto.id)})
        else:
            item.estado='eliminado'
            item.save()
            rel = relacion.objects.filter(itemHijo=item)
            for r in rel:
                r.estado=False
                r.save()
            url='/proyectos/detalles/'+str(item.fase.proyecto.id)
            return HttpResponseRedirect(url)

class listarItemParaCrearRelacion(TemplateView):
    """
        Vista para listar los item candidatos a ser padres y crear una Relacion
        :param id: El identificador del item
    """
    def get(self, request, *args, **kwargs):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        itemHijo = items.objects.get(id=kwargs['id'])
        faseAct = itemHijo.fase
        listaItems=items.objects.filter(fase=faseAct).exclude(id=itemHijo.id).exclude(estado='eliminado')
        if(faseAct.orden>1):
            proyecto = faseAct.proyecto
            faseAnt = fases.objects.get(proyecto=proyecto, orden=faseAct.orden-1)
            listaItems=(items.objects.filter(fase=faseAct).exclude(id=itemHijo.id) | items.objects.filter(fase=faseAnt))
        return render(self.request, 'relaciones/crearRelacion.html', {'items':listaItems, 'id':itemHijo.id, 'nombreProyecto':itemHijo.fase.proyecto.nombre, 'url':'/proyectos/detalles/'+str(itemHijo.fase.proyecto.id)})

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
        queryset = relacion.objects.filter(itemHijo__fase__proyecto__id=kwargs['id']).exclude(estado=False)
        proyecto = Proyectos.objects.get(id=kwargs['id'])
        return render(self.request, 'relaciones/listar.html',{'relaciones':queryset, 'proyecto':proyecto.nombre, 'idProyecto':proyecto.id})

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
        listaItems = relacionItemLineaBase.objects.filter(item=item)
        solicitudes=solicitudCambio.objects.filter(item=item, estado='aceptada').order_by('pk')
        solicitud = 0
        for s in solicitudes:
            solicitud = s.id
        if listaItems:
            tieneHijos=True
        else:
            tieneHijos=False
        return render(self.request, 'items/listarAtributos.html',{'item':item, 'atributos':atributos,'tieneHijos':tieneHijos, 'nombreProyecto':item.fase.proyecto.nombre, 'url':'/proyectos/detalles/'+str(item.fase.proyecto.id), 'solicitud':solicitud})

class mostrarDetallesV(TemplateView):
    """
        Vista que muestra los detalles de un item
        :param id: El identificador del item
    """
    def get(self, request, *args, **kwargs):
        item = items.objects.get(id=kwargs['id'])
        atributos = atributo.objects.filter(item=item, version=kwargs['idV']).order_by('pk')
        return render(self.request, 'items/listarOtrasVersiones.html',{'item':item, 'atributos':atributos, 'version':kwargs['idV'], 'nombreProyecto':item.fase.proyecto.nombre, 'url':'/proyectos/detalles/'+str(item.fase.proyecto.id)})

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
        return render(self.request, 'items/listarVersiones.html',{'item':item, 'range':range(1,item.versionAct+1), 'nombreProyecto':item.fase.proyecto.nombre,'url':'/proyectos/detalles/'+str(item.fase.proyecto.id)})

class ReversionVersiones(TemplateView):
    """
        Vista que muestra las posibles versiones para reversionar un item
    """
    def get(self, request, *args, **kwargs):
        item = items.objects.get(id=kwargs['id'])
        return render(self.request, 'items/reversion.html',{'item':item, 'range':range(1,item.versionAct+1), 'nombreProyecto':item.fase.proyecto.nombre,'url':'/proyectos/detalles/'+str(item.fase.proyecto.id)})


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
        Vista para crear un nuevo tipo de item
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
        Vista que define la cantidad de atributos a agregar a un tipo de item
    """
    def get(self, request, *args, **kwargs):
        return render(request,'items/tipoItem/agregarAtributo.html',{'tipos':tipoItem.objects.order_by('nombre')})

class formularioAgregarAtributoAlTipoItem(TemplateView):
    """
        Vista que muestra un formulario con N atributos nuevos para agregar a un tipo de item
    """
    def post(self, request, *args, **kwargs):
        ti=tipoItem.objects.get(id=request.POST['id'])
        cant=int(request.POST['cantidad'])
        return render(request,'items/tipoItem/agregarAtributosN.html',{'id':ti.id,'range':range(1,cant+1),'cantidad':cant})

class verAtributosTipoItems(TemplateView):
    """
        Vista para ver los atributos de un tipo de item
    """
    def get(self, request, *args, **kwargs):
        ti = tipoItem.objects.get(id=kwargs['id'])
        listaAt = pickle.loads(ti.atributos)
        return render(request, 'items/tipoItem/mostrar.html', {'atributos':listaAt, 'tipo':ti})

class verTipoItems(ListView):
    """
        Ver los detalles de un tipo de item
    """
    model = tipoItem
    context_object_name = 'tipos'
    template_name = 'items/tipoItem/listar.html'

class modificarAtributoDeTipoItem(TemplateView):
    """
        Vista para modificar los atributos de un tipo de item
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
        Vista para eliminar un tipo de Item
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
        return HttpResponseRedirect('/proyectos/detalles/'+str(item.fase.proyecto.id))

class graficar(TemplateView):
    """
        Vista para visualizar graficamente la estructura de un proyecto, hereda atributos y metodos de la clase TemplateView
    """

    def get(self, request, *args, **kwargs):
        cadena = 'digraph A {\n'
        proyecto = Proyectos.objects.get(id=kwargs['id'])
        listaFases = fases.objects.filter(proyecto=proyecto)
        c = 0
        for f in listaFases:
            cadena += '\tsubgraph cluster' + str(c) + '{\n'
            c+=1
            n=0
            cadena += '\t\tnode [style=filled,color=black];\n'
            cadena += '\t\tcolor=lightgrey;\n'
            listaitems = items.objects.filter(fase=f).exclude(estado='eliminado')
            listaRelitemsEnLB=relacionItemLineaBase.objects.filter(item__in=listaitems).exclude(item__estado='eliminado')
            listaItemEnLB = []
            for r in listaRelitemsEnLB:
                listaItemEnLB.append(r.item)
            conItems=set(listaitems)
            conItemsEnLB=set(listaItemEnLB)
            conItemsNoLB=conItems-conItemsEnLB
            lineaBase = lineasBase.objects.filter(fase=f)

            for l in lineaBase:
                cadena += '\t\tsubgraph cluster' + str(n) + '{\n'
                cadena += '\t\t\tnode [style=filled,color=black];\n'
                cadena += '\t\t\tcolor=lightgrey;\n'
                n+=1
                listaRelEnLB = relacionItemLineaBase.objects.filter(linea=l)
                for a in listaRelEnLB:
                    cadena += '\t\t\t' + str(a.item.id) + ' [style=bold,label="'+ a.item.nombre + '"];\n'
                cadena += '\t\t\tlabel="'+l.nombre+'";\n'
                cadena += '\t\t}\n'
            for item in conItemsNoLB:
                cadena += '\t\t' + str(item.id) + ' [style=bold,label="'+ item.nombre + '"];\n'
            cadena += '\t\tlabel="'+f.nombre+'";\n'
            cadena += '\t}\n'
        listaRelaciones = relacion.objects.filter(itemHijo__fase__proyecto=proyecto).exclude(itemHijo__estado='eliminado').exclude(itemPadre__estado='eliminado')
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
        return render(request,'relaciones/graficar.html', {'proyecto': proyecto.nombre, 'archivo':archivo, 'idProyecto':proyecto.id, 'nombreProyecto':proyecto.nombre, 'url':'/proyectos/detalles/'+str(proyecto.id)})

class finalizarItem(FormView):
    """
        Vista para finalizar items de un proyecto, hereda atributos y metodos de la clase FormView
    """

    form_class = ComentariosLog
    template_name = 'items/finalizar.html'
    success_url = reverse_lazy('listar_itemsFinalizados')      # Se mostrara la vista 'listar_items' en el caso de eliminacion exitosa

    def form_valid(self, form):
        item = items.objects.get(id=self.kwargs['id'])

        #se encuentra la fase que contiene al item
        fase = item.fase
        nroFase = fase.orden

        padreAntecesor = None       #inicializacion

        try:
             #se busca una relacion padre-hijo o antecesor-sucesor
             relacionPadreAntecesor = relacion.objects.get(itemHijo_id=item.id)

             #se busca el item padre en el modelo items
             padreAntecesor = relacionPadreAntecesor.itemPadre
             if(padreAntecesor.estado != 'finalizado'):
                return render(self.request, 'error/general.html', {'mensaje':'El item padre aun no ha sido finalizado'})
        except:
             #si no se trata de la 1ra fase no puede estar aislado, informar
             if(nroFase!=1):
                return render(self.request, 'error/general.html', {'mensaje':'El item no es de la fase 1 y no posee un padre (aislado)'})

        item.estado = 'finalizado'
        item.save()
        return HttpResponseRedirect('/proyectos/detalles/'+str(item.fase.proyecto.id))


class listarItemsFinalizados(ListView):
    """
        Vista de listado de items finalizados, hereda atributos y metodos de la clase ListView
    """
    model = items
    template_name = 'items/listarFinalizados.html'
    context_object_name = 'items'

class listarItemCandidatos(TemplateView):
    def get(self, request, *args, **kwargs):
        proyecto = Proyectos.objects.get(id=kwargs['id'])
        return render(self.request, 'items/listarCandidatos.html', {'nombreProyecto': proyecto.nombre, 'idProyecto': kwargs['id'],'candidatos':items.objects.filter(estado='eliminado', fase__proyecto__id=kwargs['id']).exclude(fase__estado='finalizada'), 'url':'/proyectos/detalles/'+str(proyecto.id)})


class revivirItem(TemplateView):
    def get(self, request, *args, **kwargs):
        idItem = kwargs['id']
        item=items.objects.get(id=idItem)
        rel = relacion.objects.get(itemHijo=item)
        print rel
        if rel.itemPadre.estado == 'eliminado':
            itemsCandiatos = items.objects.filter(fase=int(item.fase.id)-1).exclude(estado='eliminado') | items.objects.filter(fase=int(item.fase.id)).exclude(estado='eliminado')
            if itemsCandiatos:
                return render(self.request, 'items/asignarPadre.html', {'idProyecto': item.fase.proyecto, 'candidatos':itemsCandiatos, 'idItem':int(item.id)})
            else:
                return render(self.request, 'error/general.html', {'mensaje':'No hay padres candidatos', 'url':'/proyectos/detalles/'+str(item.fase.proyecto.id)})
        else:
            item.estado = 'creado'
            rel.estado = True
            item.save()
            rel.save()
            return HttpResponseRedirect('/proyectos/detalles/'+str(item.fase.proyecto.id))

    def post(self, request, *args, **kwargs):
        itemHijo = items.objects.get(id=request.POST['idHijo'])
        itemPadre = items.objects.get(id=request.POST['idPadre'])
        rel = relacion.objects.get(itemHijo=itemHijo)
        rel.delete()
        nuevaRelacion= relacion(itemHijo=itemHijo, itemPadre=itemPadre, estado=True)
        nuevaRelacion.save()
        itemHijo.estado = 'creado'
        itemHijo.save()
        return HttpResponseRedirect('/proyectos/detalles/'+str(itemHijo.fase.proyecto.id))
