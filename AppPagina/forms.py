from django import forms
from .models import Estudiantes

class EstudiantesForm(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = '__all__'