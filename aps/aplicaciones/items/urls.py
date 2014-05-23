""" Aqui se definen las urls que permitiran visualizar las distintas vistas creadas en el archivo VIEWS.py de
     la aplicacion 'items'.
     Todas las urls definidas aqui esta relacionadas con la administracion de items
"""
from django.conf.urls import patterns, url
from django.contrib import admin

from .views import adminItems, crearItem, crearItemEnFase, listarItems, listarItemsEliminados, modificarItems, eliminarItems, \
    listarItemParaCrearRelacion, crearRelacion, listarRelaciones, eliminarRelacion, agregarAtributo, mostrarDetalles, mostrarDetallesV, \
    modificarAtributo, eliminarAtributo, listarVersiones, ReversionVersiones, reversionar, crearTipoItem, agregarAtributoAlTipoItem, \
    definirCantidadAtributos, formularioAgregarAtributoAlTipoItem, verAtributosTipoItems, verTipoItems, modificarAtributoDeTipoItem, \
    eliminarTipoItem, importar, finalizarItem, listarItemsFinalizados, graficar


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', adminItems.as_view(), name='admin_items'),
    url(r'^crear/', crearItem.as_view(), name='crear_item'),
    url(r'^crearEnFase/(?P<id>\d+)$', crearItemEnFase.as_view(), name='crear_item_en_fase'),
    url(r'^importar/(?P<id>\d+)$', importar.as_view(), name='crear_item_en_fase'),
    url(r'^listar/finalizados/', listarItemsFinalizados.as_view(), name='listar_itemsFinalizados'),
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
    url(r'^atributos/modificar/(?P<id>\d+)$', modificarAtributo.as_view(), name='modificar_atributo'),
    url(r'^atributos/eliminar/(?P<id>\d+)$', eliminarAtributo.as_view(), name='eliminar_atributo'),

    url(r'^reversionar/(?P<id>\d+)$', ReversionVersiones.as_view()),
    url(r'^reversionar/$', reversionar.as_view()),
    url(r'^tipoItem/crear/$', crearTipoItem.as_view(), name='crearTipoItem'),
    #url(r'^$', .as_view(), name=''),
    url(r'^tipoItem/add/$', agregarAtributoAlTipoItem.as_view()),
    url(r'^tipoItem/addAtrib/$', formularioAgregarAtributoAlTipoItem.as_view()),
    url(r'^tipoItem/definir/$', definirCantidadAtributos.as_view()),
    url(r'^tipoItem/mostrar/(?P<id>\d+)$', verAtributosTipoItems.as_view()),
    url(r'^tipoItem/listar/$', verTipoItems.as_view(), name='listar_tipoitem'),
    url(r'^tipoItem/modificar/(?P<id>\d+)$', modificarAtributoDeTipoItem.as_view(), name=''),
    url(r'^tipoItem/eliminar/(?P<id>\d+)$', eliminarTipoItem.as_view()),
    url(r'^relaciones/graficar/(?P<id>\d+)$', graficar.as_view()),
    url(r'^finalizar/(?P<id>\d+)$', finalizarItem.as_view()),


)
