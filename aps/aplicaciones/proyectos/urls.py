""" Aqui se definen las urls que permitiran visualizar las distintas vistas creadas en el archivo VIEWS.py de
    la aplicacion 'proyectos'.
    Todas las urls definidas aqui esta relacionadas con la administracion de proyectos
"""

from django.conf.urls import patterns, url

from .views import *


urlpatterns = patterns('',

    url(r'^crear/$', crearProyecto.as_view(), name='crear_proyecto'),
    url(r'^admin/$', adminProyecto.as_view(), name='admin_proyecto'),
    url(r'^listar/$', listarProyectosAJAX.as_view(), name='listar_proyectos'),
    url(r'^listar_ajax/$', proyectos_ajax.as_view(), name='listar_proyectos_ajax'),
    url(r'^modificar/(?P<id>\d+)$', modificarProyectos.as_view(), name='modificar_proyectos'),
    url(r'^eliminar/(?P<id>\d+)$', eliminarProyectos.as_view(), name='eliminar_proyectos'),
    url(r'^iniciar/(?P<id>\d+)$', iniciarProyecto.as_view(), name='iniciar_proyecto'),
    url(r'^noIniciados/$', listarProyectosNoIniciados.as_view(), name='listar_proyectos_no_iniciados'),
    url(r'^detalles/(?P<id>\d+)$', detallesProyecto.as_view(), name='detalle_proyecto'),
    url(r'^miembros/$', adminComite.as_view(), name='admin_comite'),
    url(r'^listarMiembros_ajax/$', miembrosAJAX.as_view(), name='miembros_ajax'),
    url(r'^editMiembro/(?P<id>\d+)$', editMiembro.as_view(), name='editar_miembro'),
    url(r'^agregarMiembro/(?P<id>\d+)$', editMiembro.as_view(), name='agregar_miembro'),

)
