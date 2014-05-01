from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User, Group
from django.http import HttpResponse

from aps.aplicaciones.permisos.models import Permisos
from aps.aplicaciones.proyectos.models import Proyectos
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.items.models import items



# Create your views here.
class admin(TemplateView):
    """ Vista de administracion de proyectos, hereda atributos y metodos de la clase TemplateView """
    template_name = 'permisos/admin.html'

class listar(ListView):
    """ Vista de listado de proyectos, hereda atributos y metodos de la clase ListView """
    template_name = 'permisos/listar.html'
    model = User
    context_object_name = 'usuarios'

class crear(CreateView):
    """ Vista de creacion de proyectos, hereda atributos y metodos de la clase CreateView """
    template_name = 'permisos/crear.html'      # Se define la direccion y nombre del template
    model = Permisos                                  # Se asocia al modelo 'items'
    success_url = reverse_lazy('listar_permisos')      # Se mostrara la vista 'listar_proyecto' en el caso de registro exitoso

    def form_valid(self, form):
        """ Se extiende la funcion form_valid, se agrega el codigo adicional de abajo a la funcion original """
        permiso = form.save()
        permiso.save()
        return super(crear, self).form_valid(form)


class permisos_ajax(TemplateView):
    def get(self, request, *args, **kwargs):
        id_usuario = request.GET['idusuario']
        print 'id usuario: ' + str(id_usuario)
        permisos = Permisos.objects.filter(usuario__id=id_usuario)
        print 'permisos '
        print permisos
        datajson = '['
        c=1
        for p in permisos:
            print 'vuelta' + str(c)
            c+=1
            proyecto=fase=item=atributo='none'
            tipo=p.tipoObjeto
            print 'tipo objeto' + str(tipo)
            pk_id=p.id_fk
            if tipo =='proyecto' and pk_id!=0:
                proyecto=Proyectos.objects.get(id=pk_id).nombre
                print 'entro por proyecto' + str(proyecto)
            elif tipo =='fase':
                fase=fases.objects.get(id=pk_id).nombre
                print 'entro por fase' + str(fase)
            elif tipo =='item':
                item=items.objects.get(id=pk_id).nombre
                print 'entro por item' + str(item)
            datajson+='{"pk": ' + str(p.id) + ', "model": "permisos.permisos", "fields": {'
            datajson+='"permiso": "' + p.permiso + '", '
            datajson+='"tipoObjeto": "' + p.tipoObjeto + '", '
            datajson+='"proyecto": "' + proyecto + '", '
            datajson+='"fases": "' + fase + '", '
            datajson+='"items": "' + item + '"}},'
            print 'json1--> ' + datajson
        if (len(datajson)>1):
            datajson=datajson[:-1]
        datajson+=']'
        print 'json2--> ' + datajson
        # data = serializers.serialize('json',permisos,fields=('permiso','tipoObjeto','proyecto','fases','items'))
        # print data
        return HttpResponse(datajson, content_type = 'application/json')

class eliminar(DeleteView):
    """ Vista para Eliminar un permiso """
    model = Permisos
    template_name = 'permisos/delete.html'
    success_url = reverse_lazy('listar_permisos')      # Se mostrara la vista 'listar_permisos' en el caso de modificacion exitosa

    def get_object(self, queryset=None):
        """ Se extiende la funcion get_object, se agrega el codigo adicional de abajo a la funcion original """
        obj = Permisos.objects.get(id=self.kwargs['id'])
        return obj

class listarGrupos(ListView):
    """ Vista de listado de proyectos, hereda atributos y metodos de la clase ListView """
    template_name = 'permisos/listarGrupos.html'
    model = Group
    context_object_name = 'grupos'

class permisos_grupos_ajax(TemplateView):
    def get(self, request, *args, **kwargs):
        id_grupo = request.GET['idgrupo']
        permisos = Permisos.objects.filter(grupo__id=id_grupo)
        datajson = '['
        for p in permisos:
            proyecto=fase=item=atributo='none'
            tipo=p.tipoObjeto
            pk_id=p.id_fk
            if tipo =='proyecto' and pk_id!=0:
                proyecto=Proyectos.objects.get(id=pk_id).nombre
            elif tipo =='fase':
                fase=fases.objects.get(id=pk_id).nombre
            elif tipo =='item':
                item=items.objects.get(id=pk_id).nombre
            datajson+='{"pk": ' + str(p.id) + ', "model": "permisos.permisos", "fields": {'
            datajson+='"permiso": "' + p.permiso + '", '
            datajson+='"tipoObjeto": "' + p.tipoObjeto + '", '
            datajson+='"proyecto": "' + proyecto + '", '
            datajson+='"fases": "' + fase + '", '
            datajson+='"items": "' + item + '"}},'
        if (len(datajson)>1):
            datajson=datajson[:-1]
        datajson+=']'
        #data = serializers.serialize('json',permisos,fields=('permiso','tipoObjeto','proyecto','fases','items'))
        return HttpResponse(datajson, content_type = 'application/json')