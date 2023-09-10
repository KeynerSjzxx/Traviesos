from django.contrib import admin
from .models import PQRS, Tipo_pqrs, Estado
# Register your models here.

admin.site.register(Tipo_pqrs)
admin.site.register(Estado)

@admin.register(PQRS)
class pqrstAdmin(admin.ModelAdmin):
    list_display = ('Tipo_pqrs', 'create_at', 'correo', 'descripcion')
    search_fields = ('create_at',)
    list_filter = ('Tipo_pqrs',)
    list_per_page = 10