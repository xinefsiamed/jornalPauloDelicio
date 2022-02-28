from django_summernote.widgets import SummernoteWidget
from django.forms import ModelForm
from .models import Post

class FormPost(ModelForm):
  class Meta:
    model = Post
    fields = ['titulo_post', 'conteudo_post', 'excerto_post', 'categoria_post', 'imagem_post']
    widgets = {
      'conteudo_post': SummernoteWidget(),
      'excerto_post': SummernoteWidget(),
    }

