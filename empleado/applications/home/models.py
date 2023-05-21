from django.db import models

# Create your models here.

class PruebaModels(models.Model):
    """Model definition for Prueba."""

    titulo = models.CharField(max_length=30)
    sub_titulo = models.CharField(max_length=20)