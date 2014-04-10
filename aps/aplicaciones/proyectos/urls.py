from django.conf.urls import patterns, url
from aps.aplicaciones.proyectos.views import \
    crearProyecto, \
    adminProyecto, \
    listarProyectos, \
    modificarProyectos, \
    eliminarProyectos, \
    listarProyectosNoIniciados, \
    iniciarProyecto

urlpatterns = patterns('',
    url(r'^crear/$', crearProyecto.as_view(), name='crear_proyecto'),
    url(r'^admin/$', adminProyecto.as_view(), name='admin_proyecto'),
    url(r'^listar/$', listarProyectos.as_view(), name='listar_proyectos'),
    url(r'^modificar/(?P<id>\d+)$', modificarProyectos.as_view(), name='modificar_proyectos'),
    url(r'^eliminar/(?P<id>\d+)$', eliminarProyectos.as_view(), name='eliminar_proyectos'),
    url(r'^iniciar/(?P<id>\d+)$', iniciarProyecto.as_view(), name='iniciar_proyecto'),
    url(r'^noIniciados/$', listarProyectosNoIniciados.as_view(), name='listar_proyectos_no_iniciados'),
)
