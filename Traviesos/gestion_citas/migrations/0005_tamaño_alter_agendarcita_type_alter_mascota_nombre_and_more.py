# Generated by Django 4.2.4 on 2023-09-06 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_citas', '0004_alter_agendarcita_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tamaño',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamaño', models.CharField(choices=[('Seleccionar', 'Seleccionar'), ('Grande', 'Grande'), ('Mediano', 'Mediano'), ('Pequeño', 'Pequeño')], max_length=30)),
            ],
            options={
                'verbose_name': 'tamaño',
                'verbose_name_plural': 'tamaño',
                'db_table': 'tamaño',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='agendarcita',
            name='type',
            field=models.CharField(choices=[('Seleccionar', 'Seleccionar'), ('Baño', 'Baño'), ('Peluqueada', 'Peluqueria'), ('Baño y Peluqueada', 'Baño y Peluqueria')], max_length=100, verbose_name='Tipo cita'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='nombre',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='agendarcita',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_citas.tamaño'),
        ),
    ]
