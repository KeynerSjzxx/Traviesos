from django.db import models

# Create your models here.

class Agendar_cita(models.Model):
    tipo_cita = [
        ('Seleccionar','Seleccionar'),
        ('Baño','Baño'),
        ('Peluqueada','Peluqueada'),
        ('Baño y Peluqueada','Baño y Peluqueada'),
    ]
    
    tamaño_mascota = [
        ('Seleccionar','Seleccionar'),
        ('Grande','Grande'),
        ('mediano','mediano'),
        ('pequeño','pequeño'),
    ]
    
    type = models.CharField(max_length=100, choices=tipo_cita, verbose_name='Tipo cita')
    size = models.CharField(max_length=100, choices=tamaño_mascota, verbose_name='Tamaño mascota')
    name = models.CharField(max_length=100, verbose_name='Nombre mascosta')
    day = models.DateField(verbose_name='Fecha de la cita')
    hour = models.TimeField(verbose_name='Hora de la cita')
    phone = models.CharField(max_length=15, verbose_name='Numero de contacto')
    
    def __str__(self):
        return self.name