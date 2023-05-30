from django.contrib import admin
from .models import EmpleadoModel, HabilidadesModel

# Register your models here.


admin.site.register(HabilidadesModel)


class EmpleadoAdmin(admin.ModelAdmin):
    '''Admin View for Empleado'''
    
    # Que fila de la tabla queremos que aparesca
    list_display = (
        'id',
        'first_name',
        'last_name',
        'depart',
        'job',
        'full_name',    
    )
    def full_name(self,obj):
        return obj.first_name + ' ' + obj.last_name 
    
    # Buscador
    search_fields = (
        'first_name',
        'last_name',
    )
    # Filtros
    list_filter = (
        'job',
        'depart',
        'ability',
    )
    filter_horizontal = ('ability',)


admin.site.register(EmpleadoModel, EmpleadoAdmin)