"""
    Aqui se definen las urls que permitiran visualizar las distintas vistas creadas en el archivo VIEWS.py
    de la aplicacion 'inicio'.
    Todas las urls definidas aqui esta relacionadas con el inicio de sesion
"""
from django.conf.urls import patterns, url

from aps.aplicaciones.inicio.views import home, Registrarse, UpdateUser, ActualizarPassView
from aps.aplicaciones.inicio.views import CrearGrupo, adminGrupos, listarGrupos, eliminarGrupo, listarUsuarios
from aps.aplicaciones.inicio.views import asignarGrupo, listarUsuariosDeGrupo, eliminarUser, errorPermiso, error

urlpatterns = patterns('',
    url(r'^$','django.contrib.auth.views.login',{'template_name':'inicio/index.html'}, name='login'),
    url(r'^cerrar/$','django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^inicio/$', home.as_view(), name='home'),
    url(r'^registrarse/$', Registrarse.as_view(), name='registrarse'),
    url(r'^modificar/(?P<id>\d+)$', UpdateUser.as_view(), name='updateUser'),
    url(r'^modificar/password/$', ActualizarPassView.as_view(), name='updatePassword'),
    url(r'^Grupos/admin/$', adminGrupos.as_view(), name='admin_grupos'),
    url(r'^Grupos/crear/$', CrearGrupo.as_view(), name='crear_grupos'),
    url(r'^Grupos/listar/$', listarGrupos.as_view(), name='listar_grupos'),
    url(r'^Grupos/eliminar/(?P<id>[\w]+)$', eliminarGrupo.as_view(), name='delete_grupo'),
    url(r'^Grupos/asignar/(?P<id>[\w]+)$', asignarGrupo.as_view(), name='asignar_grupo'),
    url(r'^usuarios/eliminar/(?P<id>[\w]+)$', eliminarUser.as_view(), name='eliminar_usuarios_de_grupo'),
    url(r'^usuarios/listar/', listarUsuarios.as_view(), name='listar_usuarios'),
    url(r'^error/permisos/', errorPermiso.as_view(), name='error_permiso'),
    url(r'^error/', error.as_view(), name='error'),
    url(r'^Grupos/listarUsuarios/(?P<id>[\w]+)$', listarUsuariosDeGrupo.as_view(), name='listar_usuarios_de_grupo'),
)