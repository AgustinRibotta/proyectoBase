# Generated by Django 4.2.1 on 2023-05-22 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamentomodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamentomodel',
            options={'ordering': ['id'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': 'Mis Departamentos'},
        ),
    ]