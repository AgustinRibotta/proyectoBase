from django.db import models
from applications.departamento.models import DepartamentoModel
from ckeditor.fields import RichTextField

# Create your models here.

class HabilidadesModel(models.Model):
    """Model definition for HabilidadesModel."""

    # TODO: Define fields here
    
    ability = models.CharField(
        'Habilidades', 
        max_length=50
    )

    class Meta:
        """Meta definition for Habilidades."""

        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empelado'
        ordering = ['id']
        unique_together = ['ability',]

    def __str__(self):
        """Unicode representation of Habilidades."""
        return str(self.id) + ' - ' + self.ability 
        pass


class EmpleadoModel(models.Model):
    """Model definition for EmpleadoModel."""

    JOB_CHOICES = (
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','otro'),
    )
    
    # TODO: Define fields here
    
    first_name = models.CharField(
        'Nombres', 
        max_length=50
    )
    last_name = models.CharField(
        'Apellido', 
        max_length=50
    )
    full_name = models.CharField(
        'Nombre Completo', 
        max_length=120,
        blank=True
    )
    job = models.CharField(
        'Trabajo', 
        max_length=1, 
        choices=JOB_CHOICES
    )
    depart = models.ForeignKey(
        DepartamentoModel, 
        on_delete=models.CASCADE
    )
    # image = models.ImageField(
        # , 
        # upload_to=None, 
        # height_field=None, 
        # width_field=None, 
        # max_length=None
    # )
    
    ability = models.ManyToManyField(
        HabilidadesModel
    )
    cv = RichTextField(
        blank=True
    )
    
    class Meta:
        """Meta definition for EmpleadoModel."""
  
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']

    def __str__(self):
        """Unicode representation of EmpleadoModel."""
        
        return str(self.id) + ' - ' + self.first_name + '  ' + self.last_name
