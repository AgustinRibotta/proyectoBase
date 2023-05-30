from django.urls import path
from . import views

app_name = 'empleados_app'

urlpatterns = [
    path(
        'list-empleado/', 
        views.ListAllListView.as_view(), 
        name= 'lista'
    ),
    path(
        'area/<short_name>/', 
        views.ListByAreaListView.as_view(), 
        name='area'
    ),
    path(
        'job/', 
        views.ListByJobListView.as_view(), 
        name='job'
    ),
    path(
        'buscar-empleado/', 
        views.ListEmpleadoByKwordListView.as_view(), 
        name='buscar'
    ),
    path(
        'habilidades/', 
        views.abiltyByEmpleadoListView.as_view(), 
        name='habilidad'
    ),
    path(
        'ver-detalle/<pk>/', 
        views.EmpleadoDetailView.as_view(), 
        name= 'detalle'
    ),
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(), 
        name= 'add'
    ),
    path(
        'success/', 
        views.SuccessTemplateView.as_view(), 
        name= 'success'
    ),
]
