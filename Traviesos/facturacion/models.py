from django.db import models
from landing.models import  users
from inventario.models import productos
# Create your models here.
class cart(models.Model):
    users = models.ForeignKey(users, null=True, blank=True, on_delete=models.CASCADE) #uno a muchos
    productos = models.ManyToMany(productos)
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ''


    