from django.db import models


# Create your models here.


class Autor(models.Model):
    nome = models.CharField(max_length=250, null=False)
    apelido = models.CharField(max_length=250, null=False)
    email = models.CharField(null=False, max_length=100)
    verified = models.BooleanField(null=False)

    def __str__(self) -> str:
        return f'{self.nome} {self.apelido}'


class BlogOwner(models.Model):
    nome = models.CharField(max_length=100, null=False)
    repogit = models.CharField(max_length=1000, null=False)
    python = models.CharField(max_length=250, null=False)

    def __str__(self) -> str:
        return self.nome


class Blog(models.Model):
    nome = models.CharField(max_length=250, null=False)
    dono = models.OneToOneField(BlogOwner, on_delete=models.CASCADE, related_name="dono_blog")

    def __str__(self) -> str:
        return f'{self.nome}'


class Area(models.Model):
    nome = models.CharField(max_length=250, null=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="area_blog")

    def __str__(self) -> str:
        return self.nome


class Artigo(models.Model):
    titulo = models.CharField(max_length=250, null=False)
    conteudo = models.CharField(max_length=1000, null=False)
    imagem = models.ImageField(upload_to='images/', null=True, blank=True)
    link = models.CharField(max_length=250, null=False)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="artigo_area")
    autor = models.ManyToManyField(Autor, related_name="artigo_autor")

    def __str__(self) -> str:
        return f'{self.titulo}: {self.conteudo}'


class Comentario(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="comentario_autor")
    texto = models.CharField(max_length=1000, null=False)
    likes = models.IntegerField(default=0)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name="comentario_artigo")

    def __str__(self) -> str:
        return f'{self.autor}: {self.texto}: {self.likes}'


class Projeto(models.Model):
    titulo = models.CharField(max_length=250, null=False)
    descricao = models.CharField(max_length=250, null=False)
    imagem = models.ImageField(upload_to='images/', null=True, blank=True)
    cadeira = models.CharField(max_length=250, null=False)

    def __str__(self) -> str:
        return f'{self.titulo}: {self.descricao}: {self.cadeira}'
