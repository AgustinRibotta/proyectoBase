# Generated by Django 4.2.1 on 2023-05-30 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleadomodel',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombre Completo'),
        ),
    ]