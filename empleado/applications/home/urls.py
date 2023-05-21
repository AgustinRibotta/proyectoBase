from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.indexView.as_view()),
    path('list/', views.PruebaListVi1ew.as_view()),
    path('list_test/', views.PruebaModelsListView.as_view()),
]
