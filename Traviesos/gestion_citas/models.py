from django.db import models
from django.contrib.auth.models import User

#modelo de tamaño
class Tamano(models.Model):
    Tamaño = models.CharField(max_length=30)

    def __str__(self):
        return self.Tamaño

    class Meta:
        verbose_name = 'Tamaño'
        verbose_name_plural = 'Tamaños'
        db_table = 'tamaño'
        ordering = ['id']        
        
#modelo de tipos citas
class Tipo_citas(models.Model):
    nombre_tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_tipo

    class Meta:
        verbose_name = 'Tipo cita'
        verbose_name_plural = 'Tipo citas'
        db_table = 'tipo_citas'
        ordering = ['id']     

#modelo de raza
class Raza(models.Model):
    raza = models.CharField(max_length=30)
    
    def __str__(self):
        return self.raza
    
    class Meta:
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'
        db_table = 'raza'
        ordering = ['id']     

#modelo de mascotas
class Mascota(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=30, unique=True)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    peso = models.CharField(max_length=30, default='0')
    tamano = models.ForeignKey(Tamano, on_delete=models.CASCADE)
    edad = models.IntegerField(verbose_name='Edad', default=0)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'
        db_table = 'mascota'
        ordering = ['id']

#modelo de citas
class AgendarCita(models.Model):
    nombre_tipo = models.ForeignKey(Tipo_citas, on_delete=models.CASCADE, default=1)
    Nombre = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='agendarcitas_name', null=False, blank=False)
    Fecha = models.DateField(verbose_name='Fecha de la cita')
    Hora = models.TimeField(verbose_name='Hora de la cita')
    Telefono = models.CharField(max_length=15, verbose_name='Número de contacto')
    descripcion = models.TextField(max_length=200, verbose_name='Descripcion', default='')

    def __str__(self):
        return str(self.Nombre)
    
    class Meta:
        verbose_name = 'Agendar cita'
        verbose_name_plural = 'Agendar citas'
        db_table = 'AgendarCita'
        ordering = ['id']
