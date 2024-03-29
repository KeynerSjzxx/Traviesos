from django.db import models

class Categoria(models.Model):
    Nombre_categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre_categoria
    
    class Meta:
        verbose_name = 'Categoria producto'
        verbose_name_plural = 'Categorias producto'
        db_table = 'categorias'
        ordering = ['id'] 

class Producto(models.Model):
    Nombre_producto = models.CharField(max_length=30)
    Precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    Stock_producto = models.IntegerField()
    Imagen_producto = models.CharField(max_length=100)
    Descripcion_producto = models.CharField(max_length=50)
    Id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre_producto
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'productos'
        ordering = ['id']