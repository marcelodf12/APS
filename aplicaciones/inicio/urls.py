from django.conf.urls import patterns, include, url
from .views import home

urlpatterns = patterns('',
    url(r'^$','django.contrib.auth.views.login',
        {'template_name':'inicio/index.html'}, name='login'),
    url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',
        name='logout'),
    url(r'^inicio/$', home.as_view(),
        name='home'),

)
