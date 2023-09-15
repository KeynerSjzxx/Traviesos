from django.db import models
from inventario.models import Producto
from carts.models import Cart
from inventario.models import Compras
from django.contrib.auth.models import User as BaseUser

class User(BaseUser):
    # tus campos personalizados aquí

    class Meta:
        # ...

# Agrega el related_name personalizado en la relación ForeignKey
class Cart(models.Model):
    users = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='facturacion_carts')
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ''

class Compra(models.Model):  # Cambia "Compras" a "Compra" para que coincida con las convenciones de nombres
    
    date = models.DateField(verbose_name='Fecha de compra')  # Cambia 'Tipo compra' a 'Fecha de compra'
    idProduct = models.ForeignKey(Producto, on_delete=models.CASCADE)
    day = models.DateField(verbose_name='Fecha de la compra', null=True, blank=True)  # Cambia "Fecha de la cita" a algo más apropiado
    hour = models.TimeField(verbose_name='Hora de la compra', null=True, blank=True)  # Cambia "Hora de la cita" a algo más apropiado
    
    def __str__(self):
        return str(self.idProduct)  # Cambia el retorno para mostrar algo significativo
    