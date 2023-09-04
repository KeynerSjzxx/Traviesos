from django.contrib import admin
from inventario.models import Categoria, Producto, Stock, Marca, Proveedor

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Stock)
admin.site.register(Marca)
admin.site.register(Proveedor)