from django import forms
from ejemplo.models import Alumnos, Docentes, Familiar

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)
    widget=forms.TextInput(attrs={'placeholder':'Busque algo'})

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class AlumnosForm(forms.ModelForm):
  class Meta:
    model = Alumnos
    fields = ['nombre', 'curso', 'numero_matricula']

class DocentesForm(forms.ModelForm):
  class Meta:
    model = Docentes
    fields = ['nombre', 'asignatura', 'grado']