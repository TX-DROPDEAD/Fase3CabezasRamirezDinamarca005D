from django.test import TestCase
from Admin_Noticias.models import Formulario, AreaPostular, NivelEducacional
from Admin_Noticias.forms import FormularioForm

class FormularioTest(TestCase):
    def test_valid_form(self):
        area_postular = Formulario.objects.create(area_postular='Publicidad Gaming',descripcion= 'Trabaja con nosotros diseñando la publicidad de nuestro sitio web.')
        area_postular= Formulario.objects(pk='c05533b0-1021-4728-ad38-eed43314c5ce').pk
        e= NivelEducacional.objects.create(nivel_educacional='Secundaria Completa',descripcion='Posee nivel enseñanza media completa.')
        e= NivelEducacional.objects(pk='c05533b0-1021-4728-ad38-eed43314c5ce').pk
        f= Formulario.objects.create(id_postulacion = c05533b0-1021-4728-ad38-eed43314c5ce,
         nombre='Hola mi nombre es pepe', apellido='21', correo='diego@gmail.com',numero = 123213123,
         nivel_estudios= 'Secundaria Completa',
         motivo='gola')
        f.save()
        data = { 'id_postulacion' : f.id_postulacion, 
                'area_postular': area_postular, 
                'nombre': f.nombre, 
                'apellido':f.apellido, 
                'correo': f.correo, 
                'numero': f.numero, 
                'niveleducacional': e,
                'motivo' : f.motivo, }
        form = Formulario(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    

    def test_invalid_form(self):
        area_postular = Formulario.objects.create(area_postular='Publicidad Gaming',descripcion= 'Trabaja con nosotros diseñando la publicidad de nuestro sitio web.')
        e= NivelEducacional.objects.create(nivel_educacional='Secundaria Completa',descripcion='Posee nivel enseñanza media completa.')
        f= Formulario.objects.create(id_postulacion = c05533b0-1021-4728-ad38-eed43314c5ce,
         nombre='Hola mi nombre es pepe', apellido='21', correo='diego@gmail.com',numero = 123213123,
         nivel_estudios= 'Secundaria Completa',
         motivo='gola')
        data = { 'id_postulacion' : f.id_postulacion, 
                'area_postular': area_postular, 
                'nombre': f.nombre, 
                'apellido':f.apellido, 
                'correo': f.correo, 
                'numero': f.numero, 
                'niveleducacional': e,
                'motivo' : f.motivo, }
        form = Formulario(data=data)
        self.assertFalse(form.is_valid())