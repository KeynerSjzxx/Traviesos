from django.db import models
from inventario.models import Producto
from django.contrib.auth.models import User 

class compras(models.Model):
    create_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="Fecha de creacion",
        verbose_name="Fecha de creacion"
    )
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.cliente)
    
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        db_table = 'compras'
        ordering = ['id']
        
class unidades_compras(models.Model):
    compra = models.ForeignKey(compras, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Agregar esta línea
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Compra: {self.compra}, Cantidad: {self.cantidad}"

    class Meta:
        verbose_name = 'Unidades de compra'
        verbose_name_plural = 'Unidades de compras'
        db_table = 'unidades de compras'
        ordering = ['id']
