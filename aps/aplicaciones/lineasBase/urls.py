from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import crear, retornarItemsDeFaseAJAX

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^crear/(?P<id>\d+)$', crear.as_view(), name='crear_linea_base'),
    url(r'^listaItems/', retornarItemsDeFaseAJAX.as_view(), name='retornar_items'),
)
