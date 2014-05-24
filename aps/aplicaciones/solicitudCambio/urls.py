from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import crearSolicitudCambio

admin.autodiscover()
urlpatterns = patterns('',
   url(r'^crear/(?P<id>\d+)$', crearSolicitudCambio.as_view(), name='crear_solicitud_cambio'),

)
