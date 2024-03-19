from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AgendarCita, Mascota, Tamano, Raza,Tipo_citas
# Register your models here.

@admin.register(Tamano)
class TamañoAdmin(ImportExportModelAdmin):
    pass

@admin.register(Raza)
class RazaAdmin(ImportExportModelAdmin):
    pass

@admin.register(Tipo_citas)
class Tipo_citasAdmin(ImportExportModelAdmin):
    pass

@admin.register(Mascota)
class MacotaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'raza', 'peso', 'tamano', 'edad')
    list_editable = ('peso', 'tamano','edad',)
    search_fields = ('raza', 'tamano',)
    list_filter = ('raza', 'tamano', 'peso', 'edad', )
    list_per_page = 10

@admin.register(AgendarCita)
class CitasAdmin(admin.ModelAdmin):
    list_display = ('nombre_tipo', 'Nombre', 'Fecha', 'Hora', 'Telefono', 'descripcion')
    list_editable = ('Fecha', 'Hora',)
    search_fields = ('Tipo_cita',)
    list_filter = ('nombre_tipo',)
    list_per_page = 10