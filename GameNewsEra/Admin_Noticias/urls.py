from django.urls import path
from . import views

urlpatterns = [
    #Path paginas principales
    path('home/', views.index, name='index'),
    path('videogames/', views.videogames, name='videogames'),
    path('consolas/', views.consolas, name='consolas'),
    path('gracias/', views.gracias, name='gracias'),
]

urlpatterns += [
    #Path CRUD Autor
    path('autor/create/', views.AutorCreate.as_view(), name='autor_create'),
    path('autor/<str:pk>/', views.AutorDetailView.as_view(), name='autor_detail'),
    path('autor/<str:pk>/update/', views.AutorUpdate.as_view(), name='autor_update'),
    path('autor/<str:pk>/delete/', views.AutorDelete.as_view(), name='autor_delete'),
    path('autores/', views.AutorListView.as_view(), name='autor_list'),
    #Path CRUD Noticia
    path('noticia/create/', views.NoticiaCreate.as_view(), name='noticia_create'),
    path('noticia/<str:pk>/', views.NoticiaDetailView.as_view(), name='noticia_detail'),
    path('noticia/<str:pk>/update/', views.NoticiaUpdate.as_view(), name='noticia_update'),
    path('noticia/<str:pk>/delete/', views.NoticiaDelete.as_view(), name='noticia_delete'),
    path('noticias/', views.NoticiaListView.as_view(), name='noticia_list'),
    #Path CRUD Consola
    path('consola/create/',views.ConsolaCreate.as_view(), name = 'consola_create'),
    path('consola/<str:pk>/',views.ConsolaDetailView.as_view(), name = 'consola_detail'),
    path('consola/<str:pk>/update/',views.ConsolaUpdate.as_view(), name = 'consola_update'),
    path('consola/<str:pk>/delete/',views.ConsolaDelete.as_view(), name = 'consola_delete'),
    path('lista_consolas/', views.ConsolaListView.as_view(), name='consola_list'),
    #Crud Formulario
    path('admin_noticias/Formulario/create/', views.formulario_nuevo,name='contacto_create'),
    path('admin_noticias/gracias/<str:pk>', views.FormDetailView.as_view(), name='gracias_detail'),
]