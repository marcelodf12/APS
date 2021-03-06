"""
    Aqui se definen las urls que invocaran las distintas vistas creadas en el archivo VIEWS.py
    de la aplicacion 'fases'.
"""

from django.conf.urls import patterns, url
from django.contrib import admin

from .views import adminFases, listarFases , modificarFases, eliminarFase, crearFaseEnProyecto, finalizarFase, listarFasesFinalizadas


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', adminFases.as_view(), name='admin_fases'),
    url(r'^listar/finalizadas/', listarFasesFinalizadas.as_view(), name='listar_fasesFinalizadas'),
    url(r'^listar/', listarFases.as_view(), name='listar_fases'),
    url(r'^modificar/(?P<id>\d+)$', modificarFases.as_view(), name='modificar_fases'),
    url(r'^eliminar/(?P<id>\d+)$', eliminarFase.as_view(), name='eliminar_fase'),
    url(r'^crearEnProyecto/(?P<id>\d+)$', crearFaseEnProyecto.as_view(), name='crear_fase_en_proyecto'),
    url(r'^finalizar/(?P<id>\d+)$', finalizarFase.as_view(), name='crear_fase_en_proyecto'),
)