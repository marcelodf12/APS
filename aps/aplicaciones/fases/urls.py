from django.conf.urls import patterns, url
from django.contrib import admin
from .views import adminFases, crearFase, listarFases, modificarFases


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', adminFases.as_view(), name='admin_fases'),
    url(r'^crear/', crearFase.as_view(), name='crear_fases'),
    url(r'^listar/', listarFases.as_view(), name='listar_fases'),
    #url(r'^modificar/1/', modificarFases.as_view(), name='modificar_fases'),
    url(r'^modificar/\d+/$', modificarFases.as_view(), name='modificar_fases'),

    #url(r'^modificar/(?P<id>\d+)$', modificarFases.as_view(), name='modificar_fases'),
)