"""
    Aqui se definen las urls que invocaran las distintas vistas creadas en el archivo VIEWS.py
    de la aplicacion 'solicitudCambio'.
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import crearSolicitudCambio, listarVotaciones, votar, ejecutarSolicitud, adminSolicitudes, listar

admin.autodiscover()
urlpatterns = patterns('',
   url(r'^crear/(?P<id>\d+)$', crearSolicitudCambio.as_view(), name='crear_solicitud_cambio'),
   url(r'^listar/(?P<estado>[a-z]+)$', listar.as_view()),
   url(r'^Votaciones/', listarVotaciones.as_view(), name='listarVotaciones'),
   url(r'^admin/', adminSolicitudes.as_view(), name='listarVotaciones'),
   url(r'^votar/(?P<id>\d+)$', votar.as_view()),
   url(r'^ejecutar/(?P<id>\d+)$', ejecutarSolicitud.as_view()),
)