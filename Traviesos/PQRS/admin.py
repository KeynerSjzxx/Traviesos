from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import PQRS, Tipo_pqrs, Estado
from .resources import PqrsResource, EstadoResource
# Register your models here.

@admin.register(Estado)
class estadoAdmin(ImportExportModelAdmin):
    resource_class = EstadoResource

@admin.register(Tipo_pqrs)
class tipoAdmin(ImportExportModelAdmin):
    resource_class = PqrsResource

@admin.register(PQRS)
class pqrstAdmin(admin.ModelAdmin):
    list_display = ('Tipo_pqrs', 'create_at', 'correo', 'descripcion')
    search_fields = ('create_at',)
    list_filter = ('Tipo_pqrs',)
    list_per_page = 10