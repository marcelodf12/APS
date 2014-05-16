""" Aqui se definen las urls que permitiran visualizar las distintas vistas creadas en el archivo VIEWS.py de
     la aplicacion 'items'.
     Todas las urls definidas aqui esta relacionadas con la administracion de items
"""
from django.conf.urls import patterns, url
from django.contrib import admin

from .views import *


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', adminItems.as_view(), name='admin_items'),
    url(r'^crear/', crearItem.as_view(), name='crear_item'),
    url(r'^crearEnFase/(?P<id>\d+)$', crearItemEnFase.as_view(), name='crear_item_en_fase'),
    url(r'^listar/', listarItems.as_view(), name='listar_item'),
    url(r'^listar_eliminados/', listarItemsEliminados.as_view()),
    url(r'^modificar/(?P<id>\d+)$', modificarItems.as_view(), name='modificar_items'),
    url(r'^eliminar/(?P<id>\d+)$', eliminarItems.as_view(), name='eliminar_items'),
    url(r'^relaciones/listarParaCrear/(?P<id>\d+)$', listarItemParaCrearRelacion.as_view(), name='listarItemParaCrearRelacion'),
    url(r'^relaciones/crear/$', crearRelacion.as_view(), name='crear_relacion'),
    url(r'^relaciones/listar/(?P<id>\d+)$', listarRelaciones.as_view(), name='listar_relaciones'),
    url(r'^relaciones/eliminar/(?P<id>\d+)$', eliminarRelacion.as_view(), name='eliminar_relaciones'),

    url(r'^atributos/agregar/(?P<id>\d+)$', agregarAtributo.as_view(), name='agregar_atributo'),
    url(r'^atributos/listar/(?P<id>\d+)$', mostrarDetalles.as_view(), name='detalles_Item'),
    url(r'^atributos/listar/(?P<id>\d+)/(?P<idV>\d+)$', mostrarDetallesV.as_view(), name='detalles_Item'),
    url(r'^atributos/listarVersiones/(?P<id>\d+)$', listarVersiones.as_view(), name='listar_versiones'),

    url(r'^reversionar/(?P<id>\d+)$', ReversionVersiones.as_view()),
    url(r'^reversionar/$', reversionar.as_view()),
)
