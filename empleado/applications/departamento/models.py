from django.db import models

# Create your models here.

class DepartamentoModel(models.Model):

    name = models.CharField(
        'Nombre', 
        max_length=50
    )
    short_name = models.CharField(
        'Nombre Corto', 
        max_length=50, 
        unique=True
    )
    anulate = models.BooleanField(
        'Anulado', 
        default = False
    )
    
    # De esta manera le modificamos el nombre a la trabla
    
    class Meta:
        """Meta definition for DepartamentoModel."""

        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Mis Departamentos'
        ordering = ['id']
        unique_together = ('name','short_name') 

    def __str__(self):

        return str(self.id) + ' - ' + self.short_name


