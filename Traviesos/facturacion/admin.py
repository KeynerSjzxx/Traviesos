from django.contrib import admin

# Register your models here.
from . models import cart

admin.site.register(cart)
from .models import Compras
# Register your models here.

admin.site.register(Compras)