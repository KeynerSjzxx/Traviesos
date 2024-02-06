from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Tipo_pqrs(models.Model):
    id = models.AutoField(primary_key=True)
    Tipo_pqrs = models.CharField(max_length=30)
    
    def __str__(self):
        return self.Tipo_pqrs
    
    class Meta:
        verbose_name = 'Tipo pqrs'
        verbose_name_plural = 'Tipos pqrs'
        db_table = 'tipo_pqrs'
        ordering = ['id']
        
class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    Estado_pqrs = models.CharField(max_length=30)

    def __str__(self):
        return self.Estado_pqrs

class PQRS(models.Model):
    id = models.AutoField(primary_key=True)
    Tipo_pqrs = models.ForeignKey(Tipo_pqrs, on_delete=models.CASCADE)
    create_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="Fecha de creacion",
        verbose_name="Fecha de creacion"
    )
    Nombre = models.CharField(max_length=100, verbose_name='Nombre Usuario')
    Descripcion = models.TextField(max_length=500, verbose_name='Descripcion')
    Respuesta = models.CharField(max_length=150, blank=True, null=True)
    Estado_pqrs = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.Nombre

# Esta función se ejecutará después de que se guarde una instancia de PQRS
@receiver(post_save, sender=PQRS)
def actualizar_estado(sender, instance, **kwargs):
    if instance.Respuesta and instance.Estado_pqrs.Estado_pqrs == "Pendiente":
        estado_respuesta = Estado.objects.get(Estado_pqrs="Respuesta")
        instance.Estado_pqrs = estado_respuesta
        instance.save()

    class Meta:
        verbose_name = 'PQRS'
        verbose_name_plural = 'PQRS´s'
        db_table = 'pqrs'
        ordering = ['id']
