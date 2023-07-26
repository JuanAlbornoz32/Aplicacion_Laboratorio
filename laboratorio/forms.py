from django import forms
from .models import Laboratorio

class Laboratorioform(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ('nombre', 'ciudad', 'pais')