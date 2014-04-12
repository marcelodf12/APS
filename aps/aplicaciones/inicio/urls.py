from django.conf.urls import patterns, url

from aps.aplicaciones.inicio.views import home, Registrarse

urlpatterns = patterns('',
    """ Aqui se definen las urls que permitiran visualizar las distintas vistas creadas en el archivo VIEWS.py
     de la aplicacion 'inicio'.
     Todas las urls definidas aqui esta relacionadas con el inicio de sesion """

    url(r'^$','django.contrib.auth.views.login',
        {'template_name':'inicio/index.html'}, name='login'),
    url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',
        name='logout'),
    url(r'^inicio/$', home.as_view(),
        name='home'),
    url(r'^registrarse/$', Registrarse.as_view(), name='registrarse'),

)
