from django.test import TestCase
from Admin_Noticias.models import Autor, Consola, Noticia


class AutorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Autor.objects.create(id_autor='59b15a9d-4873-4215-bb1f-e0655799dee4', nom_autor='Diego Dinamarca Abarca')
    
    def test_nom_autor_label(self):
        autor=Autor.objects.get(id_autor='59b15a9d-4873-4215-bb1f-e0655799dee4')
        field_label= autor._meta.get_field('nom_autor').verbose_name
        self.assertEquals(field_label, 'nom autor')

    def test_nom_autor_max_length(self):
        autor=Autor.objects.get(id_autor='59b15a9d-4873-4215-bb1f-e0655799dee4')
        max_length = autor._meta.get_field('nom_autor').max_length
        self.assertEquals(max_length, 25)

    def test_get_absolute_url(self):
        autor=Autor.objects.get(id_autor='59b15a9d-4873-4215-bb1f-e0655799dee4')
        self.assertEquals(autor.get_absolute_url(), '/access/autor/59b15a9d-4873-4215-bb1f-e0655799dee4/')

class ConsolaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Consola.objects.create(id_consola='7e2177b7-5682-4fb1-a4eb-ed1f30edf779', nombre='PS4 PRO', generacion= '8va generación')

    def test_nom_consola_label(self):
        consola=Consola.objects.get(id_consola='7e2177b7-5682-4fb1-a4eb-ed1f30edf779')
        field_label=consola._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label, 'nombre')

    def test_nom_consola_max_length(self):
        consola=Consola.objects.get(id_consola='7e2177b7-5682-4fb1-a4eb-ed1f30edf779')
        max_length= consola._meta.get_field('nombre').max_length
        self.assertEquals(max_length, 50)

    def test_generacion_consola_max_length(self):
        consola=Consola.objects.get(id_consola='7e2177b7-5682-4fb1-a4eb-ed1f30edf779')
        max_length=consola._meta.get_field('generacion').max_length
        self.assertEquals(max_length, 25)


    def test_get_absolute_url(self):
        consola=Consola.objects.get(id_consola='7e2177b7-5682-4fb1-a4eb-ed1f30edf779')
        self.assertEquals(consola.get_absolute_url(),'/access/consola/7e2177b7-5682-4fb1-a4eb-ed1f30edf779/')

'''class NoticiaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Noticia.objects.create(
        id_noticia='8232340b-c6b2-4662-9f5d-e128ee9ca922', titulo='FARCRY 6 promete una Increíble Experiencia', subtitulo='Ubisoft confirma que Far Cry 6 llegará a 4K en PS5 y XBOX SERIES X',
        parrafo1='Tras el anuncio del nuevo Far Cry 6, que ya hemos podido ver en primera persona, se causó cierto revuelo alrededor de un mensaje que formaba parte de la campaña de marketing del videjuego. Según esta, Far Cry 6 llegaría a 4K Ultra HD “solo en Xbox One X y Xbox Series X”, quedándose en HDR en Xbox One S, lo que dejaba fuera a las consolas de Sony, algo que dio pie a pensar que ni PS4 Pro, y ni siquiera la próxima consola de la compañía nipona, PS5, llegarían a tal resolución. Afortunadamente sí será de tal manera.',
        imagen='/mediaupdates/f6-3.jpg',
        bajadaimagen='Far Cry 6 ya tiene fecha concreta de lanzamiento, y será el próximo 18 de febrero de 2021 tanto en la generación actual, PS4 y Xbox One, como en la futura, PS5 y Xbox Series X, además de en Google Stadia y PC.',
        video='https://www.youtube.com/embed/rgPZ1PG8bD4', 
        parrafo2='La colaboración cercana entre Microsoft y Ubisoft para la publicidad de Far Cry 6 era ya patente, pero dichos rumores se acrecentaron cuando la editora gala borró un tweet en respuesta a un fan preguntando acerca de este asunto, y en el que reiteraba dicha resolución solo para las consolas más potentes de la familia Xbox. Sin embargo, desde Ubisoft se ha rectificado esa información. “Para dejarlo claro, Far Cry 6 estará disponible en 4K en PS5, PS4 Pro y también PC”, han asegurado desde Ubisoft. “Compartiremos más detalles más adelante”, tranquilizando no solo a los poseedores de ambas consolas, sino también a los de un ordenador.', 
        autor='59b15a9d-4873-4215-bb1f-e0655799dee4')

    def test_nom_titulo(self):
        noticia=Noticia.objects.get(id_noticia='8232340b-c6b2-4662-9f5d-e128ee9ca922')
        field_label=noticia._meta.get_field('titulo').verbose_name
        self.assertEquals(field_label, 'titulo')
    
    def test_parrafo1_max_length(self):
        noticia=Noticia.objects.get(id_noticia='8232340b-c6b2-4662-9f5d-e128ee9ca922')
        max_length=noticia._meta.get_field('parrafo1').max_length
        self.assertEquals(max_length, 100)
    
    def test_get_absolute_url(self):
        noticia=Noticia.objects.get(id_noticia='8232340b-c6b2-4662-9f5d-e128ee9ca922')
        self.assertEquals(noticia.get_absolute_url(),'/access/noticia/8232340b-c6b2-4662-9f5d-e128ee9ca922/')
 '''      