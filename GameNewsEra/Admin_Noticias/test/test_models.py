from django.test import TestCase
from . models import Autor, Consola, Noticia, Formulario

class AutorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Autor.objects.create(id_autor=1, nom_autor='Juan Perez')
    
    def test_nom_autor_label(self):
        autor=Autor.objects.get(id_autor=1)
        field_label= autor._meta.get_field('nom_autor').verbose_name
        self.assertEquals(field_label, 'nom_autor')

    def test_nom_autor_max_length(self):
        autor=Autor.objects.get(id_autor=1)
        max_length = autor._meta.get_field('nom_autor').max_length
        self.assertEquals(max_length, 25)

    def test_get_absolute_url(self):
        autor=Autor.objects.get(id_autor=1)
        self.assertEquals(autor.get_absolute_url(), '/admin_noticias/autor_detail/1')

class ConsolaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Consola.objects.create(id_consola=1, nombre='PS5', generacion= 'Ultima Generacion')

    def test_nom_consola_label(self):
        consola=Consola.objects.get(id_consola=1)
        field_label=consola._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label, 'nombre')

    def test_nom_consola_max_length(self):
        consola=Consola.objects.get(id_consola=1)
        max_length= consola._meta.get_field('nombre').max_length
        self.assertEquals(max_length, 50)

    def test_generacion_consola_max_length(self):
        consola=Consola.objects.get(id_consola=1)
        max_length=consola._meta.get_field('generacion').max_length
        self.assertEquals(max_length, 25)

    def test_get_absolute_url(self):
        consola=Consola.objects.get(id_consola=1)
        self.assertEquals(consola.get_absolute_url(),'/admin_noticias/consola_detail/1')

class NoticiaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Noticia.objects.create(id_noticia=1, titulo='FALL GUYS 2DA TEMPORADA', descripcion='El juego que fue en su momento, el mas jugado a nivel mundial, el 18 de octubre lanzo su 2da temporada.', tipo_noticia='novedad',autor=1)
        
    def test_nom_titulo(self):
        noticia=Noticia.objects.get(id_noticia=1)
        field_label=noticia._meta.get_field('titulo').verbose_name
        self.assertEquals(field_label, 'titulo')
    
    def test_descripcion_max_length(self):
        noticia=Noticia.objects.get(id_noticia=1)
        max_length=noticia._meta.get_field('descripcion').max_length
        self.assertEquals(max_length, 100)
    
    def test_get_absolute_url(self):
        noticia=Noticia.objects.get(id_noticia=1)
        self.assertEquals(noticia.get_absolute_url(),'/admin_noticias/noticia_detail/1')

 class FormularioModelTest(TestCase):
     @classmethod
     def setUpTestData(cls):
         Formulario.objects.create()       

    