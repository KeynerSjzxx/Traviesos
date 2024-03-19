from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import compras, unidades_compras

admin.site.register(unidades_compras)

@admin.register(compras)
class ComprasAdmin(ImportExportModelAdmin):
    list_display = ('create_at', 'cliente', 'total')
    list_editable = ('total',)
    search_fields = ('cliente',)
    list_filter = ('cliente',)
    list_per_page = 10