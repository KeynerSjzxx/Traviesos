from django import forms
from .models import AgendarCita, Mascota, Tamano, Raza

class FormAgendarCita(forms.ModelForm):
    class Meta:
        model = AgendarCita
        fields = '__all__'
        
    Nombre = forms.ModelChoiceField(
        queryset=Mascota.objects.all(),
        empty_label="Seleccionar una mascota",
        to_field_name='nombre',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    
class informacion_mascota(forms.ModelForm):
        class Meta:
            model = Mascota
            fields = ['nombre','raza','peso','tamano','edad']
    
        raza = forms.ModelChoiceField(
        queryset=Raza.objects.all(),
        empty_label="Seleccionar una raza",
        to_field_name='raza',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
        
        tamano = forms.ModelChoiceField(
        queryset=Tamano.objects.all(),
        empty_label="Seleccionar un tamaño",
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
       
       