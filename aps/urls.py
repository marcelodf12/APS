from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('aplicaciones.inicio.urls')),
    url(r'^items/', include('aplicaciones.items.urls')),
    url(r'^proyectos/', include('aplicaciones.proyectos.urls')),
    url(r'^fases/', include('aplicaciones.fases.urls')),

)
