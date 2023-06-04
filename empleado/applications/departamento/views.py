from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import (
    FormView,
)
from applications.empleados.models import EmpleadoModel
from .models import DepartamentoModel
from applications.departamento.forms import NewDepartamentoForm



# Create your views here.


class NewDepartamento(FormView):
    template_name =  'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '.'
    
    def form_valid(self, form):
        print('############ Estamos en form valid ##############')
        
        depa = DepartamentoModel(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shor_name'],
        )
        depa.save()
        
        nombre = form.cleaned_data['name']
        apellido = form.cleaned_data['first_name']
        EmpleadoModel.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            depart = depa,
        )

        return super(NewDepartamento, self).form_valid(form)