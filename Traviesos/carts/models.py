import uuid
from django.db import models
from django.contrib.auth.models import User  # Debes importar "User" en lugar de "user" si es el modelo de usuario predeterminado de Django
from inventario.models import Producto
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Agrega una relación con el usuario
    products = models.ManyToManyField(Producto, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cart_id

@receiver(pre_save, sender=Cart)
def create_cart_id(sender, instance, *args, **kwargs):
    """
    Esta función se ejecutará antes de guardar un nuevo carrito.
    Genera un nuevo cart_id si no se proporciona uno.
    """
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())
