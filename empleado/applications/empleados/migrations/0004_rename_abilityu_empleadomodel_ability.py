# Generated by Django 4.2.1 on 2023-05-22 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_alter_habilidadesmodel_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleadomodel',
            old_name='abilityu',
            new_name='ability',
        ),
    ]
