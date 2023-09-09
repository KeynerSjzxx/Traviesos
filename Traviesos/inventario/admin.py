from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Categoria, Producto, Stock, Marca, Proveedor
from .resources import ProductoResource  # Asegúrate de importar tu recurso

admin.site.register(Categoria)
admin.site.register(Stock)
admin.site.register(Marca)
admin.site.register(Proveedor)

@admin.register(Producto)
class ProductoAdmin(ImportExportModelAdmin):  # Utiliza ImportExportModelAdmin en lugar de admin.ModelAdmin
    list_display = ('Nombre_producto', 'Precio_producto', 'Imagen_producto', 'Descripcion_producto', 'Id_marca', 'Id_categoria')
    list_editable = ('Precio_producto','Imagen_producto', 'Descripcion_producto',)
    search_fields = ('Nombre_producto', 'Precio_producto',)
    list_filter = ('Id_categoria',)
    list_per_page = 10
    resource_class = ProductoResource  # Asigna tu recurso de importación/exportación aquí

    
    