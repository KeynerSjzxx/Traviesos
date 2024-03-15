from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Categoria, Producto
from .models import Categoria, Producto
from .resources import ProductoResource  # Asegúrate de importar tu recurso

admin.site.register(Categoria)

@admin.register(Producto)
class ProductoAdmin(ImportExportModelAdmin):  # Utiliza ImportExportModelAdmin en lugar de admin.ModelAdmin
    list_display = ('Nombre_producto', 'Precio_producto', 'Stock_producto',  'Imagen_producto', 'Descripcion_producto', 'Id_categoria')
    list_editable = ('Precio_producto','Imagen_producto', 'Stock_producto',  'Descripcion_producto',)
    search_fields = ('Nombre_producto', 'Precio_producto', 'Stock_producto',)
    list_filter = ('Id_categoria',)
    list_per_page = 10
    resource_class = ProductoResource  # Asigna tu recurso de importación/exportación aquí

    
    