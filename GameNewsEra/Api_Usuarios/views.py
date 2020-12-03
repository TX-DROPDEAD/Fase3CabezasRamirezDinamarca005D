from django.shortcuts import render
from django.contrib.auth.models import User, Group    
from rest_framework import viewsets
from rest_framework import permissions
from Api_Usuarios.serializers import UserSerializer, GroupSerializer, AutorSerializer, NoticiaSerializer, ConsolaSerializer
from Admin_Noticias.models import Autor, Noticia, NivelEducacional, Consola

class UserViewSet(viewsets.ModelViewSet): 
    queryset = User.objects.all().order_by('-date_joined') 
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.IsAuthenticated]

class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    permission_classes = [permissions.IsAuthenticated]

class ConsolaViewSet(viewsets.ModelViewSet):
    queryset = Consola.objects.all()
    serializer_class = ConsolaSerializer
    permission_classes = [permissions.IsAuthenticated]