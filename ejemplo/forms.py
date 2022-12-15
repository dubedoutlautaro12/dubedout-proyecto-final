from django import forms
from ejemplo.models import Familiar, Mascota

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100,
                            widget= forms.TextInput(attrs={'placeholder': 'Busque algo...'}))

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class MascotaForm(forms.ModelForm):
    class Meta:
      model = Mascota
      fields = ['nombre', 'dueno', 'peso']