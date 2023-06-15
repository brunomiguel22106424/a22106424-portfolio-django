from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .forms import *
from .models import *


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def index_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/index.html', context)


def login_view_autenticacao(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:blog'))

        else:
            return render(request, 'portfolio/login.html', {
                'message': "erro"
            })

    return render(request, 'portfolio/login.html')


def playground_view(request):
    return render(request, 'portfolio/playground.html')


def blog_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    context = {'artigos': Artigo.objects.all(),
               'autores': Autor.objects.all(),
               'comentarios': Comentario.objects.all()}

    return render(request, 'portfolio/blog.html', context)


def novo_autor_view(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:blog')
    context = {'form': form}
    return render(request, 'portfolio/novoAutor.html', context)


def novo_artigo_view(request):
    form = ArtigoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:blog')
    context = {'form': form}
    return render(request, 'portfolio/novoArtigo.html', context)


def novo_comentario_view(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:blog')
    context = {'form': form}
    return render(request, 'portfolio/novoComentario.html', context)


def edita_artigo_view(request, artigo_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    artigo = get_object_or_404(Artigo, pk=artigo_id)

    if request.method == 'POST':
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('portfolio:blog')

    else:
        form = ArtigoForm(instance=artigo)

    context = {
        'artigo': Artigo,
        'artigo_id': artigo_id,
        'form': form,
    }

    return render(request, 'portfolio/edita.html', context)


def apaga_artigo_view(request, artigo_id):
    Artigo.objects.get(id=artigo_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def comentarios_view(request, artigo_id):
    artigo = Artigo.objects.get(pk=artigo_id)
    comentarios = Comentario.objects.filter(artigo=artigo)

    return render(request, 'portfolio/comentarios.html', {
        "artigos": artigo,
        "comentarios": comentarios
    })


def dar_like_comentario_view(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    comentario.likes += 1
    comentario.save()

    # redirecionar para a página de detalhes do artigo ou para onde você desejar
    return redirect('portfolio:comentarios', artigo_id=comentario.artigo.id)


def video_view(request):
    return render(request, 'portfolio/video.html')
