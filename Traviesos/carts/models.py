import uuid
from django.db import models

from django.contrib.auth.models import user
from inventario.models import Producto

from django.db.models.signals import pre_save

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=:)
