from django.db import models
from inventario.models import Producto
# Create your models here.

class Compras(models.Model):
    
    date = models.DateField(verbose_name='Tipo compra')
    idProduct = models.ForeignKey(Producto, on_delete=models.CASCADE)
    day = models.DateField(verbose_name='Fecha de la cita')
    hour = models.TimeField(verbose_name='Hora de la cita')
    phone = models.CharField(max_length=15, verbose_name='Numero de contacto')
    
    def __str__(self):
        return self.idProduct

    