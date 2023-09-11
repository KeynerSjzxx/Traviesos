from django import forms
from .models import InformacionAdicionalUsuario

class InformacionAdicionalUsuarioForm(forms.ModelForm):
    class Meta:
        model = InformacionAdicionalUsuario
        fields = ['Nombre_completo', 'Fecha_nacimiento', 'Correo', 'Numero_telefonico', 'Dirreccion_recidencia', 'Numero_tarjeta', 'cvv']
