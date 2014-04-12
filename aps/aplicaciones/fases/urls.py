from django.conf.urls import patterns, include, url
from django.contrib import admin
from aps.aplicaciones.fases.views import adminFases , crearFase, listarFases

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', adminFases.as_view(), name='admin_fases'),
    url(r'^crear/', crearFase.as_view(), name='crear_fases'),
    url(r'^listar/', listarFases.as_view(), name='listar_fases'),
)