from import_export import resources
from .models import Producto

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto
        fields = ('Nombre_producto', 'Precio_producto', 'Imagen_producto', 'Descripcion_producto', 'Id_categoria')