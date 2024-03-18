from django.db import models
from inventario.models import Producto
from inventario.models import Compras
from django.contrib.auth.models import User 

class compras(models.Model):
    create_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="Fecha de creacion",
        verbose_name="Fecha de creacion"
    )
    Cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    Total = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.Cliente
    
    class Meta:
        verbose_name = 'Compras'
        verbose_name_plural = 'Compras'
        db_table = 'compras'
        ordering = ['id']