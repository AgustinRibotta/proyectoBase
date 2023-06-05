from django.urls import path
from . import views

urlpatterns = [
    path(
        'home/', 
        views.indexView.as_view(),
        name='home',
    ),
    path(
        'list/', 
        views.PruebaListVi1ew.as_view(),
        name='lista',
    ),
    path(
        'list_test/', 
        views.PruebaModelsListView.as_view(),
        name='test',
    ),
    path(
        'add-home/', 
        views.PruebaCreateView.as_view(),
        name='add',
    ),
    path(
        'template/', 
        views.ResumenFundationView.as_view(),
        name='Fundation',
    ),
]
