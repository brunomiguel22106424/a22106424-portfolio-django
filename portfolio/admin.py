from django.contrib import admin
from .models import Autor, BlogOwner, Blog, Area, Artigo, Comentario, Like

# Register your models here.
admin.site.register(Autor)
admin.site.register(BlogOwner)
admin.site.register(Blog)
admin.site.register(Area)
admin.site.register(Artigo)
admin.site.register(Comentario)
admin.site.register(Like)
