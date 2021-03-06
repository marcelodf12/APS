"""
     Aqui se definen las urls que permitiran visualizar las distintas vistas creadas en el archivo VIEWS.py
     include(Parametro) incluye las urls que se encuentran definidas en Parametro.
     Aqui se encuentran las urls "raiz" que permiten acceder a las urls de todas las aplicaciones
     incluimos los archivos URL.py de todas las aplicaciones
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT,} ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('aplicaciones.inicio.urls')),
    url(r'^items/', include('aplicaciones.items.urls')),
    url(r'^proyectos/', include('aplicaciones.proyectos.urls')),
    url(r'^fases/', include('aplicaciones.fases.urls')),
    url(r'^permisos/', include('aplicaciones.permisos.urls')),
    url(r'^lineasBase/', include('aplicaciones.lineasBase.urls')),
    url(r'^solicitudCambio/', include('aplicaciones.solicitudCambio.urls')),
    url(r'^reportes/', include('aplicaciones.reportes.urls'))

)
