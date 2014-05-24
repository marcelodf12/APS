"""
    Aqui se definen las urls que permitiran visualizar las distintas vistas creadas en el archivo VIEWS.py
    de la aplicacion 'lineasBase'.
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import crear, retornarItemsDeFaseAJAX, listarLineasBase, listarDetallesLineasBase

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^crear/(?P<id>\d+)$', crear.as_view(), name='crear_linea_base'),
    url(r'^listaItems/', retornarItemsDeFaseAJAX.as_view(), name='retornar_items'),
    url(r'^listar/(?P<id>\d+)$', listarLineasBase.as_view()),
    url(r'^listarDetalles/(?P<id>\d+)$', listarDetallesLineasBase.as_view()),
)
