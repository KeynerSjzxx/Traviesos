from django.db import models

class Marca(models.Model):
    Nombre_marca = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre_marca
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        db_table = 'marcas'
        ordering = ['id']

class Categoria(models.Model):
    Nombre_categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre_categoria
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categorias'
        ordering = ['id'] 

class Producto(models.Model):
    Nombre_producto = models.CharField(max_length=30)
    Precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    Imagen_producto = models.CharField(max_length=100)
    Descripcion_producto = models.CharField(max_length=50)
    Id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre_producto
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'productos'
        ordering = ['id']

class Stock(models.Model):
    Id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Stock_Cantidad = models.IntegerField()
    
    def __str__(self):
        return self.Id_producto
    
    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
        db_table = 'stocks'
        ordering = ['id']

class Proveedor(models.Model):
    Nombre_proveedor = models.CharField(max_length=30)
    Apellido_proveedor = models.CharField(max_length=30)
    Telefono_Proveedor = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_proveedor
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedores'
        ordering = ['id']
