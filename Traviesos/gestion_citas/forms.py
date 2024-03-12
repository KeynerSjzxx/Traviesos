from django import forms
from .models import AgendarCita, Mascota, Tamano, Raza, Tipo_citas

# Formulario para agendar citas
class FormAgendarCita(forms.ModelForm):
    class Meta:
        model = AgendarCita
        fields = ['Nombre', 'nombre_tipo', 'Fecha', 'Hora', 'Telefono', 'descripcion']
    
    # Campo para seleccionar una mascota
    Nombre = forms.ModelChoiceField(
        queryset=Mascota.objects.all(),
        empty_label="Seleccionar una mascota",
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    
    # Campo para seleccionar un tipo de cita
    nombre_tipo = forms.ModelChoiceField(
        queryset=Tipo_citas.objects.all(),
        empty_label="Seleccionar una cita",
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
     

# Formulario para la información de la mascota
class informacion_mascota(forms.ModelForm):
        class Meta:
            model = Mascota
            fields = ['nombre','raza','peso','tamano','edad']
            
    # Campo para seleccionar una raza
        raza = forms.ModelChoiceField(
            queryset=Raza.objects.all(),
            empty_label="Seleccionar una raza",
            widget=forms.Select(attrs={'class': 'form-select'}),
        )
    # Campo para seleccionar un tamaño
        tamano = forms.ModelChoiceField(
            queryset=Tamano.objects.all(),
            empty_label="Seleccionar un tamaño",
            widget=forms.Select(attrs={'class': 'form-select'}),
        )
       
       