from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import Template, Context
from . models import Autor, Consola, Noticia, Formulario, AreaPostular, NivelEducacional
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from . forms import FormularioForm, NoticiaForm
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.

@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")

def index(request):

    return render(request, 'index.html', context={},)

def videogames(request):

    return render(request, 'videogames.html', context={},)

def consolas(request):
 
    return render(request, 'consolas.html', context={},)

def contacto(request):

    nro_autores = Autor.objects.all().count()
    nro_noticias = Noticia.objects.all().count()
    nro_consolas = Consola.objects.all().count()

    return render(request, 'contacto_form.html', context={'nro_autores':nro_autores, 'nro_noticias':nro_noticias, 'nro_consolas':nro_consolas},)

def gracias(request):

    return render(request, 'gracias.html', context={},)


# CRUD Autor
class AutorCreate(CreateView):

    model = Autor
    fields = '__all__'

class AutorUpdate(UpdateView):

    model = Autor
    fields = ['nom_autor','educacion','numero','correo']

class AutorDelete(DeleteView):
    
    model = Autor
    success_url = reverse_lazy('index')

class AutorDetailView(generic.DetailView):

    model = Autor

class AutorListView(generic.ListView):

    model = Autor
    template_name = 'templates/admin_noticias/autor_list.html'
    paginate_by = 3

# CRUD Noticia
class NoticiaCreate(CreateView):

    model = Noticia
    fields = '__all__'

class NoticiaUpdate(UpdateView):

    model = Noticia
    fields = ['id_noticia','portada','titulo','subtitulo','parrafo1','imagen','bajadaimagen','video','parrafo2','autor']

class NoticiaDelete(DeleteView):

    models = Noticia
    queryset = Noticia.objects.all()
    success_url = reverse_lazy('index')

class NoticiaDetailView(generic.DetailView):

    model = Noticia

class NoticiaListView(generic.ListView):

    model = Noticia
    template_name = 'templates/admin_noticias/noticia_list.html'
    paginate_by = 10

#CRUD Consola
class ConsolaCreate(CreateView):
    model = Consola
    fields = '__all__'
    initial = {'generacion':'Novena Generacion'}
    

class ConsolaUpdate(UpdateView):
    model = Consola
    fields = ['nombre','generacion']

class ConsolaDelete(DeleteView):
    model = Consola
    success_url = reverse_lazy('index')

class ConsolaDetailView(generic.DetailView):
    model = Consola

class ConsolaListView(generic.ListView):

    model = Consola
    template_name = 'templates/admin_noticias/consola_list.html'
    paginate_by = 3

class FormDetailView(generic.DetailView):
    model = Formulario
    
def formulario_nuevo(request):
    if request.method == "POST":
        form = FormularioForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form.save_m2m()
            return redirect('gracias_detail', pk=post.pk)
    else:
        nro_autores = Autor.objects.all().count()
        nro_noticias = Noticia.objects.all().count()
        nro_consolas = Consola.objects.all().count()

        form = FormularioForm()
        return render(request, 'admin_noticias/contacto_form.html', 
        {'form': form, 'nro_autores':nro_autores, 'nro_noticias':nro_noticias, 'nro_consolas':nro_consolas})


def noticia_nueva(request, id):
    noticia = Noticia.objects.get(id_noticia=id)
    data = {
        'form':NoticiaForm(instance=noticia)
    }

    if request.method == "POST":
        form = NoticiaForm(request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form.save_m2m()
        data['form'] = NoticiaForm(instance=Noticia.objects.get(id_noticia=id))

    return render(request, 'admin_noticias/noticia_list', context={})

