from django.db import models

# Create your models here.

class PQRS(models.Model):
    TIPOS_PQRS = [
    ('Peticion','Peticion'),
    ('Queja','Queja'),
    ('Reclamo','Reclamo'),
    ('Sugerencia','Sugerencia'),
    ]
    
    Type = models.CharField(max_length=100, choices=TIPOS_PQRS, verbose_name= 'TIPO PQRS')
    Date = models.DateField(verbose_name='Fecha')
    Name = models.CharField(max_length=100, verbose_name='Nombre Usuario')
    Sender = models.TextField(max_length=500, verbose_name='Descripcion')