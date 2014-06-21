""" Los nombres de clases son los nombres de las vistas que posteriormente son invocadas en el archivo URLS.py
Las vistas son definidas en base a los modelos definidos en el archivo MODELS.py """


from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.core import serializers
from aps.aplicaciones.permisos.models import Permisos
from aps.aplicaciones.proyectos.models import Proyectos, Miembros
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.items.models import items


# Create your views here.
class admin(TemplateView):
    """ Vista de administracion de proyectos, hereda atributos y metodos de la clase TemplateView """
    template_name = 'permisos/admin.html'
    def get(self, request, *args, **kwargs):
        if Permisos.valido(usuario=self.request.user,permiso='ADMINVER',tipoObjeto='permiso',id=0) or self.request.user.is_superuser==True:
            return render(request,'permisos/admin.html')
        return render(self.request, 'error/permisos.html')

class listar(ListView):
    """ Vista de listado de proyectos, hereda atributos y metodos de la clase ListView """
    template_name = 'permisos/listar.html'
    model = User
    context_object_name = 'usuarios'

class crear(TemplateView):
    def get(self, request, *args, **kwargs):
        if Permisos.valido(usuario=self.request.user,permiso='ADMINADD',tipoObjeto='permiso',id=0) or self.request.user.is_superuser==True:
            usuarios = User.objects.filter()
            grupos = Group.objects.filter()
            return render(request, 'permisos/crear.html', {'usuarios':usuarios, 'grupos':grupos})
        return render(self.request, 'error/permisos.html')

    def post(self, request, *args, **kwargs):
        id_usuario = request.POST['usuario']
        id_grupo = request.POST['grupo']
        permiso = request.POST['permiso']
        print id_usuario
        print id_grupo
        print permiso
        if int(id_usuario) == 0 and int(id_grupo) == 0:
            usuarios = User.objects.filter()
            grupos = Group.objects.filter()
            return render(request, 'permisos/crear.html', {'usuarios':usuarios, 'grupos':grupos, 'msj':'Seleccione un usuario o grupo'})
        try:
            usuario = User.objects.get(id=id_usuario)
            if not Permisos.valido(usuario=usuario,permiso=permiso,tipoObjeto='permiso',id=0):
                p = Permisos(permiso=permiso, tipoObjeto='permiso', id_fk=0, usuario=usuario)
                p.save()
        except:
            pass
        try:
            grupo = Group.objects.get(id=id_grupo)
            if not Permisos.valido(grupo=grupo,permiso=permiso,tipoObjeto='permiso',id=0):
                p = Permisos(permiso=permiso, tipoObjeto='permiso', id_fk=0, grupo=grupo)
                p.save()
        except:
            pass
        return HttpResponseRedirect('/permisos/admin/')

class permisos_ajax(TemplateView):
    def get(self, request, *args, **kwargs):
        id_usuario = request.GET['idusuario']
        #print 'id usuario: ' + str(id_usuario)
        permisos = Permisos.objects.filter(usuario__id=id_usuario)
        #print 'permisos '
        #print permisos
        datajson = '['
        c=1
        for p in permisos:
            print 'vuelta' + str(c)
            c+=1
            proyecto=fase=item=atributo='none'
            tipo=p.tipoObjeto
            #print 'tipo objeto' + str(tipo)
            pk_id=p.id_fk
            if tipo =='proyecto' and pk_id!=0:
                proyecto=Proyectos.objects.get(id=pk_id).nombre
                #print 'entro por proyecto' + str(proyecto)
            elif tipo =='fase':
                fase=fases.objects.get(id=pk_id).nombre
                #print 'entro por fase' + str(fase)
            elif tipo =='item':
                item=items.objects.get(id=pk_id).nombre
                #print 'entro por item' + str(item)
            datajson+='{"pk": ' + str(p.id) + ', "model": "permisos.permisos", "fields": {'
            datajson+='"permiso": "' + p.permiso + '", '
            datajson+='"tipoObjeto": "' + p.tipoObjeto + '", '
            datajson+='"proyecto": "' + proyecto + '", '
            datajson+='"fases": "' + fase + '", '
            datajson+='"items": "' + item + '"}},'
            #print 'json1--> ' + datajson
        if (len(datajson)>1):
            datajson=datajson[:-1]
        datajson+=']'
        #print 'json2--> ' + datajson
        # data = serializers.serialize('json',permisos,fields=('permiso','tipoObjeto','proyecto','fases','items'))
        # print data
        return HttpResponse(datajson, content_type = 'application/json')

class eliminar(DeleteView):
    """ Vista para Eliminar un permiso """
    model = Permisos
    template_name = 'permisos/delete.html'
    success_url = reverse_lazy('admin_permisos')      # Se mostrara la vista 'listar_permisos' en el caso de modificacion exitosa
    def get(self, request, *args, **kwargs):
        if Permisos.valido(usuario=self.request.user,permiso='ADMINDEL',tipoObjeto='permiso',id=0) or self.request.user.is_superuser==True:
            return super(eliminar, self).get(request, args, kwargs)
        return render(self.request, 'error/permisos.html')

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

class asignarAProyecto(TemplateView):
    """
    Vista para asignar permisos especificos a usuarios en un determinado proyecto
    """
    def get(self, request, *args, **kwargs):
        id_proyecto = kwargs['id']
        proyecto = Proyectos.objects.get(id=id_proyecto)
        if(not proyecto.lider==self.request.user):
            return render(self.request, 'error/permisos.html')
        comite = Miembros.objects.filter(proyecto__id=id_proyecto)
        return render(request, 'permisos/proyectos.html', {'usuarios':comite, 'idProyecto':id_proyecto})
    def post(self, request, *args, **kwargs):
        try:
            usuario = User.objects.get(id=request.POST['usuario'])
        except:
            return HttpResponseRedirect('/proyectos/detalles/'+str(request.POST['idProyecto']))
        lista = request.POST.getlist('permisos')
        permisos = Permisos.objects.filter(usuario__id=request.POST['usuario'], tipoObjeto='proyecto', id_fk=request.POST['idProyecto'])
        for p in permisos:
            p.delete()
        for p in lista:
            aux = Permisos(usuario=usuario, tipoObjeto='proyecto', id_fk=request.POST['idProyecto'], permiso=p)
            aux.save()
        return HttpResponseRedirect('/proyectos/detalles/'+str(request.POST['idProyecto']))


class proyectos_ajax(TemplateView):
    """
    Respuesta AJAX con permisos actuales de un usuario sobre un determinado proyecto
    """
    def get(self, request, *args, **kwargs):
        id_proyecto = request.GET['id']
        estado = request.GET['estado']
        permisos = Permisos.objects.filter(usuario__id=estado, tipoObjeto='proyecto', id_fk=id_proyecto)
        print permisos
        data = serializers.serialize('json',permisos,fields=('permiso'))
        return HttpResponse(data, content_type = 'application/json')