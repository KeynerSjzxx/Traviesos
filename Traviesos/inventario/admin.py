from django.contrib import admin
from inventario.models import Categoria, Producto, Stock, Marca, Proveedor

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Stock)
admin.site.register(Marca)
admin.site.register(Proveedor)

@admin.register(Producto)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Nombre_producto', 'Precio_producto', 'Imagen_producto', 'Descripcion_producto', 'Id_marca', 'Id_categoria')
    list_editable = ('Precio_producto','Imagen_producto', 'Descripcion_producto',)
    search_fields = ('Nombre_producto', 'Precio_producto',)
    list_filter = ('Id_categoria',)
    list_per_page = 10