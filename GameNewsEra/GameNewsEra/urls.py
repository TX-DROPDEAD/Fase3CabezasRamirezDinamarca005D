"""GameNewsEra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from rest_framework import routers
from Api_Usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('access/', include('Admin_Noticias.urls')),
    path('accounts/', include('Sesion.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='inicio.html'), name='inicio'),
]

router = routers.DefaultRouter()
router.register(r'Usuarios', views.UserViewSet)
router.register(r'Grupos', views.GroupViewSet)
router.register(r'Autores', views.AutorViewSet)
router.register(r'Noticias', views.NoticiaViewSet)
router.register(r'Consolas', views.ConsolaViewSet)

urlpatterns += [
    path('router', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
