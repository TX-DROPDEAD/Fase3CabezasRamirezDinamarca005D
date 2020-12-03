from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Admin_Noticias.models import Autor, Noticia, Consola

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User  
        fields = ['url', 'username', 'email', 'groups'] 


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ['url','id_autor','nom_autor','numero','correo']

class NoticiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Noticia
        fields = ['url','id_noticia','portada','titulo',
        'subtitulo','parrafo1','imagen','bajadaimagen','video','parrafo2','autor']

class ConsolaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consola
        fields = ['url','id_consola','nombre','generacion']
        