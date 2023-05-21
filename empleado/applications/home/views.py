from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from applications.home.models import PruebaModels

# Create your views here.

class indexView(TemplateView):
    template_name = "home/home.html"
    

class PruebaListVi1ew(ListView):
    
    template_name = "home/list.html"
    queryset = ['A', 'B', 'C']
    context_object_name = 'lista'
    

class PruebaModelsListView(ListView):
    model = PruebaModels
    template_name = "home/prueba.html"
    context_object_name = 'list_tests'

