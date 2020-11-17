from django import forms
from . models import Formulario, AreaPostular, NivelEducacional

class FormularioForm(forms.ModelForm):
    codigo = forms.CharField(label='Id Postulacion',max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    area_postular = forms.ModelChoiceField(queryset=AreaPostular.objects.all(), initial=1 ,label='Area',
        widget=forms.Select(
        attrs={
            'class':'form-control' 
        }
        ))
    nombre = forms.CharField(label='Nombre',max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    apellido = forms.CharField(label='Apellido',max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    correo = forms.EmailField(label='Correo',max_length=50, widget=forms.EmailInput(
        attrs={
            'class':'form-control'
        }
    ))
    numero = forms.IntegerField(label='Numero',required=True, widget=forms.NumberInput(
        attrs={
            'class':'form-control'
        }
    ))
    nivel_estudios = forms.ModelChoiceField(queryset=NivelEducacional.objects.all(), initial=1, label='Estudios',
        widget=forms.Select(
        attrs={
            'class':'form-control' 
        }
    ))
    motivo = forms.CharField(label='Motivo',max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = Formulario
        fields = ('codigo','area_postular','nombre','apellido','correo','numero','nivel_estudios','motivo')