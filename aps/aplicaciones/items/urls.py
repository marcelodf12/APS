from django.conf.urls import patterns, include, url
from django.contrib import admin
from aps.aplicaciones.items.views import adminItems, crearItem, listarItems

admin.autodiscover()

urlpatterns = patterns('',
    """ Aqui se definen las urls que permitiran visualizar las distintas vistas creadas en el archivo VIEWS.py de
     la aplicacion 'items'.
     Todas las urls definidas aqui esta relacionadas con la administracion de items """

    url(r'^admin/', adminItems.as_view(), name='admin_items'),
    url(r'^crear/', crearItem.as_view(), name='crear_item'),
    url(r'^listar/', listarItems.as_view(), name='listar_item'),
)
