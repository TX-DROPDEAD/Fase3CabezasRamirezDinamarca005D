from django.test import TestCase
from . models import Autor, Consola, Noticia, Formulario, AreaPostular, NivelEducacional
from Admin_Noticias.forms import FormularioForm

class FormularioTest(TestCase):
    def test_valid_form(self):
        area_postular = Formulario.objects.create(area_postular='1', descripcion='esto es una descripcion')
        area_postular= Formulario.objects(pk=1).pk
        
        e= NivelEducacional.objects.create(nivel_educacional='1',descripcion='esto es una descripcion')
        e= NivelEducacional.objects(pk=1).pk
        f= Formulario.objects.create(id_postulacion = '1', nombre='Pepito', apellido='Flores', correo='estoesunemail@gmail.com',numero = 56392509,motivo='Quiero ingresar a este equipo de trabajo porque me encanta todo lo relacionado al mundo de los juegos, lo encuentro entretenido, me informo yo y muchas personas mas.')
        f.save()
        data = {'area_postular': area_postular, 'niveleducacional': e,'id_postulacion' : f.id_postulacion, 'nombre': f.nombre, 'apellido':f.apellido, 'correo': f.correo, 'numero': f.numero, 'motivo' : f.motivo, }
        form = Formulario(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        area_postular = Formulario.objects.create(area_postular='1', descripcion='esto es una descripcion')   
        e= NivelEducacional.objects.create(nivel_educacional='',descripcion='esto es una descripcion') 
        f= Formulario.objects.create(id_postulacion = '1', nombre='', apellido='Flores', correo='estoesunemail@gmail.com',numero = 56392509,motivo='Quiero ingresar a este equipo de trabajo porque me encanta todo lo relacionado al mundo de los juegos, lo encuentro entretenido, me informo yo y muchas personas mas.')
        data = {'area_postular': area_postular, 'niveleducacional': e,'id_postulacion' : f.id_postulacion, 'nombre': f.nombre, 'apellido':f.apellido, 'correo': f.correo, 'numero': f.numero, 'motivo' : f.motivo, }
        form = Formulario(data=data)
        self.assertFalse(form.is_valid())