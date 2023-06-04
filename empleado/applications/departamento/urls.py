from django.urls import path
from . import views

urlpatterns = [
    path(
        'new-departamento', 
        views.NewDepartamento.as_view(), 
        name= 'new-dep'
    ),

]
