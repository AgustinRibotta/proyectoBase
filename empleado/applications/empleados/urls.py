from django.urls import path
from . import views

urlpatterns = [
    path('list-empleado/', views.ListAllListView.as_view()),
    path('area/', views.ListByAreaListView.as_view()),
]
