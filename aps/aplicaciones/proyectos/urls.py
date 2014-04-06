from django.conf.urls import patterns, url
from aps.aplicaciones.proyectos.views import crearProyecto, adminProyecto, listarProyectos

urlpatterns = patterns('',
    url(r'^crear/$', crearProyecto.as_view(), name='crear_proyecto'),
    url(r'^admin/$', adminProyecto.as_view(), name='admin_proyecto'),
    url(r'^listar/$', listarProyectos.as_view(), name='listar_proyectos'),
)
