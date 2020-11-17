from django.contrib import admin
from . models import Autor, Consola, Formulario, Noticia, AreaPostular, NivelEducacional
# Register your models here.



admin.site.register(Autor)
admin.site.register(Consola)
admin.site.register(Formulario)
admin.site.register(Noticia)
admin.site.register(NivelEducacional)
admin.site.register(AreaPostular)
