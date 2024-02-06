from django import forms
from .models import PQRS, Tipo_pqrs

class FormAgendarPqrs(forms.ModelForm):
    class Meta:
        model = PQRS
        fields = ['Nombre', 'Descripcion', 'Tipo_pqrs']  # Cambié 'correo' por 'Nombre' y 'descripcion' por 'Descripcion'

    def __init__(self, *args, **kwargs):
        super(FormAgendarPqrs, self).__init__(*args, **kwargs)
        self.fields['Tipo_pqrs'].empty_label = "Seleccionar"
