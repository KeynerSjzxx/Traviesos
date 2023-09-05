from django.db import models

# Create your models here.
class Compra(models.Model):[
    cliente = models.ForeignKey(User, on_delete=models.CASCADE) ,
    productos = models.ManyToManyField('Producto', through='DetalleCompra')   ,                                                      
    fecha_compra = models.DateTimeField(auto_now_add=True),
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
]

    