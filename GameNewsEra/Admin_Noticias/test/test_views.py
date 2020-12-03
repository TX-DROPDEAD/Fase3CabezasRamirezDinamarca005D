from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from Admin_Noticias.models import Autor, Consola

class AutorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        numero_de_autor = 4

        for autor_id in range(numero_de_autor):
            Autor.objects.create(
                id_autor=f'59b15a9d-4873-4215-bb1f-e0655799dee4 {autor_id}', 
                nom_autor=f'Diego Dinamarca Abarca{autor_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/admin_noticias/autor_detail/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('autor_detail'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        responde = self.client.get(reverse('autor_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_noticias/autor_detail.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('autor_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['autor_detail']) == '59b15a9d-4873-4215-bb1f-e0655799dee4')

    def test_list_all_autors(self):
        response = self.client.get(reverse('autor_detail')+ '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['autor_detail']) == '59b15a9d-4873-4215-bb1f-e0655799dee4')
 
class ConsolaListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        numero_consola = 4

        for consola_id in range(numero_consola):
            Consola.objects.create(
                id_consola=f'1 {consola_id}', 
                nombre=f'PS5 {consola_id}', 
                generacion= f'Ultima Generacion {consola_id}',
                )
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/admin_noticias/consola_detail/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('consola_detail'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('consola_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_noticias/consola_detail.html')

    def test_pagination_is_ten(self):
        response = self .client.get(reverse('consola_detail'))  
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['consola_detail']) == 10) 

    def test_list_all_consolas(self):
        response = self.client.get(reverse('consola_detail')+ '?page=3')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['consola_detail']) == 3)     