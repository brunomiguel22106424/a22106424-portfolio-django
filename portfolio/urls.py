from django.shortcuts import render
from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path('index', views.index_view, name='index'),
    path('home', views.home_page_view, name='home'),
    path('blog', views.blog_page_view, name='blog'),
    path('novoAutor', views.novo_autor_view, name='novoAutor'),
    path('novoArtigo', views.novo_artigo_view, name='novoArtigo'),
    path('edita/<int:artigo_id>', views.edita_artigo_view, name='edita'),
    path('apaga/<int:artigo_id>', views.apaga_artigo_view, name='apaga'),
    path('novoComentario', views.novo_comentario_view, name='novoComentario'),
    path('comentarios<int:artigo_id>', views.comentarios_view, name='comentarios'),
    path('comentarios/<int:comentario_id>/like/', views.dar_like_comentario_view, name='dar_like_comentario'),
    path('playground.html', views.playground_view, name='playground'),
    path('login', views.login_view_autenticacao, name='login'),
    path('video', views.video_view, name='video'),
]