# Generated by Django 4.2.4 on 2023-09-07 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_citas', '0009_alter_agendarcita_descripcion_alter_mascota_raza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendarcita',
            name='Tipo_cita',
            field=models.CharField(choices=[('Seleccionar', 'Seleccionar'), ('Baño', 'Baño'), ('Peluqueria', 'Peluqueria'), ('Baño y Peluqueria', 'Baño y Peluqueria')], max_length=100, verbose_name='Tipo cita'),
        ),
    ]
