from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import crearSolicitudCambio, listarVotaciones, votar

admin.autodiscover()
urlpatterns = patterns('',
   url(r'^crear/(?P<id>\d+)$', crearSolicitudCambio.as_view(), name='crear_solicitud_cambio'),
   url(r'^Votaciones/', listarVotaciones.as_view(), name='listarVotaciones'),
   url(r'^votar/(?P<id>\d+)$', votar.as_view()),
)