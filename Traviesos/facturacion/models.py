from django.db import models
from inventario.models import Producto
from inventario.models import Proveedor
from inventario.models import Marca
from inventario.models import Categoria

class Producto(models.Model):
    nomProducto = models.CharField(max_length=30)
    precioProducto = models.DecimalField(max_digits=10, decimal_places=2)
    imgProducto = models.ImageField(upload_to='productos/')
    descripProducto = models.CharField(max_length=50)
    idMarca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomProducto
    
class Compras(models.Model):
    fechaCompra = models.DateTimeField(verbose_name='Fecha de compra')
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantProductoComprado = models.IntegerField(verbose_name='Cantidad de productos comprados')
    idProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Compra ID: {self.id}, Producto: {self.idProducto}, Cantidad: {self.cantProductoComprado}"

class Proveedor(models.Model):
    idProveedor = models.BigAutoField(primary_key=True, verbose_name='ID del proveedor')
    Nombre_proveedor = models.CharField(max_length=30, verbose_name='Nombre del proveedor')
    Apellido_proveedor = models.CharField(max_length=30, verbose_name='Apellido del proveedor')
    Telefono_Proveedor = models.CharField(max_length=50, verbose_name='Teléfono del proveedor')

    def __str__(self):
        return f"{self.Nombre_proveedor} {self.Apellido_proveedor}"