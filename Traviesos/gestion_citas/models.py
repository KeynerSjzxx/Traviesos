from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    raza = models.CharField(max_length=30,default='')
    peso = models.CharField(max_length=30, default='0')
    edad =  models.IntegerField(verbose_name='Edad', default=0)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento', default='2000-01-01')
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'
        db_table = 'mascota'
        ordering = ['id']
        
        
class Tamaño(models.Model):
    nombre = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    tamaño = models.CharField(
        max_length=100,
        choices=[
            ('Seleccionar', 'Seleccionar'),
            ('Grande', 'Grande'),
            ('Mediano', 'Mediano'),
            ('Pequeño', 'Pequeño'),
        ],
        verbose_name='Tamaño', default='Seleccionar'
    )

    def __str__(self):
        return self.tamaño

    class Meta:
        verbose_name = 'tamaño'
        verbose_name_plural = 'tamaños'
        db_table = 'tamaño'
        ordering = ['id']        
        
        
        

class AgendarCita(models.Model):
    tipo_cita = [
        ('Seleccionar', 'Seleccionar'),
        ('Baño', 'Baño'),
        ('Peluqueria', 'Peluqueria'),
        ('Baño y Peluqueria', 'Baño y Peluqueria'),
    ]
    
    Tipo_cita = models.CharField(max_length=100, choices=tipo_cita, verbose_name='Tipo cita')
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
