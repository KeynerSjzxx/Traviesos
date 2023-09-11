from django.db import models
from django.contrib.auth.models import User

class InformacionAdicionalUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Nombre_completo = models.CharField(max_length=255)
    Fecha_nacimiento = models.DateField()
    Correo = models.EmailField()
    Numero_telefonico = models.CharField(max_length=15)
    Dirreccion_recidencia = models.CharField(max_length=30)
    Numero_tarjeta = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4)

    class Meta:
        verbose_name = 'Información Adicional de Usuario'
        verbose_name_plural = 'Información Adicional de Usuarios'