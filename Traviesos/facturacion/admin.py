from django.contrib import admin
from .models import Compras
# Register your models here.
from .forms import CompraAdminForm

class CompraAdmin(admin.ModelAdmin):
    form = CompraAdminForm
    list_display = ['id', 'fechaCompra', 'idProducto', 'cantProductoComprado', 'idProveedor']  # Personaliza las columnas que deseas mostrar en la lista de compras

admin.site.register(Compras, CompraAdmin)
admin.site.register(Compras)