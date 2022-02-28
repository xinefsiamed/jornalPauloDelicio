from django.db import models
from posts.models import Post
from django.utils import timezone
# Create your models here.


class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=150, verbose_name="Nome")
    comentario = models.TextField(verbose_name="Comentario")
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
    data_comentario = models.DateTimeField(default=timezone.now)
    publicado_comentario = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_comentario
