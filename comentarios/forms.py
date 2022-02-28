from django.forms import ModelForm
from .models import Comentario

class FormComentario(ModelForm):

  def clean(self):
    data = self.cleaned_data
    nome = data.get('nome_comentario')
    comentario = data.get('comentario')


    if len(nome) < 5:
      self.add_error(
        'nome_comentario',
        'Nome precisa ter mais que 5 caracteres'
      )

    if len(comentario) < 20:
      self.add_error(
        'comentario',
        'Comentario precisa ter mais que 20 caracteres'
      )

  class Meta:
    model = Comentario
    fields = ('nome_comentario', 'comentario')

  def __init__(self, *args, **kwargs):
    super(FormComentario, self).__init__(*args, **kwargs)
    self.fields['nome_comentario'].widget.attrs.update({'class': 'input-nome'})
    self.fields['comentario'].widget.attrs.update({'class': 'input-comentario'})