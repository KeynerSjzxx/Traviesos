from django.db import models

# Create your models here.
class Carrito(models.Model):
    User = models.Foreig #uno a muchos
    