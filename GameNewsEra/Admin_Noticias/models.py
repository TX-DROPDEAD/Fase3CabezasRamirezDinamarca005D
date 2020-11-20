from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class NivelEducacional(models.Model):
    nivel_educacional = models.CharField(max_length = 100, blank=True, null=True)
    descripcion = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ['nivel_educacional']
    
    def __str__(self):
        return self.nivel_educacional

    

class AreaPostular(models.Model):
    area_postular = models.CharField(max_length = 100,blank=True, null=True)
    descripcion = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ['area_postular']
    
    def __str__(self):
        return self.area_postular

class Autor(models.Model):

    id_autor = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = 'Indique el ID del Autor de noticia')
    nom_autor = models.CharField(max_length = 25, help_text='Indique el nombre del Autor')
    educacion =  models.ForeignKey('NivelEducacional', on_delete = models.SET_NULL, null= True, blank=True, help_text='Indique el nivel de estudios de Autor')
    numero = models.IntegerField(blank = True, null = True, help_text='Indique el número de contacto del Autor')
    correo = models.EmailField(max_length = 50, error_messages = {"Error": "Digite un formato válido!"}, help_text='Indique el correo del Autor')

    def __str__(self):

        return f'{self.nom_autor}, {str(self.correo)}'

    def get_absolute_url(self):
        
        return reverse('autor_detail', args=[str(self.id_autor)])

class Noticia(models.Model):

    id_noticia = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = 'Indique el ID de la Noticia')
    titulo = models.CharField(max_length = 50, help_text='Indique el titular de la noticia')
    descripcion = models.TextField(max_length = 100, help_text='Agrege una pequeña descripción de la noticia')
    tipo_de_noticia = models.CharField(max_length = 50, null = True ,help_text='Debe indicar el tipo de noticia, por ejemplo novedad, popular etc.')
    autor = models.ForeignKey(Autor, on_delete = models.SET_NULL, null= True)
    
    def __str__(self):

        return f'{self.titulo}, {self.id_noticia}' 

    def get_absolute_url(self):
        
        return reverse('noticia_detail', args=[str(self.id_noticia)])

class Consola(models.Model):

    id_consola = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = 'Indique el ID de la Noticia')
    nombre = models.CharField(max_length = 50, help_text='Indique el Nombre de la Consola')
    generacion = models.CharField(max_length = 25, help_text='Indique la Generación a la que pertenece la Consola')

    def __str__(self):

        return f'{self.nombre}, {str(self.id_consola)}, {str(self.generacion)}'

    def get_absolute_url(self):
        
        return reverse('consola_detail', args=[str(self.id_consola)])

    
class Formulario(models.Model):
    
    id_postulacion = models.UUIDField(primary_key = True, default = uuid.uuid4)
    area_postular = models.ForeignKey('AreaPostular', on_delete=models.SET_NULL, null=True, blank=True, help_text='Indique el Areal a Postular') 
    nombre = models.CharField(max_length = 50, help_text='Indique el nombre del postulante')
    apellido = models.CharField(max_length = 50, help_text='Indique los apellidos del postulante')
    correo = models.EmailField(max_length = 50, error_messages = {"Error": "Digite un formato válido!"}, help_text='Indique el correo del postulante')
    numero = models.IntegerField(blank = True, null = True, help_text='Indique el número de contacto del postulante')
    nivel_estudios = models.ForeignKey('NivelEducacional', on_delete=models.SET_NULL, null=True, blank=True, help_text='Indique el nivel de estudios del postulante')
    motivo = models.TextField(max_length = 500, help_text='Motivo por el cual quiere ser parte del equipo')

    class Meta:
        ordering = ['id_postulacion']

    def __str__(self):

        return self.nombre

    def get_absolute_url(self):
        
        return reverse('gracias_detail', args=[str(self.id_postulacion)])
