from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AgendarCita, Mascota, Tamano, Raza
# Register your models here.

@admin.register(Tamano)
class TamañoAdmin(ImportExportModelAdmin):
    pass

@admin.register(Raza)
class RazaAdmin(ImportExportModelAdmin):
    pass

@admin.register(Mascota)
class MacotaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'raza', 'peso', 'tamano', 'edad')
    list_editable = ('peso', 'tamano','edad',)
    search_fields = ('raza', 'tamano',)
    list_filter = ('raza',)
    list_per_page = 10

@admin.register(AgendarCita)
class CitasAdmin(admin.ModelAdmin):
    list_display = ('Tipo_cita', 'Nombre', 'Fecha', 'Hora', 'Telefono', 'descripcion')
    list_editable = ('Fecha', 'Hora',)
    search_fields = ('Tipo_cita',)
    list_filter = ('Tipo_cita',)
    list_per_page = 10