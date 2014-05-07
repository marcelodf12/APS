"""
    Aqui se definen las urls que permitiran visualizar las distintas vistas creadas en el archivo VIEWS.py
    de la aplicacion 'items'.
"""

from django.conf.urls import patterns, url
from django.contrib import admin

from .views import adminItems, crearItem, listarItems, modificarItems, eliminarItems, listarItemsEliminados, crearItemEnFase


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', adminItems.as_view(), name='admin_items'),
    url(r'^crear/', crearItem.as_view(), name='crear_item'),
    url(r'^crearEnFase/(?P<id>\d+)$', crearItemEnFase.as_view(), name='crear_item_en_fase'),
    url(r'^listar/', listarItems.as_view(), name='listar_item'),
    url(r'^listar_eliminados/', listarItemsEliminados.as_view()),
    url(r'^modificar/(?P<id>\d+)$', modificarItems.as_view(), name='modificar_items'),
    url(r'^eliminar/(?P<id>\d+)$', eliminarItems.as_view(), name='eliminar_items'),
)
