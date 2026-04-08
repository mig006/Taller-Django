from django import forms
from .models import Cancion


class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['titulo', 'artista', 'album', 'genero', 'duracion_segundos', 'fecha_lanzamiento']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'artista': forms.TextInput(attrs={'class': 'form-control'}),
            'album': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-select'}),
            'duracion_segundos': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'fecha_lanzamiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'duracion_segundos': 'Duración (segundos)',
            'fecha_lanzamiento': 'Fecha de lanzamiento',
        }
