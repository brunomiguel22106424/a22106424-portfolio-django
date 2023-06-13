from django import forms
from django.forms import ModelForm
from .models import *


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'adicionar nome...'}),
            'apelido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'adicionar apelido...'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'adicionar email...'}),
        }

        labels = {
            'nome': 'nome',
            'apelido': 'apelido',
            'email': 'email',
            'verified': 'verified',
        }


class ArtigoForm(ModelForm):
    class Meta:
        model = Artigo
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'adicionar nome...'}),
            'conteudo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'adicionar apelido...'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'adicionar link...'}),
        }

        labels = {
            'titulo': 'titulo',
            'conteudo': 'conteudo',
            'imagem': 'imagem',
            'link': 'link',
            'area': 'area',
            'autor': 'autor',
        }


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'

        widgets = {
            'texto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'adicionar comentário...'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'adicionar link...'}),
            'likes': forms.NumberInput(attrs={'disabled': 'True'}),
        }

        labels = {
            'autor': 'autor',
            'texto': 'texto',
            'likes': 'likes',
            'artigo': 'artigo',
        }
