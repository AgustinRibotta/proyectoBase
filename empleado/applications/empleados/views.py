from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
)

# Models
from .models import EmpleadoModel
from .admin import EmpleadoAdmin
# Create your views here.

# Lista de empeads
class ListAllListView(ListView):
    model = EmpleadoModel
    template_name = "empleados/list_all.html"
    context_object_name = 'list'
    paginate_by = 4


# Lista de empelados de un area
class ListByAreaListView(ListView):
    template_name = "empleados/list_area.html"

    # Filtro de area por una queryset
    def get_queryset(self):
        area = self.kwargs['short_name']
        list = EmpleadoModel.objects.filter(
        depart__short_name = area, 
        )
        return list 
    

class ListByJobListView(ListView):
    template_name = "empleados/list_job.html"
    context_object_name = 'jobs'
    # Filtro de area por una queryset
    def get_queryset(self):
        kword = self.request.GET.get('kword')
        list = EmpleadoModel.objects.filter(
        job = kword, 
        )
        return list
    
    
class ListEmpleadoByKwordListView(ListView):
    # Lista Empelados por Palabra Clave
    template_name = "empleados/by_wkord.htm"
    context_object_name = 'empleados'
    
    def get_queryset(self):
        kword = self.request.GET.get('kword',)
        list = EmpleadoModel.objects.filter(
        first_name = kword, 
        )
        return list
    

class abiltyByEmpleadoListView(ListView):
    template_name = "empleados/abilty.html"
    context_object_name = 'abilty'
    
    def get_queryset(self):
        kword = self.request.GET.get('kword')
        try:
            empleado = EmpleadoModel.objects.get(id= kword, )
            
            return empleado.ability.all()
        except:
            empleado = EmpleadoModel.objects.all()
            
            return empleado
        

class EmpleadoDetailView(DetailView):
    model = EmpleadoModel
    template_name = "empleados/detai_view.html"
    
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes' 
        return context
    

class SuccessTemplateView(TemplateView):
    template_name = "empleados/success.html"


class EmpleadoCreateView(CreateView):
    model = EmpleadoModel
    template_name = "empleados/add.html"
    # fields = ('__all__')
    fields = [
        'first_name',
        'last_name',
        'job',
        'depart',
        'ability',
    ]
    # success_url = '/success/'
    success_url = reverse_lazy ('empleados_app:success')

    def form_valid(self, form: BaseModelForm):
        # Logica del proceso
        # empleado = form.save()
        # De esta manera creamos una instacias antes de guardar, para evitar guardad dos veces
        empleado = form.save(commit=False)
        # De esta manera verificamos que interceptamos todo lo que se gurado en la base de datos
        # print (empleado)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)






