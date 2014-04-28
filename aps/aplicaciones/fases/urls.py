from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import adminFases, listarFases , modificarFases, eliminarFase, crearFaseEnProyecto

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', adminFases.as_view(), name='admin_fases'),
    url(r'^listar/', listarFases.as_view(), name='listar_fases'),
    url(r'^modificar/(?P<id>\d+)$', modificarFases.as_view(), name='modificar_fases'),
    url(r'^eliminar/(?P<id>\d+)$', eliminarFase.as_view(), name='eliminar_fase'),
    url(r'^crearEnProyecto/$', crearFaseEnProyecto.as_view(), name='crear_fase_en_proyecto'),
)