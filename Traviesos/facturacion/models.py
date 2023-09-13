from django.db import models
from inventario.models import Producto
from django.contrib.auth.models import User
# Create your models here.
class cart(models.Model):
    users = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) #uno a muchos
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ''
    
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
    