# Generated by Django 4.2.1 on 2023-05-22 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamentomodel',
            options={'ordering': ['name'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': 'Mis Departamentos'},
        ),
        migrations.AlterUniqueTogether(
            name='departamentomodel',
            unique_together={('name', 'short_name')},
        ),
    ]
