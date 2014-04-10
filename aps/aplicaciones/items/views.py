from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from aps.aplicaciones.items.models import items


# Create your views here.
class adminItems(TemplateView):
    template_name = 'items/admin.html'

class crearItem(CreateView):
    model = items
    template_name = 'items/crear.html'
    success_url = reverse_lazy("admin_items")
    #fields = ['nombre', 'complejidad']

    def form_valid(self, form):
        item=form.save()
        item.versionAct = 1
        item.estado = 'creado'
        item.save()
        return super(crearItem, self).form_valid(form)

class listarItems(ListView):
    model = items
    template_name = 'items/listar.html'
    context_object_name = 'items'