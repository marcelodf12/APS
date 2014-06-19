"""
    Aqui se definen las urls que permitiran visualizar las distintas vistas creadas en el archivo VIEWS.py
    de la aplicacion 'inicio'.
    Todas las urls definidas aqui esta relacionadas con el inicio de sesion
"""
from django.conf.urls import patterns, url
from .views import reporteProyecto

urlpatterns = patterns('',
    url(r'^proyecto/(?P<id>\d+)$', reporteProyecto.as_view(), name='updateUser'),
)