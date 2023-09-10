from django import forms
from .models import PQRS, Tipo_pqrs

class FormAgendarPqrs(forms.ModelForm):
    class Meta:
        model = PQRS
        fields = ['correo', 'descripcion', 'Tipo_pqrs']
        
    def __init__(self, *args, **kwargs):
        super(FormAgendarPqrs, self).__init__(*args, **kwargs)
        self.fields['Tipo_pqrs'].empty_label = "Seleccionar"