from django.shortcuts import render
from django.views.generic import (
    ListView
)
# Models
from .models import EmpleadoModel

# Create your views here.

# Lista de empeads
class ListAllListView(ListView):
    model = EmpleadoModel
    template_name = "empleados/list_all.html"
    context_object_name = 'list'


# Lista de empelados de un area
class ListByAreaListView(ListView):
    queryset = EmpleadoModel.objects.filter(
        depart__short_name ='Administracion', 
    )
    template_name = "empleados/list_area.html"

