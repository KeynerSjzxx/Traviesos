from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AgendarCita, Mascota, Tamaño, Raza
# Register your models here.

@admin.register(Tamaño)
class TamañoAdmin(ImportExportModelAdmin):
    pass

@admin.register(Raza)
class RazaAdmin(ImportExportModelAdmin):
    pass

@admin.register(Mascota)
class MacotaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'raza', 'peso', 'Tamaño', 'edad', 'fecha_nacimiento')
    list_editable = ('peso', 'Tamaño','edad',)
    search_fields = ('raza', 'Tamaño',)
    list_filter = ('raza',)
    list_per_page = 10

@admin.register(AgendarCita)
class CitasAdmin(admin.ModelAdmin):
    list_display = ('Tipo_cita', 'Nombre', 'Fecha', 'Hora', 'Telefono', 'descripcion')
    list_editable = ('Fecha', 'Hora',)
    search_fields = ('Tipo_cita',)
    list_filter = ('Tipo_cita',)
    list_per_page = 10