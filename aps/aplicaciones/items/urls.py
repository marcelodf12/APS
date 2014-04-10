from django.conf.urls import patterns, include, url
from django.contrib import admin
from aps.aplicaciones.items.views import adminItems, crearItem, listarItems

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', adminItems.as_view(), name='admin_items'),
    url(r'^crear/', crearItem.as_view(), name='crear_item'),
    url(r'^listar/', listarItems.as_view(), name='listar_item'),
)
