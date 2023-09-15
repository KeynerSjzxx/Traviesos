import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User as BaseUser

class User(BaseUser):
    # tus campos personalizados aquí

    class Meta:
        # ...

# Agrega el related_name personalizado en la relación ForeignKey
class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='carts')
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ''

@receiver(pre_save, sender=Cart)
def create_cart_id(sender, instance, *args, **kwargs):
    """
    Esta función se ejecutará antes de guardar un nuevo carrito.
    Genera un nuevo cart_id si no se proporciona uno.
    """
    if not instance.cart_id:
        instance.cart_id = uuid.uuid4()  # Genera un nuevo cart_id