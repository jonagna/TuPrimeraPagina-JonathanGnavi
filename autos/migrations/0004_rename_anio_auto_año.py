# Generated by Django 5.2 on 2025-04-07 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0003_rename_marcas_auto_marca_remove_auto_año_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auto',
            old_name='anio',
            new_name='año',
        ),
    ]
