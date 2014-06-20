"""
    Aqui se definen las urls que invocaran las distintas vistas creadas en el archivo VIEWS.py
    de la aplicacion 'reportes'.
"""
from django.conf.urls import patterns, url
from .views import reporteProyecto

urlpatterns = patterns('',
    url(r'^proyecto/(?P<id>\d+)$', reporteProyecto.as_view(), name='updateUser'),
)