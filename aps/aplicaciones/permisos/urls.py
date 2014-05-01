""" Aqui se definen las urls que permitiran visualizar las distintas vistas creadas en el archivo VIEWS.py de
    la aplicacion 'proyectos'.
    Todas las urls definidas aqui esta relacionadas con la administracion de proyectos
"""

from django.conf.urls import patterns, url

from aps.aplicaciones.permisos.views import admin, crear, listar, permisos_ajax, eliminar, listarGrupos, permisos_grupos_ajax

urlpatterns = patterns('',

    url(r'^crear/$', crear.as_view(), name='crear_permisos'),
    url(r'^admin/$', admin.as_view(), name='admin_permisos'),
    url(r'^listar/$', listar.as_view(), name='listar_permisos'),
    url(r'^listar_ajax/$', permisos_ajax.as_view(), name='listar_permisos_ajax'),
    url(r'^listarGrupos/$', listarGrupos.as_view(), name='listar_permisos'),
    url(r'^listar_grupos_ajax/$', permisos_grupos_ajax.as_view(), name='listar_permisos_ajax'),
    url(r'^eliminar/(?P<id>[\w]+)$', eliminar.as_view(), name='delete_permiso'),
    # url(r'^modificar/(?P<id>\d+)$', modificarProyectos.as_view(), name='modificar_proyectos'),
    # url(r'^iniciar/(?P<id>\d+)$', iniciarProyecto.as_view(), name='iniciar_proyecto'),
    # url(r'^noIniciados/$', listarProyectosNoIniciados.as_view(), name='listar_proyectos_no_iniciados'),
)