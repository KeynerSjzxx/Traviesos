# Generated by Django 5.0.2 on 2024-03-15 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='Id_marca',
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
    ]