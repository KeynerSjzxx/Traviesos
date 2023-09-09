from django.contrib import admin
from .models import AgendarCita, Mascota, Tamaño, Raza
# Register your models here.

admin.site.register(Tamaño)
admin.site.register(Raza)

@admin.register(Mascota)
class MacotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'peso', 'Tamaño', 'edad', 'fecha_nacimiento')
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