from django import forms
from .models import PQRS, Tipo_pqrs

class FormAgendarPqrs(forms.ModelForm):
    class Meta:
        model = PQRS
        fields = ['Tipo_pqrs','Descripcion', 'Nombre']

    Tipo_pqrs = forms.ModelChoiceField(
        queryset=Tipo_pqrs.objects.all(),
        empty_label="Seleccionar un tipo",
        widget=forms.Select(attrs={'class': 'form-select'}),
    
    )
    
    
