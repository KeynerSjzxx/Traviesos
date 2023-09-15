from django.db import models

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
    
    class Meta:
        verbose_name = 'Estado_pqrs'
        verbose_name_plural = 'Estado_pqrs´s'
        db_table = 'estado'
        ordering = ['id']

class PQRS(models.Model):
    id = models.AutoField(primary_key=True)
    Tipo_pqrs = models.ForeignKey(Tipo_pqrs, on_delete=models.CASCADE)
    create_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="Fecha de creacion",
        verbose_name="Fecha de creacion"
    )
    correo = models.CharField(max_length=100, verbose_name='correo electronico', blank=True, null=True)
    descripcion = models.TextField(max_length=500, verbose_name='Descripcion')
    Estado_pqrs = models.ForeignKey(Estado, on_delete=models.CASCADE, blank=True, null=True)
    Respuesta = models.CharField(max_length=150)

    def __str__(self):
        return self.correo

    class Meta:
        verbose_name = 'PQRS'
        verbose_name_plural = 'PQRS´s'
        db_table = 'pqrs'
        ordering = ['id']