from django import forms
from .models import Compra  # Asegúrate de importar tu modelo de Compra

class CompraAdminForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'