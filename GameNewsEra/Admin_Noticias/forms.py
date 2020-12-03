from django import forms
from . models import Formulario, AreaPostular, NivelEducacional, Noticia

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
        fields = ('area_postular','nombre','apellido','correo','numero','nivel_estudios','motivo')

class NoticiaForm(forms.ModelForm):
    codigo = forms.CharField(label='Codigo de la Noticia', max_length=50, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    portada = forms.ImageField(widget=forms.ImageField(
        
    ))
    titulo = forms.CharField(label='Titulo', max_length=50, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    subtitulo = forms.CharField(label='Subtitulo', max_length=50, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    parrafo1 = forms.CharField(label='Parrafo 1', max_length=500, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    imagen = forms.ImageField(widget=forms.ImageField(

    ))
    bajadaimagen = forms.CharField(label='Bajada Imagen', max_length=60, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    video = forms.CharField(label='Link del Video', max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    parrafo2 = forms.CharField(label='Parrafo 2', max_length=500, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = Noticia
        fields = ('codigo', 'portada', 'titulo', 'subtitulo', 'parrafo1', 'imagen', 'bajadaimagen', 'video', 'parrafo2')